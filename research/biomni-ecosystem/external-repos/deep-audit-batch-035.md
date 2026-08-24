# External repository deep audit — Batch 035

Observed at: `2026-08-24T06:29:01Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1513–1562**.
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
| `DEEP_AUDIT_CANDIDATE` | 14 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 33 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 12 families for security-sensitive primitives, 10 for privacy/data-governance terms, and 10 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1513 | `aevo98765/CellProfiler` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1514 | `andrewsu/ScriptShare` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1515 | `tschaffter/SynapseWebClient` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1516 | `alexj-lee/proteinmpnn` | `DEEP_AUDIT_CANDIDATE` | 0 | 55/60/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1517 | `Vik-u/kcat-km` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1518 | `Vik-u/DeepFRI` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1519 | `HelloWorldLTY/scDeepSort` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1520 | `inodb/sufam` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/2/14 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1521 | `HelloWorldLTY/scAAnet` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1522 | `amehrjou/dynamo-release` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1523 | `yarikoptic/repronim.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1524 | `zskylarli/scrna-bacteria-integration` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/2/7 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1525 | `KSUN63/DLPacker` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1526 | `yarikoptic/datalad-mihextras` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1527 | `fionaxc/gossis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1528 | `michiyasunaga/LinkBERT` | `DEEP_AUDIT_CANDIDATE` | 0 | 19/1/6 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1529 | `zskylarli/bacteriaGAN` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1530 | `andrewsu/cellxgene` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1531 | `HelloWorldLTY/scTransformer` | `DEEP_AUDIT_CANDIDATE` | 0 | 11/6/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1532 | `vladsavelyev/hail-elasticsearch-pipelines` | `DEEP_AUDIT_CANDIDATE` | 543 | 19/1/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1533 | `amehrjou/genedisco` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1534 | `alexj-lee/harnik-rna-spatial-journalclub` | `DEEP_AUDIT_CANDIDATE` | 0 | 56/80/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1535 | `andrewsu/RTX` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1536 | `Vik-u/rdchiral` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1537 | `tschaffter/genenetweaver` | `DEEP_AUDIT_CANDIDATE` | 0 | 146/55/70 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1538 | `Mr-Milk/UnMicst` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1539 | `Liripo/AutomaticCellTypeIdentification` | `DOC_METADATA_MAINTENANCE_ONLY` | 3 | 0/0/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1540 | `yarikoptic/neurodebian` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1541 | `inodb/HTAN-Data-Ingress-Docs` | `DEEP_AUDIT_CANDIDATE` | 129 | 0/16/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1542 | `tschaffter/gh-openapi-docs` | `DEEP_AUDIT_CANDIDATE` | 4 | 3/0/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1543 | `Vik-u/DeepConv-DTI` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1544 | `tschaffter/Synapse-React-Client` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1545 | `tschaffter/resource-discovery-api` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1546 | `zhanxw/rvtests` | `DEEP_AUDIT_CANDIDATE` | 0 | 348/4/7 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1547 | `dabulseco/SMILES_generator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1548 | `yarikoptic/neurodatapub` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1549 | `HelloWorldLTY/neurips2021_multimodal_topmethods` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1550 | `yarikoptic/MRIcroGL` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1551 | `inodb/cbioportal-frontend-archive-1` | `DEEP_AUDIT_CANDIDATE` | 0 | 24/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1552 | `tschaffter/resource-discovery-portal` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1553 | `HelloWorldLTY/Bioinfor_researchers_atlas` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1554 | `tangxuan82/CNN_protein_landscape` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1555 | `changwn/ChIP-seq_JiZhang` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1556 | `NKalavros/rstudio` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1557 | `HelloWorldLTY/Awesome-Bioinformatics-Papers` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1558 | `HelloWorldLTY/BiAE` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1559 | `Vik-u/SteadyState-MFA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1560 | `erhuve/SlicerCompose` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1561 | `leezx/scvelo_notebooks` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1562 | `inodb/hdash` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 1516 — `alexj-lee/proteinmpnn`

Bounded repositories: `alexj-lee/proteinmpnn`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 120, code 55, documentation 60, data 0, manifests 2.

Static security flags: `{"dynamic_code_execution": 179, "browser_html_injection": 79, "sql_string_construction": 20, "path_input": 6, "mutable_remote_install": 6, "server_exposure": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 20, "upload_or_remote_transfer": 9, "human_genomics": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 116, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1520 — `inodb/sufam`

Bounded repositories: `inodb/sufam`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 28, code 9, documentation 2, data 14, manifests 2.

Static security flags: `{"shell_or_process_execution": 14, "filesystem_mutation": 4, "path_input": 3, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"human_genomics": 70, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 7, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1524 — `zskylarli/scrna-bacteria-integration`

Bounded repositories: `zskylarli/scrna-bacteria-integration`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 1, documentation 2, data 7, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1528 — `michiyasunaga/LinkBERT`

Bounded repositories: `michiyasunaga/LinkBERT`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 27, code 19, documentation 1, data 6, manifests 0.

Static security flags: `{"shell_or_process_execution": 18}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 26, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1529 — `zskylarli/bacteriaGAN`

Bounded repositories: `zskylarli/bacteriaGAN`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 3, documentation 1, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 1, "network_fetch": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 3}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1531 — `HelloWorldLTY/scTransformer`

