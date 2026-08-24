# External repository deep audit — Batch 012

Observed at: `2026-08-24T06:20:24Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **363–412**.
- Canonical families: **50**.
- Canonical repository records: **50**.
- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.
- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.

## Static acquisition and review method

Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.

Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.

## Result summary

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 17 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 30 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 17 families for security-sensitive primitives, 15 for privacy/data-governance terms, and 13 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 363 | `yarikoptic/neuroai` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 364 | `leizhou69/EvoS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 365 | `Nigmat-future/20260426-circuit-icb-pan-cancer-immune-checkpoint-blockade-resistance-cell-state-atlas` | `DEEP_AUDIT_CANDIDATE` | 0 | 72/23/31 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 366 | `averyself/wmdp-agentic-eval` | `DEEP_AUDIT_CANDIDATE` | 0 | 15/4/16 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 367 | `yarikoptic/makeprov` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 368 | `inodb/cbioportal-cell-explorer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 369 | `yarikoptic/ngff-spec` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 370 | `div0-space/qmsolve-playful` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 371 | `yarikoptic/babs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 372 | `PMK89/stellarium` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 373 | `andrewsu/calibr-briefing` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/42/1 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 374 | `yarikoptic/dandi-feedstock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 375 | `yarikoptic/fuji` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 376 | `Nigmat-future/publishable-research-orchestrator` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/5/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 377 | `dabulseco/andrej-karpathy-skills` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 378 | `inodb/cancerhotspots` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 379 | `yarikoptic/prism-studio` | `DEEP_AUDIT_CANDIDATE` | 754 | 24/2/15 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 380 | `yarikoptic/BIDS-examples` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 381 | `yarikoptic/dcm_validate` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 382 | `yarikoptic/rt-cloud` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 383 | `yohyoh-wang/staRgate-flowjo-plugin` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 384 | `jissen706/Timbre` | `DEEP_AUDIT_CANDIDATE` | 0 | 91/10/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 385 | `mkoretsky1/Localising_SOZ_from_SPES` | `DEEP_AUDIT_CANDIDATE` | 3 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 386 | `Ali-Maq/civic-extraction-agent` | `DEEP_AUDIT_CANDIDATE` | 0 | 63/14/122 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 387 | `Ali-Maq/oncocite-langchain` | `DEEP_AUDIT_CANDIDATE` | 0 | 55/18/36 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 388 | `KalinNonchev/pathology-hooknet-tls-pytorch` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/5/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 389 | `Nigmat-future/pad-to-vibe` | `DEEP_AUDIT_CANDIDATE` | 0 | 15/10/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 390 | `leizhou69/DeepS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 391 | `inodb/genome-nexus` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 392 | `inodb/genome-nexus-importer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 393 | `rsflinn/autism-brain-explorer` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 394 | `mickaelleclercq/AutoFigure-Edit` | `DEEP_AUDIT_CANDIDATE` | 0 | 38/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 395 | `Rasic2/gvasp` | `DEEP_AUDIT_CANDIDATE` | 0 | 46/43/22 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 396 | `psknlr/drug_agent` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 397 | `yarikoptic/ds000113` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 398 | `yarikoptic/skill-scanner` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 399 | `inodb/cbiopubkb` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/358/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 400 | `andrewsu/HARVEST` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 401 | `PabloPauling/Protenix` | `DEEP_AUDIT_CANDIDATE` | 4 | 2/0/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 402 | `jaechang-hits/awesome-claude-skills` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 403 | `jaechang-hits/awesome-claude-code-toolkit` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 404 | `kwskws1998/gaze_reward` | `DEEP_AUDIT_CANDIDATE` | 0 | 12/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 405 | `yarikoptic/neurod3` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 406 | `de-grave/awesome-mcp-servers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 407 | `erhuve/skills` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 408 | `yaswanth169/delphi-epidata` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 409 | `yarikoptic/claude-scientific-writer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 410 | `yarikoptic/hackathon2026` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 411 | `SnowLightPath/extended-mind` | `DEEP_AUDIT_CANDIDATE` | 0 | 28/2/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 412 | `alexs42/awesome-claude-skills` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 365 — `Nigmat-future/20260426-circuit-icb-pan-cancer-immune-checkpoint-blockade-resistance-cell-state-atlas`

Bounded repositories: `Nigmat-future/20260426-circuit-icb-pan-cancer-immune-checkpoint-blockade-resistance-cell-state-atlas`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 128, code 72, documentation 23, data 31, manifests 2.

Static security flags: `{"network_fetch": 15, "dynamic_code_execution": 2, "path_input": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 328, "named_biomedical_cohort": 70, "human_genomics": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 96, "hardcoded_threshold": 4}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 366 — `averyself/wmdp-agentic-eval`

Bounded repositories: `averyself/wmdp-agentic-eval`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 36, code 15, documentation 4, data 16, manifests 1.

