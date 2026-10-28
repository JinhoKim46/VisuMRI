# MRI sample collection status

32 datasets across eight anatomies. Raw data is local and gitignored.

| Dataset | Status | Header dimensions | Coils | Temporal | Domain |
|---|---|---|---|---|---|
| ixi-mra | inspected | [512, 512, 100] | unknown | static | image |
| prostatex | inspected | [128, 84] | unknown | unknown | image |
| msd-prostate | inspected | [320, 320, 20, 2] | unknown | unknown | image |
| ixi-brain | inspected | [256, 256, 150] | unknown | static | image |
| openneuro-ds000221-mpi-leipzig | inspected | [384, 512, 28] | unknown | static | image |
| ocmr-cardiac-cine | inspected | [512, 208, 1] | 15 | dynamic | k-space |
| free-breathing-liver-grpe-ismrmrd | inspected | [154, 154, 154] | 6 | unknown | k-space |
| zenodo-sms-t1-radial-flash | inspected | [512, 1, 1, 16, 1, 1, 1, 1, 1, 1, 210, 1, 1, 1, 1, 1] | unknown | unknown | unknown |
| zenodo-radial-flash-cardiac-t1 | inspected | [256, 218, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] | unknown | unknown | unknown |
| qsm-challenge-2016 | inspected | [160, 160, 160] | unknown | static | image |

## Documentation-only datasets

- **topcow-mra-ct**: Range HEAD probe: HTTP/1.1 200 OK, content-type: application/octet-stream, content-length: 10512833650. No ZIP downloaded because HTTP 206 was not returned.
- **topcow-zenodo-mra-lausanne**: Range probe did not return 206
- **picai-public**: Range HEAD probe: HTTP/1.1 200 OK, content-type: application/octet-stream, content-length: 5368893021. No ZIP downloaded because HTTP 206 was not returned.
- **fastmri-prostate**: Gated: requires provider approval/login; no authenticated download attempted.
- **fastmri-knee**: Gated: requires provider approval/login; no authenticated download attempted.
- **skm-tea-knee**: Gated: requires provider approval/login; no authenticated download attempted.
- **mridata-stanford-fse-knee-hf-mirror**: Public HDF5 download timed out after 300 seconds: 1,238,820,537 of 3,565,160,448 bytes received. Incomplete file removed; no header inspection attempted. Mirror license CC BY-NC 4.0; original mridata.org license unverified.
- **mrnet-knee**: Provider now links to Stanford Redivis. Its published distribution metadata requiresSubscription=true; no anonymous MRI download was available. Gated; license to verify.
- **fastmri-brain**: Gated: requires provider approval/login; no authenticated download attempted.
- **m4raw-brain**: Range probe did not return 206
- **calgary-campinas-brain**: Source routes downloads through CONP or a request form; no direct anonymous sample URL was verified. No form submitted.
- **cmrxrecon-2023-cardiac-kspace**: Gated: requires provider approval/login; no authenticated download attempted.
- **sunnybrook-cardiac-dicom**: Range HEAD probe: HTTP/1.1 200 OK, Content-Type: text/html; charset=UTF-8. No ZIP downloaded because HTTP 206 was not returned.
- **acdc-cardiac-cine**: Source links to Human Heart collection 637218c173e9f0047faa00fb. API lookup returned 404; alternate database endpoint timed out after 30 seconds. No sample URL verified.
- **chaos-liver-mri-dicom**: Range probe did not return 206
- **liverhccseg-multiphase-mri**: Range probe did not return 206
- **amos22-abdominal-mri**: Range probe did not return 206
- **cmrxrecon-t1-mapping**: Gated: requires provider approval/login; no authenticated download attempted.
- **rrsg2020-t1-challenge**: Range probe did not return 206
- **mpg-7t-trt-mp2rage**: Published FTP endpoint ftp://141.5.101.133/ timed out after 20 seconds. Alternative XNAT workflow not authenticated; license to verify.
- **qsm-challenge-2.0-sim**: Range probe did not return 206
- **qsm-consensus-example-data**: Range probe did not return 206

## Limits and validation

- Dimensions are header values. ISMRMRD dimensions are encoding matrices, not reconstructed image shapes.
- BART samples remain small TAR archives containing matched headers and complex payloads. Header dimensions and payload lengths were checked; axis semantics remain unknown.
- PROSTATEx sample is one DICOM image, not a complete series.
- Liver GRPE source/header anatomy discrepancy remains unresolved.
- Large ZIP downloads were skipped when the required HEAD range probe did not return 206. This records observed server behavior, not a permanent claim that ranges are unsupported.
- Safety checks cover unsafe names, existing-file preservation, TAR/ZIP fetching, BART dimensions/payload size, and visible malformed ISMRMRD errors.
- Supabase was not resynced.
- Changes and inspection status are published through PR #1; local raw files are not included.
