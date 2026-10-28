# Literature review: visualization layouts and styles by data type

Scope: display recommendations for each MRI data type that VisuMRI will show. Organized by data type, not anatomy. Every reference is in `kb/references.yaml` with its citation, DOI or URL, and verification note. Reference ids below link to that file.

**Read this first:**
- The paper named in the request, PubMed 42640344, is about **MRCP** (T2 fluid-bright MRI of the bile ducts), not contrast MRA. Its idea (segment, then suppress overlapping secondary bright structures before the MIP) is transferable, but its evidence is for MRCP.
- Several sources were verified from Crossref metadata only, not the full text. Their recommendation lines rest on abstracts or search summaries. The entries say which.
- Some areas have little or no support in the sources found. Those are listed under "Gaps".

## 1. Static 3D volumes (orthogonal / MPR, orientation convention)

- **Recommend:** show orthogonal views, and define the left-right orientation rather than assuming one. A neurological (patient right on image right) or radiological (patient left on image right) convention is a display choice. Derive the convention from the voxel-to-world matrix and let the viewer flip it. ([nibabel-neuro-radio-conventions], [fieldtrip-plotting-convention])
- **Measurements:** measure on double-oblique MPR planes perpendicular to the vessel centerline. ([scmr-2020-postprocessing])
- **Quantitative images** (see section 4) also apply here.

## 2. Dynamic / time-series (cine loop, x-t)

- **Recommend:** show cine loops together, with the long-axis views alongside the short-axis stack. ([scmr-2020-postprocessing], [kramer-2020-cmr-protocols])
- **x-t (M-mode):** show an x-t strip from a user-drawn line beside the cine, with markers for end-systole and the onset of peak contraction, plus a percent-contraction curve. ([pednekar-2011-mmode-cine], conference abstract, weak)
- **Gap:** no guideline found for generic cine loop or x-t display settings for non-cardiac dynamic data. [kramer-2020-cmr-protocols] specifies the plane set only.

## 3. Angiography (MIP, rotating MIP, secondary-anatomy removal)

- **Secondary-anatomy removal (the requested idea):** segment the volume into primary and secondary structures, then suppress overlapping bright secondary anatomy before the MIP. The reported reader scores improved overlap (3.5 vs 2.5) and confidence (3.4 vs 3.2) on a 4-point scale. This is MRCP, not MRA. ([pubmed-42640344])
- **Projections:** show MIP over a full range of angles (about 180 degrees) to see overlap. Use limited-volume or thin slab MIPs to reduce overlap. ([tanenbaum-2002-mra-rendering])
- **Boundaries:** crop or edit the volume boundaries before the MIP, so unwanted structures do not project over vessels. ([tsuruda-1992-mra-artifacts])
- **Source images:** keep the source images available and check them. Projections alone can mislead. ([tanenbaum-2002-mra-rendering], [tsuruda-1992-mra-artifacts])
- **MIP vs volume rendering:** MIP loses depth. Offer both and choose by task. ([fishman-2006-vr-vs-mip] — **CT angiography**, not MRI)

## 4. Quantitative maps (T1/T2/QSM colormaps)

- **Avoid rainbow / jet colormaps.** Use perceptually uniform maps matched to the data (sequential vs diverging), colour-vision-deficiency safe, never stretched, and always with a colour bar. ([crameri-2020-misuse-colour])
- **Relaxometry (T1, T2, T2*):** use the log-processed Lipari colormap for T1/R1 and log-processed Navia for T2/T2*/R2/R2*. Show invalid (0) values as black. Include numbered colour bar with units. Use the same maps for all anatomies. ([fuderer-2025-relaxometry-colormaps], full text fetched from PMC; the ISMRM endorsement wording was removed from the citation because it was not confirmed)
- **Ranges:** set the colour look-up table to site-specific normal ranges, or use greyscale with processing that highlights abnormality. ([messroghli-2017-scmr-mapping], [scmr-2020-postprocessing])
- **QSM:** default to linear greyscale (about -0.2 to +0.2 ppm for healthy brain) or a linear perceptually uniform colormap, not jet. State the window, mask to the reliable region, report ppm and the reference region. ([qsm-consensus-2024])

## 5. k-space and coil display

- **Coil combination for display:** optimal SNR combination, or root-sum-of-squares of coil magnitudes (near-optimal at high SNR; raises the noise floor in dark regions and loses phase). ([roemer-1990-nmr-phased-array])
- **Coil mosaic:** show multi-coil k-space and per-coil images as a mosaic. Ground truth is the RSS of coil images, center-cropped to 320×320 in fastMRI figures. ([zbontar-2018-fastmri], [knoll-2020-fastmri-dataset])
- **Gap:** no standalone source found on log-magnitude k-space display. The only support is general dynamic-range background. Treat log-magnitude k-space as an untested default and verify it in the first viewer build.

## 6. Reconstruction comparison (side-by-side, difference, metrics)

- **Layout:** zero-filled, model reconstruction, and ground truth side by side. Report NMSE, PSNR, and SSIM (7×7 window, k1=0.01, k2=0.03). ([zbontar-2018-fastmri], [wang-2004-ssim])
- **Metrics alone are not enough.** Judge with quantitative metrics first, then a blinded radiologist assessment. ([knoll-2020-fastmri-challenge-overview], [muckley-2021-fastmri-challenge])
- **Use several metrics and the images.** RMSE and SSIM alone correlated poorly with radiologist scores in one study. Show failure modes (lost or hallucinated small pathology) visually. ([mason-2020-iqm-vs-radiologists], [muckley-2021-fastmri-challenge])

## Gaps and caveats

- **Weakest evidence:** k-space display (section 5), generic cine and x-t display (section 2), and rotating MIP (section 3, only the 180-degree projection note).
- **Old sources:** [tsuruda-1992-mra-artifacts] and [tanenbaum-2002-mra-rendering] are older, and their recommendations are for MRA practice of that time.
- **Crossref-only:** Kramer 2020, Roemer 1990, Fishman 2006, Wang 2004, Mason 2020, and the Knoll papers. Their lines rest on abstracts.
- **Not MRI:** [fishman-2006-vr-vs-mip] is CT.
- **Next step:** search for a 2023–2026 source on dynamic and cine display, and for a log-magnitude k-space display reference, before relying on either.
