# External repository deep audit — Batch 026

Observed at: `2026-08-24T06:26:06Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1063–1112**.
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
| `DEEP_AUDIT_CANDIDATE` | 11 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 36 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 8 families for security-sensitive primitives, 8 for privacy/data-governance terms, and 7 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1063 | `yarikoptic/datalad-core` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/3/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1064 | `HelloWorldLTY/Awesome-DNA-Language-Modelling` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/9/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1065 | `gutendzx/radiosleep` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1066 | `yarikoptic/nipreps.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1067 | `andrewsu/Updated-DrugMAP-Parser` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1068 | `yarikoptic/simple2_NIDM_examples` | `DEEP_AUDIT_CANDIDATE` | 3 | 0/1/21 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1069 | `drgmk/SpaceM` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1070 | `yarikoptic/dandisets-linkml-status-tools` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1071 | `HelloWorldLTY/EPInformer` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/2/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1072 | `yarikoptic/ngff` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1073 | `andrewsu/TranslatorTechnicalDocumentation` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1074 | `andrewsu/biothings_explorer`, `ahueb/biothings_explorer` | `DEEP_AUDIT_CANDIDATE` | 4 | 0/2/17 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1075 | `tangxuan82/MeDeT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1076 | `yarikoptic/bids2table` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1077 | `yarikoptic/mixs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1078 | `leezx/3ca` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1079 | `yarikoptic/docs-2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1080 | `yarikoptic/joss` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1081 | `Mr-Milk/SpatialTis` | `DEEP_AUDIT_CANDIDATE` | 0 | 30/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1082 | `jaybee84/nf-synapse` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1083 | `Liripo/biobear` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1084 | `tangxuan82/Digital-Twins-in-Healthcare` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1085 | `HelloWorldLTY/DNABERT_S`, `jaybee84/DNABERT_S` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1086 | `jaybee84/scicomp-provisioner` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1087 | `tangxuan82/fit4function` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1088 | `HelloWorldLTY/BEND` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1089 | `th86/bits-to-binders-resources` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1090 | `tangxuan82/TaxDiff` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1091 | `yarikoptic/reproducibility-biblio` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1092 | `yarikoptic/psychopy_linux_installer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1093 | `yarikoptic/physioqc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1094 | `Vincentcchu/bia` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1095 | `yarikoptic/buffy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1096 | `siavashre/CRISPRCATCH` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1097 | `yarikoptic/dandi_s3_log_parser` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1098 | `HelloWorldLTY/ldsc`, `explorerwjy/ldsc` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1099 | `Sanat-Mishra/Sheltzer-Lab-Fusions-Analysis` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1100 | `yarikoptic/nwbinspector` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1101 | `HelloWorldLTY/scDRS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1102 | `dabulseco/BLAST` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1103 | `yarikoptic/bids-starter-kit` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1104 | `Sanat-Mishra/JAFFA` | `DEEP_AUDIT_CANDIDATE` | 2 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1105 | `yarikoptic/reproschema-ui` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1106 | `alexj-lee/OmegaFold` | `DEEP_AUDIT_CANDIDATE` | 3 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1107 | `leezx/bt2m` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/44/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1108 | `KSUN63/DynamicBind` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1109 | `vladsavelyev/spack` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1110 | `alexj-lee/PyDSSP` | `DEEP_AUDIT_CANDIDATE` | 6 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1111 | `inodb/spectra` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1112 | `yarikoptic/CAJAL` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 1063 — `yarikoptic/datalad-core`

Bounded repositories: `yarikoptic/datalad-core`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 14, code 3, documentation 3, data 2, manifests 5.

Static security flags: `{"mutable_remote_install": 5, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1068 — `ReproNim/simple2_NIDM_examples`

Bounded repositories: `yarikoptic/simple2_NIDM_examples`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 22, code 0, documentation 1, data 21, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 21, "upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1071 — `pinellolab/EPInformer`

Bounded repositories: `HelloWorldLTY/EPInformer`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 17, code 10, documentation 2, data 5, manifests 0.

Static security flags: `{"unsafe_deserialization": 13, "dynamic_code_execution": 8, "network_fetch": 4, "mutable_remote_install": 4, "shell_or_process_execution": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 2, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1074 — `biothings/biothings_explorer`

Bounded repositories: `andrewsu/biothings_explorer`, `ahueb/biothings_explorer`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 22, code 0, documentation 2, data 17, manifests 3.

Static security flags: `{"mutable_remote_install": 3}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 13}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1081 — `Mr-Milk/SpatialTis`

Bounded repositories: `Mr-Milk/SpatialTis`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 43, code 30, documentation 5, data 0, manifests 7.

Static security flags: `{"mutable_remote_install": 5, "server_exposure": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 4}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1096 — `siavashre/CRISPRCATCH`

Bounded repositories: `siavashre/CRISPRCATCH`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 4, documentation 1, data 1, manifests 0.

Static security flags: `{"shell_or_process_execution": 31, "sql_string_construction": 8, "path_input": 4}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1099 — `Sanat-Mishra/Sheltzer-Lab-Fusions-Analysis`

Bounded repositories: `Sanat-Mishra/Sheltzer-Lab-Fusions-Analysis`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 2, documentation 1, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 15}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 9}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1104 — `Oshlack/JAFFA`

Bounded repositories: `Sanat-Mishra/JAFFA`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1106 — `HeliXonProtein/OmegaFold`

Bounded repositories: `alexj-lee/OmegaFold`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 2, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 1, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1107 — `leezx/bt2m`

Bounded repositories: `leezx/bt2m`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 60, code 10, documentation 44, data 4, manifests 1.

Static security flags: `{"dynamic_code_execution": 34, "browser_html_injection": 22, "sql_string_construction": 15, "mutable_remote_install": 14, "path_input": 2, "network_fetch": 1}`.

Privacy/data-governance flags: `{"human_genomics": 10, "upload_or_remote_transfer": 8}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 3, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1110 — `ShintaroMinami/PyDSSP`

Bounded repositories: `alexj-lee/PyDSSP`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
