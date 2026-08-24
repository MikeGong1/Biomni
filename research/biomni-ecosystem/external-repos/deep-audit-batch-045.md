# External repository deep audit — Batch 045

Observed at: `2026-08-24T06:32:58Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **2013–2062**.
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
| `DEEP_AUDIT_CANDIDATE` | 35 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 10 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 2 |
| `EMPTY` | 0 |

Static-review flags were present in 24 families for security-sensitive primitives, 21 for privacy/data-governance terms, and 21 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 2013 | `inodb/2014-05-mdopson-viral` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/3 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 2014 | `inodb/CONCOCT` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 2015 | `inodb/2014-09-haspeborg-moose-project` | `DEEP_AUDIT_CANDIDATE` | 0 | 0/5/3 | REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead |
| 2016 | `inodb/2014-11-masmvali-presentation` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/45/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2017 | `yarikoptic/utopia-documents-neuroplugins` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2018 | `inodb/masmvaliweb` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2019 | `inodb/metassemble` | `DEEP_AUDIT_CANDIDATE` | 0 | 20/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2020 | `inodb/slurm` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2021 | `inodb/CONCOCT-test-data` | `DEEP_AUDIT_CANDIDATE` | 3 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2022 | `inodb/masmvali-publication` | `DEEP_AUDIT_CANDIDATE` | 0 | 6/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2023 | `inodb/ETTLIMS` | `DEEP_AUDIT_CANDIDATE` | 21 | 4/7/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2024 | `inodb/envgen.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2025 | `yarikoptic/matplotlib` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 2026 | `yarikoptic/Neurosynth` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2027 | `inodb/masmvali` | `DEEP_AUDIT_CANDIDATE` | 0 | 16/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2028 | `yarikoptic/nitest-balls1` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/8/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2029 | `inodb/2014-06-favorite-microbe` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/44/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2030 | `tschaffter/jmod` | `DEEP_AUDIT_CANDIDATE` | 0 | 56/20/44 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2031 | `yarikoptic/protege` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2032 | `inodb/2014-06-lims-developers-workshop` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/44/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2033 | `inodb/2014-5-metagenomics-workshop` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/32/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2034 | `yarikoptic/pystatsmodels` | `DEEP_AUDIT_CANDIDATE` | 0 | 657/79/6 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2035 | `inodb/bioinfo-outreach` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/46/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2036 | `andrewsu/nobProject` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2037 | `th86/TCGAfastlane` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2038 | `inodb/2014-3-lims-presentation` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/44/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2039 | `zhanxw/SPD` | `DEEP_AUDIT_CANDIDATE` | 0 | 38/4/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2040 | `inodb/facs` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2041 | `tschaffter/libsde` | `DEEP_AUDIT_CANDIDATE` | 0 | 13/5/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2042 | `yarikoptic/biostar-central` | `DEEP_AUDIT_CANDIDATE` | 2 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2043 | `zhanxw/SeqMinerCmd` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2044 | `zhanxw/vcf2geno` | `DEEP_AUDIT_CANDIDATE` | 0 | 78/2/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2045 | `th86/ezMA` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2046 | `inodb/snakemake-parallel-bwa` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2047 | `inodb/gefes` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/1/6 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2048 | `inodb/2013-metagenomics-workshop-gbg` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/23/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2049 | `yarikoptic/hrf_estimation` | `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 | 4/1/0 | CLOSE_METADATA_FALSE_POSITIVE; no bounded biomedical or scientific-agent capability verified |
| 2050 | `yarikoptic/pybetaseries` | `DEEP_AUDIT_CANDIDATE` | 8 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2051 | `jucor/ggmcmc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2052 | `zhanxw/libStatGen` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2053 | `th86/SurvivalCluster` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2054 | `th86/progEval` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2055 | `inodb/ProBin` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2056 | `yarikoptic/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2057 | `inodb/assembly-workshop` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/24/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2058 | `yarikoptic/psychopy_ext` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 2059 | `zhanxw/laser` | `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 | 10/0/0 | CLOSE_METADATA_FALSE_POSITIVE; no bounded biomedical or scientific-agent capability verified |
| 2060 | `inodb/khmer` | `DEEP_AUDIT_CANDIDATE` | 835 | 31/14/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2061 | `jucor/torch-gsl` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 2062 | `yarikoptic/regressioncv` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 2015 — `inodb/2014-09-haspeborg-moose-project`

