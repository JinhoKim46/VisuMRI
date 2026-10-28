# qsm-challenge-2016

- **Anatomy:** QSM
- **Formats:** NIfTI, MATLAB .mat
- **Access:** open
- **License:** [license to verify]  (page states no terms) (status: license to verify)
- **Source:** http://www.neuroimaging.at/pages/qsm.php
- **Page title (evidence):** Quantitative Susceptibility Mapping Software | Neuroimaging - Medical University of Graz
- **Size:** 240 MB (qsm_recon_challenge_2016.zip) - over 200 MB, not downloaded
- **Acquisition parameters:** not published on page (search snippets from papers: Siemens Tim Trio 3T, multi-orientation GRE magnitude/phase + MPRAGE; unverified)
- **Sample file:** data/raw/qsm-challenge-2016/chi_cosmos.nii.gz

## Analysis

Inspected from one sample file: `data/raw/qsm-challenge-2016/chi_cosmos.nii.gz` (header only).

- **Format:** NIfTI
- **Dimensions:** [160, 160, 160]
- **Coils:** unknown
- **Static or dynamic:** static
- **Domain:** image
- **Fields read:** NIfTI dim, NIfTI pixdim

**Note:** This is the reference susceptibility map (COSMOS), an image. It is not raw phase or magnitude data, so it cannot test the QSM reconstruction input.

## Notes from discovery

Original qsm.neuroimaging.at redirects to this page. NIfTI not confirmed.

## Sample verification — 2026-10-28

```yaml
format: NIfTI
shape: &id001
- 160
- 160
- 160
voxel_size_mm:
- 1.062
- 1.062
- 1.071
domain: image
static_or_dynamic: static
coil_count: unknown
fields_read:
- NIfTI dim
- NIfTI pixdim
inspected: true
basis: file header
sample_path: data/raw/qsm-challenge-2016/chi_cosmos.nii.gz
source_checked_at: '2026-10-28'
dimensions: *id001
```