Static security flags: `{"network_fetch": 4, "path_input": 4, "server_exposure": 3, "dynamic_code_execution": 2, "hardcoded_secret_shape": 2, "shell_or_process_execution": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 376 — `Nigmat-future/publishable-research-orchestrator`

Bounded repositories: `Nigmat-future/publishable-research-orchestrator`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 1, documentation 5, data 1, manifests 0.

Static security flags: `{"sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 379 — `MRI-Lab-Graz/prism-studio`

Bounded repositories: `yarikoptic/prism-studio`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 45, code 24, documentation 2, data 15, manifests 3.

Static security flags: `{"shell_or_process_execution": 10, "server_exposure": 5, "filesystem_mutation": 5, "mutable_remote_install": 3, "path_input": 2, "sql_string_construction": 2, "dynamic_code_execution": 1}`.

Privacy/data-governance flags: `{"human_genomics": 20, "upload_or_remote_transfer": 16, "clinical_or_patient_data": 8}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 20}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 384 — `jissen706/Timbre`

Bounded repositories: `jissen706/Timbre`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 109, code 91, documentation 10, data 5, manifests 3.

Static security flags: `{"network_fetch": 29, "filesystem_mutation": 18, "server_exposure": 6, "shell_or_process_execution": 2, "hardcoded_secret_shape": 2, "path_input": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 62, "upload_or_remote_transfer": 32}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 280, "unseeded_randomness": 149, "hardcoded_absolute_path": 24, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 385 — `norrisjamie23/Localising_SOZ_from_SPES`

Bounded repositories: `mkoretsky1/Localising_SOZ_from_SPES`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 4, code 2, documentation 0, data 0, manifests 2.

Static security flags: `{}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 513, "clinical_or_patient_data": 7}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 386 — `Ali-Maq/civic-extraction-agent`

Bounded repositories: `Ali-Maq/civic-extraction-agent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 206, code 63, documentation 14, data 122, manifests 5.

Static security flags: `{"sql_string_construction": 61, "network_fetch": 29, "server_exposure": 12, "path_input": 5, "dynamic_code_execution": 4, "mutable_remote_install": 4, "shell_or_process_execution": 3}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 3530, "human_genomics": 604, "upload_or_remote_transfer": 37, "named_biomedical_cohort": 14}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 44, "hardcoded_absolute_path": 10, "hardcoded_threshold": 8}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 387 — `Ali-Maq/oncocite-langchain`

Bounded repositories: `Ali-Maq/oncocite-langchain`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 115, code 55, documentation 18, data 36, manifests 5.

Static security flags: `{"network_fetch": 25, "dynamic_code_execution": 23, "sql_string_construction": 12, "server_exposure": 6, "shell_or_process_execution": 4, "mutable_remote_install": 4, "path_input": 3, "filesystem_mutation": 1, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 827, "human_genomics": 260, "upload_or_remote_transfer": 30, "named_biomedical_cohort": 7}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 14, "assertion_as_validation": 4, "hardcoded_threshold": 3, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 388 — `KalinNonchev/pathology-hooknet-tls-pytorch`

Bounded repositories: `KalinNonchev/pathology-hooknet-tls-pytorch`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 5, documentation 5, data 1, manifests 0.

Static security flags: `{"dynamic_code_execution": 4, "unsafe_deserialization": 4}`.

Privacy/data-governance flags: `{"human_genomics": 3, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 4, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 389 — `Nigmat-future/pad-to-vibe`

Bounded repositories: `Nigmat-future/pad-to-vibe`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 33, code 15, documentation 10, data 3, manifests 5.

Static security flags: `{"network_fetch": 5}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 393 — `rsflinn/autism-brain-explorer`

Bounded repositories: `rsflinn/autism-brain-explorer`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 7, code 3, documentation 2, data 1, manifests 1.

Static security flags: `{"browser_html_injection": 7, "sql_string_construction": 2, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 19, "human_genomics": 9, "named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 394 — `mickaelleclercq/AutoFigure-Edit`

Bounded repositories: `mickaelleclercq/AutoFigure-Edit`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 44, code 38, documentation 2, data 0, manifests 3.

Static security flags: `{"network_fetch": 17, "browser_html_injection": 9, "shell_or_process_execution": 7, "dynamic_code_execution": 3, "server_exposure": 3, "filesystem_mutation": 2, "path_input": 2, "sql_string_construction": 2, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 50, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"network_model_code": 2, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 395 — `Rasic2/gvasp`

Bounded repositories: `Rasic2/gvasp`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 125, code 46, documentation 43, data 22, manifests 11.

Static security flags: `{"filesystem_mutation": 32, "sql_string_construction": 8, "mutable_remote_install": 7, "path_input": 3, "shell_or_process_execution": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 6}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 15, "hardcoded_absolute_path": 2, "unseeded_randomness": 1, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 399 — `inodb/cbiopubkb`

Bounded repositories: `inodb/cbiopubkb`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 361, code 1, documentation 358, data 2, manifests 0.

Static security flags: `{"sql_string_construction": 34, "network_fetch": 3, "shell_or_process_execution": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 3064, "human_genomics": 1246, "named_biomedical_cohort": 916, "upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 1, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 401 — `bytedance/Protenix`

Bounded repositories: `PabloPauling/Protenix`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 2, documentation 0, data 1, manifests 0.

Static security flags: `{"unsafe_deserialization": 1, "network_fetch": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 8, "unseeded_randomness": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 404 — `Telefonica-Scientific-Research/gaze_reward`

Bounded repositories: `kwskws1998/gaze_reward`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 16, code 12, documentation 3, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 8, "mutable_remote_install": 6, "dynamic_code_execution": 4, "shell_or_process_execution": 2, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 3, "unseeded_randomness": 1, "network_model_code": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 411 — `SnowLightPath/extended-mind`

Bounded repositories: `SnowLightPath/extended-mind`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 35, code 28, documentation 2, data 2, manifests 2.

Static security flags: `{"network_fetch": 31, "hardcoded_secret_shape": 9, "shell_or_process_execution": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 1}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
