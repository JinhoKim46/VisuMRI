# ocmr-cardiac-cine

- **Anatomy:** cardiac
- **Formats:** ISMRMRD, HDF5
- **Access:** open
- **License:** No named license. Terms and Conditions page: 'I will utilize this dataset only for research and educational purposes.' 'I will neither sell this dataset or its components nor monetize from it.' 'I acknowledge that all datasets derived from the OCMR dataset are also subject to these terms and conditions.' Must cite https://arxiv.org/abs/2008.03410 (status: license to verify)
- **Source:** https://ocmr.info/instructions/
- **Page title (evidence):** Downloading Instructions | OCMR (also fetched https://ocmr.info/ 'OCMR-Open-Access Multi-Coil k-Space Dataset for Cardiovascular Magnetic Resonance Imaging' and https://ocmr.info/download/ 'Terms and Conditions | OCMR')
- **Size:** Home page (as of Aug 11 2023): fully sampled 165 files/279 slices; prospectively undersampled 212 files/842 slices. Full tarball size not stated ('large'): https://ocmr.s3.amazonaws.com/data/ocmr_cine.tar.gz (do NOT download; subset download via https://github.com/MRIOSU/OCMR)
- **Acquisition parameters:** not published on fetched pages (only: some fully sampled data from 0.55T Free.Max; params struct has FOV, TRes, flipAngle_deg, sequence_type; kData dims kx,ky,kz,coil,phase,set,slice,rep,avg)
- **Sample file:** data/raw/ocmr-cardiac-cine/fs_0001_1_5T.h5

## Analysis

Inspected from one sample file: `data/raw/ocmr-cardiac-cine/fs_0001_1_5T.h5` (header only).

- **Format:** ISMRMRD raw
- **Dimensions:** [512, 208, 1]
- **Coils:** 15
- **Static or dynamic:** dynamic
- **Domain:** k-space
- **Fields read:** dataset/xml: encoding/encodedSpace/matrixSize, dataset/xml: acquisitionSystemInformation/receiverChannels, dataset/xml: measurementInformation/protocolName, dataset/data.shape, dataset/xml: encoding/encodingLimits/phase/maximum, dataset/xml: encoding/encodingLimits/repetition/maximum

**Note:** Dynamic is inferred from the ISMRMRD phase-encoding maximum (18). That index is taken to be the cardiac phase; the cine loop is not checked against the image.

## Sample verification — 2026-10-28

```yaml
format: ISMRMRD raw
encoding_matrix: &id001
- 512
- 208
- 1
coil_count: 15
acquisitions: 3952
domain: k-space
static_or_dynamic: dynamic
phase_maximum: '18'
repetition_maximum: '0'
protocol_name: trufi_cine_4ch_prop_trigger
fields_read:
- 'dataset/xml: encoding/encodedSpace/matrixSize'
- 'dataset/xml: acquisitionSystemInformation/receiverChannels'
- 'dataset/xml: measurementInformation/protocolName'
- dataset/data.shape
- 'dataset/xml: encoding/encodingLimits/phase/maximum'
- 'dataset/xml: encoding/encodingLimits/repetition/maximum'
inspected: true
basis: file header
sample_path: data/raw/ocmr-cardiac-cine/fs_0001_1_5T.h5
source_checked_at: '2026-10-28'
dimensions: *id001
```
