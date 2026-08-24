# External repository deep audit — Batch 042

Observed at: `2026-08-24T06:31:30Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1863–1912**.
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
| `DEEP_AUDIT_CANDIDATE` | 19 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 28 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 11 families for security-sensitive primitives, 12 for privacy/data-governance terms, and 10 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1863 | `changwn/rankTest` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1864 | `jaybee84/pyNBS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1865 | `zhanxw/BayesSLAM` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1866 | `vladsavelyev/Venn` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/3/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1867 | `vladsavelyev/umccrise` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1868 | `NKalavros/cBioportal-Queries` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1869 | `drgmk/wtf` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1870 | `vladsavelyev/VarDict` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1871 | `vladsavelyev/NGS_Reporting_TestData` | `DEEP_AUDIT_CANDIDATE` | 0 | 45/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1872 | `Mr-Milk/SYSU-Software-2017` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1873 | `leezx/MBSIT` | `DEEP_AUDIT_CANDIDATE` | 0 | 14/7/7 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1874 | `yarikoptic/reproducible-imaging` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1875 | `yarikoptic/scikit-image` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1876 | `vladsavelyev/pcgr_predispose` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1877 | `zhanxw/cromwellDashboard` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1878 | `zhanxw/cromwell` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1879 | `yarikoptic/stimfit` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1880 | `yarikoptic/pymvpa2-feedstock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1881 | `explorerwjy/CUMC` | `DEEP_AUDIT_CANDIDATE` | 0 | 167/10/9 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1882 | `kuanlinhuang/AD_SPI1_project` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1883 | `ahueb/Access-Checker` | `DEEP_AUDIT_CANDIDATE` | 4 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1884 | `jaybee84/cNF_brousseau_hippo` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1885 | `jaybee84/rnaseq_tutorial` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1886 | `inodb/pathway-mapper` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1887 | `vladsavelyev/MultiQC_az` | `DEEP_AUDIT_CANDIDATE` | 0 | 13/9/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1888 | `jaybee84/scRNA.seq.course` | `DEEP_AUDIT_CANDIDATE` | 942 | 5/7/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1889 | `yarikoptic/dcm_qa` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1890 | `yarikoptic/shablona` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1891 | `yarikoptic/CARMIN-API` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1892 | `kuanlinhuang/PopularGenes` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1893 | `yarikoptic/dcm2niix` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1894 | `vladsavelyev/bxtools` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1895 | `vladsavelyev/HapCUT2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1896 | `changwn/dockstore_tool_arriba` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1897 | `yarikoptic/freesurfer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1898 | `th86/transmeddatasets` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1899 | `yarikoptic/cbbs-imaging-docs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1900 | `PMK89/IpySci` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1901 | `jaybee84/GoodDoc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1902 | `yarikoptic/hcp2bids` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1903 | `vladsavelyev/cloudbiolinux` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1904 | `kuanlinhuang/PDXNatComm2017` | `DEEP_AUDIT_CANDIDATE` | 0 | 32/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1905 | `explorerwjy/CohortPCA` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1906 | `explorerwjy/GenoTying_with_Dnn` | `DEEP_AUDIT_CANDIDATE` | 0 | 40/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1907 | `andrewsu/go-site`, `goodb/go-site` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1908 | `th86/monocle-release` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1909 | `zhanxw/mctoolsr` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1910 | `MinxZ/Invasive-Species-Monitoring` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1911 | `lxasqjc/OpenPNM` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1912 | `kexinhuang12345/logd74` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 1863 — `changwn/rankTest`

Bounded repositories: `changwn/rankTest`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1866 — `vladsavelyev/Venn`

Bounded repositories: `vladsavelyev/Venn`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 7, code 1, documentation 3, data 2, manifests 1.

Static security flags: `{"shell_or_process_execution": 2}`.

Privacy/data-governance flags: `{"human_genomics": 9}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1868 — `NKalavros/cBioportal-Queries`

Bounded repositories: `NKalavros/cBioportal-Queries`.

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

