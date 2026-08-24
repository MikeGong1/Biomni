# External repository deep audit — Batch 041

Observed at: `2026-08-24T06:31:11Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1813–1862**.
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
| `DEEP_AUDIT_CANDIDATE` | 22 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 24 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 4 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 12 families for security-sensitive primitives, 11 for privacy/data-governance terms, and 13 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1813 | `jaybee84/TRAP_Dashboard` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1814 | `vladsavelyev/lumpy-sv` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1815 | `yarikoptic/gearificator` | `DEEP_AUDIT_CANDIDATE` | 0 | 17/4/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1816 | `NKalavros/Gene-Expression-and-Mutation-Associations` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1817 | `Sanat-Mishra/MarkAndRecapture` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1818 | `andrewsu/ngly1-neo4j-guides` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1819 | `vladsavelyev/superFreq` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1820 | `yarikoptic/OSODOS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1821 | `Sanat-Mishra/Population-Growth-Models` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1822 | `zhanxw/MicrobiomeBayesDiff` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1823 | `jaybee84/ceres` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1824 | `tschaffter/synapseDocs` | `DEEP_AUDIT_CANDIDATE` | 295 | 3/39/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1825 | `tangxuan82/digital_twin_by_GAN` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1826 | `zhanxw/microbiomeViz` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1827 | `Mr-Milk/bioinformatics-programming-homework` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1828 | `jaybee84/Gene_Exp_Viewer` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1829 | `NKalavros/NeuralTuringMachine` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1830 | `vladsavelyev/sequana` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1831 | `yarikoptic/gearificated-nipype` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/4/27 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1832 | `vladsavelyev/joinx` | `DEEP_AUDIT_CANDIDATE` | 6 | 0/0/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1833 | `drgmk/hd98800_alma_c5` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1834 | `yarikoptic/datalad-revolution` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1835 | `jaybee84/markov-link-method` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1836 | `yarikoptic/exchange` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1837 | `yarikoptic/mrtrix3` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1838 | `inodb/oncokb` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1839 | `inodb/oncokb-public` | `DEEP_AUDIT_CANDIDATE` | 85 | 11/34/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1840 | `manu-tej/dPCA` | `DEEP_AUDIT_CANDIDATE` | 4 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1841 | `drgmk/feb-accel` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1842 | `kexinhuang12345/mitotic_spindle` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1843 | `yarikoptic/simple_workflow` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1844 | `drgmk/automated_exocomet_hunt` | `DEEP_AUDIT_CANDIDATE` | 22 | 1/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1845 | `vladsavelyev/cyvcf2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1846 | `yarikoptic/BidsModelSchema` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1847 | `Sanat-Mishra/IISER-Mohali` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1848 | `yarikoptic/tpl-MNI152NLin2009cAsym` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1849 | `zhanxw/rvtests-docker` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1850 | `th86/gislkit` | `DEEP_AUDIT_CANDIDATE` | 0 | 41/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1851 | `lxasqjc/numSCAL_basic` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1852 | `drgmk/cb_2018` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1853 | `yarikoptic/datalad-service` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1854 | `yarikoptic/whole-tale` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1855 | `drgmk/uvplot` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1856 | `shengyongniu/bulk_rna_seq_tophat` | `DEEP_AUDIT_CANDIDATE` | 0 | 16/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1857 | `shengyongniu/bulk_ATAC_seq` | `DEEP_AUDIT_CANDIDATE` | 0 | 13/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1858 | `lxasqjc/Deeper-Image-Quality-Transfer-Training-Low-Memory-Neural-Networks-for-3D-Images` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1859 | `andrewsu/Applied-Bioinformatics_Homeworks` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1860 | `andrewsu/Applied-Bioinformatics` | `DEEP_AUDIT_CANDIDATE` | 2 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1861 | `shengyongniu/eQTL` | `DEEP_AUDIT_CANDIDATE` | 12 | 0/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1862 | `shengyongniu/SeqTU` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 1815 — `yarikoptic/gearificator`

Bounded repositories: `yarikoptic/gearificator`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 26, code 17, documentation 4, data 2, manifests 1.

Static security flags: `{"filesystem_mutation": 5, "mutable_remote_install": 4, "shell_or_process_execution": 3, "path_input": 2, "dynamic_code_execution": 1, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 16}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 29, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1816 — `NKalavros/Gene-Expression-and-Mutation-Associations`

