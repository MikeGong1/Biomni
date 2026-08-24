# External repository deep audit — Batch 022

Observed at: `2026-08-24T06:24:45Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **863–912**.
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
| `DEEP_AUDIT_CANDIDATE` | 8 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 39 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 5 families for security-sensitive primitives, 4 for privacy/data-governance terms, and 4 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 863 | `gutendzx/LPSGM` | `DEEP_AUDIT_CANDIDATE` | 0 | 49/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 864 | `yarikoptic/heudiconv-feedstock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 865 | `shaunporwal/DICOM-MCP` | `DEEP_AUDIT_CANDIDATE` | 0 | 6/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 866 | `Vik-u/DiffDock`, `KSUN63/DiffDock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 867 | `andrewsu/knowledge-graph-hub.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 868 | `yarikoptic/NiChart_Project` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 869 | `aevo98765/materials` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/0/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 870 | `ryanDing26/Diabetes-Classifier` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 871 | `gutendzx/XSleepFusion` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 872 | `gutendzx/sleep_analysis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 873 | `yarikoptic/scholarly` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 874 | `KSUN63/MolBERT` | `DEEP_AUDIT_CANDIDATE` | 1 | 3/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 875 | `yarikoptic/BMAT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 876 | `yarikoptic/sleap-io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 877 | `changwn/CARTmath` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 878 | `yarikoptic/dmptool-1` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 879 | `andrewsu/TranslatorArchitecture` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 880 | `tangxuan82/digitaltwin2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 881 | `sbonner0/hetionet` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 882 | `yarikoptic/invenio-app-rdm` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 883 | `vladsavelyev/MultiQC_NGI` | `DEEP_AUDIT_CANDIDATE` | 3 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 884 | `Ali-Maq/clinvar-query-system` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 885 | `yarikoptic/digital_slide_archive` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 886 | `Ali-Maq/civic-benchmark-dataset-creation` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 887 | `yarikoptic/fairsharing.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 888 | `tangxuan82/ansr-dt` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 889 | `psknlr/PubMed-MCP-Server` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 890 | `Ali-Maq/civic-docs_api` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 891 | `yarikoptic/PyNIDM` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 892 | `shaunporwal/dicom-viewer` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 893 | `tangxuan82/Cardiac-Digital-Twin` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 894 | `psknlr/pubmearch` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 895 | `psknlr/paper-search-mcp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 896 | `yarikoptic/ossig` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 897 | `yarikoptic/verse` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 898 | `yarikoptic/hackathon2025` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 899 | `yarikoptic/ipyniivue` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 900 | `yarikoptic/brain2print` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 901 | `yarikoptic/dcmqi` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 902 | `yarikoptic/DesktopCommanderMCP` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 903 | `MikeGong1/MMQTL-sourcecode` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 904 | `yarikoptic/dicom-validator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 905 | `kwskws1998/EEGNet` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 906 | `yarikoptic/swo`, `tschaffter/swo` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 907 | `yarikoptic/the-fair-cookbook` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 908 | `VinnySha/GrandHack-CardioSense` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/6/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 909 | `yarikoptic/niivue` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 910 | `gutendzx/vlm-fairness` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 911 | `Liripo/atlas-feature-selection-benchmark` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 912 | `yarikoptic/neurosift-mcps` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 863 — `Deng-GuiFeng/LPSGM`

Bounded repositories: `gutendzx/LPSGM`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 52, code 49, documentation 2, data 0, manifests 0.

Static security flags: `{"filesystem_mutation": 39, "dynamic_code_execution": 12, "unsafe_deserialization": 10, "path_input": 8, "sql_string_construction": 6, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 17, "hardcoded_absolute_path": 7, "assertion_as_validation": 3}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 865 — `shaunporwal/DICOM-MCP`

Bounded repositories: `shaunporwal/DICOM-MCP`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 6, documentation 2, data 0, manifests 2.

Static security flags: `{"dynamic_code_execution": 1, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 3}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 870 — `ryanDing26/Diabetes-Classifier`

Bounded repositories: `ryanDing26/Diabetes-Classifier`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 3, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 3, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 874 — `BenevolentAI/MolBERT`

Bounded repositories: `KSUN63/MolBERT`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 3, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 9, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 883 — `NationalGenomicsInfrastructure/MultiQC_NGI`

Bounded repositories: `vladsavelyev/MultiQC_NGI`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 1, "network_fetch": 1, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 886 — `Ali-Maq/civic-benchmark-dataset-creation`

Bounded repositories: `Ali-Maq/civic-benchmark-dataset-creation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 2, documentation 2, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 30, "dynamic_code_execution": 15, "sql_string_construction": 9, "path_input": 4, "filesystem_mutation": 2, "mutable_remote_install": 2, "network_fetch": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 23}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 908 — `VinnySha/GrandHack-CardioSense`

Bounded repositories: `VinnySha/GrandHack-CardioSense`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 18, code 9, documentation 6, data 1, manifests 2.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 15}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 911 — `theislab/atlas-feature-selection-benchmark`

Bounded repositories: `Liripo/atlas-feature-selection-benchmark`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

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