### Order 1871 — `vladsavelyev/NGS_Reporting_TestData`

Bounded repositories: `vladsavelyev/NGS_Reporting_TestData`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 45, code 45, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 224, "sql_string_construction": 119, "browser_html_injection": 72, "path_input": 8}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 8, "human_genomics": 5}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1873 — `leezx/MBSIT`

Bounded repositories: `leezx/MBSIT`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 28, code 14, documentation 7, data 7, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 18, "hardcoded_threshold": 8}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1876 — `vladsavelyev/pcgr_predispose`

Bounded repositories: `vladsavelyev/pcgr_predispose`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 1, data 1, manifests 0.

Static security flags: `{"shell_or_process_execution": 7, "path_input": 6}`.

Privacy/data-governance flags: `{"human_genomics": 62, "clinical_or_patient_data": 2, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1877 — `zhanxw/cromwellDashboard`

Bounded repositories: `zhanxw/cromwellDashboard`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 1, documentation 1, data 1, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1881 — `explorerwjy/CUMC`

Bounded repositories: `explorerwjy/CUMC`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 186, code 167, documentation 10, data 9, manifests 0.

Static security flags: `{"dynamic_code_execution": 37, "filesystem_mutation": 20, "path_input": 12, "unsafe_deserialization": 6, "shell_or_process_execution": 5}`.

Privacy/data-governance flags: `{"human_genomics": 1423, "named_biomedical_cohort": 8, "clinical_or_patient_data": 3}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 110, "unseeded_randomness": 1, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1882 — `kuanlinhuang/AD_SPI1_project`

Bounded repositories: `kuanlinhuang/AD_SPI1_project`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 9, documentation 1, data 0, manifests 0.

Static security flags: `{"path_input": 3}`.

Privacy/data-governance flags: `{"human_genomics": 9, "named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 10}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1883 — `UNC-Libraries/Access-Checker`

Bounded repositories: `ahueb/Access-Checker`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1887 — `vladsavelyev/MultiQC_az`

Bounded repositories: `vladsavelyev/MultiQC_az`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 24, code 13, documentation 9, data 1, manifests 1.

Static security flags: `{"sql_string_construction": 4, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1888 — `hemberg-lab/scRNA.seq.course`

Bounded repositories: `jaybee84/scRNA.seq.course`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 16, code 5, documentation 7, data 2, manifests 1.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1889 — `neurolabusc/dcm_qa`

Bounded repositories: `yarikoptic/dcm_qa`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1892 — `kuanlinhuang/PopularGenes`

Bounded repositories: `kuanlinhuang/PopularGenes`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 5, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1900 — `PMK89/IpySci`

Bounded repositories: `PMK89/IpySci`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1904 — `kuanlinhuang/PDXNatComm2017`

Bounded repositories: `kuanlinhuang/PDXNatComm2017`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 33, code 32, documentation 1, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 80, "named_biomedical_cohort": 11}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 258}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1905 — `explorerwjy/CohortPCA`

Bounded repositories: `explorerwjy/CohortPCA`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 7, code 5, documentation 2, data 0, manifests 0.

Static security flags: `{"filesystem_mutation": 3}`.

Privacy/data-governance flags: `{"human_genomics": 31}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 3, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1906 — `explorerwjy/GenoTying_with_Dnn`

Bounded repositories: `explorerwjy/GenoTying_with_Dnn`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 44, code 40, documentation 2, data 0, manifests 2.

Static security flags: `{"shell_or_process_execution": 36, "network_fetch": 18, "server_exposure": 8, "filesystem_mutation": 4}`.

Privacy/data-governance flags: `{"human_genomics": 206}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 16, "hardcoded_absolute_path": 8, "unseeded_randomness": 3, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1910 — `MinxZ/Invasive-Species-Monitoring`

Bounded repositories: `MinxZ/Invasive-Species-Monitoring`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 4, documentation 1, data 1, manifests 0.

Static security flags: `{"dynamic_code_execution": 4, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
