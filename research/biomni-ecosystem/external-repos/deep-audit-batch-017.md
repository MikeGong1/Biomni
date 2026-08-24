# External repository deep audit — Batch 017

Observed at: `2026-08-24T06:22:56Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **613–662**.
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
| `DEEP_AUDIT_CANDIDATE` | 16 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 33 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 1 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 14 families for security-sensitive primitives, 12 for privacy/data-governance terms, and 10 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 613 | `Edison-A-N/mcp-garden` | `DEEP_AUDIT_CANDIDATE` | 0 | 19/12/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 614 | `aevo98765/mcp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 615 | `tangxuan82/scPRINT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 616 | `marcosbolanos/BindCraft`, `th86/BindCraft`, `samarth-kadaba/BindCraft` | `DEEP_AUDIT_CANDIDATE` | 18 | 12/3/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 617 | `b-snel/scenicplus` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 618 | `yarikoptic/agentic-neurodata-conversion` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 619 | `yarikoptic/facemap` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 620 | `samarth-kadaba/CAR-TPA` | `DEEP_AUDIT_CANDIDATE` | 0 | 21/18/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 621 | `Vik-u/fk-rfdiffusion` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 622 | `HelloWorldLTY/BAITSAO` | `DEEP_AUDIT_CANDIDATE` | 0 | 56/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 623 | `Nigmat-future/AgenticBioAnalysis` | `DEEP_AUDIT_CANDIDATE` | 0 | 18/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 624 | `yarikoptic/zotero-google-docs-integration` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 625 | `tangxuan82/SynthPert` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 626 | `Rakshitha-Ireddi/SpelkeBench` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 627 | `Ali-Maq/Qwen-Agent` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 628 | `Mr-Milk/wsidata-feedstock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 629 | `yarikoptic/aind-ephys-curation` | `DEEP_AUDIT_CANDIDATE` | 2 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 630 | `yarikoptic/zotero-connectors` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 631 | `JinL0/fastmcpcloud-test` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 632 | `yarikoptic/physiopy.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 633 | `psknlr/agents-zhongyi` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 634 | `th86/ColabFold`, `leizhou69/ColabFold` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 635 | `tangxuan82/LangPert` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 636 | `ryanDing26/HistoPath` | `DEEP_AUDIT_CANDIDATE` | 0 | 20/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 637 | `NKalavros/PopScalescRNAseq` | `DEEP_AUDIT_CANDIDATE` | 0 | 88/8/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 638 | `shantanusharma/generative-virtual-screening` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 639 | `HelloWorldLTY/Delphi` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 640 | `tangxuan82/transcriptformer`, `jaybee84/transcriptformer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 641 | `dabulseco/alphagenome`, `leizhou69/alphagenome`, `Ali-Maq/alphagenome` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 642 | `Vik-u/Brenda_Agent` | `DEEP_AUDIT_CANDIDATE` | 0 | 45/13/13 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 643 | `Vik-u/ai4g-flood` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 644 | `Ali-Maq/CIvic_database_documenation-` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 645 | `th86/predict-airr` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 646 | `tangxuan82/Synapses-Emergency-Healthcare-System` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 647 | `shantanusharma/evals` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 648 | `ryanDing26/emDNA-GPU` | `DEEP_AUDIT_CANDIDATE` | 0 | 19/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 649 | `tangxuan82/TumorTwin` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 650 | `leizhou69/CellVoyager` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 651 | `yarikoptic/MRI_Ontology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 652 | `yarikoptic/physiopy-repository-template` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 653 | `dabulseco/LearnChemE.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 654 | `tangxuan82/dt4co` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 655 | `Liripo/pySCENIC` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 656 | `samutiti/cellpose_batchable` | `DEEP_AUDIT_CANDIDATE` | 3 | 3/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 657 | `yarikoptic/niwrap` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 658 | `vlln/paper2report` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 659 | `tangxuan82/TwinAI` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 660 | `Ali-Maq/OncoCITE` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 661 | `HelloWorldLTY/SpaIM` | `DEEP_AUDIT_CANDIDATE` | 2 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 662 | `tangxuan82/idpcolab` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 613 — `Edison-A-N/mcp-garden`

Bounded repositories: `Edison-A-N/mcp-garden`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 40, code 19, documentation 12, data 3, manifests 4.

