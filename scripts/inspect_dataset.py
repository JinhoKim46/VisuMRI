"""Read one MRI file's header and report its acquisition facts as JSON.

Reads headers only, never the full pixel or k-space payload, so it stays light.

Supported:
  .h5 / .hdf5 / .mat (v7.3)  -> HDF5 keys and shapes; guesses k-space vs image
  .h5 ISMRMRD raw            -> ISMRMRD header: encoding matrix, coils, acquisitions
  .nii / .nii.gz             -> NIfTI header: dims, voxel size, time points
  .dcm (file or folder)      -> DICOM tags: modality, sequence, coil name, counts
  .mha / .mhd                -> MetaImage header (via nibabel is not used; read text header)

Usage (from the repo root):
  .venv/bin/python -I scripts/inspect_dataset.py <path>

Output: JSON on stdout. Fields it cannot determine are left out, not guessed.
"""

import json
import sys
from pathlib import Path

import h5py


def inspect_h5(path: Path) -> dict:
    info = {"format": "HDF5", "datasets": {}}
    with h5py.File(path, "r") as f:
        def visit(name, obj):
            if isinstance(obj, h5py.Dataset):
                info["datasets"][name] = {"shape": list(obj.shape), "dtype": str(obj.dtype)}
        f.visititems(visit)
    names = " ".join(info["datasets"]).lower()
    if "kspace" in names or "k-space" in names:
        info["domain"] = "k-space"
    elif "image" in names or "recon" in names:
        info["domain"] = "image"
    return info


def inspect_ismrmrd(path: Path) -> dict:
    import xml.etree.ElementTree as ET

    with h5py.File(path, "r") as f:
        root = ET.fromstring(f["dataset/xml"][0])
        ns = {"m": "http://www.ismrm.org/ISMRMRD"}
        def value(key):
            node = root.find(".//" + "m:" + key.replace("/", "/m:"), ns)
            return node.text if node is not None else None
        matrix = [int(value("encoding/encodedSpace/matrixSize/" + axis)) for axis in "xyz"]
        phase_max = value("encoding/encodingLimits/phase/maximum")
        repetition_max = value("encoding/encodingLimits/repetition/maximum")
        dynamic = any(v is not None and int(v) > 0 for v in (phase_max, repetition_max))
        return {"format": "ISMRMRD raw", "encoding_matrix": matrix,
                "coil_count": int(value("acquisitionSystemInformation/receiverChannels")),
                "acquisitions": f["dataset/data"].shape[0], "domain": "k-space",
                "static_or_dynamic": "dynamic" if dynamic else "unknown",
                "phase_maximum": phase_max, "repetition_maximum": repetition_max,
                "protocol_name": value("measurementInformation/protocolName"),
                "fields_read": ["dataset/xml: encoding/encodedSpace/matrixSize",
                                "dataset/xml: acquisitionSystemInformation/receiverChannels",
                                "dataset/xml: measurementInformation/protocolName", "dataset/data.shape",
                                "dataset/xml: encoding/encodingLimits/phase/maximum",
                                "dataset/xml: encoding/encodingLimits/repetition/maximum"]}


def inspect_nifti(path: Path) -> dict:
    import nibabel as nib

    img = nib.load(str(path))
    shape = list(img.shape)
    info = {
        "format": "NIfTI",
        "shape": shape,
        "voxel_size_mm": [round(float(z), 3) for z in img.header.get_zooms()[:3]],
        "domain": "image",
        "static_or_dynamic": "unknown" if len(shape) > 3 else "static",
        "coil_count": "unknown",
        "fields_read": ["NIfTI dim", "NIfTI pixdim"],
    }
    if len(shape) == 4 and shape[3] > 1:
        info["fourth_dimension_size"] = shape[3]
    return info


