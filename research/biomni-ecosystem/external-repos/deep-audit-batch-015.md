# External repository deep audit — Batch 015

Observed at: `2026-08-24T06:22:12Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **513–562**.
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
| `DEEP_AUDIT_CANDIDATE` | 17 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 29 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 1 |

Static-review flags were present in 15 families for security-sensitive primitives, 12 for privacy/data-governance terms, and 9 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 513 | `Edison-A-N/inspector` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 514 | `yarikoptic/OpenScholar` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 515 | `Vik-u/mu-protein` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 516 | `gutendzx/BrainIAC` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 517 | `gutendzx/ECGFounder` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 518 | `inodb/mcp-agent-base-1` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 519 | `goodb/spoke_genelab` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 520 | `jissen706/Abdominal-Symprom-Clarify-Bot` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 521 | `jissen706/aliquot-first-class-tracker` | `DEEP_AUDIT_CANDIDATE` | 0 | 69/2/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 522 | `Ali-Maq/CohortGenerator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 523 | `Rakshitha-Ireddi/storm` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 524 | `leezx/Vibe-Researching` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/19/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 525 | `Rakshitha-Ireddi/CRYOGEM` | `DEEP_AUDIT_CANDIDATE` | 0 | 44/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 526 | `HelloWorldLTY/PertBench` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 527 | `yarikoptic/cito` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 528 | `dabulseco/GeoPrompt` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/24/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 529 | `jaechang-hits/standigm_paper_citation` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 530 | `leizhou69/RCL-identifier` | `DEEP_AUDIT_CANDIDATE` | 0 | 22/22/37 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 531 | `yaswanth169/deepscholar` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 532 | `KyleNeverGivesUp/weather-mcp-server` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 533 | `inodb/cbio-agent-null` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 534 | `MinxZ/MMSplice_MTSplice` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 535 | `shantanusharma/lidar` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 536 | `yarikoptic/Documentation-2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 537 | `yarikoptic/fret-analysis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 538 | `alexs42/Claudeception` | `DEEP_AUDIT_CANDIDATE` | 9 | 1/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 539 | `dabulseco/dna_mutation_sonification` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 540 | `yarikoptic/abcd-dictionary-chatbot` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 541 | `leezx/AI-CoScientist` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/2/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 542 | `th86/OpenCode-ST` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/5/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 543 | `yarikoptic/NBDCtoolsData` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 544 | `hanlin-yang/evo2-MCP` | `DEEP_AUDIT_CANDIDATE` | 0 | 401/115/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 545 | `gutendzx/SleepGPT1` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 546 | `th86/OpenCode-TCRSeq-ML-pipeline` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/2/21 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 547 | `shantanusharma/RNAPro` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 548 | `yarikoptic/mercure` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 549 | `Charvijain16/Autonomous_loop_AI_Science_Discovery` | `EMPTY` | 0 | 0/0/0 | CLOSE_EMPTY_OR_UNAVAILABLE_ARTIFACT; no integration capability retained |
| 550 | `gutendzx/GluFormer_Nature` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 551 | `Vincentcchu/anndictionary` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 552 | `Liripo/spatialdata-io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 553 | `andrewsu/TestHarness` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 554 | `marcosbolanos/boltzgen`, `Vik-u/boltzgen` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 555 | `Vik-u/Momentum_Process_ScriptGen` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/10/45 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 556 | `shantanusharma/DORA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 557 | `yaswanth169/aitom` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 558 | `jissen706/PyTorch-Medical-Image-Classification-Project` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/4/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 559 | `HelloWorldLTY/drugplayground` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 560 | `KyleNeverGivesUp/mcp-server-kyle` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 561 | `jucor/planning-with-files` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 562 | `hanlin-yang/BioAiSaaS-main` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/45/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |

## Candidate and blocker details

### Order 520 — `jissen706/Abdominal-Symprom-Clarify-Bot`

Bounded repositories: `jissen706/Abdominal-Symprom-Clarify-Bot`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 521 — `jissen706/aliquot-first-class-tracker`

Bounded repositories: `jissen706/aliquot-first-class-tracker`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 75, code 69, documentation 2, data 2, manifests 2.

