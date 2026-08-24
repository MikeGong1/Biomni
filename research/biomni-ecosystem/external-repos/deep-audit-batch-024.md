# External repository deep audit — Batch 024

Observed at: `2026-08-24T06:25:14Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **963–1012**.
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
| `DEEP_AUDIT_CANDIDATE` | 16 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 29 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 5 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 14 families for security-sensitive primitives, 10 for privacy/data-governance terms, and 10 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 963 | `psknlr/mcp-simple-pubmed` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 964 | `th86/ImmuneBuilder` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 965 | `HelloWorldLTY/task_batch_integration` | `DEEP_AUDIT_CANDIDATE` | 17 | 3/0/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 966 | `Thiraput01/CIBMTR-Equity-in-post-HCT-Survival-Predictions` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 967 | `drgmk/alma_var` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 968 | `tangxuan82/Healthcare` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 969 | `kexinhuang12345/nextjs-ai-bio-assistant` | `DEEP_AUDIT_CANDIDATE` | 0 | 101/2/9 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 970 | `SongyouZhong/dbdataset` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 971 | `yarikoptic/latex-nihbiosketch` | `DEEP_AUDIT_CANDIDATE` | 6 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 972 | `yarikoptic/siibra-python` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 973 | `gutendzx/BiomedCLIP_data_pipeline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 974 | `Rakshitha-Ireddi/polyp-ddpm` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 975 | `samarth-kadaba/TCellAI` | `DEEP_AUDIT_CANDIDATE` | 0 | 17/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 976 | `yarikoptic/podman-hpc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 977 | `sszhu/Medical-SAM2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 978 | `yarikoptic/amaretti` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 979 | `vlln/figure-extractor` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 980 | `goodb/pi-team` | `DEEP_AUDIT_CANDIDATE` | 0 | 59/33/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 981 | `Edison-A-N/fastapi_mcp` | `DEEP_AUDIT_CANDIDATE` | 15 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 982 | `KalinNonchev/DeepCell` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 983 | `23abdul23/DeepSeaROV` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 984 | `marcosbolanos/t1diab-sadm-mk2` | `DEEP_AUDIT_CANDIDATE` | 1 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 985 | `Ali-Maq/Variant_Annontation_ProjectX` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/2/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 986 | `gutendzx/SleepXViT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 987 | `anngvu/htan-linkml` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 988 | `yarikoptic/rapidtide` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 989 | `zhuyitan/Pipeline-Processing-TCGA-Slides-for-MIL` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 990 | `yarikoptic/repronim.org` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 991 | `andrewsu/ontogpt`, `yarikoptic/ontogpt` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 992 | `yarikoptic/openalex-gui` | `DEEP_AUDIT_CANDIDATE` | 449 | 24/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 993 | `yarikoptic/openalex-guts` | `DEEP_AUDIT_CANDIDATE` | 1963 | 34/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 994 | `HelloWorldLTY/GenesTroBot` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 995 | `HelloWorldLTY/Tangram` | `DEEP_AUDIT_CANDIDATE` | 2 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 996 | `yarikoptic/bkbit` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 997 | `HelloWorldLTY/pascient` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 998 | `vladsavelyev/nanostring` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 999 | `leezx/computational-epigenetic-target-discovery` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/7/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1000 | `yarikoptic/bart` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1001 | `samarth-kadaba/ColabDesign` | `DEEP_AUDIT_CANDIDATE` | 5 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1002 | `HelloWorldLTY/enformer-pytorch` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1003 | `vladsavelyev/nextflow` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1004 | `yarikoptic/website` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1005 | `yarikoptic/lucinda` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1006 | `KSUN63/DeepDTA-Pytorch` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/3/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1007 | `yarikoptic/pulpy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1008 | `tangxuan82/Deep_diversification_AAV` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1009 | `yarikoptic/legacy-bids-validator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1010 | `leezx/computational-PROTAC-development` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/3/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1011 | `HelloWorldLTY/RobustCell` | `DEEP_AUDIT_CANDIDATE` | 0 | 114/4/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1012 | `yarikoptic/python-sdk` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 965 — `openproblems-bio/task_batch_integration`

Bounded repositories: `HelloWorldLTY/task_batch_integration`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 5, code 3, documentation 0, data 2, manifests 0.

Static security flags: `{"mutable_remote_install": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 966 — `Thiraput01/CIBMTR-Equity-in-post-HCT-Survival-Predictions`

Bounded repositories: `Thiraput01/CIBMTR-Equity-in-post-HCT-Survival-Predictions`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 5, documentation 1, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 3}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 967 — `drgmk/alma_var`

