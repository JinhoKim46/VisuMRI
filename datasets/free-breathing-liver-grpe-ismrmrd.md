# free-breathing-liver-grpe-ismrmrd

- **Anatomy:** liver
- **Formats:** ISMRMRD, HDF5
- **Access:** open
- **License:** cc-by-4.0 (status: stated)
- **Source:** https://zenodo.org/records/20758499
- **Page title (evidence):** Free-breathing MRI of the liver (Zenodo, v4, published June 19, 2026); earlier v3 https://zenodo.org/records/15849308 same title
- **Size:** 283.8 MB total: grpe_t1_free_breathing.mrd 104.7 MB, .seq 3.8 MB, displacement_fields.npy 175.3 MB (.mrd is >50 MB, not downloaded)
- **Acquisition parameters:** 3D Golden radial phase encoding (GRPE), free breathing, Pulseq sequence provided; field strength, matrix, TR/TE not published on page
- **Sample file:** data/raw/free-breathing-liver-grpe-ismrmrd/grpe_t1_free_breathing.mrd

## Analysis

Inspected from one sample file: `data/raw/free-breathing-liver-grpe-ismrmrd/grpe_t1_free_breathing.mrd` (header only).

- **Format:** ISMRMRD raw
- **Dimensions:** [154, 154, 154]
- **Coils:** 6
- **Static or dynamic:** unknown
- **Domain:** k-space
- **Fields read:** dataset/xml: encoding/encodedSpace/matrixSize, dataset/xml: acquisitionSystemInformation/receiverChannels, dataset/xml: measurementInformation/protocolName, dataset/data.shape, dataset/xml: encoding/encodingLimits/phase/maximum, dataset/xml: encoding/encodingLimits/repetition/maximum

**Note:** Protocol name is 'Test_short_libbalanceCheckOn_phantom': this is a phantom test scan, not a human liver. The k-space header is valid ISMRMRD.

## Sample verification — 2026-10-28

```yaml
format: ISMRMRD raw
encoding_matrix: &id001
- 154
- 154
- 154
coil_count: 6
acquisitions: 10800
domain: k-space
static_or_dynamic: unknown
phase_maximum: '0'
repetition_maximum: '0'
protocol_name: Test_short_libbalanceCheckOn_phantom
fields_read:
- 'dataset/xml: encoding/encodedSpace/matrixSize'
- 'dataset/xml: acquisitionSystemInformation/receiverChannels'
- 'dataset/xml: measurementInformation/protocolName'
- dataset/data.shape
- 'dataset/xml: encoding/encodingLimits/phase/maximum'
- 'dataset/xml: encoding/encodingLimits/repetition/maximum'
inspected: true
basis: file header
sample_path: data/raw/free-breathing-liver-grpe-ismrmrd/grpe_t1_free_breathing.mrd
source_checked_at: '2026-10-28'
dimensions: *id001
caveat: Source describes liver; header protocol name includes phantom. Temporal behavior
  and anatomy cannot be established from this header.
```
