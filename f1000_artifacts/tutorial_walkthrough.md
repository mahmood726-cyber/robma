# Tutorial Walkthrough

Updated: 2026-03-06

1. Open the documented project entry file in `README.md`.
2. Load example dataset: `f1000_artifacts/example_dataset.csv`.
3. Rebuild the checksum summary with `python f1000_artifacts/build_validation_summary.py`.
4. Confirm the expected capsule metrics in `f1000_artifacts/validation_summary.md`: 4 study rows, 540 participants, 82 events, pooled checksum effect 0.134 (SE 0.055; 95% CI 0.026 to 0.242).
5. Compare the leave-one-out checksum range in the same file (0.100 to 0.193) against the current dataset to confirm the shipped example was not altered silently.
6. Keep conclusions bounded to capsule reproducibility and reviewer auditability rather than claiming a full local ROBMA engine.
