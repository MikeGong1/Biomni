# External repository deep audit — Batch 011

Observed at: `2026-08-24T06:19:44Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **313–362**.
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
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 29 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 1 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 1 |

Static-review flags were present in 17 families for security-sensitive primitives, 13 for privacy/data-governance terms, and 11 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 313 | `Liripo/ai-skills` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/25/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 314 | `psknlr/TaoTCM-Hermes-SkillBank` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 315 | `Vik-u/Bayesian-Agent` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 316 | `marcosbolanos/ProSST` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 317 | `de-grave/claude-ai-mcp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 318 | `shantanusharma/helm`, `chaudhariatul/helm` | `DEEP_AUDIT_CANDIDATE` | 5 | 11/3/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 319 | `starboy-3/pyro` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 320 | `reacher-z/wlha` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 321 | `yarikoptic/datalad-fuse` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 322 | `Pidem/HCLSBenchmarks` | `EMPTY` | 0 | 0/0/0 | CLOSE_EMPTY_OR_UNAVAILABLE_ARTIFACT; no integration capability retained |
| 323 | `yarikoptic/brain_data_standards_ontologies` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 324 | `samarth-kadaba/A-Very-Questionable-Scheme-for-Gradient-Descent` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 325 | `inodb/cbioportal-core` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 326 | `de-grave/beacon-v2-nci` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 327 | `goodb/AWS_Claude_Skill` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 328 | `vlln/pdffigures2-zig` | `DEEP_AUDIT_CANDIDATE` | 0 | 18/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 329 | `kuanlinhuang/paperclip` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 330 | `samutiti/SubCellNuc` | `DEEP_AUDIT_CANDIDATE` | 32 | 31/3/10 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 331 | `yarikoptic/BIDS-Manager` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 332 | `yarikoptic/dandi-archive` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 333 | `yarikoptic/UnitRefine` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 334 | `yarikoptic/bids-validator-rs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 335 | `yarikoptic/bids-mosaic` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 336 | `yarikoptic/BCO_Documentation` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 337 | `Irishaze/agentic-rag` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/2/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 338 | `shengyongniu/mergedna` | `DEEP_AUDIT_CANDIDATE` | 0 | 14/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 339 | `yarikoptic/BIDS_minimize` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 340 | `inodb/cbioportal-docker-compose` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 341 | `yarikoptic/spikeinterface-gui` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 342 | `yarikoptic/datalad-catalog` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 343 | `yarikoptic/onvoc-widget` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 344 | `PayFv/coros-mcp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 345 | `vlln/AutoFigure` | `DEEP_AUDIT_CANDIDATE` | 1 | 4/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 346 | `SongyouZhong/Image2Smile` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/6/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 347 | `Vik-u/Primer_Design_and_Worklists` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 348 | `vlln/pdffigures-mcp-server` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 349 | `marcosbolanos/fitness-landscapes` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 350 | `yarikoptic/nep-review` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 351 | `HelloWorldLTY/UKBioLM` | `DEEP_AUDIT_CANDIDATE` | 0 | 63/9/11 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 352 | `HelloWorldLTY/spEMO` | `DEEP_AUDIT_CANDIDATE` | 0 | 42/3/14 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 353 | `Vik-u/MolViBench-open` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 354 | `jissen706/Electricity-Magnetism-Simulations` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/6/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 355 | `Vik-u/Matterix` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 356 | `yarikoptic/grobid` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 357 | `yarikoptic/BIDS-flux-docs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 358 | `Ayushmaniar/powerpoint-mcp` | `DEEP_AUDIT_CANDIDATE` | 0 | 15/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 359 | `goodb/saw-rnaseq-dogfood` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/3/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 360 | `Vincentcchu/cell_agents` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/11/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 361 | `Vincentcchu/CellTypeEval` | `DEEP_AUDIT_CANDIDATE` | 0 | 26/11/712 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 362 | `HelloWorldLTY/hygieia` | `DEEP_AUDIT_CANDIDATE` | 0 | 69/9/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 313 — `Liripo/ai-skills`

Bounded repositories: `Liripo/ai-skills`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 30, code 3, documentation 25, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 3, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"human_genomics": 14}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 318 — `stanford-crfm/helm`

Bounded repositories: `shantanusharma/helm`, `chaudhariatul/helm`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 17, code 11, documentation 3, data 3, manifests 0.

Static security flags: `{"mutable_remote_install": 2, "network_fetch": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 46, "upload_or_remote_transfer": 3, "human_genomics": 2}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 44}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 320 — `reacher-z/wlha`

Bounded repositories: `reacher-z/wlha`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 1, documentation 3, data 0, manifests 0.

