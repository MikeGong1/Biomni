# Research Log

## 2026-08-23 — SciAgent-Skills ecosystem deep audit

- Experimental hypothesis: SciAgent-Skills may contain independently useful, integration-ready scientific capabilities beyond Biomni's frozen baseline.
- Observed failure: Static review found material cross-domain scientific errors, unreproducible benchmark claims, unsafe instruction and supply-chain surfaces, and incomplete provenance across the 203-Skill corpus; three fork variants also lacked sufficient correctness, runtime, privacy, license, or integration evidence.
- Suspected cause: The corpus is an instruction-generation collection assembled from heterogeneous tools and services without a uniform executable validation, provenance, or safety contract.
- Modification: Froze and normalized the source branch/PR DAG, all 203 active Skills and 85 ancillary files, and all 34 public forks; retained only 125 bounded clean-room requirement leads and seven change/two lineage records.
- Result change: External deep-audit batch 001 advanced from 2 complete plus 1 partial to 3/3 complete; SciAgent-Skills is now `DEEP_AUDITED` and rejected as-is with no Feature/Implementation allocation.
- Retained: Yes; research-only database, manifests, detailed report, coverage, index, and resume-state updates retained.
