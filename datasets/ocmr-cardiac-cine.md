# ocmr-cardiac-cine

- **Anatomy:** cardiac
- **Formats:** ISMRMRD, HDF5
- **Access:** open
- **License:** No named license. Terms and Conditions page: 'I will utilize this dataset only for research and educational purposes.' 'I will neither sell this dataset or its components nor monetize from it.' 'I acknowledge that all datasets derived from the OCMR dataset are also subject to these terms and conditions.' Must cite https://arxiv.org/abs/2008.03410 (status: license to verify)
- **Source:** https://ocmr.info/instructions/
- **Page title (evidence):** Downloading Instructions | OCMR (also fetched https://ocmr.info/ 'OCMR-Open-Access Multi-Coil k-Space Dataset for Cardiovascular Magnetic Resonance Imaging' and https://ocmr.info/download/ 'Terms and Conditions | OCMR')
- **Size:** Home page (as of Aug 11 2023): fully sampled 165 files/279 slices; prospectively undersampled 212 files/842 slices. Full tarball size not stated ('large'): https://ocmr.s3.amazonaws.com/data/ocmr_cine.tar.gz (do NOT download; subset download via https://github.com/MRIOSU/OCMR)
- **Acquisition parameters:** not published on fetched pages (only: some fully sampled data from 0.55T Free.Max; params struct has FOV, TRes, flipAngle_deg, sequence_type; kData dims kx,ky,kz,coil,phase,set,slice,rep,avg)
- **Sample file:** none recorded

## Analysis

Not inspected. No sample file was downloaded in this pass, so dimensions, coil count, and static-vs-dynamic are not yet recorded. Re-run `scripts/inspect_dataset.py` on one downloaded file to fill these in.
