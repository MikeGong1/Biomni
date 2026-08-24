# External repository deep audit — Batch 046

Observed at: `2026-08-24T06:48:24Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **2063–2069**.
- Canonical families: **7**.
- Canonical repository records: **7**.
- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.
- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.

## Static acquisition and review method

Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.

Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.

## Result summary

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 3 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 2 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 2 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 3 families for security-sensitive primitives, 2 for privacy/data-governance terms, and 3 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 2063 | `inodb/snakemake-uppmax-demo` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 2064 | `yarikoptic/qnotero` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2065 | `yarikoptic/nipy-notebooks` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2066 | `hannes-brt/FlowVB` | `DEEP_AUDIT_CANDIDATE` | 0 | 34/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2067 | `yarikoptic/nipy-suite` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 2068 | `yarikoptic/NiPy-OLD` | `DEEP_AUDIT_CANDIDATE` | 0 | 467/109/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2069 | `yarikoptic/scipy3` | `DEEP_AUDIT_CANDIDATE` | 176 | 42/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 2066 — `hannes-brt/FlowVB`

Bounded repositories: `hannes-brt/FlowVB`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 36, code 34, documentation 1, data 0, manifests 1.

Static security flags: `{"sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 5, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2068 — `yarikoptic/NiPy-OLD`

Bounded repositories: `yarikoptic/NiPy-OLD`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 616, code 467, documentation 109, data 0, manifests 37.

Static security flags: `{"dynamic_code_execution": 46, "filesystem_mutation": 34, "sql_string_construction": 22, "shell_or_process_execution": 18, "network_fetch": 14, "path_input": 4}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 49, "human_genomics": 6, "upload_or_remote_transfer": 5, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 333, "assertion_as_validation": 62, "hardcoded_threshold": 17, "hardcoded_absolute_path": 3}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2069 — `stefanv/scipy3`

Bounded repositories: `yarikoptic/scipy3`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 43, code 42, documentation 0, data 0, manifests 1.

Static security flags: `{"network_fetch": 12, "dynamic_code_execution": 9, "unsafe_deserialization": 3, "filesystem_mutation": 3}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 692, "assertion_as_validation": 37, "unseeded_randomness": 23}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
