# External repository deep audit — Batch 018

Observed at: `2026-08-24T06:23:19Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **663–712**.
- Canonical families: **50**.
- Canonical repository records: **53**.
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

Static-review flags were present in 15 families for security-sensitive primitives, 13 for privacy/data-governance terms, and 11 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 663 | `gutendzx/SPICED` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 664 | `Edison-A-N/mcpadapt` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 665 | `xinwuye/UniDock-PTV3` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 666 | `SongyouZhong/binana` | `DEEP_AUDIT_CANDIDATE` | 2 | 4/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 667 | `ryanDing26/Hackaging-team-Ryan` | `DEEP_AUDIT_CANDIDATE` | 0 | 16/2/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 668 | `ryanDing26/aging-theories` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 669 | `anngvu/nextflow-infra`, `jaybee84/nextflow-infra` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 670 | `yarikoptic/datoviz` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 671 | `tangxuan82/DigitalTwin` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/7/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 672 | `Javkhaa/skills` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 673 | `yarikoptic/probeinterface` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 674 | `yarikoptic/phy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 675 | `sophicle/sensory` | `DEEP_AUDIT_CANDIDATE` | 0 | 12/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 676 | `tangxuan82/Greedoc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 677 | `anngvu/synapse-mcp`, `jaybee84/synapse-mcp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 678 | `yarikoptic/fissa` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 679 | `SongyouZhong/DECIMER-Image-Segmentation` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 680 | `Rasic2/dpdispatcher` | `DEEP_AUDIT_CANDIDATE` | 20 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 681 | `tangxuan82/T1DSim_AI` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 682 | `yarikoptic/bootstrap_MRIQC` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 683 | `Vik-u/MomentumPyClient` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 684 | `HasanAldhahi/biomni_agent` | `DEEP_AUDIT_CANDIDATE` | 0 | 85/15/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 685 | `yarikoptic/dicompare` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 686 | `yarikoptic/protocol_qc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 687 | `SongyouZhong/DECIMER-Image_Transformer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 688 | `marcosbolanos/Cheminformatics_molecule_property_project` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 689 | `vladsavelyev/mcp_biomni` | `DEEP_AUDIT_CANDIDATE` | 0 | 13/1/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 690 | `dabulseco/ProLLaMA`, `tangxuan82/ProLLaMA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 691 | `leezx/TRIDENT` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/5/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 692 | `yarikoptic/HALFpipe` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 693 | `tangxuan82/PERIODONTAL_DIGITAL-TWIN` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 694 | `Harrydirk41/ProTDyn` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 695 | `Nigmat-future/Gastric-Cancer-scRNA-seq-Analysis-Pipeline---GSE163558` | `DEEP_AUDIT_CANDIDATE` | 0 | 29/4/10 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 696 | `Vik-u/SynBioKB-Agent` | `DEEP_AUDIT_CANDIDATE` | 0 | 61/7/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 697 | `Vik-u/la-proteina` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 698 | `kwskws1998/jspsych-experiment` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 699 | `Ali-Maq/CUREBench` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 700 | `leizhou69/str-analysis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 701 | `th86/pymutualinformation` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 702 | `Nigmat-future/cellhop` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 703 | `mickaelleclercq/bioAgent` | `DEEP_AUDIT_CANDIDATE` | 0 | 29/6/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 704 | `Nigmat-future/rverflow` | `DEEP_AUDIT_CANDIDATE` | 0 | 12/1/16 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 705 | `andrewsu/reusabledata` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 706 | `yarikoptic/neuroboros` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 707 | `tangxuan82/from_scratch_to_twin` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 708 | `tangxuan82/itwinai` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 709 | `th86/awesome_bioinfo` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 710 | `yarikoptic/open-retina` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 711 | `marcosbolanos/Virtual-Cell-Challenge` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 712 | `RyanLi1028/Biomni-SkyRL` | `DEEP_AUDIT_CANDIDATE` | 16 | 40/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 666 — `durrantlab/binana`

Bounded repositories: `SongyouZhong/binana`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 5, code 4, documentation 1, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 7}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 667 — `ryanDing26/Hackaging-team-Ryan`

Bounded repositories: `ryanDing26/Hackaging-team-Ryan`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 21, code 16, documentation 2, data 3, manifests 0.

