# External repository deep audit — Batch 039

Observed at: `2026-08-24T06:30:32Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1713–1762**.
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
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 35 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 1 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 8 families for security-sensitive primitives, 8 for privacy/data-governance terms, and 8 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1713 | `hannes-brt/COVID-19` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1714 | `inodb/mira-graphql` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1715 | `inodb/mira-react` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1716 | `inodb/es-loaders` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1717 | `inodb/r-workshop-march-2019` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1718 | `jaybee84/covid-chestxray-dataset` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1719 | `zhanxw/MicrobiotaProcess` | `DEEP_AUDIT_CANDIDATE` | 3 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1720 | `Vik-u/MolecularTransformer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1721 | `jaybee84/rootstock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1722 | `yarikoptic/dandi.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1723 | `inodb/revmut` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/10/9 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1724 | `inodb/spectrum-viz-website` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1725 | `inodb/cellassign` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1726 | `tschaffter/ctsi-mcw-deid` | `DEEP_AUDIT_CANDIDATE` | 3 | 0/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1727 | `yarikoptic/AllenSDK` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1728 | `inodb/readthedocs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1729 | `changwn/scRNAseq_pipelines` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1730 | `Javkhaa/rna_seq_analysis` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/3/11 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1731 | `vladsavelyev/Conpair` | `DEEP_AUDIT_CANDIDATE` | 5 | 8/8/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1732 | `jaybee84/kairos` | `DEEP_AUDIT_CANDIDATE` | 27 | 20/3/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1733 | `NKalavros/MUDAN` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1734 | `jucor/HighRes-net` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1735 | `yarikoptic/human-connectome-project-openaccess` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1736 | `kexinhuang12345/drug-bert` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1737 | `changwn/Chinese-Medical-QA-Data` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1738 | `yarikoptic/pynwb-feedstock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1739 | `vladsavelyev/ClearUp` | `DEEP_AUDIT_CANDIDATE` | 0 | 30/10/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1740 | `jaybee84/NF_LandscapePaper_2019-1` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/3/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1741 | `Vik-u/BRENDA-Parser` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1742 | `leezx/GWA_tutorial` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1743 | `Zethson/MHCBoost` | `DEEP_AUDIT_CANDIDATE` | 0 | 28/392/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1744 | `Ali-Maq/report-nips-style` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1745 | `yarikoptic/mne-study-template` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1746 | `leezx/gatk4-jupyter-notebook-tutorials` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1747 | `manu-tej/Fish_counter` | `DEEP_AUDIT_CANDIDATE` | 0 | 6/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1748 | `tschaffter/Synapse-Repository-Services` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1749 | `leezx/atac-seq-pipeline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1750 | `leezx/chip-seq-pipeline2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1751 | `yarikoptic/reproin` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1752 | `yarikoptic/spikeforest2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1753 | `inodb/clinical-timeline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1754 | `yarikoptic/spikeinterface` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1755 | `explorerwjy/spark_genomics` | `DEEP_AUDIT_CANDIDATE` | 0 | 21/4/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1756 | `NKalavros/fesetup` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1757 | `yarikoptic/module-intro` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1758 | `mickaelleclercq/mirdup` | `DEEP_AUDIT_CANDIDATE` | 0 | 26/4/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1759 | `yarikoptic/allen-neuropixels-try1` | `DEEP_AUDIT_CANDIDATE` | 0 | 0/0/1 | REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead |
| 1760 | `andrewsu/bte_schema` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1761 | `Ali-Maq/Linguistic-Explorer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1762 | `andrewsu/translator-hackathon-20190917` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 1719 — `YuLab-SMU/MicrobiotaProcess`

Bounded repositories: `zhanxw/MicrobiotaProcess`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 0, documentation 0, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1723 — `inodb/revmut`

Bounded repositories: `inodb/revmut`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 31, code 9, documentation 10, data 9, manifests 2.

Static security flags: `{"shell_or_process_execution": 9, "filesystem_mutation": 4, "path_input": 3, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 156, "human_genomics": 11, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 7}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1726 — `jayurbain/ctsi-mcw-deid`

Bounded repositories: `tschaffter/ctsi-mcw-deid`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 0, documentation 1, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 6}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 96}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1730 — `Javkhaa/rna_seq_analysis`

Bounded repositories: `Javkhaa/rna_seq_analysis`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 18, code 4, documentation 3, data 11, manifests 0.

Static security flags: `{"mutable_remote_install": 7, "shell_or_process_execution": 2, "network_fetch": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 18, "human_genomics": 6}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 3, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1731 — `nygenome/Conpair`

Bounded repositories: `vladsavelyev/Conpair`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 20, code 8, documentation 8, data 3, manifests 1.

Static security flags: `{"mutable_remote_install": 3, "sql_string_construction": 3, "shell_or_process_execution": 1}`.

Privacy/data-governance flags: `{"human_genomics": 14}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1732 — `nf-osi/kairos`

Bounded repositories: `jaybee84/kairos`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 28, code 20, documentation 3, data 2, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 177}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1739 — `vladsavelyev/ClearUp`

Bounded repositories: `vladsavelyev/ClearUp`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 43, code 30, documentation 10, data 0, manifests 3.

Static security flags: `{"dynamic_code_execution": 69, "sql_string_construction": 49, "browser_html_injection": 25, "shell_or_process_execution": 17, "path_input": 6, "filesystem_mutation": 4, "server_exposure": 2, "hardcoded_secret_shape": 2, "unsafe_deserialization": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 186, "clinical_or_patient_data": 126, "upload_or_remote_transfer": 21, "named_biomedical_cohort": 5}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 13, "hardcoded_absolute_path": 9, "unseeded_randomness": 5, "hardcoded_threshold": 5}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1740 — `jaybee84/NF_LandscapePaper_2019-1`

Bounded repositories: `jaybee84/NF_LandscapePaper_2019-1`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 6, code 1, documentation 3, data 1, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 3, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1743 — `Zethson/MHCBoost`

Bounded repositories: `Zethson/MHCBoost`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 424, code 28, documentation 392, data 2, manifests 1.

Static security flags: `{"path_input": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1747 — `manu-tej/Fish_counter`

Bounded repositories: `manu-tej/Fish_counter`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 6, documentation 1, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 5, "filesystem_mutation": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 5}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1755 — `explorerwjy/spark_genomics`

Bounded repositories: `explorerwjy/spark_genomics`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 30, code 21, documentation 4, data 4, manifests 0.

Static security flags: `{"network_fetch": 24, "path_input": 6}`.

Privacy/data-governance flags: `{"human_genomics": 147}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 68, "unseeded_randomness": 3, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1758 — `mickaelleclercq/mirdup`

Bounded repositories: `mickaelleclercq/mirdup`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 31, code 26, documentation 4, data 1, manifests 0.

Static security flags: `{"dynamic_code_execution": 10, "shell_or_process_execution": 4, "sql_string_construction": 4}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 9, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1759 — `yarikoptic/allen-neuropixels-try1`

Bounded repositories: `yarikoptic/allen-neuropixels-try1`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 2, code 0, documentation 0, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead**.

### Order 1762 — `andrewsu/translator-hackathon-20190917`

Bounded repositories: `andrewsu/translator-hackathon-20190917`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 5, documentation 0, data 0, manifests 0.

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
