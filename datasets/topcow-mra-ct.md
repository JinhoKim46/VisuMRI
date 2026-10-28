# topcow-mra-ct

- **Anatomy:** angiography
- **Formats:** NIfTI
- **Access:** open
- **License:** CC BY-NC (Attribution-NonCommercial). By downloading the data you agree with the license terms. (CROWN subset: its own data usage agreement.) (status: stated)
- **Source:** https://topcow23.grand-challenge.org/data/
- **Page title (evidence):** Data - Topology-Aware Anatomical Segmentation of the Circle of Willis - Grand Challenge
- **Size:** not published on this page (patient counts only: 90 train, 5 val, 35 test, plus 20 CROWN MRAs). Zenodo record 15692630 lists 14.4 GB total; TopCoW2024_Data_Release.zip 10.5 GB
- **Acquisition parameters:** MRA: Siemens Skyra or Avanto Fit, 3T or 1.5T, TOF-3D or TOF-3D multi-slab; in-plane ~0.29-0.35 mm, slice ~0.5-0.6 mm. Paired CTA also included.
- **Sample file:** none recorded

## Analysis

Not inspected. No sample file was downloaded in this pass, so dimensions, coil count, and static-vs-dynamic are not yet recorded. Re-run `scripts/inspect_dataset.py` on one downloaded file to fill these in.

## Notes from discovery

Latest data on Zenodo https://zenodo.org/records/15692630 (page title 'TopCoW Training Data and External Testsets | Zenodo', fetched). Per-file licenses there: TopCoW2024_Data_Release.zip 'Open use. Must provide the source. Use for commercial purposes requires permission of the data owner.'; MRA_Lausanne.zip (1.3 GB) 'CC0 No Rights Reserved'; MRA_IXI_HH.zip (517.3 MB) 'Creative Commons CC BY-SA 3.0 license'. Separate record https://zenodo.org/records/10990868 (title 'TopCoW 2024 (2nd Edition): ...') carries only a PDF, license 'Creative Commons Attribution 4.0 International'.