Static security flags: `{"browser_html_injection": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 324 — `samarth-kadaba/A-Very-Questionable-Scheme-for-Gradient-Descent`

Bounded repositories: `samarth-kadaba/A-Very-Questionable-Scheme-for-Gradient-Descent`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 7, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 37}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 328 — `vlln/pdffigures2-zig`

Bounded repositories: `vlln/pdffigures2-zig`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 23, code 18, documentation 3, data 0, manifests 1.

Static security flags: `{"network_fetch": 5, "mutable_remote_install": 3, "filesystem_mutation": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 330 — `CellProfiling/SubCellPortable`

Bounded repositories: `samutiti/SubCellNuc`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 44, code 31, documentation 3, data 10, manifests 0.

Static security flags: `{"dynamic_code_execution": 29, "unsafe_deserialization": 14, "path_input": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 47, "unseeded_randomness": 15, "assertion_as_validation": 10, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 337 — `Irishaze/agentic-rag`

Bounded repositories: `Irishaze/agentic-rag`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 7, documentation 2, data 2, manifests 0.

Static security flags: `{"network_fetch": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 338 — `shengyongniu/mergedna`

Bounded repositories: `shengyongniu/mergedna`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 18, code 14, documentation 1, data 0, manifests 3.

Static security flags: `{"dynamic_code_execution": 6, "unsafe_deserialization": 4, "sql_string_construction": 2, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1485, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 38, "unseeded_randomness": 5}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 345 — `ResearAI/AutoFigure`

Bounded repositories: `vlln/AutoFigure`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 4, code 4, documentation 0, data 0, manifests 0.

Static security flags: `{"filesystem_mutation": 4, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 346 — `SongyouZhong/Image2Smile`

Bounded repositories: `SongyouZhong/Image2Smile`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 15, code 7, documentation 6, data 0, manifests 2.

Static security flags: `{"filesystem_mutation": 8, "server_exposure": 6, "network_fetch": 4}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 348 — `vlln/pdffigures-mcp-server`

Bounded repositories: `vlln/pdffigures-mcp-server`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 4, documentation 4, data 0, manifests 1.

Static security flags: `{"network_fetch": 8, "filesystem_mutation": 6, "shell_or_process_execution": 3, "server_exposure": 2}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 22, "clinical_or_patient_data": 3}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 349 — `marcosbolanos/fitness-landscapes`

Bounded repositories: `marcosbolanos/fitness-landscapes`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 3, documentation 0, data 0, manifests 2.

Static security flags: `{"path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 434}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 351 — `HelloWorldLTY/UKBioLM`

Bounded repositories: `HelloWorldLTY/UKBioLM`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 83, code 63, documentation 9, data 11, manifests 0.

Static security flags: `{"unsafe_deserialization": 25, "filesystem_mutation": 15, "mutable_remote_install": 13, "shell_or_process_execution": 4, "dynamic_code_execution": 3, "sql_string_construction": 3}`.

Privacy/data-governance flags: `{"human_genomics": 63, "named_biomedical_cohort": 14, "upload_or_remote_transfer": 7}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 49, "assertion_as_validation": 44, "unseeded_randomness": 16, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 352 — `HelloWorldLTY/spEMO`

Bounded repositories: `HelloWorldLTY/spEMO`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 60, code 42, documentation 3, data 14, manifests 1.

Static security flags: `{"mutable_remote_install": 20, "unsafe_deserialization": 16, "dynamic_code_execution": 6, "network_fetch": 1, "hardcoded_secret_shape": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 6}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 26, "hardcoded_absolute_path": 5, "unseeded_randomness": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 358 — `Ayushmaniar/powerpoint-mcp`

Bounded repositories: `Ayushmaniar/powerpoint-mcp`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 19, code 15, documentation 3, data 0, manifests 1.

Static security flags: `{"dynamic_code_execution": 2, "filesystem_mutation": 2, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 359 — `goodb/saw-rnaseq-dogfood`

Bounded repositories: `goodb/saw-rnaseq-dogfood`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 12, code 8, documentation 3, data 1, manifests 0.

Static security flags: `{"network_fetch": 2, "dynamic_code_execution": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 4, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 360 — `Vincentcchu/cell_agents`

Bounded repositories: `Vincentcchu/cell_agents`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 21, code 10, documentation 11, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 361 — `Vincentcchu/CellTypeEval`

Bounded repositories: `Vincentcchu/CellTypeEval`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 750, code 26, documentation 11, data 712, manifests 1.

Static security flags: `{"hardcoded_secret_shape": 11, "dynamic_code_execution": 3, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 362 — `HelloWorldLTY/hygieia`

Bounded repositories: `HelloWorldLTY/hygieia`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 84, code 69, documentation 9, data 5, manifests 1.

Static security flags: `{"shell_or_process_execution": 125, "network_fetch": 37, "unsafe_deserialization": 34, "dynamic_code_execution": 14, "sql_string_construction": 13, "filesystem_mutation": 10, "path_input": 7, "hardcoded_secret_shape": 6, "mutable_remote_install": 3}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 76, "human_genomics": 62, "named_biomedical_cohort": 28, "upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 30, "hardcoded_threshold": 16, "assertion_as_validation": 4, "hardcoded_absolute_path": 3, "network_model_code": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
