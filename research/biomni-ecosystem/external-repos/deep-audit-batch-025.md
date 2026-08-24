# External repository deep audit — Batch 025

Observed at: `2026-08-24T06:25:40Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1013–1062**.
- Canonical families: **50**.
- Canonical repository records: **52**.
- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.
- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.

## Static acquisition and review method

Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.

Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.

## Result summary

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 9 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 37 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 4 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 8 families for security-sensitive primitives, 8 for privacy/data-governance terms, and 7 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1013 | `yarikoptic/PyShEx` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1014 | `Chahat08/CSE564_Final_Project` | `DEEP_AUDIT_CANDIDATE` | 0 | 12/3/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1015 | `sszhu/statannotations` | `DEEP_AUDIT_CANDIDATE` | 9 | 19/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1016 | `siavashre/OM2BFB` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1017 | `Rasic2/APEX` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1018 | `marcosbolanos/MeshTree` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/45/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1019 | `yarikoptic/B-SOID` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1020 | `tangxuan82/Med-Real2Sim` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1021 | `yarikoptic/vocalpy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1022 | `jucor/krippendorff` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/1/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1023 | `yarikoptic/clinica` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1024 | `yarikoptic/arcana` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1025 | `Liripo/sc-type` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1026 | `marcosbolanos/kaggle_medicalPremiums` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/0/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1027 | `leezx/AI-Drug-Discovery-Design` | `DEEP_AUDIT_CANDIDATE` | 63 | 11/3/7 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1028 | `yarikoptic/schema` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1029 | `HelloWorldLTY/task-dge-perturbation-prediction-analysis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1030 | `yarikoptic/paperscraper` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1031 | `HelloWorldLTY/Orthrus` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1032 | `yarikoptic/bids-schema` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1033 | `PabloCabaleiro/variantbenchmarking` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1034 | `Vik-u/esmdiff` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1035 | `HelloWorldLTY/gReLU` | `DEEP_AUDIT_CANDIDATE` | 4 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1036 | `yarikoptic/learning-from-brains` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1037 | `yarikoptic/neuvue-app` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1038 | `yarikoptic/mriqc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1039 | `HelloWorldLTY/Geneverse` | `DEEP_AUDIT_CANDIDATE` | 0 | 131/44/12 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1040 | `gutendzx/CIMSleepNet` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1041 | `yarikoptic/quarto-cli` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1042 | `andrewsu/DrugMechDB`, `ahueb/DrugMechDB` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1043 | `goodb/scidata`, `yarikoptic/scidata` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1044 | `Liripo/scRepertoire` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1045 | `yarikoptic/hed-python` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1046 | `HelloWorldLTY/openproblems` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1047 | `yarikoptic/allenCCF` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1048 | `yarikoptic/datalad-extensions` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1049 | `HelloWorldLTY/DANCE_NIPS2024` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1050 | `tangxuan82/druggpt` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1051 | `Liripo/sgs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1052 | `Liripo/scRNAtoolVis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1053 | `yarikoptic/patch-denoising` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1054 | `inodb/htan_missing_manual` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1055 | `gutendzx/NonContactApneaDetection` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1056 | `Liripo/scCustomize` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1057 | `HelloWorldLTY/GeneCompass` | `DOC_METADATA_MAINTENANCE_ONLY` | 3 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1058 | `Rasic2/GVaspWeb` | `DEEP_AUDIT_CANDIDATE` | 0 | 24/5/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1059 | `andrewsu/information-resource-registry` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1060 | `Liripo/scGPT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1061 | `tuln128/alde_forked` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1062 | `yarikoptic/2024-incf-poster` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |

## Candidate and blocker details

### Order 1014 — `Chahat08/CSE564_Final_Project`

Bounded repositories: `Chahat08/CSE564_Final_Project`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 18, code 12, documentation 3, data 1, manifests 2.

Static security flags: `{"network_fetch": 13, "server_exposure": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1015 — `getzze/statannotations`

Bounded repositories: `sszhu/statannotations`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 21, code 19, documentation 1, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 12}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1016 — `siavashre/OM2BFB`

Bounded repositories: `siavashre/OM2BFB`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 9, code 5, documentation 3, data 0, manifests 0.

Static security flags: `{"path_input": 7, "shell_or_process_execution": 5, "filesystem_mutation": 2, "dynamic_code_execution": 1, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1022 — `jucor/krippendorff`

Bounded repositories: `jucor/krippendorff`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 42, code 27, documentation 1, data 5, manifests 7.

Static security flags: `{"mutable_remote_install": 5}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1026 — `marcosbolanos/kaggle_medicalPremiums`

Bounded repositories: `marcosbolanos/kaggle_medicalPremiums`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 2, code 1, documentation 0, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1027 — `gsh150801/AI-drug-design`

Bounded repositories: `leezx/AI-Drug-Discovery-Design`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 21, code 11, documentation 3, data 7, manifests 0.

Static security flags: `{"mutable_remote_install": 20, "dynamic_code_execution": 5}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 19, "upload_or_remote_transfer": 6, "named_biomedical_cohort": 3, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 2, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1035 — `Genentech/gReLU`

Bounded repositories: `HelloWorldLTY/gReLU`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 3}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1039 — `HelloWorldLTY/Geneverse`

Bounded repositories: `HelloWorldLTY/Geneverse`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 196, code 131, documentation 44, data 12, manifests 5.

Static security flags: `{"path_input": 55, "mutable_remote_install": 35, "network_fetch": 23, "dynamic_code_execution": 11, "unsafe_deserialization": 11, "server_exposure": 9, "browser_html_injection": 7, "hardcoded_secret_shape": 5, "sql_string_construction": 3, "filesystem_mutation": 2, "shell_or_process_execution": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 31, "clinical_or_patient_data": 3, "human_genomics": 2, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 90, "unseeded_randomness": 7, "network_model_code": 3, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1058 — `Rasic2/GVaspWeb`

Bounded repositories: `Rasic2/GVaspWeb`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 34, code 24, documentation 5, data 2, manifests 2.

Static security flags: `{"network_fetch": 7, "filesystem_mutation": 6, "shell_or_process_execution": 4, "server_exposure": 2, "sql_string_construction": 2, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 165, "named_biomedical_cohort": 8}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
