# External repository deep audit — Batch 037

Observed at: `2026-08-24T06:29:44Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1613–1662**.
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
| `DEEP_AUDIT_CANDIDATE` | 16 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 26 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 7 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 1 |
| `EMPTY` | 0 |

Static-review flags were present in 16 families for security-sensitive primitives, 14 for privacy/data-governance terms, and 11 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1613 | `leezx/VariantToGene` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1614 | `yarikoptic/reproseed` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1615 | `yarikoptic/brainhack_jupyter_book` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1616 | `tschaffter/nlpsandbox-schemas` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1617 | `changwn/SnapATAC` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1618 | `jaybee84/research` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1619 | `Zethson/guide-seq-container` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1620 | `yarikoptic/metadata-model` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1621 | `Pidem/mgp-tcn` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1622 | `yarikoptic/data-multi-subject` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1623 | `jaybee84/iatlas.api.client` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1624 | `yarikoptic/testkraken` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1625 | `tangxuan82/u24_lymphocyte` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1626 | `Vik-u/EnzymePromiscuityClassification` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1627 | `zhanxw/MetaPrism` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1628 | `zhanxw/BayesSMILES` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1629 | `zhanxw/BayesSMILES_web` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/5/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1630 | `DevinDeSilva/astropy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1631 | `vladsavelyev/cacao` | `DEEP_AUDIT_CANDIDATE` | 21 | 5/0/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1632 | `vladsavelyev/oviraptor` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/4/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1633 | `yarikoptic/roiextractors` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1634 | `vladsavelyev/NGS_Utils` | `DEEP_AUDIT_CANDIDATE` | 0 | 89/24/27 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1635 | `zhanxw/MB-GAN` | `DEEP_AUDIT_CANDIDATE` | 0 | 21/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1636 | `Zethson/igem_tuebingen_website` | `DEEP_AUDIT_CANDIDATE` | 0 | 38/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1637 | `changwn/cellrank` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1638 | `kexinhuang12345/MolDesigner-Public` | `DEEP_AUDIT_CANDIDATE` | 0 | 11/3/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1639 | `changwn/DTF-Drug-Synergy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1640 | `changwn/mars` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1641 | `inodb/hsim` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1642 | `drgmk/pandeia-disks` | `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 | 4/1/2 | CLOSE_METADATA_FALSE_POSITIVE; no bounded biomedical or scientific-agent capability verified |
| 1643 | `NKalavros/NinjaPCR` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1644 | `kexinhuang12345/CASTER` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1645 | `kexinhuang12345/scGNN` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1646 | `vladsavelyev/cpsr` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1647 | `vladsavelyev/pcgr` | `DEEP_AUDIT_CANDIDATE` | 11 | 6/0/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1648 | `jaybee84/NF_data_curator` | `DEEP_AUDIT_CANDIDATE` | 40 | 4/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1649 | `changwn/enrichR` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1650 | `leezx/ModuleSelection` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1651 | `tschaffter/synapsePythonClient` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1652 | `vladsavelyev/gridss` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1653 | `jaybee84/druid` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1654 | `lishengting/stLFR_V1.3` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1655 | `vladsavelyev/seqr` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1656 | `vladsavelyev/gnomad-browser` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1657 | `vladsavelyev/reference_data` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/2/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1658 | `leezx/TI` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1659 | `explorerwjy/BrainDisorders` | `DEEP_AUDIT_CANDIDATE` | 0 | 23/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1660 | `jaybee84/JHU-biobank` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/0/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1661 | `kexinhuang12345/DrugDataResource` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1662 | `yarikoptic/terms` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 1613 — `leezx/VariantToGene`

Bounded repositories: `leezx/VariantToGene`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 2, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 1}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1629 — `zhanxw/BayesSMILES_web`

Bounded repositories: `zhanxw/BayesSMILES_web`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 19, code 9, documentation 5, data 2, manifests 3.

