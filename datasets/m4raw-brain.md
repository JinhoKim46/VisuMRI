# m4raw-brain

- **Anatomy:** brain
- **Formats:** HDF5
- **Access:** open
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0). (status: stated)
- **Source:** https://zenodo.org/records/8056074
- **Page title (evidence):** M4Raw: A multi-contrast, multi-repetition, multi-channel MRI k-space dataset for low-field MRI research [V1.6] | Zenodo
- **Size:** 27.9 GB total (zips: test 5.0, GRE 4.8, motion 2.5, train 12.7, val 3.0 GB)
- **Acquisition parameters:** 0.3 T whole-body scanner (per https://github.com/mylyu/M4Raw); T1w, T2w, FLAIR (+GRE in V1.5); in-plane ~1.2 mm, through-plane 5 mm; 183 volunteers; coils/TR/TE not published on Zenodo page
- **Sample file:** none recorded

## Analysis

Not inspected. No sample file was downloaded in this pass, so dimensions, coil count, and static-vs-dynamic are not yet recorded. Re-run `scripts/inspect_dataset.py` on one downloaded file to fill these in.

## Notes from discovery

GitHub README lists a Google Drive sample folder for one subject (https://drive.google.com/drive/folders/1RQT9oqoBd0xsevhyKSCxKiLuoEb2erhB); size not verified, so not recorded as sample_file_url. Corroborating pages: https://github.com/mylyu/M4Raw, https://huggingface.co/datasets/mylyu/M4Raw_brain (cc-by-4.0).
