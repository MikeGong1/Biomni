# External repository deep audit — Batch 040

Observed at: `2026-08-24T06:30:47Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1763–1812**.
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
| `DEEP_AUDIT_CANDIDATE` | 15 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 35 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 0 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 10 families for security-sensitive primitives, 13 for privacy/data-governance terms, and 6 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1763 | `yarikoptic/ten-years` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1764 | `NKalavros/mdpr-full` | `DEEP_AUDIT_CANDIDATE` | 0 | 11/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1765 | `inodb/genome-nexus-cli` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1766 | `kexinhuang12345/ESPF` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/7/6 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1767 | `Sanat-Mishra/Analysing-Synonymous-Mutations.` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1768 | `yarikoptic/PyMVPA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1769 | `NKalavros/thyroid-cancer-a-bioinformatics-approach` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1770 | `drgmk/exocomet_hunt_TESS_sector_results` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1771 | `drgmk/exocomet_hunt` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1772 | `Vik-u/brendapy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1773 | `vladsavelyev/TargQC` | `DEEP_AUDIT_CANDIDATE` | 0 | 31/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1774 | `yarikoptic/nipype_tutorial` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1775 | `changwn/ATAC_integrity` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1776 | `yarikoptic/kwyk` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1777 | `changwn/MTCT` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1778 | `jaybee84/cdom` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1779 | `yarikoptic/ds000164` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1780 | `jaybee84/sandbox-provisioner` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1781 | `jaybee84/rare-disease-workflows` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1782 | `jaybee84/nf-hackathon-2019` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1783 | `shengyongniu/MIMOSCA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1784 | `inodb/cbsp-hackathon` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1785 | `yarikoptic/najafi-2018-nwb` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1786 | `vladsavelyev/MegaQC` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1787 | `inodb/oncoprintjs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1788 | `vladsavelyev/manta` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1789 | `jaybee84/sage-workflows-sandbox` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/19/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1790 | `jaybee84/nfResources` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1791 | `yarikoptic/eegBidsCreator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1792 | `yarikoptic/fmriflows` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1793 | `jaybee84/NEXUS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1794 | `zhanxw/TCR_explorer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1795 | `vladsavelyev/simple_sv_annotation` | `DEEP_AUDIT_CANDIDATE` | 33 | 0/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1796 | `jaybee84/Genie` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1797 | `tschaffter/mortality_prediction_docker_model` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1798 | `zhanxw/TCR_explorer_package` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1799 | `inodb/msk-insight` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1800 | `manu-tej/Kinect2` | `DEEP_AUDIT_CANDIDATE` | 0 | 11/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1801 | `inodb/vcf2maf` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1802 | `inodb/biogene-backend` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1803 | `jaybee84/synapseAnnotations` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1804 | `vladsavelyev/cawdor` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/9 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1805 | `jaybee84/synapser` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1806 | `inodb/session-service` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1807 | `shengyongniu/rSeqTU` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1808 | `zhanxw/birdseed2vcf` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1809 | `vladsavelyev/umcaw` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/12/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1810 | `jaybee84/scrattch.hicat` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1811 | `jaybee84/Zika-RNAseq-Pipeline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1812 | `vladsavelyev/Sarek` | `DEEP_AUDIT_CANDIDATE` | 0 | 24/37/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 1764 — `NKalavros/mdpr-full`

Bounded repositories: `NKalavros/mdpr-full`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 14, code 11, documentation 1, data 1, manifests 0.

Static security flags: `{"shell_or_process_execution": 29, "filesystem_mutation": 19, "sql_string_construction": 4, "server_exposure": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 4, "hardcoded_absolute_path": 2, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1766 — `kexinhuang12345/ESPF`

Bounded repositories: `kexinhuang12345/ESPF`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 14, code 1, documentation 7, data 6, manifests 0.

Static security flags: `{"dynamic_code_execution": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1767 — `Sanat-Mishra/Analysing-Synonymous-Mutations.`

Bounded repositories: `Sanat-Mishra/Analysing-Synonymous-Mutations.`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 4, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 4}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 5}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1769 — `NKalavros/thyroid-cancer-a-bioinformatics-approach`

Bounded repositories: `NKalavros/thyroid-cancer-a-bioinformatics-approach`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 4, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1773 — `vladsavelyev/TargQC`

Bounded repositories: `vladsavelyev/TargQC`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 40, code 31, documentation 5, data 0, manifests 2.

Static security flags: `{"filesystem_mutation": 20, "shell_or_process_execution": 13, "path_input": 2, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{"human_genomics": 5, "upload_or_remote_transfer": 3}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 9, "unseeded_randomness": 2, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1775 — `changwn/ATAC_integrity`

Bounded repositories: `changwn/ATAC_integrity`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 3, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 7}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1777 — `changwn/MTCT`

Bounded repositories: `changwn/MTCT`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 10, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1789 — `jaybee84/sage-workflows-sandbox`

Bounded repositories: `jaybee84/sage-workflows-sandbox`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 20, code 1, documentation 19, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 11, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1795 — `AstraZeneca-NGS/simple_sv_annotation`

Bounded repositories: `vladsavelyev/simple_sv_annotation`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 0, documentation 1, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 6}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1800 — `manu-tej/Kinect2`

Bounded repositories: `manu-tej/Kinect2`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 13, code 11, documentation 1, data 1, manifests 0.

Static security flags: `{"shell_or_process_execution": 48, "filesystem_mutation": 10, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 23}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 7, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1804 — `vladsavelyev/cawdor`

Bounded repositories: `vladsavelyev/cawdor`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 13, code 3, documentation 1, data 9, manifests 0.

Static security flags: `{"shell_or_process_execution": 16, "filesystem_mutation": 3, "mutable_remote_install": 3}`.

Privacy/data-governance flags: `{"human_genomics": 14, "named_biomedical_cohort": 12, "clinical_or_patient_data": 6}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 5, "hardcoded_absolute_path": 4}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1807 — `shengyongniu/rSeqTU`

Bounded repositories: `shengyongniu/rSeqTU`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 5, documentation 2, data 1, manifests 1.

Static security flags: `{"sql_string_construction": 8}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1808 — `ding-lab/birdseed2vcf`

Bounded repositories: `zhanxw/birdseed2vcf`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 12, "named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1809 — `vladsavelyev/umcaw`

Bounded repositories: `vladsavelyev/umcaw`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 20, code 2, documentation 12, data 3, manifests 2.

Static security flags: `{"mutable_remote_install": 5}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1812 — `nf-core/sarek`

Bounded repositories: `vladsavelyev/Sarek`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 78, code 24, documentation 37, data 4, manifests 12.

Static security flags: `{"mutable_remote_install": 76, "dynamic_code_execution": 13, "shell_or_process_execution": 8, "filesystem_mutation": 4, "sql_string_construction": 4, "network_fetch": 3, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 387, "upload_or_remote_transfer": 17, "clinical_or_patient_data": 13, "named_biomedical_cohort": 6}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
