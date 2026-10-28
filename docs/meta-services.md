# Meta services for VisuMRI — suggestions

Status key: **verified** = confirmed by a search this session; **unverified** = named from memory, check before relying on it.

| Service / model | Status | What it could do for VisuMRI |
|---|---|---|
| **SAM 3** (Segment Anything with Concepts) | verified: released 2025-11-19; open code and checkpoints under the SAM License | Per-segment masks from a short noun phrase (e.g. "liver", "vessel", "prostate"), which fits the per-segment details feature. Also the basis for removing secondary anatomy before MIP. |
| **SAM 2** (video segmentation) | unverified (known Meta release; not searched this session) | Propagating a mask through a cine or dynamic series, one frame to the next. Useful for dynamic data (cardiac cine, dynamic contrast). |
| **Llama API** (`META_API_KEY`, probably this) | verified: a Llama API exists, currently a limited preview with a waitlist; the key page is at llama.developer.meta.com/docs. Confirm that `META_API_KEY` is for this service. | Reading the acquisition header and suggesting a reconstruction method, or drafting a plain-language acquisition summary. The LLM would not touch raw k-space. |
| **DINOv3** | verified: released 2025-08; pre-trained models with a license that allows commercial use | Image embeddings for quality control and for retrieving similar datasets and references from the knowledge base. |
| **V-JEPA 2** | verified as a model (1.2B params); release license not confirmed | Video-level embeddings for dynamic and cine data, for classifying the motion type. |
| **Nougat** | unverified (not found in this session's search) | Turning reference PDFs in the knowledge base into text, so each new reference can be indexed when it is added. |
| **CoTracker** | unverified (not found in this session's search) | Point tracking across a cine series, to measure motion for dynamic display. |

## Notes

- Check each license before any commercial use. SAM 3 is under the SAM License. Confirm DINOv3 and V-JEPA 2 terms on their pages.
- The Llama API is in preview, so plan for an outage. Keep every feature working without it.
- None of these is required for v0. v0 is data collection and literature review only; these are for later stages.
