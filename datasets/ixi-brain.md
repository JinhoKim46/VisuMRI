# ixi-brain

- **Anatomy:** brain
- **Formats:** NIfTI
- **Access:** open
- **License:** This data is made available under the Creative Commons CC BY-SA 3.0 license. (status: stated)
- **Source:** https://brain-development.org/ixi-dataset/
- **Page title (evidence):** IXI Dataset – Brain Development
- **Size:** Nearly 600 MR images from normal healthy subjects (GB not published on fetched page)
- **Acquisition parameters:** T1, T2, PD, MRA, DWI (15 directions); Hammersmith Philips 3T, Guy's Philips 1.5T, IOP GE 1.5T; TR/TE not listed on this page (linked scanner pages not fetched)
- **Sample file:** data/raw/ixi-brain/IXI002-Guys-0828-T1.nii.gz

## Analysis

Inspected from one sample file: `data/raw/ixi-brain/IXI002-Guys-0828-T1.nii.gz` (header only).

- **Format:** NIfTI
- **Dimensions:** [256, 256, 150]
- **Coils:** unknown
- **Static or dynamic:** static
- **Domain:** image
- **Fields read:** NIfTI dim, NIfTI pixdim

**Note:** T1-weighted volume from IXI (Guys site). Header only; coils not stated in NIfTI.

## Sample verification — 2026-10-28

```yaml
format: NIfTI
shape: &id001
- 256
- 256
- 150
voxel_size_mm:
- 0.938
- 0.938
- 1.2
domain: image
static_or_dynamic: static
coil_count: unknown
fields_read:
- NIfTI dim
- NIfTI pixdim
inspected: true
basis: file header
sample_path: data/raw/ixi-brain/IXI002-Guys-0828-T1.nii.gz
source_checked_at: '2026-10-28'
dimensions: *id001
```
