# External repository deep audit — Batch 014

Observed at: `2026-08-24T06:21:37Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **463–512**.
- Canonical families: **50**.
- Canonical repository records: **51**.
- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.
- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.

## Static acquisition and review method

Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.

Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.

## Result summary

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 21 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 27 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 1 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 1 |

Static-review flags were present in 19 families for security-sensitive primitives, 16 for privacy/data-governance terms, and 14 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 463 | `r-siddiqi/Hofstadter` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 464 | `yaswanth169/feeding-deployment` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 465 | `jucor/claude-code-lsp-skill` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/2/1 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 466 | `gutendzx/HEARTS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 467 | `yaswanth169/AirStack` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 468 | `gutendzx/SleepLM` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 469 | `gutendzx/OSF-Open-Sleep-FM` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 470 | `yarikoptic/nipype` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 471 | `jissen706/Magellan` | `DEEP_AUDIT_CANDIDATE` | 0 | 65/3/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 472 | `yarikoptic/excalidraw-diagram-skill` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 473 | `Rakshitha-Ireddi/PULSAR` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 474 | `kuanlinhuang/Biomni-Lite` | `DEEP_AUDIT_CANDIDATE` | 0 | 67/87/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 475 | `gutendzx/Cardiac-Sensing-FM` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 476 | `jucor/zotero-scipdf` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 477 | `zskylarli/cellocate` | `DEEP_AUDIT_CANDIDATE` | 0 | 6/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 478 | `gutendzx/wav2sleep` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 479 | `KSUN63/datawarrior` | `DEEP_AUDIT_CANDIDATE` | 3 | 4/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 480 | `Vik-u/BioAgentHub_Crawler` | `DEEP_AUDIT_CANDIDATE` | 0 | 24/5/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 481 | `yaswanth169/ModelGenerator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 482 | `andrewsu/JTK_Cycle2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 483 | `andrewsu/jtk-cycle` | `DEEP_AUDIT_CANDIDATE` | 2 | 4/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 484 | `yarikoptic/nipoppy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 485 | `Liripo/cellranger_learn` | `DEEP_AUDIT_CANDIDATE` | 0 | 672/4/7 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 486 | `gutendzx/Resp-Agent` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 487 | `alexs42/Celltype_cli` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 488 | `zhanxw/seqminer` | `DEEP_AUDIT_CANDIDATE` | 0 | 223/34/8 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 489 | `kuanlinhuang/Biomni_AD_ADA_entries` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 490 | `de-grave/openonco-mcp` | `DEEP_AUDIT_CANDIDATE` | 0 | 17/6/11 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 491 | `shantanusharma/deepchem` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 492 | `yarikoptic/PROBE` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 493 | `Vik-u/BioAgentHub` | `DEEP_AUDIT_CANDIDATE` | 0 | 39/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 494 | `yarikoptic/book` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 495 | `yarikoptic/metaxy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 496 | `yaswanth169/robomimic` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 497 | `Chahat08/Zarr_Rechunker` | `EMPTY` | 0 | 0/0/0 | CLOSE_EMPTY_OR_UNAVAILABLE_ARTIFACT; no integration capability retained |
| 498 | `explorerwjy/EphysSumStats` | `DEEP_AUDIT_CANDIDATE` | 0 | 15/6/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 499 | `yaswanth169/av-dar` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 500 | `HasanAldhahi/cross-precision-llm-deployment-biomni` | `DEEP_AUDIT_CANDIDATE` | 0 | 22/19/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 501 | `dabulseco/WBCD_ml_app` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 502 | `xinwuye/UniDock-Pointcept` | `DEEP_AUDIT_CANDIDATE` | 117 | 39/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 503 | `yarikoptic/Kosmos`, `Vik-u/Kosmos` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 504 | `th86/DrugDevAgent` | `DEEP_AUDIT_CANDIDATE` | 0 | 11/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 505 | `HelloWorldLTY/CellForge` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 506 | `inodb/mcp-agent-base` | `DEEP_AUDIT_CANDIDATE` | 2 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 507 | `yarikoptic/ndx-wearables` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 508 | `Ali-Maq/medgemma-kaggle-2026` | `DEEP_AUDIT_CANDIDATE` | 0 | 13/12/33 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 509 | `yaswanth169/curobo` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 510 | `yarikoptic/osa` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 511 | `tangxuan82/finches` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 512 | `Vik-u/AgentFlow` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 463 — `r-siddiqi/Hofstadter`

