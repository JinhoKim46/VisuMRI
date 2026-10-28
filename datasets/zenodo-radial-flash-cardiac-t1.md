# zenodo-radial-flash-cardiac-t1

- **Anatomy:** T1 mapping
- **Formats:** BART cfl/hdr
- **Access:** open
- **License:** cc-by-4.0 (status: stated)
- **Source:** https://zenodo.org/records/5707688
- **Page title (evidence):** Data for: Free-Breathing Myocardial T1 Mapping using Inversion-Recovery Radial FLASH and Motion-Resolved Model-Based Reconstruction (Part 1/2) | Zenodo
- **Size:** 36.3 GB total (volunteer.tgz 4.2 MB; others 1.3-7.1 GB); Part 2/2 at https://zenodo.org/records/7350323 (not fetched by me)
- **Acquisition parameters:** not published on page (paper DOI 10.1002/mrm.29521)
- **Sample file:** data/raw/zenodo-radial-flash-cardiac-t1/volunteer.tgz

## Analysis

See the dated sample verification below.

## Sample verification — 2026-10-28

```yaml
format: BART cfl/hdr in TAR
dimensions:
- 256
- 218
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
header_member: volunteer/volunteer/MOLLI/apex/T1maps/vol9-MOLLI-apex.hdr
payload_member: volunteer/volunteer/MOLLI/apex/T1maps/vol9-MOLLI-apex.cfl
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
sample_path: data/raw/zenodo-radial-flash-cardiac-t1/volunteer.tgz
source_checked_at: '2026-10-28'
```
