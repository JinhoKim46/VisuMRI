# prostatex

- **Anatomy:** prostate
- **Formats:** DICOM, MHD/ZRAW
- **Access:** open
- **License:** CC BY 3.0. Data Citation Required: Users must abide by the TCIA Data Usage Policy and Restrictions. (status: stated)
- **Source:** https://www.cancerimagingarchive.net/collection/prostatex/
- **Page title (evidence):** PROSTATEx - The Cancer Imaging Archive (TCIA)
- **Size:** 16.67 GB total; DICOM images 16.18 GB; Ktrans/lesion/thumbnails 498 MB
- **Acquisition parameters:** 3T Siemens MAGNETOM Trio and Skyra, no endorectal coil. T2 TSE ~0.5 mm in-plane, 3.6 mm slice; PD + DCE 3D turbo flash ~1.5 mm in-plane, 4 mm slice, 3.5 s temporal; DWI ss-EPI 2 mm in-plane, 3.6 mm slice, b=50/400/800. TR/TE not on page.
- **Sample file:** data/raw/prostatex/00000001.dcm

## Analysis

Inspected from one sample file: `data/raw/prostatex/00000001.dcm` (header only).

- **Format:** DICOM
- **Dimensions:** [128, 84]
- **Coils:** unknown
- **Static or dynamic:** unknown
- **Domain:** image
- **Fields read:** Rows, Columns, Modality, SeriesDescription, SequenceName, MagneticFieldStrength

**Note:** One slice from a DWI (diffusion) series, not a T2 series. The sample alone does not show the full ProstateX protocol.

## Notes from discovery

Download requires TCIA Data Retriever (Aspera for Ktrans). Open, no login on page.

## Sample verification — 2026-10-28

```yaml
format: DICOM
dimensions:
- 128
- 84
coil_count: unknown
static_or_dynamic: unknown
fields_read:
- Rows
- Columns
- Modality
- SeriesDescription
- SequenceName
- MagneticFieldStrength
file_count: 1
modality: MR
series_description: ep2d_diff_tra_DYNDIST_MIXCALC_BVAL
sequence_name: '*ep_b50_800'
field_strength_t: 3.0
domain: image
inspected: true
basis: file header
sample_path: data/raw/prostatex/00000001.dcm
source_checked_at: '2026-10-28'
```
