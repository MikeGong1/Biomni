# External repository deep audit — Batch 010

Observed at: `2026-08-24T06:19:22Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **263–312**.
- Canonical families: **50**.
- Canonical repository records: **56**.
- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.
- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.

## Static acquisition and review method

Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.

Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.

## Result summary

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 17 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 26 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 7 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 22 families for security-sensitive primitives, 17 for privacy/data-governance terms, and 10 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 263 | `KalinNonchev/awesome-single-cell-foundation` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 264 | `KalinNonchev/Awesome-Single-Cell-Foundation-Models` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 265 | `yarikoptic/datalad-git-annex` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 266 | `shantanusharma/mindsdb` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 267 | `vlln/paperutils` | `DEEP_AUDIT_CANDIDATE` | 0 | 34/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 268 | `vlln/skit` | `DEEP_AUDIT_CANDIDATE` | 0 | 40/16/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 269 | `vlln/mineru-api-skill` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/3/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 270 | `vlln/background-task-skill` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 271 | `Vik-u/md-lab` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 272 | `NKalavros/headlessagents-rankings` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/2/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 273 | `psknlr/Bone-Bioinformetics` | `DEEP_AUDIT_CANDIDATE` | 1 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 274 | `sbonner0/Proteina-Complexa` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 275 | `de-grave/openscience` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 276 | `manu-tej/ai-scientists` | `DEEP_AUDIT_CANDIDATE` | 0 | 81/25/131 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 277 | `yarikoptic/claimbound-evidence` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 278 | `de-grave/OpenClaw-Medical-Skills` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 279 | `Vik-u/SimVault` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 280 | `kwskws1998/masked_ae_atari_and_cognitive_task` | `DEEP_AUDIT_CANDIDATE` | 0 | 47/11/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 281 | `HelloWorldLTY/LAMDNA` | `DEEP_AUDIT_CANDIDATE` | 0 | 152/11/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 282 | `andrewsu/DN-meta-analysis` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/8/9 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 283 | `yarikoptic/bcbs-book` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/2/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 284 | `yarikoptic/bettercode` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 285 | `andrewsu/okn-registry` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 286 | `shengyongniu/multimodal-rag` | `DEEP_AUDIT_CANDIDATE` | 0 | 22/5/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 287 | `HelloWorldLTY/depression_detection` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 288 | `inodb/fastVEP` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 289 | `drgmk/sdf` | `DEEP_AUDIT_CANDIDATE` | 0 | 33/56/68 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 290 | `vlln/subagents-skill` | `DEEP_AUDIT_CANDIDATE` | 0 | 36/15/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 291 | `inodb/datahub`, `jaybee84/datahub` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 292 | `Vik-u/biosecbench-refusal` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 293 | `Pidem/medmarks`, `Rakshitha-Ireddi/med-lm-envs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 294 | `vlln/skills-source` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/1 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 295 | `vlln/remote-exec-skill` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/2/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 296 | `vlln/autofigure-skill` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 297 | `vlln/quay-skill` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/2/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 298 | `inodb/cbioportal-navigator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 299 | `kewserseid/AI-Assistant` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 300 | `yarikoptic/CanlabCore` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 301 | `yarikoptic/AuthorshipExtractor` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 302 | `de-grave/bionemo-agent-toolkit` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 303 | `Lancelot-Xie/Supergoal` | `DEEP_AUDIT_CANDIDATE` | 0 | 20/43/6 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 304 | `Edison-A-N/langfuse-mcp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 305 | `inodb/oncotree` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 306 | `HelloWorldLTY/evo2`, `shantanusharma/evo2`, `dabulseco/evo2`, `alexj-lee/evo2`, `Vik-u/evo2` | `DEEP_AUDIT_CANDIDATE` | 5 | 0/1/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 307 | `Vik-u/molecule-name-lookup` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 308 | `yarikoptic/petprep` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 309 | `yarikoptic/my-skills` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 310 | `yarikoptic/mobspy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 311 | `Harrydirk41/ConformFlow` | `DEEP_AUDIT_CANDIDATE` | 0 | 116/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 312 | `starboy-3/pyvene` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 267 — `vlln/paperutils`

Bounded repositories: `vlln/paperutils`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 36, code 34, documentation 2, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 32, "network_fetch": 26, "mutable_remote_install": 2, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 2, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 6}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 268 — `vlln/skit`

Bounded repositories: `vlln/skit`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 62, code 40, documentation 16, data 1, manifests 4.

Static security flags: `{"filesystem_mutation": 18, "dynamic_code_execution": 11, "mutable_remote_install": 10, "sql_string_construction": 5, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 270 — `vlln/background-task-skill`

Bounded repositories: `vlln/background-task-skill`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 2, documentation 2, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 273 — `pariskang/Bone-Bioinformetics`

Bounded repositories: `psknlr/Bone-Bioinformetics`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 274 — `NVIDIA-BioNeMo/Proteina-Complexa`

Bounded repositories: `sbonner0/Proteina-Complexa`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"filesystem_mutation": 2}`.

Privacy/data-governance flags: `{"human_genomics": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 276 — `manu-tej/ai-scientists`

Bounded repositories: `manu-tej/ai-scientists`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 240, code 81, documentation 25, data 131, manifests 2.

Static security flags: `{"dynamic_code_execution": 30, "filesystem_mutation": 23, "network_fetch": 17, "shell_or_process_execution": 16, "hardcoded_secret_shape": 13, "browser_html_injection": 10, "path_input": 8, "sql_string_construction": 4, "server_exposure": 2}`.

Privacy/data-governance flags: `{"human_genomics": 333, "clinical_or_patient_data": 136, "upload_or_remote_transfer": 43, "named_biomedical_cohort": 28}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 95}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 280 — `kwskws1998/masked_ae_atari_and_cognitive_task`

Bounded repositories: `kwskws1998/masked_ae_atari_and_cognitive_task`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 63, code 47, documentation 11, data 1, manifests 1.

Static security flags: `{"dynamic_code_execution": 22, "unsafe_deserialization": 13, "shell_or_process_execution": 8, "network_fetch": 7, "path_input": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 96, "unseeded_randomness": 39}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 281 — `HelloWorldLTY/LAMDNA`

Bounded repositories: `HelloWorldLTY/LAMDNA`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 174, code 152, documentation 11, data 4, manifests 4.

Static security flags: `{"shell_or_process_execution": 114, "dynamic_code_execution": 67, "unsafe_deserialization": 45, "network_fetch": 36, "mutable_remote_install": 21, "sql_string_construction": 14, "filesystem_mutation": 13, "path_input": 6, "hardcoded_secret_shape": 5}`.

Privacy/data-governance flags: `{"human_genomics": 77, "clinical_or_patient_data": 46, "upload_or_remote_transfer": 12, "named_biomedical_cohort": 3}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 364, "unseeded_randomness": 72, "hardcoded_threshold": 14, "hardcoded_absolute_path": 7, "network_model_code": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 282 — `andrewsu/DN-meta-analysis`

Bounded repositories: `andrewsu/DN-meta-analysis`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 26, code 9, documentation 8, data 9, manifests 0.

Static security flags: `{"network_fetch": 14, "path_input": 2, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 13, "human_genomics": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 286 — `shengyongniu/multimodal-rag`

Bounded repositories: `shengyongniu/multimodal-rag`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 31, code 22, documentation 5, data 1, manifests 3.

Static security flags: `{"network_fetch": 9, "dynamic_code_execution": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 58}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 289 — `drgmk/sdf`

Bounded repositories: `drgmk/sdf`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 160, code 33, documentation 56, data 68, manifests 1.

Static security flags: `{"filesystem_mutation": 14, "sql_string_construction": 9, "unsafe_deserialization": 7, "network_fetch": 5}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 15, "assertion_as_validation": 8, "unseeded_randomness": 5, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 290 — `vlln/subagents-skill`

Bounded repositories: `vlln/subagents-skill`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 52, code 36, documentation 15, data 1, manifests 0.

Static security flags: `{"shell_or_process_execution": 50, "mutable_remote_install": 3, "sql_string_construction": 3, "dynamic_code_execution": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 8, "unseeded_randomness": 2, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 296 — `vlln/autofigure-skill`

Bounded repositories: `vlln/autofigure-skill`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 3, documentation 5, data 0, manifests 0.

Static security flags: `{"network_fetch": 13, "mutable_remote_install": 2, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 303 — `Lancelot-Xie/Supergoal`

Bounded repositories: `Lancelot-Xie/Supergoal`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 70, code 20, documentation 43, data 6, manifests 0.

Static security flags: `{"shell_or_process_execution": 75, "filesystem_mutation": 10, "dynamic_code_execution": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 306 — `ArcInstitute/evo2`

Bounded repositories: `HelloWorldLTY/evo2`, `shantanusharma/evo2`, `dabulseco/evo2`, `alexj-lee/evo2`, `Vik-u/evo2`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS, IMMUTABLE_CHANGED_BLOBS; files read 3, code 0, documentation 1, data 2, manifests 0.

Static security flags: `{"mutable_remote_install": 2, "network_fetch": 1}`.

Privacy/data-governance flags: `{"human_genomics": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 307 — `Vik-u/molecule-name-lookup`

Bounded repositories: `Vik-u/molecule-name-lookup`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 5, documentation 1, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 4, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 3}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 37}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 311 — `Harrydirk41/ConformFlow`

Bounded repositories: `Harrydirk41/ConformFlow`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 121, code 116, documentation 4, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 17, "network_fetch": 8, "shell_or_process_execution": 7, "unsafe_deserialization": 7, "path_input": 4, "mutable_remote_install": 2, "sql_string_construction": 2, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 23, "human_genomics": 19, "named_biomedical_cohort": 13, "clinical_or_patient_data": 7}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 241, "unseeded_randomness": 31, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
