# fastmri-prostate

- **Anatomy:** prostate
- **Formats:** ISMRMRD, HDF5, DICOM
- **Access:** gated
- **License:** No separate license named. 'Each dataset has its own Data Sharing Agreement.' 'NYU fastMRI data may be used for internal research or educational purposes only' (status: stated)
- **Source:** https://fastmri.med.nyu.edu/
- **Page title (evidence):** fastMRI Dataset (heading: Welcome to the fastMRI Dataset); also NYU Data Catalog 'fastMRI' https://datacatalog.med.nyu.edu/dataset/10389
- **Size:** not published (312 exams)
- **Acquisition parameters:** 3T; axial T2W and axial DWI per exam. Coils/TR/TE/matrix not on fetched pages (Scientific Data paper 10.1038/s41597-024-03252-w could not be fetched, paywall redirect).
- **Sample file:** none recorded

## Analysis

Not inspected. No sample file was downloaded in this pass, so dimensions, coil count, and static-vs-dynamic are not yet recorded. Re-run `scripts/inspect_dataset.py` on one downloaded file to fill these in.

## Notes from discovery

Catalog page says raw data is vendor-neutral ISMRMRD and 'Application Required'. The word HDF5 for the prostate set was NOT confirmed on a fetched primary page; ISMRMRD files are HDF5 containers. Redistribution not allowed, so do not commit samples.