Static security flags: `{"network_fetch": 16, "hardcoded_secret_shape": 6, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 46, "human_genomics": 12, "named_biomedical_cohort": 8}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 668 — `ryanDing26/aging-theories`

Bounded repositories: `ryanDing26/aging-theories`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 4, documentation 0, data 0, manifests 0.

Static security flags: `{"network_fetch": 6, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 671 — `tangxuan82/DigitalTwin`

Bounded repositories: `tangxuan82/DigitalTwin`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 12, code 4, documentation 7, data 1, manifests 0.

Static security flags: `{"network_fetch": 4, "browser_html_injection": 4}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 8}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 675 — `sophicle/sensory`

Bounded repositories: `sophicle/sensory`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 14, code 12, documentation 1, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 5, "unsafe_deserialization": 3, "hardcoded_secret_shape": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 3, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 4, "network_model_code": 2, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 680 — `deepmodeling/dpdispatcher`

Bounded repositories: `Rasic2/dpdispatcher`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 682 — `yarikoptic/bootstrap_MRIQC`

Bounded repositories: `yarikoptic/bootstrap_MRIQC`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 2, documentation 3, data 0, manifests 0.

Static security flags: `{"filesystem_mutation": 6, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 684 — `HasanAldhahi/biomni_agent`

Bounded repositories: `HasanAldhahi/biomni_agent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 107, code 85, documentation 15, data 4, manifests 2.

Static security flags: `{"shell_or_process_execution": 112, "network_fetch": 37, "unsafe_deserialization": 33, "sql_string_construction": 20, "dynamic_code_execution": 16, "filesystem_mutation": 10, "hardcoded_secret_shape": 9, "path_input": 6, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 75, "clinical_or_patient_data": 69, "named_biomedical_cohort": 6, "upload_or_remote_transfer": 3}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 31, "hardcoded_absolute_path": 16, "hardcoded_threshold": 15, "network_model_code": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 689 — `vladsavelyev/mcp_biomni`

Bounded repositories: `vladsavelyev/mcp_biomni`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 20, code 13, documentation 1, data 2, manifests 3.

Static security flags: `{"shell_or_process_execution": 10, "server_exposure": 10, "filesystem_mutation": 8, "dynamic_code_execution": 7}`.

Privacy/data-governance flags: `{"human_genomics": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 140, "hardcoded_absolute_path": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 694 — `Harrydirk41/ProTDyn`

Bounded repositories: `Harrydirk41/ProTDyn`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 2, documentation 1, data 3, manifests 1.

Static security flags: `{"filesystem_mutation": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 695 — `Nigmat-future/Gastric-Cancer-scRNA-seq-Analysis-Pipeline---GSE163558`

Bounded repositories: `Nigmat-future/Gastric-Cancer-scRNA-seq-Analysis-Pipeline---GSE163558`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 44, code 29, documentation 4, data 10, manifests 0.

Static security flags: `{"network_fetch": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 35, "clinical_or_patient_data": 14}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 4}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 696 — `Vik-u/SynBioKB-Agent`

Bounded repositories: `Vik-u/SynBioKB-Agent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 74, code 61, documentation 7, data 0, manifests 6.

Static security flags: `{"network_fetch": 17, "path_input": 8, "dynamic_code_execution": 6, "server_exposure": 2, "hardcoded_secret_shape": 2, "shell_or_process_execution": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 23}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 701 — `th86/pymutualinformation`

Bounded repositories: `th86/pymutualinformation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 702 — `Nigmat-future/cellhop`

Bounded repositories: `Nigmat-future/cellhop`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 17, code 9, documentation 5, data 0, manifests 2.

Static security flags: `{"filesystem_mutation": 4}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 3}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 703 — `mickaelleclercq/bioAgent`

Bounded repositories: `mickaelleclercq/bioAgent`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 36, code 29, documentation 6, data 0, manifests 1.

Static security flags: `{"shell_or_process_execution": 10, "sql_string_construction": 4, "filesystem_mutation": 2, "dynamic_code_execution": 1, "server_exposure": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 704 — `Nigmat-future/rverflow`

Bounded repositories: `Nigmat-future/rverflow`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 30, code 12, documentation 1, data 16, manifests 1.

Static security flags: `{"sql_string_construction": 8, "dynamic_code_execution": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 712 — `NovaSky-AI/SkyRL`

Bounded repositories: `RyanLi1028/Biomni-SkyRL`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 43, code 40, documentation 1, data 0, manifests 2.

Static security flags: `{"network_fetch": 18, "dynamic_code_execution": 12, "shell_or_process_execution": 8, "unsafe_deserialization": 5, "mutable_remote_install": 5, "sql_string_construction": 3, "filesystem_mutation": 2, "server_exposure": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1200, "human_genomics": 13, "named_biomedical_cohort": 10, "clinical_or_patient_data": 8}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 43, "unseeded_randomness": 33, "hardcoded_threshold": 3, "network_model_code": 3, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
