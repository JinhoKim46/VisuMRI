# zenodo-sms-t1-radial-flash

- **Anatomy:** T1 mapping
- **Formats:** BART cfl/hdr
- **Access:** open
- **License:** cc-by-4.0 (status: stated)
- **Source:** https://zenodo.org/records/3969809
- **Page title (evidence):** Data for: Model-Based Reconstruction for Simultaneous Multi-Slice T1 Mapping using Single-Shot Inversion-Recovery Radial FLASH | Zenodo
- **Size:** 5.5 GB total; smallest archives e.g. brain-inter5.tgz 10.1 MB, brain-sms3-aligned.tgz 24.4 MB, phantom-sms3.tgz 60.3 MB
- **Acquisition parameters:** not published on page (paper DOI 10.1002/mrm.28497)
- **Sample file:** data/raw/zenodo-sms-t1-radial-flash/brain-inter5.tgz

## Analysis

See the dated sample verification below.

## Notes from discovery

Direct file URL not captured from page; files listed as brain-inter5.tgz etc. Raw k-space (non-Cartesian), BART format.

## Sample verification — 2026-10-28

```yaml
format: BART cfl/hdr in TAR
dimensions:
- 512
- 1
- 1
- 16
- 1
- 1
- 1
- 1
- 1
- 1
- 210
- 1
- 1
- 1
- 1
- 1
header_member: brain/inter5/vol_1-inter5-center.hdr
payload_member: brain/inter5/vol_1-inter5-center.cfl
coil_count: unknown
static_or_dynamic: unknown
domain: unknown
fields_read:
- 'BART # Dimensions'
- TAR member names and sizes
caveat: BART dimensions do not encode anatomy or axis semantics; domain and temporal
  behavior require acquisition documentation.
inspected: true
basis: file header
sample_path: data/raw/zenodo-sms-t1-radial-flash/brain-inter5.tgz
source_checked_at: '2026-10-28'
```
