# External repository deep audit — Batch 009

Observed at: `2026-08-24T06:18:57Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **213–262**.
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
| `DEEP_AUDIT_CANDIDATE` | 13 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 35 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 2 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 13 families for security-sensitive primitives, 10 for privacy/data-governance terms, and 9 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 213 | `KalinNonchev/scRNA-seq_notes` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 214 | `KalinNonchev/lazyslide-models` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 215 | `KalinNonchev/Awesome-Virtual-Cell` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 216 | `KalinNonchev/Awesome-Spatial-Transcriptomics-Pathology-Large-Models` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 217 | `KalinNonchev/Awesome-SpatialOmics-AI` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 218 | `KalinNonchev/awesome-spatial-omics` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 219 | `KalinNonchev/Awesome-Pathology-VLMs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 220 | `KalinNonchev/awesome-pathology-spatial-omics` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 221 | `KalinNonchev/Awesome-His-to-Spatial-Transcriptomics-Translation` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 222 | `KalinNonchev/Awesome-Generative-Models-in-Pathology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 223 | `KalinNonchev/awesome-foundation-model-single-cell-papers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 224 | `HelloWorldLTY/awesome-deep-learning-single-cell-papers`, `KalinNonchev/awesome-deep-learning-single-cell-papers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 225 | `KalinNonchev/awesome-computational-biology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 226 | `KalinNonchev/Awesome-AI-Pathology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 227 | `KalinNonchev/Awesome-AI4DigitalPathology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 228 | `KyleNeverGivesUp/llm-bio-automl` | `DEEP_AUDIT_CANDIDATE` | 0 | 98/49/30 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 229 | `shantanusharma/generative-protein-binder-design` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 230 | `yaswanth169/Cryosparc_mcp_Server` | `DEEP_AUDIT_CANDIDATE` | 0 | 22/2/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 231 | `yaswanth169/CryoEMAgent` | `DEEP_AUDIT_CANDIDATE` | 0 | 31/3/6 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 232 | `Mr-Milk/data-analysis-template` | `DEEP_AUDIT_CANDIDATE` | 0 | 12/5/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 233 | `andrewsu/glygen-mcp-test-2` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/2/13 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 234 | `andrewsu/glyco-variant-annotation` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/3/20 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 235 | `MikeGong1/mmQTL-pipeline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 236 | `reacher-z/vidground` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 237 | `psknlr/Tao-TCM-KG` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 238 | `vlln/mip` | `DEEP_AUDIT_CANDIDATE` | 0 | 34/14/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 239 | `tuln128/SGPO` | `DEEP_AUDIT_CANDIDATE` | 5 | 4/0/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 240 | `drgmk/scrna` | `DEEP_AUDIT_CANDIDATE` | 0 | 12/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 241 | `KalinNonchev/Awesome-Single-cell-Spatial-Transcriptomics-Imputation` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 242 | `KalinNonchev/awesome-multimodal-in-medical-imaging` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 243 | `KalinNonchev/Awesome-Healthcare-Foundation-Models` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 244 | `KalinNonchev/Awesome-Medical-VLMs-and-Datasets` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 245 | `KalinNonchev/Awesome-Medical-Multimodal-Models-and-Datasets` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 246 | `KalinNonchev/Awesome-Medical-Dataset` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 247 | `KalinNonchev/Awesome-AI4Med` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 248 | `KalinNonchev/awesome-pathology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 249 | `KalinNonchev/Awesome-Foundation-Models-for-Advancing-Healthcare` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 250 | `andrewsu/glygen-mcp-server` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 251 | `psknlr/TCM-Harness` | `DEEP_AUDIT_CANDIDATE` | 0 | 241/231/277 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 252 | `yarikoptic/BORIS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 253 | `XxxKrabs/clinical-asr-robustness` | `DEEP_AUDIT_CANDIDATE` | 0 | 491/23/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 254 | `KalinNonchev/awesome-deepbio` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 255 | `KalinNonchev/Awesome-Multi-Modal-Foundation-Models-for-Computational-Pathology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 256 | `KalinNonchev/ML-SRT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 257 | `KalinNonchev/Awesome-Foundation-Models-in-Medical-Imaging` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 258 | `jaechang-hits/Awesome-Bioinformatics`, `KalinNonchev/Awesome-Bioinformatics` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 259 | `KalinNonchev/Awesome-Bio-Foundation-Models` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 260 | `kwskws1998/aiffel` | `DEEP_AUDIT_CANDIDATE` | 39 | 35/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 261 | `KalinNonchev/Awesome-Single-Cell-Clustering` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 262 | `KalinNonchev/awesome-multimodal-multiomic-multiscale-papers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 228 — `KyleNeverGivesUp/llm-bio-automl`

Bounded repositories: `KyleNeverGivesUp/llm-bio-automl`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 179, code 98, documentation 49, data 30, manifests 2.

