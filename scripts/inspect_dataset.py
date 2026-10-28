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
        info["time_points"] = shape[3]
    return info


def inspect_dicom(path: Path) -> dict:
    import pydicom

    files = sorted(path.rglob("*.dcm")) if path.is_dir() else [path]
    first = pydicom.dcmread(str(files[0]), stop_before_pixels=True)
    info = {
        "format": "DICOM",
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
        info["static_or_dynamic"] = "dynamic" if int(frames) > 1 else "static"
    info = {k: v for k, v in info.items() if v is not None}
    return info


def inspect_mha(path: Path) -> dict:
    info = {"format": "MetaImage"}
    for line in path.read_text(errors="ignore").splitlines()[:30]:
        if "=" in line:
            key, value = (s.strip() for s in line.split("=", 1))
            if key in ("DimSize", "ElementSpacing", "ElementType"):
                info[key] = value
    return info


def inspect(path: Path) -> dict:
    name = path.name.lower()
    if path.is_dir() or name.endswith(".dcm"):
        return inspect_dicom(path)
    if name.endswith(".nii") or name.endswith(".nii.gz"):
        return inspect_nifti(path)
    if name.endswith((".mha", ".mhd")):
        return inspect_mha(path)
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