Static security flags: `{"mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 4, "named_biomedical_cohort": 4}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1631 — `sigven/cacao`

Bounded repositories: `vladsavelyev/cacao`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 8, code 5, documentation 0, data 3, manifests 0.

Static security flags: `{"shell_or_process_execution": 11}`.

Privacy/data-governance flags: `{"human_genomics": 6, "clinical_or_patient_data": 2, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1632 — `vladsavelyev/oviraptor`

Bounded repositories: `vladsavelyev/oviraptor`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 16, code 5, documentation 4, data 4, manifests 2.

Static security flags: `{"mutable_remote_install": 2, "shell_or_process_execution": 1}`.

Privacy/data-governance flags: `{"human_genomics": 18, "clinical_or_patient_data": 3, "upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1634 — `vladsavelyev/NGS_Utils`

Bounded repositories: `vladsavelyev/NGS_Utils`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 144, code 89, documentation 24, data 27, manifests 2.

Static security flags: `{"dynamic_code_execution": 71, "shell_or_process_execution": 49, "browser_html_injection": 24, "filesystem_mutation": 20, "sql_string_construction": 20, "path_input": 12, "mutable_remote_install": 3, "unsafe_deserialization": 2}`.

Privacy/data-governance flags: `{"human_genomics": 146, "clinical_or_patient_data": 10, "upload_or_remote_transfer": 7}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 40, "unseeded_randomness": 4}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1635 — `zhanxw/MB-GAN`

Bounded repositories: `zhanxw/MB-GAN`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 23, code 21, documentation 1, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 3, "dynamic_code_execution": 2, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 65}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 8, "hardcoded_threshold": 5, "assertion_as_validation": 3}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1636 — `Zethson/igem_tuebingen_website`

Bounded repositories: `Zethson/igem_tuebingen_website`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 44, code 38, documentation 3, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 21, "browser_html_injection": 10, "shell_or_process_execution": 5, "sql_string_construction": 4, "server_exposure": 2, "filesystem_mutation": 2, "path_input": 1, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1638 — `kexinhuang12345/MolDesigner-Public`

Bounded repositories: `kexinhuang12345/MolDesigner-Public`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 17, code 11, documentation 3, data 2, manifests 0.

Static security flags: `{"unsafe_deserialization": 7, "mutable_remote_install": 5, "dynamic_code_execution": 3, "network_fetch": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 8, "hardcoded_threshold": 4, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1644 — `kexinhuang12345/CASTER`

Bounded repositories: `kexinhuang12345/CASTER`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 11, code 8, documentation 2, data 1, manifests 0.

Static security flags: `{"dynamic_code_execution": 9, "unsafe_deserialization": 6}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 3, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1645 — `kexinhuang12345/scGNN`

Bounded repositories: `kexinhuang12345/scGNN`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 3, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 3}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1647 — `sigven/pcgr`

Bounded repositories: `vladsavelyev/pcgr`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 8, code 6, documentation 0, data 2, manifests 0.

Static security flags: `{"shell_or_process_execution": 22, "path_input": 15, "sql_string_construction": 4}`.

Privacy/data-governance flags: `{"human_genomics": 269, "clinical_or_patient_data": 15, "named_biomedical_cohort": 9}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 2, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1648 — `nf-osi/NF_data_curator`

Bounded repositories: `jaybee84/NF_data_curator`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 7, code 4, documentation 2, data 1, manifests 0.

Static security flags: `{"sql_string_construction": 6}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 34, "upload_or_remote_transfer": 13}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1652 — `PapenfussLab/gridss`

Bounded repositories: `vladsavelyev/gridss`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 1}`.

Privacy/data-governance flags: `{"human_genomics": 20}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1657 — `vladsavelyev/reference_data`

Bounded repositories: `vladsavelyev/reference_data`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 4, documentation 2, data 2, manifests 2.

Static security flags: `{"shell_or_process_execution": 2, "unsafe_deserialization": 2, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 16, "upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1658 — `leezx/TI`

Bounded repositories: `leezx/TI`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 2, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1659 — `explorerwjy/BrainDisorders`

Bounded repositories: `explorerwjy/BrainDisorders`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 23, code 23, documentation 0, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 3, "dynamic_code_execution": 2}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 99, "human_genomics": 28, "upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 158, "unseeded_randomness": 43, "hardcoded_threshold": 15, "assertion_as_validation": 5}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
