# External repository deep audit — Batch 013

Observed at: `2026-08-24T06:20:57Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **413–462**.
- Canonical families: **50**.
- Canonical repository records: **60**.
- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.
- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.

## Static acquisition and review method

Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.

Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.

## Result summary

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 13 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 33 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 4 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 14 families for security-sensitive primitives, 12 for privacy/data-governance terms, and 9 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 413 | `yarikoptic/undata` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 414 | `Nigmat-future/pretext-med` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 415 | `Nigmat-future/thrombin-comparison` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/4/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 416 | `tangxuan82/TwinWeaver` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 417 | `kuanlinhuang/boltz`, `sbonner0/boltz`, `shantanusharma/boltz`, `dabulseco/boltz` | `DEEP_AUDIT_CANDIDATE` | 13 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 418 | `inodb/vibe-vep` | `DEEP_AUDIT_CANDIDATE` | 0 | 148/52/19 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 419 | `inodb/genome-nexus-frontend` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 420 | `yarikoptic/dFC` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 421 | `yarikoptic/PiEEG-server` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 422 | `Javkhaa/everything-claude-code` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 423 | `yarikoptic/sciagent` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 424 | `yarikoptic/bids-rs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 425 | `de-grave/BioReason` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 426 | `alexs42/PaperBanana`, `Vik-u/PaperBanana` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 427 | `alexs42/k-dense-byok` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 428 | `alexs42/LabClaw` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 429 | `lulaiao/ChemClaw` | `DEEP_AUDIT_CANDIDATE` | 10 | 25/8/10 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 430 | `marcosbolanos/autorigami-` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 431 | `HelloWorldLTY/autoresearch`, `yarikoptic/autoresearch`, `leizhou69/K_autoresearch`, `jaybee84/autoresearch`, `leezx/autoresearch` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 432 | `alexs42/colloquium` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 433 | `Vincentcchu/mLLMCellType` | `DEEP_AUDIT_CANDIDATE` | 0 | 33/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 434 | `Vincentcchu/CellTypeAgent` | `DEEP_AUDIT_CANDIDATE` | 0 | 23/154/155 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 435 | `yarikoptic/datalad-extension-template` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 436 | `shantanusharma/excalidraw-mcp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 437 | `tschaffter/sage-monorepo` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 438 | `yarikoptic/nwb2bids` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 439 | `yarikoptic/highdicom` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 440 | `explorerwjy/skills` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/13/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 441 | `SongyouZhong/molstar` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 442 | `zhanxw/ScopeViewer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 443 | `kwskws1998/Biomni-Obs` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/2/7 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 444 | `yarikoptic/DUO` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 445 | `andrewsu/scripps-garibaldi-hpc-skill` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 446 | `yarikoptic/james_library` | `DEEP_AUDIT_CANDIDATE` | 0 | 399/60/24 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 447 | `explorerwjy/Mouse-Geneformer` | `DEEP_AUDIT_CANDIDATE` | 26 | 42/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 448 | `yarikoptic/GabrielKP-enc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 449 | `andrewsu/mcp-proto-okn`, `goodb/mcp-proto-okn` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 450 | `yarikoptic/open-brain-consent` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 451 | `explorerwjy/Geneformer` | `DEEP_AUDIT_CANDIDATE` | 0 | 68/19/13 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 452 | `alexs42/Paper2Agent`, `lishengting/Paper2Agent` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 453 | `yarikoptic/datalad-concepts` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 454 | `kwskws1998/biomlbench` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 455 | `marcosbolanos/3dna` | `DEEP_AUDIT_CANDIDATE` | 0 | 22/3/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 456 | `yarikoptic/datalad-deprecated` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 457 | `gutendzx/sleepyland` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 458 | `yarikoptic/datalad-container` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 459 | `yarikoptic/datalad-neuroimaging` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 460 | `yaswanth169/AICO` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 461 | `Edison-A-N/cursor-controller-skill` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/4/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 462 | `yarikoptic/aind-ephys-pipeline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 414 — `Nigmat-future/pretext-med`

Bounded repositories: `Nigmat-future/pretext-med`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 1, documentation 3, data 0, manifests 2.