Bounded repositories: `drgmk/alma_var`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 1, documentation 1, data 1, manifests 1.

Static security flags: `{"filesystem_mutation": 7, "shell_or_process_execution": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 969 — `kexinhuang12345/nextjs-ai-bio-assistant`

Bounded repositories: `kexinhuang12345/nextjs-ai-bio-assistant`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 115, code 101, documentation 2, data 9, manifests 2.

Static security flags: `{"network_fetch": 9, "browser_html_injection": 4, "dynamic_code_execution": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 51, "upload_or_remote_transfer": 33}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 971 — `pmagwene/latex-nihbiosketch`

Bounded repositories: `yarikoptic/latex-nihbiosketch`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 975 — `samarth-kadaba/TCellAI`

Bounded repositories: `samarth-kadaba/TCellAI`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 18, code 17, documentation 1, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 14, "dynamic_code_execution": 6, "path_input": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 3}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 9, "unseeded_randomness": 8, "assertion_as_validation": 4}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 980 — `goodb/pi-team`

Bounded repositories: `goodb/pi-team`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 96, code 59, documentation 33, data 2, manifests 2.

Static security flags: `{"shell_or_process_execution": 33, "network_fetch": 28, "dynamic_code_execution": 18, "path_input": 13, "filesystem_mutation": 9, "browser_html_injection": 6, "server_exposure": 2, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1285, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 646}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 981 — `tadata-org/fastapi_mcp`

Bounded repositories: `Edison-A-N/fastapi_mcp`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 8, code 7, documentation 1, data 0, manifests 0.

Static security flags: `{"network_fetch": 12}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 409}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 982 — `KalinNonchev/DeepCell`

Bounded repositories: `KalinNonchev/DeepCell`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 9, code 5, documentation 2, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 2, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 4, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 984 — `dark-peak-analytics/sadm-mk2-demo`

Bounded repositories: `marcosbolanos/t1diab-sadm-mk2`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 992 — `ourresearch/openalex-gui`

Bounded repositories: `yarikoptic/openalex-gui`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 26, code 24, documentation 0, data 0, manifests 2.

Static security flags: `{"network_fetch": 4}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 8}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 993 — `ourresearch/openalex-guts`

Bounded repositories: `yarikoptic/openalex-guts`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 40, code 34, documentation 4, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 20, "network_fetch": 7, "server_exposure": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 995 — `broadinstitute/Tangram`

Bounded repositories: `HelloWorldLTY/Tangram`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 2, documentation 0, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 4, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1001 — `sokrypton/ColabDesign`

Bounded repositories: `samarth-kadaba/ColabDesign`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 4, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1006 — `KSUN63/DeepDTA-Pytorch`

Bounded repositories: `KSUN63/DeepDTA-Pytorch`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 4, documentation 3, data 3, manifests 0.

Static security flags: `{"dynamic_code_execution": 2, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1011 — `HelloWorldLTY/RobustCell`

Bounded repositories: `HelloWorldLTY/RobustCell`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 120, code 114, documentation 4, data 1, manifests 1.

Static security flags: `{"dynamic_code_execution": 46, "unsafe_deserialization": 24}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 125, "hardcoded_threshold": 71}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
