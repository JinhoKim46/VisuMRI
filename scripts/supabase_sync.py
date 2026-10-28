"""Upsert dataset metadata and the knowledge base into Supabase (idempotent).

Reads:
  datasets/index.yaml   -> top-level key `datasets`
  kb/references.yaml    -> top-level key `references`; each may list `linked_datasets`

Connection: SUPABASE_DB_URL in .env, which holds a Postgres connection string.
It is read at runtime and never printed.

Usage (run from the repo root, with the venv):
  .venv/bin/python scripts/supabase_sync.py --schema   # create tables (optional)
  .venv/bin/python scripts/supabase_sync.py            # upsert everything
"""

import argparse
import json
from pathlib import Path

import psycopg
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "supabase" / "schema.sql"


def load_env(path: Path) -> dict:
    env = {}
    for line in path.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip('"').strip("'")
    return env


DATASET_SQL = """
insert into datasets (id, anatomy, formats, source_url, sample_file_url, page_title,
                      license_text, license_status, size_text, acquisition_params,
                      access, analysis, notes_path, updated_at)
values (%(id)s, %(anatomy)s, %(formats)s, %(source_url)s, %(sample_file_url)s, %(page_title)s,
        %(license_text)s, %(license_status)s, %(size_text)s, %(acquisition_params)s,
        %(access)s, %(analysis)s, %(notes_path)s, now())
on conflict (id) do update set
    anatomy = excluded.anatomy, formats = excluded.formats, source_url = excluded.source_url,
    sample_file_url = excluded.sample_file_url, page_title = excluded.page_title,
    license_text = excluded.license_text, license_status = excluded.license_status,
    size_text = excluded.size_text, acquisition_params = excluded.acquisition_params,
    access = excluded.access, analysis = excluded.analysis, notes_path = excluded.notes_path,
    updated_at = now()
"""

REFERENCE_SQL = """
insert into kb_references (id, citation, doi, url, data_types, anatomy,
                           display_recommendation, verified, updated_at)
values (%(id)s, %(citation)s, %(doi)s, %(url)s, %(data_types)s, %(anatomy)s,
        %(display_recommendation)s, %(verified)s, now())
on conflict (id) do update set
    citation = excluded.citation, doi = excluded.doi, url = excluded.url,
    data_types = excluded.data_types, anatomy = excluded.anatomy,
    display_recommendation = excluded.display_recommendation,
    verified = excluded.verified, updated_at = now()
"""

LINK_SQL = """
insert into dataset_references (dataset_id, reference_id)
values (%s, %s)
on conflict do nothing
"""


def dataset_row(d: dict) -> dict:
    return {
        "id": d["id"],
        "anatomy": d.get("anatomy", []),
        "formats": d.get("formats", []),
        "source_url": d["source_url"],
        "sample_file_url": d.get("sample_file_url"),
        "page_title": d.get("page_title") or d.get("evidence"),
        "license_text": d.get("license_text") or d.get("license"),
        "license_status": d.get("license_status", "license to verify"),
        "size_text": d.get("size"),
        "acquisition_params": d.get("acquisition_params"),
        "access": d.get("access"),
        "analysis": json.dumps(d.get("analysis", {})),
        "notes_path": d.get("notes_path"),
    }


def reference_row(r: dict) -> dict:
    return {
        "id": r["id"],
        "citation": r["citation"],
        "doi": r.get("doi"),
        "url": r.get("url"),
        "data_types": r.get("data_type", []) if isinstance(r.get("data_type"), list) else [r["data_type"]],
        "anatomy": r.get("anatomy", []),
        "display_recommendation": r.get("display_recommendation"),
        "verified": bool(r.get("verified", False)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", action="store_true", help="run supabase/schema.sql first")
    args = parser.parse_args()

    dsn = load_env(ROOT / ".env")["SUPABASE_DB_URL"]
    datasets = yaml.safe_load((ROOT / "datasets" / "index.yaml").read_text())["datasets"]
    references = yaml.safe_load((ROOT / "kb" / "references.yaml").read_text())["references"]

    with psycopg.connect(dsn) as conn:
        with conn.cursor() as cur:
            if args.schema:
                cur.execute(SCHEMA.read_text())
            for d in datasets:
                cur.execute(DATASET_SQL, dataset_row(d))
            for r in references:
                cur.execute(REFERENCE_SQL, reference_row(r))
                for dataset_id in r.get("linked_datasets", []):
                    cur.execute(LINK_SQL, (dataset_id, r["id"]))
        conn.commit()

    print(f"upserted {len(datasets)} datasets, {len(references)} references")


if __name__ == "__main__":
    main()
