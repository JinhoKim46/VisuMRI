# skm-tea-knee

- **Anatomy:** knee
- **Formats:** HDF5, DICOM, NIfTI
- **Access:** gated
- **License:** [license to verify] (status: license to verify)
- **Source:** https://aimi.stanford.edu/datasets/skm-tea-knee-mri
- **Page title (evidence):** SKM-TEA Knee MRI | Center for Artificial Intelligence in Medicine & Imaging
- **Size:** 155 qDESS knee scans (86 train/33 val/36 test); ~900GB compressed, 1.6TB expanded (per github DATASET.md https://github.com/StanfordMIMI/skm-tea/blob/main/DATASET.md)
- **Acquisition parameters:** qDESS 3D; 2x1 parallel imaging, elliptical sampling, ARC-completed; 8 or 15/16 coils; example matrix [512,512,160], voxel 0.3125x0.3125x0.8 mm (example values); TR/TE and field strength not published on fetched pages
- **Sample file:** none; see reason below

## Analysis

See the dated sample verification below.

## Notes from discovery

AIMI page only asks to cite DOI 10.71718/2ghb-nv62; download via Redivis link (login likely, not confirmed). Repo code is MIT, not the data. Too large to bundle; the track cannot be downloaded separately.

## Sample verification — 2026-10-28

```yaml
inspected: false
basis: documentation only
reason: 'Gated: requires provider approval/login; no authenticated download attempted.'
dimensions: unknown
coil_count: unknown
static_or_dynamic: unknown
domain: unknown
fields_read: []
source_checked_at: '2026-10-28'
```
