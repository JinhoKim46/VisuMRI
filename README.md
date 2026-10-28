# VisuMRI

Universal MRI visualization and post-processing tool (in development).

**Current stage (v0):** dataset collection and literature review. Reconstruction, visualization, segmentation, and the web app are not built yet.

## Repo contents

- `datasets/` — dataset index and per-dataset analysis notes
- `kb/` — knowledge base of references
- `literature/` — literature review on visualization layouts
- `scripts/` — download scripts, the header inspector, and the Supabase sync
- `supabase/` — schema
- `docs/` — suggested Meta services

## Setup

1. Create `.env` in the repo root (not committed) with:
   - `SUPABASE_API_KEY` — Postgres connection string for the Supabase project
   - `META_API_KEY` — Meta services key
2. Create the schema by running `supabase/schema.sql` in the Supabase SQL editor.

## How to add a new dataset

See `CLAUDE.md` → "Add a new dataset".

Full steps:
1. Put a download script in `scripts/download/<id>.sh`. Raw data is never committed.
2. Add an entry to `datasets/index.yaml` (anatomy, format, source URL, license, size, acquisition parameters).
3. Download one small file to `data/raw/<id>/` and run `python -I scripts/inspect_dataset.py <file>`.
4. Write `datasets/<id>.md`.
5. Add any new references to `kb/references.yaml` and link them to the dataset id.
6. Run `python scripts/supabase_sync.py` to upsert.

## Future

A local, Docker-based web app will live on a separate branch.
