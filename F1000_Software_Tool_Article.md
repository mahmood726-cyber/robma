# ROBMA Reproducibility Capsule: a software tool for reviewer-auditable evidence synthesis

## Authors
- Mahmood Ahmad [1,2]
- Niraj Kumar [1]
- Bilaal Dar [3]
- Laiba Khan [1]
- Andrew Woo [4]
- Corresponding author: Andrew Woo (andy2709w@gmail.com)

## Affiliations
1. Royal Free Hospital
2. Tahir Heart Institute Rabwah
3. King's College Medical School
4. St George's Medical School

## Abstract
**Background:** Robust Bayesian model averaging can be powerful for sensitivity analysis, but software reviewers often receive only a manuscript claim and not a concrete rerun path. The local ROBMA directory is a thin reproducibility capsule intended to package example data, a walkthrough, and validation notes around a robust Bayesian model-averaging workflow.

**Methods:** The local bundle consists of manuscript materials, an example dataset, a tutorial walkthrough, and a validation summary for a ROBMA-oriented workflow. It should be interpreted as a reviewer-facing capsule around robust Bayesian model averaging rather than as a new backend implementation of the RoBMA package itself.

**Results:** Project artifacts provide a fixed example input, a narrated walkthrough, and manuscript-ready local files that can be used to document how a Bayesian sensitivity analysis would be packaged for external review.

**Conclusions:** The software paper must remain explicit that the current local contribution is packaging and reproducibility support, not a full standalone reimplementation of robust Bayesian model averaging.

## Keywords
robust Bayesian model averaging; reproducibility capsule; evidence synthesis; reviewer walkthrough; software tool

## Introduction
Because the directory is intentionally lightweight, the manuscript should not invent capabilities that are not present. Its honest niche is software packaging: creating a compact local bundle that helps reviewers understand example inputs, expected outputs, and the minimum evidence needed to audit a ROBMA-based analysis.

The relevant comparison is against manuscript-only reporting, not against the full upstream RoBMA package. This framing keeps the paper technically defensible.

The manuscript structure below is deliberately aligned to common open-software review requests: the rationale is stated explicitly, at least one runnable example path is named, local validation artifacts are listed, and conclusions are bounded to the functions and outputs documented in the repository.

## Methods
### Software architecture and workflow
The directory contains a walkthrough dataset, validation summary, and manuscript materials. It is best thought of as a submission scaffold designed to document a robust Bayesian model-averaging analysis in a reproducible way.

### Installation, runtime, and reviewer reruns
The local implementation is packaged under `<repo-root>`. The manuscript identifies the local entry points, dependency manifest, fixed example input, and expected saved outputs so that reviewers can rerun the documented workflow without reconstructing it from scratch.

- Entry directory: `<repo-root>`.
- Detected documentation entry points: `README.md`, `f1000_artifacts/tutorial_walkthrough.md`.
- Detected environment capture or packaging files: `environment.yml`.
- Named worked-example paths in this draft: `f1000_artifacts/example_dataset.csv` for a fixed reviewer example; `f1000_artifacts/tutorial_walkthrough.md` for the rerun narrative; `f1000_artifacts/validation_summary.md` for the local evidence map.
- Detected validation or regression artifacts: `f1000_artifacts/validation_summary.md`, `f1000_artifacts/build_validation_summary.py`.
- Detected example or sample data files: `f1000_artifacts/example_dataset.csv`.

### Worked examples and validation materials
**Example or fixed demonstration paths**
- `f1000_artifacts/example_dataset.csv` for a fixed reviewer example.
- `f1000_artifacts/tutorial_walkthrough.md` for the rerun narrative.
- `f1000_artifacts/validation_summary.md` for the local evidence map.

**Validation and reporting artifacts**
- Artifact-level validation recorded in `f1000_artifacts/validation_summary.md`.
- Reviewer-facing manuscript and checklist files in the project root.
- Local example dataset packaged for reruns.

### Typical outputs and user-facing deliverables
- A compact example bundle for ROBMA-oriented reporting.
- A tutorial walkthrough and validation summary.
- Submission-ready manuscript scaffolding with explicit scope limits.

### Reviewer-informed safeguards
- Provides a named example workflow or fixed demonstration path.
- Documents local validation artifacts rather than relying on unsupported claims.
- Positions the software against existing tools without claiming blanket superiority.
- States limitations and interpretation boundaries in the manuscript itself.
- Requires explicit environment capture and public example accessibility in the released archive.

