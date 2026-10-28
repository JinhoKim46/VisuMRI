# ixi-mra

- **Anatomy:** angiography
- **Formats:** NIfTI
- **Access:** open
- **License:** This data is made available under the Creative Commons CC BY-SA 3.0 license (status: stated)
- **Source:** https://brain-development.org/ixi-dataset/
- **Page title (evidence):** IXI Dataset – Brain Development
- **Size:** not published on page (IXI-MRA.tar; a 517.3 MB IXI-HH MRA subset appears in the TopCoW zenodo record 15692630)
- **Acquisition parameters:** Page does not give MRA TR/TE/matrix. Sites: Hammersmith Philips 3T, Guy's Philips 1.5T, IoP GE 1.5T (page does not say which sites contributed MRA)
- **Sample file:** data/raw/ixi-mra/IXI002-Guys-0828-MRA.nii.gz

## Analysis

See the dated sample verification below.

## Notes from discovery

Tar not downloaded (size unknown, likely over limit).

## Sample verification — 2026-10-28

```yaml
format: NIfTI
shape: &id001
- 512
- 512
- 100
voxel_size_mm:
- 0.469
- 0.469
- 0.8
domain: image
static_or_dynamic: static
coil_count: unknown
fields_read:
- NIfTI dim
- NIfTI pixdim
inspected: true
basis: file header
sample_path: data/raw/ixi-mra/IXI002-Guys-0828-MRA.nii.gz
source_checked_at: '2026-10-28'
dimensions: *id001
```
