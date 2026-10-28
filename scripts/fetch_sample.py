"""Fetch a pinned sample: .venv/bin/python -I scripts/fetch_sample.py <id>."""
import hashlib
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml
from remotezip import RemoteZip

ROOT = Path(__file__).resolve().parents[1]


def safe_name(name):
    if not name or '..' in name or name.startswith(('/', '\\')) or '\\' in name:
        raise ValueError('unsafe archive member or filename')
    return Path(name).name


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def fetch(id):
    entries = yaml.safe_load((ROOT / 'datasets/samples.yaml').read_text())['samples']
    item = next((x for x in entries if x['id'] == id), None)
    if item is None:
        raise ValueError('unknown dataset id')
    if item.get('reason'):
        raise ValueError(item['reason'])
    if not item.get('sha256') or item.get('size') is None:
        raise ValueError('sample has not been pinned; see dataset notes')
    safe_name(id)
    directory = ROOT / 'data/raw' / id
    filename = safe_name(item.get('zip_member') or item['filename'])
    path = directory / filename
    if directory.is_symlink() or path.is_symlink():
        raise ValueError('refusing symlink destination')
    if directory.exists() and any(directory.iterdir()):
        if list(directory.iterdir()) == [path] and path.stat().st_size == item['size'] and digest(path) == item['sha256']:
            return path
        raise ValueError('destination must be empty; existing files preserved')
    directory.mkdir(parents=True, exist_ok=True)
    temporary = directory / (filename + '.partial')
    try:
        if item.get('zip_member'):
            headers = subprocess.check_output(['curl', '-sI', '--max-time', '30', '-H', 'Range: bytes=0-0', item['url']], text=True)
            if not any(line.startswith('HTTP/') and line.split()[1] == '206' for line in headers.splitlines()):
                raise ValueError('range probe did not return 206; refusing full archive')
            with RemoteZip(item['url'], timeout=60) as archive:
                member = archive.getinfo(item['zip_member'])
                safe_name(member.filename)
                if member.file_size != item['size']:
                    raise ValueError('archive member size mismatch')
                with archive.open(member) as source, temporary.open('xb') as target:
                    shutil.copyfileobj(source, target)
        else:
            with urllib.request.urlopen(item['url'], timeout=60) as source, temporary.open('xb') as target:
                remaining = item['size']
                while remaining:
                    chunk = source.read(min(1024 * 1024, remaining))
                    if not chunk:
                        break
                    target.write(chunk)
                    remaining -= len(chunk)
                if source.read(1):
                    raise ValueError('download exceeds pinned size')
        if temporary.stat().st_size != item['size'] or digest(temporary) != item['sha256']:
            raise ValueError('sample size or SHA-256 mismatch')
        temporary.rename(path)
    finally:
        temporary.unlink(missing_ok=True)
    return path


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    try:
        print(fetch(sys.argv[1]))
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