Bounded repositories: `inodb/2014-09-haspeborg-moose-project`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 0, documentation 5, data 3, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead**.

### Order 2016 — `inodb/2014-11-masmvali-presentation`

Bounded repositories: `inodb/2014-11-masmvali-presentation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 74, code 27, documentation 45, data 0, manifests 1.

Static security flags: `{"browser_html_injection": 50, "dynamic_code_execution": 37, "sql_string_construction": 19, "mutable_remote_install": 8, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 5, "clinical_or_patient_data": 4, "human_genomics": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 11}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2017 — `yarikoptic/utopia-documents-neuroplugins`

Bounded repositories: `yarikoptic/utopia-documents-neuroplugins`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 3, documentation 1, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 2, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4, "human_genomics": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2018 — `inodb/masmvaliweb`

Bounded repositories: `inodb/masmvaliweb`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 4, documentation 4, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 4, "server_exposure": 2, "filesystem_mutation": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 16}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2019 — `inodb/metassemble`

Bounded repositories: `inodb/metassemble`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 22, code 20, documentation 2, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 2, "filesystem_mutation": 2, "path_input": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2021 — `BinPro/CONCOCT-test-data`

Bounded repositories: `inodb/CONCOCT-test-data`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- one or more immutable acquisition surfaces were unavailable or incomplete.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2022 — `inodb/masmvali-publication`

Bounded repositories: `inodb/masmvali-publication`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 6, documentation 5, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 4, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2023 — `miccheck12/SCGLIMS`

Bounded repositories: `inodb/ETTLIMS`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 12, code 4, documentation 7, data 1, manifests 0.

Static security flags: `{"mutable_remote_install": 8}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2027 — `inodb/masmvali`

Bounded repositories: `inodb/masmvali`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 20, code 16, documentation 3, data 0, manifests 1.

Static security flags: `{"path_input": 4, "shell_or_process_execution": 1, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 4}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2028 — `yarikoptic/nitest-balls1`

Bounded repositories: `yarikoptic/nitest-balls1`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 9, code 1, documentation 8, data 0, manifests 0.