Static security flags: `{"network_fetch": 8, "shell_or_process_execution": 4, "hardcoded_secret_shape": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1166}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 3}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 616 — `martinpacesa/BindCraft`

Bounded repositories: `marcosbolanos/BindCraft`, `th86/BindCraft`, `samarth-kadaba/BindCraft`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS, IMMUTABLE_CHANGED_BLOBS; files read 18, code 12, documentation 3, data 2, manifests 1.

Static security flags: `{"filesystem_mutation": 13, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 4, "hardcoded_threshold": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 620 — `samarth-kadaba/CAR-TPA`

Bounded repositories: `samarth-kadaba/CAR-TPA`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 44, code 21, documentation 18, data 0, manifests 5.

Static security flags: `{"network_fetch": 22, "server_exposure": 2, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 42, "human_genomics": 10, "named_biomedical_cohort": 4}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 622 — `HelloWorldLTY/BAITSAO`

Bounded repositories: `HelloWorldLTY/BAITSAO`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 58, code 56, documentation 2, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 200, "dynamic_code_execution": 41, "sql_string_construction": 27, "mutable_remote_install": 4}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 623 — `Nigmat-future/AgenticBioAnalysis`

Bounded repositories: `Nigmat-future/AgenticBioAnalysis`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 19, code 18, documentation 1, data 0, manifests 0.

Static security flags: `{"network_fetch": 5, "path_input": 3, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 4, "clinical_or_patient_data": 2, "human_genomics": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 629 — `AllenNeuralDynamics/aind-ephys-curation`

Bounded repositories: `yarikoptic/aind-ephys-curation`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"path_input": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 631 — `JinL0/fastmcpcloud-test`

Bounded repositories: `JinL0/fastmcpcloud-test`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 2, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{"network_fetch": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4}`.

Scientific/reproducibility flags: `{"disabled_tls_verification": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 636 — `ryanDing26/HistoPath`

Bounded repositories: `ryanDing26/HistoPath`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 25, code 20, documentation 2, data 1, manifests 1.

Static security flags: `{"dynamic_code_execution": 8, "shell_or_process_execution": 5, "unsafe_deserialization": 3, "filesystem_mutation": 2, "sql_string_construction": 2, "network_fetch": 1, "server_exposure": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 40, "named_biomedical_cohort": 4, "human_genomics": 3, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 8, "network_model_code": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 637 — `NKalavros/PopScalescRNAseq`

Bounded repositories: `NKalavros/PopScalescRNAseq`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 100, code 88, documentation 8, data 4, manifests 0.

Static security flags: `{"shell_or_process_execution": 22, "network_fetch": 8, "dynamic_code_execution": 5, "unsafe_deserialization": 4, "filesystem_mutation": 4, "server_exposure": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 32, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 9, "assertion_as_validation": 7, "network_model_code": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 639 — `gerstung-lab/Delphi`

Bounded repositories: `HelloWorldLTY/Delphi`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 642 — `Vik-u/Brenda_Agent`

Bounded repositories: `Vik-u/Brenda_Agent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 73, code 45, documentation 13, data 13, manifests 1.

Static security flags: `{"browser_html_injection": 28, "network_fetch": 15, "dynamic_code_execution": 8, "sql_string_construction": 4, "server_exposure": 3, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 5, "hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 648 — `ryanDing26/emDNA-GPU`

Bounded repositories: `ryanDing26/emDNA-GPU`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 27, code 19, documentation 5, data 0, manifests 3.

Static security flags: `{"shell_or_process_execution": 2, "path_input": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 13, "hardcoded_threshold": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 656 — `MouseLand/cellpose`

Bounded repositories: `samutiti/cellpose_batchable`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 3, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 4, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 11, "unseeded_randomness": 8, "assertion_as_validation": 2, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 658 — `vlln/paper2report`

Bounded repositories: `vlln/paper2report`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 12, code 7, documentation 3, data 0, manifests 1.

Static security flags: `{"server_exposure": 6, "network_fetch": 4, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 660 — `Ali-Maq/OncoCITE`

Bounded repositories: `Ali-Maq/OncoCITE`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"network_fetch": 1}`.

Privacy/data-governance flags: `{"human_genomics": 7}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 661 — `QSong-github/SpaIM`

Bounded repositories: `HelloWorldLTY/SpaIM`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 1, documentation 0, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