Static security flags: `{"network_fetch": 6, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 524 — `leezx/Vibe-Researching`

Bounded repositories: `leezx/Vibe-Researching`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 21, code 1, documentation 19, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 525 — `Rakshitha-Ireddi/CRYOGEM`

Bounded repositories: `Rakshitha-Ireddi/CRYOGEM`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 51, code 44, documentation 5, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 5, "unsafe_deserialization": 3, "shell_or_process_execution": 1, "path_input": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 8, "human_genomics": 1, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 50, "assertion_as_validation": 41, "hardcoded_threshold": 3}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 528 — `dabulseco/GeoPrompt`

Bounded repositories: `dabulseco/GeoPrompt`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 56, code 27, documentation 24, data 4, manifests 0.

Static security flags: `{"filesystem_mutation": 6, "shell_or_process_execution": 2, "network_fetch": 2, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 9}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 529 — `jaechang-hits/standigm_paper_citation`

Bounded repositories: `jaechang-hits/standigm_paper_citation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 1, documentation 1, data 3, manifests 0.

Static security flags: `{"network_fetch": 4}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 530 — `leizhou69/RCL-identifier`

Bounded repositories: `leizhou69/RCL-identifier`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 81, code 22, documentation 22, data 37, manifests 0.

Static security flags: `{"dynamic_code_execution": 8, "unsafe_deserialization": 5, "path_input": 4}`.

Privacy/data-governance flags: `{"human_genomics": 4, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 20, "assertion_as_validation": 2, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 532 — `KyleNeverGivesUp/weather-mcp-server`

Bounded repositories: `KyleNeverGivesUp/weather-mcp-server`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 15, code 8, documentation 3, data 0, manifests 4.

Static security flags: `{"shell_or_process_execution": 6, "network_fetch": 4, "server_exposure": 4, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 703}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 538 — `AlexMikhalev/claude-code-continuous-learning-skill`

Bounded repositories: `alexs42/Claudeception`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 5, code 1, documentation 4, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 539 — `dabulseco/dna_mutation_sonification`

Bounded repositories: `dabulseco/dna_mutation_sonification`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 7, code 3, documentation 3, data 0, manifests 0.

Static security flags: `{"network_fetch": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 16, "human_genomics": 6, "clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 542 — `th86/OpenCode-ST`

Bounded repositories: `th86/OpenCode-ST`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 16, code 8, documentation 5, data 2, manifests 1.

Static security flags: `{"dynamic_code_execution": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 544 — `hanlin-yang/evo2-MCP`

Bounded repositories: `hanlin-yang/evo2-MCP`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 750, code 401, documentation 115, data 0, manifests 125.

Static security flags: `{"network_fetch": 127, "mutable_remote_install": 41, "server_exposure": 22, "dynamic_code_execution": 17, "hardcoded_secret_shape": 12, "filesystem_mutation": 10, "shell_or_process_execution": 8, "container_privilege": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 44, "human_genomics": 10, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 28, "hardcoded_absolute_path": 4}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 546 — `th86/OpenCode-TCRSeq-ML-pipeline`

Bounded repositories: `th86/OpenCode-TCRSeq-ML-pipeline`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 32, code 9, documentation 2, data 21, manifests 0.

Static security flags: `{"path_input": 3, "dynamic_code_execution": 2, "unsafe_deserialization": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 16}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 555 — `Vik-u/Momentum_Process_ScriptGen`

Bounded repositories: `Vik-u/Momentum_Process_ScriptGen`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 63, code 7, documentation 10, data 45, manifests 0.

Static security flags: `{"server_exposure": 1, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 7}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 558 — `jissen706/PyTorch-Medical-Image-Classification-Project`

Bounded repositories: `jissen706/PyTorch-Medical-Image-Classification-Project`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 15, code 10, documentation 4, data 1, manifests 0.

Static security flags: `{"dynamic_code_execution": 5, "unsafe_deserialization": 3, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 5, "unseeded_randomness": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 559 — `HelloWorldLTY/drugplayground`

Bounded repositories: `HelloWorldLTY/drugplayground`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 7, code 5, documentation 1, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 7, "dynamic_code_execution": 5}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 9}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 560 — `KyleNeverGivesUp/mcp-server-kyle`

Bounded repositories: `KyleNeverGivesUp/mcp-server-kyle`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 0, data 0, manifests 2.

Static security flags: `{}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 430}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
