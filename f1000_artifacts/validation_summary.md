# Validation Summary

Updated: 2026-03-19

This file supports real peer-review expectations for transparent testing and reproducibility.

## Validation Inputs
- Example dataset used for walkthrough: `f1000_artifacts/example_dataset.csv`.
- Validation summary generator: `f1000_artifacts/build_validation_summary.py`.
- Validation scope: schema integrity and deterministic checksum metrics for the shipped reviewer example.

## Validation Checks
- Required columns present: 6/6 (`study_id, dose, events, total, effect, se`).
- Example dataset size: 4 study rows, 6 columns, 540 total participants, 82 total events.
- Core-field missingness: 0 blank required cells.
- Dose range in the shipped example: 0 to 30.

## Deterministic Checksum Metrics
- The bundled example dataset contains 4 studies (540 participants; 82 events) across 6 required fields with 0 missing core values.
- An inverse-variance checksum over the bundled effect/SE columns yields pooled effect 0.134 (SE 0.055; 95% CI 0.026 to 0.242).
- Leave-one-out checksum pooled effects range from 0.100 to 0.193, which provides a simple reviewer-auditable sensitivity bound for the example bundle.

## Reviewer Use
- Re-run `python f1000_artifacts/build_validation_summary.py` after changing the example data or walkthrough expectations.
- Use the reported checksum metrics to confirm that the shipped example file matches the manuscript and tutorial narrative.
- Keep claims bounded to capsule reproducibility and artifact auditability; these checks do not claim a full local reimplementation of ROBMA.
