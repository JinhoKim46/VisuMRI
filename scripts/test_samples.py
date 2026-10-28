"""Local safety checks: .venv/bin/python -I scripts/test_samples.py."""
import importlib.util
from pathlib import Path
import tempfile
import hashlib


def load(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


fetch = load('fetch_sample')
for value in ('../bad', '/bad', 'a/../bad', 'a\\bad', '..hidden'):
    try:
        fetch.safe_name(value)
    except ValueError:
        pass
    else:
        raise AssertionError(value)
assert fetch.safe_name('a/b.nii.gz') == 'b.nii.gz'
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / 'sample'
    path.write_bytes(b'known sample')
    assert fetch.digest(path) == hashlib.sha256(b'known sample').hexdigest()
inspect = load('inspect_dataset')
import h5py
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / 'broken.mrd'
    with h5py.File(path, 'w') as f:
        f.create_dataset('dataset/xml', data=[b'invalid XML'])
        f.create_dataset('dataset/data', data=[1])
    try:
        inspect.inspect(path)
    except Exception as error:
        assert type(error).__name__ == 'ParseError'
    else:
        raise AssertionError('malformed ISMRMRD silently accepted')
print('sample safety checks passed')

import io
import tarfile
import yaml
import zipfile

with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    (root / 'datasets').mkdir()
    payload = b'fixture image bytes'
    for kind in ('tar', 'zip'):
        archive_path = root / ('sample.' + kind)
        if kind == 'tar':
            with tarfile.open(archive_path, 'w') as archive:
                member = tarfile.TarInfo('nested/sample.nii')
                member.size = len(payload)
                archive.addfile(member, io.BytesIO(payload))
        else:
            with zipfile.ZipFile(archive_path, 'w') as archive:
                archive.writestr('nested/sample.nii', payload)
        item = dict(id=kind, url=archive_path.as_uri(), filename='sample.nii',
                    size=len(payload), sha256=hashlib.sha256(payload).hexdigest(),
                    archive_size=archive_path.stat().st_size)
        item[kind + '_member'] = 'nested/sample.nii'
        (root / 'datasets/samples.yaml').write_text(yaml.safe_dump({'samples': [item]}))
        fetch.ROOT = root
        path = fetch.fetch(kind)
        assert path.read_bytes() == payload
        assert fetch.fetch(kind) == path
        path.write_bytes(b'do not overwrite')
        try:
            fetch.fetch(kind)
        except ValueError:
            assert path.read_bytes() == b'do not overwrite'
        else:
            raise AssertionError('existing file overwritten')
    bart = root / 'bart.tgz'
    with tarfile.open(bart, 'w:gz') as archive:
        for name, content in [('sample.hdr', b'# Dimensions\n2 3 1\n'), ('sample.cfl', bytes(48))]:
            member = tarfile.TarInfo(name)
            member.size = len(content)
            archive.addfile(member, io.BytesIO(content))
    assert inspect.inspect(bart)['dimensions'] == [2, 3, 1]
print('TAR, small ZIP, BART, and existing-file checks passed')
