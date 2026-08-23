# Research Log

## 2026-08-23 — SciAgent-Skills ecosystem deep audit

- Experimental hypothesis: SciAgent-Skills may contain independently useful, integration-ready scientific capabilities beyond Biomni's frozen baseline.
- Observed failure: Static review found material cross-domain scientific errors, unreproducible benchmark claims, unsafe instruction and supply-chain surfaces, and incomplete provenance across the 203-Skill corpus; three fork variants also lacked sufficient correctness, runtime, privacy, license, or integration evidence.
- Suspected cause: The corpus is an instruction-generation collection assembled from heterogeneous tools and services without a uniform executable validation, provenance, or safety contract.
- Modification: Froze and normalized the source branch/PR DAG, all 203 active Skills and 85 ancillary files, and all 34 public forks; retained only 125 bounded clean-room requirement leads and seven change/two lineage records.
- Result change: External deep-audit batch 001 advanced from 2 complete plus 1 partial to 3/3 complete; SciAgent-Skills is now `DEEP_AUDITED` and rejected as-is with no Feature/Implementation allocation.
- Retained: Yes; research-only database, manifests, detailed report, coverage, index, and resume-state updates retained.

## 2026-08-24 — External fork-only families batch 002

- Experimental hypothesis: Five high-relevance BioNeMo, ClawBio, and Scanpy forks may contain substantive capabilities absent from their authoritative upstream sources.
- Observed failure: All default histories were exact source tips or source ancestors; the three apparent unique heads reduced to two generated artifacts and one exact open DOC_ONLY upstream PR ref.
- Suspected cause: Metadata-only screening correctly favored recall but treated recently pushed forks and generated branches as potential independent implementations before Git DAG normalization.
- Modification: Froze all native refs and bounded fork PR/release/child-fork surfaces, compared them against full source ref unions, statically inspected three deltas, and independently verified the DAG and native tag counts.
- Result change: Queue orders 2–4 and five repository records moved from `NOT_STARTED` to `DEEP_AUDITED`/no-substantive-unique; unresolved family count fell from 2,066 to 2,063 with no new canonical capability IDs.
- Retained: Yes; detailed batch report, five-row lineage manifest, five evidence records, repository/entity status changes, control-ledger updates, and the tag auto-follow correction retained.
