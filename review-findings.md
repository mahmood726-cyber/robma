## Multi-Persona Review: ROBMA (F1000 Capsule + E156 + Dashboard)
### Date: 2026-03-28
### Summary: 4 P0, 6 P1, 5 P2

#### P0 -- Critical
- **P0-1** [SWE]: LOO chart values in dashboard are wrong — 0.150/0.120 should be 0.138/0.111 (dashboard.html:905)
  - Fix: Replace data array with correct values
- **P0-2** [Domain+SWE]: "byte-identical output" claim false — date.today() changes daily (build_validation_summary.py:56)
  - Fix: Use fixed date or change to "numerically identical"
- **P0-3** [SWE+Domain]: environment.yml has R deps but no R code exists; README references missing files
  - Fix: Remove R deps, update README
- **P0-4** [Domain]: No public repo or DOI — F1000 submission HARD-BLOCKED
  - Fix: Create GitHub repo, push, mint Zenodo DOI

#### P1 -- Important
- **P1-1** [Security]: CDN Chart.js lacks SRI integrity hash (dashboard.html:7)
- **P1-2** [Domain]: 4/5 authors with only "Conceptualization" risks ICMJE challenge
- **P1-3** [SWE]: "Expected output" box but script writes to file, not stdout
- **P1-4** [SWE+Domain]: Absolute Windows paths in manuscript (C:\Models\ROBMA)
- **P1-5** [Domain]: Comparator tools claimed in checklist but not discussed
- **P1-6** [SWE]: Stale validation_summary.md date

#### P2 -- Minor
- **P2-1** [SWE]: var instead of const/let
- **P2-2** [SWE]: Chart y-max could auto-scale
- **P2-3** [Domain]: "low" certainty + PASS status needs clarifying note
- **P2-4** [SWE]: Add requirements.txt for Python-only reproducibility
- **P2-5** [SWE]: flowchart_blueprint.md unreferenced

#### False Positive Watch
- Scope honesty is GOOD — packaging contribution explicitly stated throughout
- Validation math (inverse-variance pooling) IS correct
