# ROBMA: a software tool for reproducible evidence-synthesis and modeling workflows

## Installation
Use `environment.yml` to create a clean local environment before running analyses.
Document any package-version mismatch encountered during first run.

## Quick Start
1. Open the primary project entry file.
2. Load `f1000_artifacts/example_dataset.csv`.
3. Run `python f1000_artifacts/build_validation_summary.py` to regenerate the reviewer checksum summary.
4. Inspect `f1000_artifacts/validation_summary.md` and confirm the expected capsule metrics and leave-one-out range.
5. Export outputs and cross-check against listed evidence artifacts.

## F1000 Package
- Manuscript: `F1000_Software_Tool_Article.md`
- Submission checklist: `F1000_Submission_Checklist_RealReview.md`
