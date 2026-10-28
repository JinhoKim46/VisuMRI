# msd-prostate

- **Anatomy:** prostate
- **Formats:** NIfTI
- **Access:** open
- **License:** AWS registry label says CC-BY-SA 4.0 International but links to CC BY 4.0; conflicting source evidence, license to verify. (status: license to verify)
- **Source:** https://registry.opendata.aws/msd/
- **Page title (evidence):** Medical Segmentation Decathlon - Registry of Open Data on AWS
- **Size:** not published for the prostate task on this page (tasks as tar.gz and uncompressed; s3://msd-for-monai, s3://msd-for-monai-eu)
- **Acquisition parameters:** not published on fetched page (medicaldecathlon.com could not be fetched)
- **Sample file:** data/raw/msd-prostate/prostate_16.nii.gz

## Analysis

Inspected from one sample file: `data/raw/msd-prostate/prostate_16.nii.gz` (header only).

- **Format:** NIfTI
- **Dimensions:** [320, 320, 20, 2]
- **Coils:** unknown
- **Static or dynamic:** unknown
- **Domain:** image
- **Fields read:** NIfTI dim, NIfTI pixdim

**Note:** The 4th dimension has length 2 and is not time; for MSD Task05 it is expected to be two MRI channels (T2 and ADC). Not confirmed from the file header alone; check the MSD dataset description.

## Notes from discovery

Task05 Prostate details (T2 + ADC, case count) not verified by fetch.

## Sample verification — 2026-10-28

```yaml
format: NIfTI
shape: &id001
- 320
- 320
- 20
- 2
voxel_size_mm:
- 0.625
- 0.625
- 3.6
domain: image
static_or_dynamic: unknown
coil_count: unknown
fields_read:
- NIfTI dim
- NIfTI pixdim
fourth_dimension_size: 2
inspected: true
basis: file header
sample_path: data/raw/msd-prostate/prostate_16.nii.gz
source_checked_at: '2026-10-28'
dimensions: *id001
caveat: Fourth dimension length 2 is not proof of time points; temporal semantics
  unknown from header.
```
