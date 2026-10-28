# openneuro-ds000221-mpi-leipzig

- **Anatomy:** brain
- **Formats:** NIfTI
- **Access:** open
- **License:** CC0 (status: stated)
- **Source:** https://github.com/OpenNeuroDatasets/ds000221
- **Page title (evidence):** GitHub - OpenNeuroDatasets/ds000221 · GitHub
- **Size:** 318 participants; GB not published on fetched pages
- **Acquisition parameters:** not published on fetched pages (legacy openfmri search snippet: Siemens Verio 3T, not fetched); modalities T1w, T2w, FLAIR, T1map, dwi, bold, fieldmap
- **Sample file:** data/raw/openneuro-ds000221-mpi-leipzig/sub-010001_ses-02_acq-lowres_FLAIR.nii.gz

## Analysis

Inspected from one sample file: `data/raw/openneuro-ds000221-mpi-leipzig/sub-010001_ses-02_acq-lowres_FLAIR.nii.gz` (header only).

- **Format:** NIfTI
- **Dimensions:** [384, 512, 28]
- **Coils:** unknown
- **Static or dynamic:** static
- **Domain:** image
- **Fields read:** NIfTI dim, NIfTI pixdim

**Note:** Low-resolution FLAIR image from OpenNeuro ds000221, one subject and session.

## Sample verification — 2026-10-28

```yaml
format: NIfTI
shape: &id001
- 384
- 512
- 28
voxel_size_mm:
- 0.43
- 0.43
- 5.0
domain: image
static_or_dynamic: static
coil_count: unknown
fields_read:
- NIfTI dim
- NIfTI pixdim
inspected: true
basis: file header
sample_path: data/raw/openneuro-ds000221-mpi-leipzig/sub-010001_ses-02_acq-lowres_FLAIR.nii.gz
source_checked_at: '2026-10-28'
dimensions: *id001
```
