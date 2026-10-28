# mridata-stanford-fse-knee-hf-mirror

- **Anatomy:** knee
- **Formats:** HDF5
- **Access:** open
- **License:** cc-by-nc-4.0 (status: license to verify)
- **Source:** https://huggingface.co/datasets/arjundd/mridata-stanford-knee-3d-fse
- **Page title (evidence):** arjundd/mridata-stanford-knee-3d-fse · Datasets at Hugging Face
- **Size:** 67.7 GB total, 3 files (train/val/test, 1 row each, per HF viewer)
- **Acquisition parameters:** From search results of papers (not fetched from the primary page): 3T GE, 8-channel coil, 320x320 matrix, TR 1550 ms / TE 25 ms, 3D FSE. Primary page: not published on fetched page
- **Sample file:** none recorded

## Analysis

Not inspected. No sample file was downloaded in this pass, so dimensions, coil count, and static-vs-dynamic are not yet recorded. Re-run `scripts/inspect_dataset.py` on one downloaded file to fill these in.

## Notes from discovery

This is a third-party HF mirror of the mridata.org Stanford fully sampled 3D FSE knees dataset. mridata.org itself could not be fetched (tool error), so the original ISMRMRD format and original license are UNVERIFIED. Third-party sources say mridata original is ISMRMRD with 19-20 volumes. Mirror license may differ from original; verify at mridata.org.
