# VisuMRI — working notes for Claude

Universal MRI visualization and post-processing tool. Built for the Meta AI Developer Hackathon.

## Scope of THIS version (v0)

v0 = **data collection and literature review only**.

- In scope: sample dataset collection, acquisition analysis, literature review on display, the knowledge base, Supabase population, and a list of suggested Meta services.
- Out of scope (do NOT build yet): reconstruction (CG-SENSE, L1-wavelet, SigPy backend), visualization, SAM segmentation, MIP / secondary-anatomy removal, the web app.
- The web app (local, Docker) is a separate future branch. Only name it in the README.

## Target project vision (for context)

Takes MRI raw data in any common format (HDF5, NIfTI, DICOM, ISMRMRD raw, others), analyses the acquisition first, asks which reconstruction to run if needed, then offers visualization chosen for the data type. Reconstruction methods are modular. Lightweight.

## Working tools

Use these by default:
- `route-work` — sizes and routes each piece of work. The current task is sized **Large**.
- `ponytail` — default tooling for this repo.
- `agent-browser` — default for browsing and fetching sources.

## Repo layout

- `datasets/index.yaml` — metadata for every dataset (one entry per dataset).
- `datasets/<id>.md` — per-dataset analysis notes.
- `kb/references.yaml` — knowledge base: every reference with citation, link, data-type/anatomy tags, display recommendation, linked dataset ids.
- `literature/review.md` — literature review on visualization layouts/styles per data type.
- `scripts/download/<id>.sh` — download scripts (raw data is never committed).
- `scripts/inspect_dataset.py` — reads one file's header and reports dims / coils / static-vs-dynamic / k-space-vs-image.
- `scripts/supabase_sync.py` — idempotent upsert of datasets and references into Supabase.
- `supabase/schema.sql` — table definitions.
- `docs/meta-services.md` — suggested Meta services and how each could help.
- `data/` — local raw files, gitignored.

## Rules

- **Secrets**: `.env` holds `SUPABASE_DB_URL` (a Postgres DSN for the Supabase project) and `META_API_KEY`. Read them from `.env` at runtime. Never hard-code or print them, never commit `.env`.
- **Large raw files stay out of git.** Store the source URL and a download script instead.
- **Every dataset needs**: anatomy, format, source URL, license/usage terms (flag unknown ones as `[license to verify]`), acquisition parameters if available, file size, and the page actually fetched as evidence.
- **Every reference needs**: citation, DOI or URL (verify it resolves), data-type tags, anatomy tags, a 1–2 line display recommendation.
- **Commit messages** end with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`.

## Add a new dataset (summary)

1. Add `scripts/download/<id>.sh` and an entry in `datasets/index.yaml`.
2. Fetch one small file into `data/raw/<id>/` and run `python -I scripts/inspect_dataset.py <file>`.
3. Write `datasets/<id>.md` with the findings. Mark anything not inspected as `source: documentation, not inspected`.
4. Add any new references to `kb/references.yaml`, linked to the dataset id.
5. Run `python scripts/supabase_sync.py` to upsert.

See `README.md` for the full guide.