Bounded repositories: `r-siddiqi/Hofstadter`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 13, code 10, documentation 2, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 126}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 6}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 468 — `yang-ai-lab/SleepLM`

Bounded repositories: `gutendzx/SleepLM`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 13, code 9, documentation 2, data 1, manifests 0.

Static security flags: `{"dynamic_code_execution": 7, "unsafe_deserialization": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 4, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 52, "unseeded_randomness": 17}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 471 — `jissen706/Magellan`

Bounded repositories: `jissen706/Magellan`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 73, code 65, documentation 3, data 2, manifests 2.

Static security flags: `{"network_fetch": 39, "dynamic_code_execution": 4, "filesystem_mutation": 2, "server_exposure": 1}`.

Privacy/data-governance flags: `{"human_genomics": 47, "clinical_or_patient_data": 10}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 5, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 474 — `kuanlinhuang/Biomni-Lite`

Bounded repositories: `kuanlinhuang/Biomni-Lite`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 162, code 67, documentation 87, data 4, manifests 3.

Static security flags: `{"shell_or_process_execution": 147, "unsafe_deserialization": 47, "network_fetch": 47, "sql_string_construction": 20, "filesystem_mutation": 14, "dynamic_code_execution": 13, "server_exposure": 10, "path_input": 7, "hardcoded_secret_shape": 2}`.

Privacy/data-governance flags: `{"human_genomics": 91, "clinical_or_patient_data": 62, "named_biomedical_cohort": 28, "upload_or_remote_transfer": 12}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 26, "hardcoded_threshold": 16, "assertion_as_validation": 4, "disabled_tls_verification": 2, "hardcoded_absolute_path": 1, "network_model_code": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 477 — `zskylarli/cellocate`

Bounded repositories: `zskylarli/cellocate`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 7, code 6, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 26}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 479 — `thsa/datawarrior`

Bounded repositories: `KSUN63/datawarrior`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 7, code 4, documentation 2, data 1, manifests 0.

Static security flags: `{"shell_or_process_execution": 2, "filesystem_mutation": 2, "path_input": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 480 — `Vik-u/BioAgentHub_Crawler`

Bounded repositories: `Vik-u/BioAgentHub_Crawler`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 35, code 24, documentation 5, data 5, manifests 1.

Static security flags: `{"network_fetch": 8, "browser_html_injection": 7, "server_exposure": 6, "shell_or_process_execution": 3, "dynamic_code_execution": 2, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 14, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 31}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 483 — `mfcovington/jtk-cycle`

Bounded repositories: `andrewsu/jtk-cycle`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 4, code 4, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 485 — `Liripo/cellranger_learn`

Bounded repositories: `Liripo/cellranger_learn`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 743, code 672, documentation 4, data 7, manifests 59.

Static security flags: `{"dynamic_code_execution": 45, "shell_or_process_execution": 41, "sql_string_construction": 24, "network_fetch": 18, "path_input": 15, "filesystem_mutation": 10, "unsafe_deserialization": 4, "mutable_remote_install": 4, "browser_html_injection": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 194, "human_genomics": 74, "named_biomedical_cohort": 11}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 350, "hardcoded_threshold": 161, "unseeded_randomness": 22, "hardcoded_absolute_path": 3}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 488 — `zhanxw/seqminer`

Bounded repositories: `zhanxw/seqminer`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 272, code 223, documentation 34, data 8, manifests 2.

