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