Bounded repositories: `HelloWorldLTY/scTransformer`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 17, code 11, documentation 6, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 7, "mutable_remote_install": 3, "dynamic_code_execution": 2, "shell_or_process_execution": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 10, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1532 — `broadinstitute/seqr-loading-pipelines`

Bounded repositories: `vladsavelyev/hail-elasticsearch-pipelines`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 25, code 19, documentation 1, data 2, manifests 2.

Static security flags: `{"shell_or_process_execution": 9, "dynamic_code_execution": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"human_genomics": 229, "upload_or_remote_transfer": 17}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 13, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1534 — `alexj-lee/harnik-rna-spatial-journalclub`

Bounded repositories: `alexj-lee/harnik-rna-spatial-journalclub`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 141, code 56, documentation 80, data 0, manifests 2.

Static security flags: `{"dynamic_code_execution": 179, "browser_html_injection": 79, "sql_string_construction": 20, "path_input": 6, "mutable_remote_install": 6}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 20, "clinical_or_patient_data": 4, "upload_or_remote_transfer": 4, "human_genomics": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 116, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1537 — `tschaffter/genenetweaver`

Bounded repositories: `tschaffter/genenetweaver`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 272, code 146, documentation 55, data 70, manifests 0.

Static security flags: `{"sql_string_construction": 40, "dynamic_code_execution": 2, "shell_or_process_execution": 2, "path_input": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 28}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 77, "unseeded_randomness": 14, "hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1541 — `ao508/HTAN-data-ingress-documentation-draft`

Bounded repositories: `inodb/HTAN-Data-Ingress-Docs`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 17, code 0, documentation 16, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 113, "upload_or_remote_transfer": 112, "clinical_or_patient_data": 21}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1542 — `ga4gh/gh-openapi-docs`

Bounded repositories: `tschaffter/gh-openapi-docs`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 6, code 3, documentation 0, data 1, manifests 2.

Static security flags: `{"mutable_remote_install": 3, "dynamic_code_execution": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1546 — `zhanxw/rvtests`

Bounded repositories: `zhanxw/rvtests`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 363, code 348, documentation 4, data 7, manifests 4.

Static security flags: `{"sql_string_construction": 29, "dynamic_code_execution": 28, "mutable_remote_install": 5}`.

Privacy/data-governance flags: `{"human_genomics": 1299, "clinical_or_patient_data": 21, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 15, "unseeded_randomness": 11, "hardcoded_threshold": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1551 — `inodb/cbioportal-frontend-archive-1`

Bounded repositories: `inodb/cbioportal-frontend-archive-1`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 44, code 24, documentation 5, data 0, manifests 13.

Static security flags: `{"filesystem_mutation": 10, "mutable_remote_install": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 28, "named_biomedical_cohort": 16, "human_genomics": 5, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1558 — `HelloWorldLTY/BiAE`

Bounded repositories: `HelloWorldLTY/BiAE`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
