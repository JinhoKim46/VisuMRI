"""Record one sample's header analysis into the dataset index and its notes file.

Runs scripts/inspect_dataset.py on a downloaded sample, normalizes the four facts the
index tracks (dims, coils, static_or_dynamic, domain), and writes them to:
  datasets/index.yaml  -> the dataset's `analysis` field (other entries untouched)
  datasets/<id>.md     -> replaces the `## Analysis` section

Usage (from the repo root):
  .venv/bin/python -I scripts/record_analysis.py <dataset-id> <sample-path> [--note "..."]
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from inspect_dataset import inspect  # noqa: E402


def normalize(raw: dict, sample: Path) -> dict:
    dims = raw.get("shape") or raw.get("dimensions") or raw.get("encoding_matrix")
    if dims is None and "variables" in raw:
        dims = {name: v["shape"] for name, v in raw["variables"].items()}
    normalized = {
        "inspected": True,
        "sample_path": str(sample.relative_to(ROOT)),
        "format": raw.get("format"),
        "dims": dims if dims is not None else "unknown",
        "coils": raw.get("coil_count", "unknown"),
        "static_or_dynamic": raw.get("static_or_dynamic", "unknown"),
        "domain": raw.get("domain", "unknown"),
        "fields_read": raw.get("fields_read", []),
    }
    # keep every other header fact the inspector returned (voxel size, DICOM tags, caveats)
    return {**raw, **normalized}


def analysis_md(d: dict, note: str | None) -> str:
    lines = [
        "## Analysis",
        "",
        f"Inspected from one sample file: `{d['sample_path']}` (header only).",
        "",
        f"- **Format:** {d['format']}",
        f"- **Dimensions:** {d['dims']}",
        f"- **Coils:** {d['coils']}",
        f"- **Static or dynamic:** {d['static_or_dynamic']}",
        f"- **Domain:** {d['domain']}",
        f"- **Fields read:** {', '.join(d['fields_read']) or 'none'}",
    ]
    if note:
        lines += ["", f"**Note:** {note}"]
    return "\n".join(lines) + "\n"


def replace_analysis_section(text: str, new_section: str) -> str:
    pattern = re.compile(r"^## Analysis\n.*?(?=^## |\Z)", re.S | re.M)
    if pattern.search(text):
        return pattern.sub(new_section + "\n", text, count=1)
    return text.rstrip() + "\n\n" + new_section


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_id")
    parser.add_argument("sample_path")
    parser.add_argument("--note", default=None)
    args = parser.parse_args()

    sample = Path(args.sample_path).resolve()
    if not sample.is_relative_to(ROOT / "data" / "raw"):
        raise SystemExit("sample must live under data/raw/ (gitignored)")

    index_path = ROOT / "datasets" / "index.yaml"
    index = yaml.safe_load(index_path.read_text())
    entry = next((d for d in index["datasets"] if d["id"] == args.dataset_id), None)
    if entry is None:
        raise SystemExit(f"unknown dataset id: {args.dataset_id}")

    analysis = normalize(inspect(sample), sample)
    if args.note:
        analysis["note"] = args.note
    entry["analysis"] = analysis
    index_path.write_text(
        "# Dataset index. One entry per dataset. Notes: datasets/<id>.md\n"
        + yaml.safe_dump(index, sort_keys=False, allow_unicode=True, width=120)
    )

    notes_path = ROOT / "datasets" / f"{args.dataset_id}.md"
    text = notes_path.read_text() if notes_path.exists() else f"# {args.dataset_id}\n"
    notes_path.write_text(replace_analysis_section(text, analysis_md(analysis, args.note)))
    print(f"recorded {args.dataset_id}: {analysis['dims']} | coils {analysis['coils']} | "
          f"{analysis['static_or_dynamic']} | {analysis['domain']}")


if __name__ == "__main__":
    main()