Static security flags: `{"filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 7}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2029 — `inodb/2014-06-favorite-microbe`

Bounded repositories: `inodb/2014-06-favorite-microbe`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 73, code 27, documentation 44, data 0, manifests 1.

Static security flags: `{"browser_html_injection": 50, "dynamic_code_execution": 37, "sql_string_construction": 19, "mutable_remote_install": 8, "path_input": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4, "human_genomics": 4, "upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 11}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2030 — `tschaffter/jmod`

Bounded repositories: `tschaffter/jmod`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 120, code 56, documentation 20, data 44, manifests 0.

Static security flags: `{"sql_string_construction": 5, "dynamic_code_execution": 4, "shell_or_process_execution": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 21}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 17, "unseeded_randomness": 3, "hardcoded_threshold": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2032 — `inodb/2014-06-lims-developers-workshop`

Bounded repositories: `inodb/2014-06-lims-developers-workshop`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 73, code 27, documentation 44, data 0, manifests 1.

Static security flags: `{"browser_html_injection": 50, "dynamic_code_execution": 37, "sql_string_construction": 19, "mutable_remote_install": 8, "path_input": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4, "human_genomics": 4, "upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 11}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2033 — `inodb/2014-5-metagenomics-workshop`

Bounded repositories: `inodb/2014-5-metagenomics-workshop`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 35, code 2, documentation 32, data 1, manifests 0.

Static security flags: `{"path_input": 2, "mutable_remote_install": 2, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2034 — `yarikoptic/pystatsmodels`

Bounded repositories: `yarikoptic/pystatsmodels`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 750, code 657, documentation 79, data 6, manifests 3.

Static security flags: `{"dynamic_code_execution": 28, "shell_or_process_execution": 26, "sql_string_construction": 23, "unsafe_deserialization": 13, "filesystem_mutation": 11, "network_fetch": 7, "mutable_remote_install": 7, "hardcoded_secret_shape": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 82, "upload_or_remote_transfer": 18, "human_genomics": 3, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 672, "assertion_as_validation": 92, "hardcoded_threshold": 54, "hardcoded_absolute_path": 13}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2035 — `inodb/bioinfo-outreach`

Bounded repositories: `inodb/bioinfo-outreach`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 75, code 27, documentation 46, data 0, manifests 1.

Static security flags: `{"browser_html_injection": 50, "dynamic_code_execution": 37, "sql_string_construction": 19, "mutable_remote_install": 10, "hardcoded_secret_shape": 2, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 5, "clinical_or_patient_data": 4, "human_genomics": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 11}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2037 — `th86/TCGAfastlane`

Bounded repositories: `th86/TCGAfastlane`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 7, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 17}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2038 — `inodb/2014-3-lims-presentation`

Bounded repositories: `inodb/2014-3-lims-presentation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 73, code 27, documentation 44, data 0, manifests 1.

Static security flags: `{"browser_html_injection": 50, "dynamic_code_execution": 37, "sql_string_construction": 19, "mutable_remote_install": 8, "path_input": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 4, "human_genomics": 4, "upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 11}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2039 — `zhanxw/SPD`

Bounded repositories: `zhanxw/SPD`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 44, code 38, documentation 4, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 5, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 5}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2040 — `SciLifeLab/facs`

Bounded repositories: `inodb/facs`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2041 — `tschaffter/libsde`

Bounded repositories: `tschaffter/libsde`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 19, code 13, documentation 5, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 3, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2042 — `ialbert/biostar-central`

Bounded repositories: `yarikoptic/biostar-central`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 15, "server_exposure": 1, "hardcoded_secret_shape": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2043 — `zhanxw/SeqMinerCmd`

Bounded repositories: `zhanxw/SeqMinerCmd`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 19}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2044 — `zhanxw/vcf2geno`

Bounded repositories: `zhanxw/vcf2geno`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 83, code 78, documentation 2, data 3, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 93, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 22}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2045 — `th86/ezMA`

Bounded repositories: `th86/ezMA`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 7, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 7}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2046 — `inodb/snakemake-parallel-bwa`

Bounded repositories: `inodb/snakemake-parallel-bwa`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 2, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 4}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2047 — `inodb/gefes`

Bounded repositories: `inodb/gefes`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 36, code 27, documentation 1, data 6, manifests 1.

Static security flags: `{"filesystem_mutation": 8, "shell_or_process_execution": 4, "dynamic_code_execution": 1, "unsafe_deserialization": 1, "path_input": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 2, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2048 — `inodb/2013-metagenomics-workshop-gbg`

Bounded repositories: `inodb/2013-metagenomics-workshop-gbg`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 31, code 8, documentation 23, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 34, "browser_html_injection": 14, "sql_string_construction": 10}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2050 — `poldrack/pybetaseries`

Bounded repositories: `yarikoptic/pybetaseries`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 2, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2053 — `th86/SurvivalCluster`

Bounded repositories: `th86/SurvivalCluster`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 3, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2054 — `th86/progEval`

Bounded repositories: `th86/progEval`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 7, documentation 0, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 10, "named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2055 — `BinPro/ProBin`

Bounded repositories: `inodb/ProBin`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 2, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2057 — `inodb/assembly-workshop`

Bounded repositories: `inodb/assembly-workshop`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 32, code 8, documentation 24, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 34, "browser_html_injection": 13, "sql_string_construction": 3, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2060 — `dib-lab/khmer`

Bounded repositories: `inodb/khmer`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 45, code 31, documentation 14, data 0, manifests 0.

Static security flags: `{"filesystem_mutation": 5, "mutable_remote_install": 5, "unsafe_deserialization": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 6, "assertion_as_validation": 3, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 2061 — `jucor/torch-gsl`

Bounded repositories: `jucor/torch-gsl`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 3, documentation 2, data 0, manifests 0.

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
