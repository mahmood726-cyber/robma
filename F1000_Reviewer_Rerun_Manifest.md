# ROBMA Reproducibility Capsule: reviewer rerun manifest

This manifest is the shortest reviewer-facing rerun path for the local software package. It lists the files that should be sufficient to recreate one worked example, inspect saved outputs, and verify that the manuscript claims remain bounded to what the repository actually demonstrates.

## Reviewer Entry Points
- Project directory: `<repo-root>`.
- Preferred documentation start points: `README.md`, `f1000_artifacts/tutorial_walkthrough.md`.
- Detected public repository root: No project-specific public repository URL was detected locally; public release root pending.
- Detected public source snapshot: No fixed public source snapshot was detected locally.
- Detected public archive record: No project-specific DOI or Zenodo record URL was detected locally; archive registration pending.
- Environment capture files: `environment.yml`.
- Validation/test artifacts: `f1000_artifacts/validation_summary.md`, `f1000_artifacts/build_validation_summary.py`.

## Worked Example Inputs
- Manuscript-named example paths: `f1000_artifacts/example_dataset.csv` for a fixed reviewer example; `f1000_artifacts/tutorial_walkthrough.md` for the rerun narrative; `f1000_artifacts/validation_summary.md` for the local evidence map; f1000_artifacts/example_dataset.csv.
- Auto-detected sample/example files: `f1000_artifacts/example_dataset.csv`.

## Expected Outputs To Inspect
- A compact example bundle for ROBMA-oriented reporting.
- A tutorial walkthrough and validation summary.
- Submission-ready manuscript scaffolding with explicit scope limits.

## Minimal Reviewer Rerun Sequence
- Start with the README/tutorial files listed below and keep the manuscript paths synchronized with the public archive.
- Create the local runtime from the detected environment capture files if available: `environment.yml`.
- Run at least one named example path from the manuscript and confirm that the generated outputs match the saved validation materials.
- Quote one concrete numeric result from the local validation snippets below when preparing the final software paper.

## Local Numeric Evidence Available
- `f1000_artifacts/validation_summary.md` reports An inverse-variance checksum over the bundled effect/SE columns yields pooled effect 0.134 (SE 0.055; 95% CI 0.026 to 0.242).