Static security flags: `{"sql_string_construction": 20, "network_fetch": 17, "dynamic_code_execution": 8, "mutable_remote_install": 6, "filesystem_mutation": 5, "browser_html_injection": 3}`.

Privacy/data-governance flags: `{"human_genomics": 675, "named_biomedical_cohort": 5, "upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 13, "hardcoded_threshold": 8, "hardcoded_absolute_path": 2, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 489 — `kuanlinhuang/Biomni_AD_ADA_entries`

Bounded repositories: `kuanlinhuang/Biomni_AD_ADA_entries`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 3, documentation 1, data 0, manifests 0.

Static security flags: `{"network_fetch": 12, "shell_or_process_execution": 2, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1, "human_genomics": 1, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 82, "hardcoded_threshold": 13, "unseeded_randomness": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 490 — `de-grave/openonco-mcp`

Bounded repositories: `de-grave/openonco-mcp`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 38, code 17, documentation 6, data 11, manifests 1.

Static security flags: `{"sql_string_construction": 21, "filesystem_mutation": 2, "server_exposure": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 361, "human_genomics": 106, "upload_or_remote_transfer": 9, "named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 493 — `Vik-u/BioAgentHub`

Bounded repositories: `Vik-u/BioAgentHub`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 44, code 39, documentation 3, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 13, "server_exposure": 6, "sql_string_construction": 4, "shell_or_process_execution": 2, "unsafe_deserialization": 1, "filesystem_mutation": 1, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"human_genomics": 16, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 498 — `explorerwjy/EphysSumStats`

Bounded repositories: `explorerwjy/EphysSumStats`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 23, code 15, documentation 6, data 2, manifests 0.

Static security flags: `{"path_input": 8, "shell_or_process_execution": 2}`.

Privacy/data-governance flags: `{"human_genomics": 10}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 7, "hardcoded_absolute_path": 7, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 500 — `HasanAldhahi/cross-precision-llm-deployment-biomni`

Bounded repositories: `HasanAldhahi/cross-precision-llm-deployment-biomni`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 44, code 22, documentation 19, data 0, manifests 2.

Static security flags: `{"shell_or_process_execution": 39, "dynamic_code_execution": 9, "filesystem_mutation": 4, "server_exposure": 3, "network_fetch": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 16, "clinical_or_patient_data": 7, "named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 2, "unseeded_randomness": 1, "network_model_code": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 501 — `dabulseco/WBCD_ml_app`

Bounded repositories: `dabulseco/WBCD_ml_app`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 1, documentation 2, data 1, manifests 0.

Static security flags: `{"unsafe_deserialization": 3}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 47}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 502 — `Pointcept/Pointcept`

Bounded repositories: `xinwuye/UniDock-Pointcept`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 41, code 39, documentation 1, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 29, "unsafe_deserialization": 6, "filesystem_mutation": 5, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 11, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 78, "assertion_as_validation": 65}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 504 — `th86/DrugDevAgent`

Bounded repositories: `th86/DrugDevAgent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 14, code 11, documentation 1, data 0, manifests 2.

Static security flags: `{"network_fetch": 15}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 45}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 505 — `gersteinlab/CellForge`

Bounded repositories: `HelloWorldLTY/CellForge`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 9, "network_fetch": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 506 — `gisetia/mcp-agent-base`

Bounded repositories: `inodb/mcp-agent-base`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 4, code 2, documentation 0, data 0, manifests 2.

Static security flags: `{"network_fetch": 3, "server_exposure": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 508 — `Ali-Maq/medgemma-kaggle-2026`

Bounded repositories: `Ali-Maq/medgemma-kaggle-2026`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 60, code 13, documentation 12, data 33, manifests 2.

Static security flags: `{"dynamic_code_execution": 4, "network_fetch": 3, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 363, "clinical_or_patient_data": 89, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 102}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