Bounded repositories: `NKalavros/Gene-Expression-and-Mutation-Associations`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 4, documentation 2, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 4}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1821 — `Sanat-Mishra/Population-Growth-Models`

Bounded repositories: `Sanat-Mishra/Population-Growth-Models`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1824 — `ychae/synapseDocs`

Bounded repositories: `tschaffter/synapseDocs`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 43, code 3, documentation 39, data 0, manifests 1.

Static security flags: `{"sql_string_construction": 7, "mutable_remote_install": 2}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 554, "upload_or_remote_transfer": 118, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1827 — `Mr-Milk/bioinformatics-programming-homework`

Bounded repositories: `Mr-Milk/bioinformatics-programming-homework`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 31, code 27, documentation 4, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 3}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1830 — `sequana/sequana`

Bounded repositories: `vladsavelyev/sequana`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 7, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 10, "hardcoded_threshold": 3, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1831 — `yarikoptic/gearificated-nipype`

Bounded repositories: `yarikoptic/gearificated-nipype`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 41, code 1, documentation 4, data 27, manifests 9.

Static security flags: `{"filesystem_mutation": 5}`.

Privacy/data-governance flags: `{"human_genomics": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1832 — `genome/joinx`

Bounded repositories: `vladsavelyev/joinx`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 0, documentation 0, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1833 — `drgmk/hd98800_alma_c5`

Bounded repositories: `drgmk/hd98800_alma_c5`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 9, code 4, documentation 4, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 22}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 7}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 3, "unseeded_randomness": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1839 — `oncokb/oncokb-public`

Bounded repositories: `inodb/oncokb-public`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 45, code 11, documentation 34, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 20, "dynamic_code_execution": 2, "server_exposure": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 78, "clinical_or_patient_data": 30, "upload_or_remote_transfer": 2, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1840 — `machenslab/dPCA`

Bounded repositories: `manu-tej/dPCA`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 2, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1841 — `drgmk/feb-accel`

Bounded repositories: `drgmk/feb-accel`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 3, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1844 — `greghope667/comet_project`

Bounded repositories: `drgmk/automated_exocomet_hunt`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 1, documentation 2, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 2, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1847 — `Sanat-Mishra/IISER-Mohali`

Bounded repositories: `Sanat-Mishra/IISER-Mohali`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 2, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1850 — `th86/gislkit`

Bounded repositories: `th86/gislkit`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 45, code 41, documentation 3, data 0, manifests 1.

Static security flags: `{"sql_string_construction": 2}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 7}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1852 — `drgmk/cb_2018`

Bounded repositories: `drgmk/cb_2018`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 7, code 5, documentation 2, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 4, "shell_or_process_execution": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 4, "unseeded_randomness": 1, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1856 — `shengyongniu/bulk_rna_seq_tophat`

Bounded repositories: `shengyongniu/bulk_rna_seq_tophat`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 17, code 16, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1857 — `shengyongniu/bulk_ATAC_seq`

Bounded repositories: `shengyongniu/bulk_ATAC_seq`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 14, code 13, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1859 — `andrewsu/Applied-Bioinformatics_Homeworks`

Bounded repositories: `andrewsu/Applied-Bioinformatics_Homeworks`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 4, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1860 — `SuLab/Applied-Bioinformatics`

Bounded repositories: `andrewsu/Applied-Bioinformatics`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 2, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1861 — `wenchichou/eQTL`

Bounded repositories: `shengyongniu/eQTL`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 0, documentation 1, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1862 — `shengyongniu/SeqTU`

Bounded repositories: `shengyongniu/SeqTU`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 4, documentation 1, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 4}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 5}`.

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