Static security flags: `{"browser_html_injection": 6, "network_fetch": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 13}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 417 — `jwohlwend/boltz`

Bounded repositories: `kuanlinhuang/boltz`, `sbonner0/boltz`, `shantanusharma/boltz`, `dabulseco/boltz`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 8, code 7, documentation 1, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 13, "network_fetch": 6, "unsafe_deserialization": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 26, "assertion_as_validation": 7}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 418 — `inodb/vibe-vep`

Bounded repositories: `inodb/vibe-vep`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 228, code 148, documentation 52, data 19, manifests 9.

Static security flags: `{"dynamic_code_execution": 46, "sql_string_construction": 27, "filesystem_mutation": 15, "mutable_remote_install": 4, "network_fetch": 3, "browser_html_injection": 3, "server_exposure": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"human_genomics": 1604, "named_biomedical_cohort": 41, "clinical_or_patient_data": 15, "upload_or_remote_transfer": 5}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 429 — `InternScience/ChemClaw`

Bounded repositories: `lulaiao/ChemClaw`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 44, code 25, documentation 8, data 10, manifests 0.

Static security flags: `{"mutable_remote_install": 10, "unsafe_deserialization": 8, "shell_or_process_execution": 6, "filesystem_mutation": 1, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 80, "unseeded_randomness": 16}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 430 — `marcosbolanos/autorigami-`

Bounded repositories: `marcosbolanos/autorigami-`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 12, code 7, documentation 2, data 1, manifests 2.

Static security flags: `{"sql_string_construction": 3, "shell_or_process_execution": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 110}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 433 — `Vincentcchu/mLLMCellType`

Bounded repositories: `Vincentcchu/mLLMCellType`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 45, code 33, documentation 4, data 0, manifests 5.

Static security flags: `{"hardcoded_secret_shape": 20, "mutable_remote_install": 6, "sql_string_construction": 2, "network_fetch": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 8, "upload_or_remote_transfer": 3, "human_genomics": 2}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 53}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 434 — `Vincentcchu/CellTypeAgent`

Bounded repositories: `Vincentcchu/CellTypeAgent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 332, code 23, documentation 154, data 155, manifests 0.

Static security flags: `{"dynamic_code_execution": 8, "mutable_remote_install": 4, "network_fetch": 3, "sql_string_construction": 3}`.

Privacy/data-governance flags: `{"human_genomics": 38, "clinical_or_patient_data": 8, "named_biomedical_cohort": 4}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 440 — `explorerwjy/skills`

Bounded repositories: `explorerwjy/skills`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 18, code 4, documentation 13, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 11}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 443 — `kwskws1998/Biomni-Obs`

Bounded repositories: `kwskws1998/Biomni-Obs`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 16, code 4, documentation 2, data 7, manifests 3.

Static security flags: `{"server_exposure": 6, "network_fetch": 2, "container_privilege": 2, "path_input": 1, "hardcoded_secret_shape": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 446 — `topherchris420/james_library`

Bounded repositories: `yarikoptic/james_library`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 530, code 399, documentation 60, data 24, manifests 45.

Static security flags: `{"hardcoded_secret_shape": 68, "shell_or_process_execution": 67, "network_fetch": 62, "dynamic_code_execution": 53, "filesystem_mutation": 49, "sql_string_construction": 31, "server_exposure": 22, "mutable_remote_install": 6, "container_privilege": 2, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 89, "human_genomics": 34, "clinical_or_patient_data": 11, "named_biomedical_cohort": 6}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 434, "hardcoded_absolute_path": 114, "unseeded_randomness": 25, "hardcoded_threshold": 7, "network_model_code": 2}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 447 — `machine-perception-robotics-group/Mouse-Geneformer`

Bounded repositories: `explorerwjy/Mouse-Geneformer`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 42, code 42, documentation 0, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 24, "dynamic_code_execution": 14, "filesystem_mutation": 10, "shell_or_process_execution": 6, "sql_string_construction": 2, "network_fetch": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 2, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 22, "unseeded_randomness": 8}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 451 — `explorerwjy/Geneformer`

Bounded repositories: `explorerwjy/Geneformer`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 101, code 68, documentation 19, data 13, manifests 1.

Static security flags: `{"unsafe_deserialization": 79, "shell_or_process_execution": 12, "sql_string_construction": 11, "dynamic_code_execution": 7, "path_input": 6, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 21, "upload_or_remote_transfer": 4, "human_genomics": 2, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 142, "assertion_as_validation": 34, "unseeded_randomness": 10, "hardcoded_threshold": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 455 — `marcosbolanos/3dna`

Bounded repositories: `marcosbolanos/3dna`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 30, code 22, documentation 3, data 1, manifests 3.

Static security flags: `{}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 309}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 61, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
