from __future__ import annotations

import csv
from pathlib import Path

# Use fixed date for reproducibility (matches original validation run)
VALIDATION_DATE = "2026-03-19"


ROOT = Path(__file__).resolve().parent
DATASET = ROOT / "example_dataset.csv"
OUTPUT = ROOT / "validation_summary.md"
REQUIRED_COLUMNS = ["study_id", "dose", "events", "total", "effect", "se"]


def main() -> None:
    with DATASET.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise ValueError("example_dataset.csv is empty")

    fieldnames = list(rows[0].keys())
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    missing_core_values = sum(
        1
        for row in rows
        for column in REQUIRED_COLUMNS
        if str(row.get(column, "")).strip() == ""
    )

    effects = [float(row["effect"]) for row in rows]
    standard_errors = [float(row["se"]) for row in rows]
    totals = [int(float(row["total"])) for row in rows]
    events = [int(float(row["events"])) for row in rows]
    doses = [float(row["dose"]) for row in rows]

    weights = [1.0 / (se * se) for se in standard_errors]
    pooled_effect = sum(weight * effect for weight, effect in zip(weights, effects)) / sum(weights)
    pooled_se = (1.0 / sum(weights)) ** 0.5
    ci_low = pooled_effect - 1.96 * pooled_se
    ci_high = pooled_effect + 1.96 * pooled_se

    leave_one_out = []
    for index in range(len(rows)):
        reduced_weights = [weight for i, weight in enumerate(weights) if i != index]
        reduced_effects = [effect for i, effect in enumerate(effects) if i != index]
        pooled = sum(weight * effect for weight, effect in zip(reduced_weights, reduced_effects)) / sum(reduced_weights)
        leave_one_out.append(pooled)

    markdown = "\n".join(
        [
            "# Validation Summary",
            "",
            f"Updated: {VALIDATION_DATE}",
            "",
            "This file supports real peer-review expectations for transparent testing and reproducibility.",
            "",
            "## Validation Inputs",
            "- Example dataset used for walkthrough: `f1000_artifacts/example_dataset.csv`.",
            "- Validation summary generator: `f1000_artifacts/build_validation_summary.py`.",
            "- Validation scope: schema integrity and deterministic checksum metrics for the shipped reviewer example.",
            "",
            "## Validation Checks",
            f"- Required columns present: {len(REQUIRED_COLUMNS)}/{len(REQUIRED_COLUMNS)} (`{', '.join(REQUIRED_COLUMNS)}`).",
            f"- Example dataset size: {len(rows)} study rows, {len(fieldnames)} columns, {sum(totals)} total participants, {sum(events)} total events.",
            f"- Core-field missingness: {missing_core_values} blank required cells.",
            f"- Dose range in the shipped example: {min(doses):.0f} to {max(doses):.0f}.",
            "",
            "## Deterministic Checksum Metrics",
            (
                f"- The bundled example dataset contains {len(rows)} studies ({sum(totals)} participants; {sum(events)} events) across "
                f"{len(REQUIRED_COLUMNS)} required fields with {missing_core_values} missing core values."
            ),
            (
                f"- An inverse-variance checksum over the bundled effect/SE columns yields pooled effect {pooled_effect:.3f} "
                f"(SE {pooled_se:.3f}; 95% CI {ci_low:.3f} to {ci_high:.3f})."
            ),
            (
                f"- Leave-one-out checksum pooled effects range from {min(leave_one_out):.3f} to {max(leave_one_out):.3f}, "
                "which provides a simple reviewer-auditable sensitivity bound for the example bundle."
            ),
            "",
            "## Reviewer Use",
            "- Re-run `python f1000_artifacts/build_validation_summary.py` after changing the example data or walkthrough expectations.",
            "- Use the reported checksum metrics to confirm that the shipped example file matches the manuscript and tutorial narrative.",
            "- Keep claims bounded to capsule reproducibility and artifact auditability; these checks do not claim a full local reimplementation of ROBMA.",
            "",
        ]
    )

    OUTPUT.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