def inspect_dicom(path: Path) -> dict:
    import pydicom

    files = sorted(path.rglob("*.dcm")) if path.is_dir() else [path]
    first = pydicom.dcmread(str(files[0]), stop_before_pixels=True)
    info = {
        "format": "DICOM",
        "dimensions": [int(first.Rows), int(first.Columns)],
        "coil_count": "unknown",
        "static_or_dynamic": "unknown",
        "fields_read": [tag for tag in ("Rows", "Columns", "NumberOfFrames", "Modality", "SeriesDescription", "SequenceName", "ReceiveCoilName", "MagneticFieldStrength") if tag in first],
        "file_count": len(files),
        "modality": str(getattr(first, "Modality", "")) or None,
        "series_description": str(getattr(first, "SeriesDescription", "")) or None,
        "sequence_name": str(getattr(first, "SequenceName", "")) or None,
        "coil_name": str(getattr(first, "ReceiveCoilName", "")) or None,
        "field_strength_t": float(first.MagneticFieldStrength) if "MagneticFieldStrength" in first else None,
        "domain": "image",
    }
    frames = getattr(first, "NumberOfFrames", None)
    if frames:
        info["frames"] = int(frames)
        info["dimensions"].append(int(frames))
    info = {k: v for k, v in info.items() if v is not None}
    return info


def inspect_matlab_v5(path: Path) -> dict:
    from scipy.io import whosmat

    variables = {name: {"shape": list(shape), "dtype": dtype} for name, shape, dtype in whosmat(str(path))}
    return {"format": "MATLAB v5", "variables": variables, "coil_count": "unknown",
            "static_or_dynamic": "unknown", "domain": "unknown",
            "fields_read": ["MATLAB v5 variable headers (scipy.io.whosmat)"]}


def inspect_mha(path: Path) -> dict:
    info = {"format": "MetaImage"}
    for line in path.read_text(errors="ignore").splitlines()[:30]:
        if "=" in line:
            key, value = (s.strip() for s in line.split("=", 1))
            if key in ("DimSize", "ElementSpacing", "ElementType"):
                info[key] = value
    return info


def inspect_bart_archive(path: Path) -> dict:
    import math
    import tarfile

    with tarfile.open(path) as archive:
        members = archive.getmembers()
        for member in members:
            if '..' in member.name or member.name.startswith('/'):
                raise ValueError('unsafe TAR member')
        headers = [m for m in members if m.isfile() and m.name.endswith('.hdr') and '/ROIs/' not in m.name]
        header = next((m for m in headers if '/T1maps/' in m.name), headers[0] if headers else None)
        if header is None or header.size > 4096:
            raise ValueError('missing or oversized BART header')
        with archive.extractfile(header) as stream:
            lines = stream.read().decode('ascii').splitlines()
        dimensions = [int(v) for line in lines if not line.startswith('#') for v in line.split()]
        if not dimensions or any(v <= 0 for v in dimensions):
            raise ValueError('invalid BART dimensions')
        payload = archive.getmember(header.name[:-4] + '.cfl')
        if not payload.isfile() or payload.size != math.prod(dimensions) * 8:
            raise ValueError('BART complex64 payload size does not match header')
        return {'format': 'BART cfl/hdr in TAR', 'dimensions': dimensions,
                'header_member': header.name, 'payload_member': payload.name,
                'coil_count': 'unknown', 'static_or_dynamic': 'unknown', 'domain': 'unknown',
                'fields_read': ['BART # Dimensions', 'TAR member names and sizes'],
                'caveat': 'BART dimensions do not encode anatomy or axis semantics; domain and temporal behavior require acquisition documentation.'}


def inspect(path: Path) -> dict:
    name = path.name.lower()
    if name.endswith((".tgz", ".tar.gz")):
        return inspect_bart_archive(path)
    if path.is_dir() or name.endswith(".dcm"):
        return inspect_dicom(path)
    if name.endswith(".nii") or name.endswith(".nii.gz"):
        return inspect_nifti(path)
    if name.endswith((".mha", ".mhd")):
        return inspect_mha(path)
    if name.endswith(".mat") and not h5py.is_hdf5(path):
        return inspect_matlab_v5(path)
    if name.endswith((".h5", ".hdf5", ".mat", ".mrd")):
        with h5py.File(path, "r") as f:
            raw = "dataset/xml" in f and "dataset/data" in f
        return inspect_ismrmrd(path) if raw else inspect_h5(path)
    raise SystemExit(f"unsupported file type: {path.name}")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    path = Path(sys.argv[1]).resolve()
    print(json.dumps(inspect(path), indent=2, default=str))


if __name__ == "__main__":
    main()
