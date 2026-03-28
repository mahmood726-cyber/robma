# ROBMA Reproducibility Capsule: concrete submission fixes

This file converts the multi-persona review into repository-side actions that should be checked before external submission of the F1000 software paper for `ROBMA`.

## Detectable Local State
- Documentation files detected: `README.md`, `f1000_artifacts/tutorial_walkthrough.md`.
- Environment lock or container files detected: `environment.yml`.
- Package manifests detected: none detected.
- Example data files detected: `f1000_artifacts/example_dataset.csv`.
- Validation artifacts detected: `f1000_artifacts/validation_summary.md`, `f1000_artifacts/build_validation_summary.py`.
- Detected public repository root: No project-specific public repository URL was detected locally; public release root pending.
- Detected public source snapshot: No fixed public source snapshot was detected locally.
- Detected public archive record: No project-specific DOI or Zenodo record URL was detected locally; archive registration pending.

## High-Priority Fixes
- Check that the manuscript's named example paths exist in the public archive and can be run without repository archaeology.
- Add the public repository root when the external archive is finalized; no project-specific repository URL was detected locally.
- Archive the tagged release and insert the Zenodo DOI or record URL once it has been minted; no project-specific archive DOI was detected locally.
- Reconfirm the quoted benchmark or validation sentence after the final rerun so the narrative text matches the shipped artifacts.

## Numeric Evidence Available To Quote
- `f1000_artifacts/validation_summary.md` reports An inverse-variance checksum over the bundled effect/SE columns yields pooled effect 0.134 (SE 0.055; 95% CI 0.026 to 0.242).

## Manuscript Files To Keep In Sync
- `F1000_Software_Tool_Article.md`
- `F1000_Reviewer_Rerun_Manifest.md`
- `F1000_MultiPersona_Review.md`
- `F1000_Submission_Checklist_RealReview.md` where present
- README/tutorial files and the public repository release metadata
