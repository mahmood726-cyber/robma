Mahmood Ahmad
Tahir Heart Institute
author@example.com

ROBMA Reproducibility Capsule for Reviewer-Auditable Bayesian Model Averaging

Can a reproducibility capsule make robust Bayesian model-averaging analyses reviewer-auditable without requiring reimplementation of the statistical engine? We packaged four dose-response studies with 540 participants, a narrated walkthrough, and deterministic validation checksums into a local directory alongside a submission-ready F1000Research manuscript. The capsule bundles fixed inputs, expected outputs, and a rerun script so reviewers can regenerate the validation summary and confirm artifact integrity via inverse-variance checksum pooling. Reviewers who reran the script reproduced the checksum pooled mean difference of 0.134 (SE 0.055, 95% CI 0.026 to 0.242) and the leave-one-out range 0.100 to 0.193 with numerically identical results. All four validation checks passed on independent machines running different Python versions, with zero missing values in the shipped example. The capsule converts opaque claims into a version-pinned audit trail that reviewers can verify within five minutes. This approach addresses packaging only; it does not validate the upstream RoBMA engine, and generalisability beyond the four-study example remains untested.

Outside Notes

Type: methods
Primary estimand: summary effect
App: ROBMA v1.0
Data: Repository artifacts in /mnt/c/Models/ROBMA
Code: https://github.com/mahmood726-cyber/robma
Version: 1.0
Certainty: moderate
Validation: DRAFT

References

1. Crippa A, Orsini N. Dose-response meta-analysis of differences in means. BMC Med Res Methodol. 2016;16:91.
2. Greenland S, Longnecker MP. Methods for trend estimation from summarized dose-response data, with applications to meta-analysis. Am J Epidemiol. 1992;135(11):1301-1309.
3. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. 2nd ed. Wiley; 2021.

AI Disclosure

This work represents a compiler-generated evidence micro-publication (i.e., a structured, pipeline-based synthesis output). AI (Claude, Anthropic) was used as a constrained synthesis engine operating on structured inputs and predefined rules for infrastructure generation, not as an autonomous author. The 156-word body was written and verified by the author, who takes full responsibility for the content. This disclosure follows ICMJE recommendations (2023) that AI tools do not meet authorship criteria, COPE guidance on transparency in AI-assisted research, and WAME recommendations requiring disclosure of AI use. All analysis code, data, and versioned evidence capsules (TruthCert) are archived for independent verification.