Static security flags: `{"shell_or_process_execution": 25, "sql_string_construction": 18, "network_fetch": 12, "dynamic_code_execution": 4, "path_input": 3, "mutable_remote_install": 3, "unsafe_deserialization": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1790, "clinical_or_patient_data": 8, "human_genomics": 8}`.

Scientific/reproducibility flags: `{"network_model_code": 11, "assertion_as_validation": 11, "unseeded_randomness": 1, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 230 — `yaswanth169/Cryosparc_mcp_Server`

Bounded repositories: `yaswanth169/Cryosparc_mcp_Server`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 26, code 22, documentation 2, data 2, manifests 0.

Static security flags: `{"sql_string_construction": 8, "network_fetch": 6, "server_exposure": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 23, "hardcoded_threshold": 11}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 231 — `yaswanth169/CryoEMAgent`

Bounded repositories: `yaswanth169/CryoEMAgent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 42, code 31, documentation 3, data 6, manifests 1.

Static security flags: `{"hardcoded_secret_shape": 10, "shell_or_process_execution": 6, "network_fetch": 3, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 131, "hardcoded_threshold": 13, "hardcoded_absolute_path": 6}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 232 — `Mr-Milk/data-analysis-template`

Bounded repositories: `Mr-Milk/data-analysis-template`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 24, code 12, documentation 5, data 5, manifests 2.

Static security flags: `{"unsafe_deserialization": 1, "server_exposure": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1448}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 19, "unseeded_randomness": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 233 — `andrewsu/glygen-mcp-test-2`

Bounded repositories: `andrewsu/glygen-mcp-test-2`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 16, code 1, documentation 2, data 13, manifests 0.

Static security flags: `{"network_fetch": 3, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 25, "named_biomedical_cohort": 19, "clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 234 — `andrewsu/glyco-variant-annotation`

Bounded repositories: `andrewsu/glyco-variant-annotation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 25, code 2, documentation 3, data 20, manifests 0.

Static security flags: `{"server_exposure": 7, "network_fetch": 3, "shell_or_process_execution": 2}`.

Privacy/data-governance flags: `{"human_genomics": 161, "clinical_or_patient_data": 43}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 236 — `reacher-z/vidground`

Bounded repositories: `reacher-z/vidground`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 5, documentation 4, data 0, manifests 1.

Static security flags: `{"path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 238 — `vlln/mip`

Bounded repositories: `vlln/mip`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 54, code 34, documentation 14, data 2, manifests 3.

Static security flags: `{"mutable_remote_install": 8, "sql_string_construction": 8, "filesystem_mutation": 5, "network_fetch": 2}`.

Privacy/data-governance flags: `{"human_genomics": 10, "upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 239 — `jsunn-y/SGPO`

Bounded repositories: `tuln128/SGPO`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 7, code 4, documentation 0, data 1, manifests 2.

Static security flags: `{"mutable_remote_install": 6}`.

Privacy/data-governance flags: `{"human_genomics": 2}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 10, "assertion_as_validation": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 240 — `drgmk/scrna`

Bounded repositories: `drgmk/scrna`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 17, code 12, documentation 2, data 1, manifests 1.

Static security flags: `{"mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 51, "unseeded_randomness": 10, "hardcoded_threshold": 5}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 251 — `psknlr/TCM-Harness`

Bounded repositories: `psknlr/TCM-Harness`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 750, code 241, documentation 231, data 277, manifests 1.

Static security flags: `{"dynamic_code_execution": 106, "browser_html_injection": 101, "network_fetch": 66, "shell_or_process_execution": 16, "filesystem_mutation": 14, "hardcoded_secret_shape": 5, "sql_string_construction": 3, "server_exposure": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 149, "human_genomics": 21, "upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 253 — `XxxKrabs/clinical-asr-robustness`

Bounded repositories: `XxxKrabs/clinical-asr-robustness`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 518, code 491, documentation 23, data 0, manifests 3.

Static security flags: `{"dynamic_code_execution": 156, "sql_string_construction": 53, "path_input": 38, "mutable_remote_install": 23, "shell_or_process_execution": 14, "network_fetch": 14, "unsafe_deserialization": 10, "filesystem_mutation": 5, "browser_html_injection": 5, "hardcoded_secret_shape": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 292, "human_genomics": 59, "upload_or_remote_transfer": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 866, "unseeded_randomness": 202, "hardcoded_threshold": 13, "hardcoded_absolute_path": 9, "network_model_code": 6}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 260 — `gmendes9/multilingual_va_prediction`

Bounded repositories: `kwskws1998/aiffel`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 39, code 35, documentation 4, data 0, manifests 0.

Static security flags: `{"path_input": 9, "dynamic_code_execution": 7, "filesystem_mutation": 6, "mutable_remote_install": 5, "unsafe_deserialization": 3, "shell_or_process_execution": 2, "network_fetch": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 13, "human_genomics": 7}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 3, "hardcoded_absolute_path": 1, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