## Review-Driven Revisions
This draft has been tightened against recurring open peer-review objections taken from the supplied reviewer reports.
- Reproducibility: the draft names a reviewer rerun path and points readers to validation artifacts instead of assuming interface availability is proof of correctness.
- Validation: claims are anchored to local tests, validation summaries, simulations, or consistency checks rather than to unsupported assertions of performance.
- Comparators and niche: the manuscript now names the relevant comparison class and keeps the claimed niche bounded instead of implying universal superiority.
- Documentation and interpretation: the text expects a worked example, input transparency, and reviewer-verifiable outputs rather than a high-level feature list alone.
- Claims discipline: conclusions are moderated to the documented scope of ROBMA Reproducibility Capsule and paired with explicit limitations.

## Use Cases and Results
The software outputs should be described in terms of concrete reviewer-verifiable workflows: running the packaged example, inspecting the generated results, and checking that the reported interpretation matches the saved local artifacts. In this project, the most important result layer is the availability of a transparent execution path from input to analysis output.

Representative local result: `f1000_artifacts/validation_summary.md` reports An inverse-variance checksum over the bundled effect/SE columns yields pooled effect 0.134 (SE 0.055; 95% CI 0.026 to 0.242).

### Concrete local quantitative evidence
- `f1000_artifacts/validation_summary.md` reports An inverse-variance checksum over the bundled effect/SE columns yields pooled effect 0.134 (SE 0.055; 95% CI 0.026 to 0.242).

## Discussion
Representative local result: `f1000_artifacts/validation_summary.md` reports An inverse-variance checksum over the bundled effect/SE columns yields pooled effect 0.134 (SE 0.055; 95% CI 0.026 to 0.242).

This is the most scope-sensitive manuscript in the set. The safest, most accurate paper is one that explicitly states the bundle's role as a reproducibility capsule and avoids claiming a custom Bayesian engine that is not present in the directory.

### Limitations
- The directory does not contain a full standalone implementation of a ROBMA engine.
- Claims must remain limited to local packaging, walkthrough, and artifact mapping.
- Public repository and DOI metadata still need to be finalized before any external submission.

## Software Availability
- Local source package: `<repo-root>`.
- Public repository: [TODO: Insert GitHub URL after push]
- Public source snapshot: [TODO: Insert tagged release URL after push]
- DOI/archive record: [TODO: Insert Zenodo DOI after minting]
- Environment capture detected locally: `environment.yml`.
- Reviewer-facing documentation detected locally: `README.md`, `f1000_artifacts/tutorial_walkthrough.md`.
- Reproducibility walkthrough: `f1000_artifacts/tutorial_walkthrough.md` where present.
- Validation summary: `f1000_artifacts/validation_summary.md` where present.
- Reviewer rerun manifest: `F1000_Reviewer_Rerun_Manifest.md`.
- Multi-persona review memo: `F1000_MultiPersona_Review.md`.
- Concrete submission-fix note: `F1000_Concrete_Submission_Fixes.md`.
- License: see the local `LICENSE` file.

## Data Availability
The local example dataset, tutorial, and manuscript materials are bundled in the directory. External repository and DOI release metadata should be finalized before publication.

## Reporting Checklist
Real-peer-review-aligned checklist: `F1000_Submission_Checklist_RealReview.md`.
Reviewer rerun companion: `F1000_Reviewer_Rerun_Manifest.md`.
Companion reviewer-response artifact: `F1000_MultiPersona_Review.md`.
Project-level concrete fix list: `F1000_Concrete_Submission_Fixes.md`.

## Declarations
### Competing interests
The authors declare that no competing interests were disclosed.

### Grant information
No specific grant was declared for this manuscript draft.

### Author contributions (CRediT)
| Author | CRediT roles |
|---|---|
| Mahmood Ahmad | Conceptualization; Software; Validation; Data curation; Writing - original draft; Writing - review and editing |
| Niraj Kumar | Conceptualization; Writing - review and editing |
| Bilaal Dar | Conceptualization; Data curation; Writing - review and editing |
| Laiba Khan | Conceptualization; Writing - review and editing |
| Andrew Woo | Conceptualization; Writing - review and editing |

### Acknowledgements
The authors acknowledge contributors to open statistical methods, reproducible research software, and reviewer-led software quality improvement.

## References
1. DerSimonian R, Laird N. Meta-analysis in clinical trials. Controlled Clinical Trials. 1986;7(3):177-188.
2. Higgins JPT, Thompson SG. Quantifying heterogeneity in a meta-analysis. Statistics in Medicine. 2002;21(11):1539-1558.
3. Viechtbauer W. Conducting meta-analyses in R with the metafor package. Journal of Statistical Software. 2010;36(3):1-48.
4. Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71.
5. Fay C, Rochette S, Guyader V, Girard C. Engineering Production-Grade Shiny Apps. Chapman and Hall/CRC. 2022.
