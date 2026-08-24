# External repository deep audit — Batch 034

Observed at: `2026-08-24T06:28:29Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1463–1512**.
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
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 25 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 12 families for security-sensitive primitives, 11 for privacy/data-governance terms, and 10 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1463 | `drgmk/pacs-model` | `DEEP_AUDIT_CANDIDATE` | 36 | 5/0/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1464 | `yarikoptic/wdl` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1465 | `kuanlinhuang/vcf2tsv` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1466 | `inodb/htan-artist` | `DEEP_AUDIT_CANDIDATE` | 6 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1467 | `changwn/PCASA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1468 | `vladsavelyev/wdl-workflows` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/10 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1469 | `vladsavelyev/warp` | `DEEP_AUDIT_CANDIDATE` | 30 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1470 | `tangxuan82/berteome` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1471 | `alexj-lee/minimal-esm-training-loop` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1472 | `HelloWorldLTY/CVQVAE` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1473 | `th86/CAR_T_TargetIdentification` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1474 | `Charvijain16/PPML-for-Aneurysm-Rupture-` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/0/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1475 | `tschaffter/schematic` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1476 | `changwn/car_t_stimulation` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1477 | `HelloWorldLTY/MAJAR` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1478 | `yarikoptic/citeproc-py-feedstock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1479 | `mkoretsky1/NSQIP_Reintubation` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1480 | `yarikoptic/DeepMReye` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1481 | `Rasic2/periodic-NBO` | `DEEP_AUDIT_CANDIDATE` | 13 | 6/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1482 | `HelloWorldLTY/Open-problems-for-single-cell-2022-Silver-medal-solution` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1483 | `HasanAldhahi/design_clarus` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1484 | `yarikoptic/nobrainer-zoo` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1485 | `shaunporwal/geneplotlab` | `DEEP_AUDIT_CANDIDATE` | 0 | 11/4/8 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1486 | `andrewsu/recount3` | `DEEP_AUDIT_CANDIDATE` | 1 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1487 | `JinL0/MRI-education-resources` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1488 | `Chahat08/Brain-Tumor-Classification` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1489 | `little2b/A-deep-learning-based-model-for-predicting-abnormal-liver-function-in-workers-in-the-automotive-manu` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1490 | `kexinhuang12345/clinicalBERT` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1491 | `Sanat-Mishra/K562-cell-line-epigenetic-analysis` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/0/30 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1492 | `leezx/CRACI` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1493 | `gutendzx/SleepXAI-An-Explainable-Deep-Learning-approach-for-Multi-class-Sleep-Stage-Identification` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1494 | `leezx/PROTAC-RL` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1495 | `yarikoptic/PyMVPA-bids-app` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1496 | `shaunporwal/gtsummary` | `DEEP_AUDIT_CANDIDATE` | 3 | 43/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1497 | `yarikoptic/pliers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1498 | `tangxuan82/Human_DT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1499 | `yarikoptic/qc-book` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1500 | `drgmk/dd` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/4/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1501 | `yarikoptic/niQC` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1502 | `vladsavelyev/gnomad_methods` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1503 | `jaybee84/miRNA_analysis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1504 | `yarikoptic/oreoni` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1505 | `jaybee84/microrna_variants` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/2/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1506 | `changwn/scTenifoldKnk` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1507 | `yarikoptic/HBN_BIDS-fmriprep_try` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/33/41 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1508 | `vladsavelyev/gnomad_qc` | `DEEP_AUDIT_CANDIDATE` | 2 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1509 | `kexinhuang12345/MolTrans` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/4/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1510 | `Vik-u/localcolabfold` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1511 | `KSUN63/e3_diffusion_for_molecules` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1512 | `Sanat-Mishra/Imig-Lab` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 1463 — `bmy21/pacs-model`

Bounded repositories: `drgmk/pacs-model`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 7, code 5, documentation 0, data 2, manifests 0.

Static security flags: `{"unsafe_deserialization": 3, "path_input": 2, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 3}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 3, "hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1465 — `kuanlinhuang/vcf2tsv`

Bounded repositories: `kuanlinhuang/vcf2tsv`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{"path_input": 2, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"human_genomics": 18}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1466 — `adamjtaylor/htan-artist`

Bounded repositories: `inodb/htan-artist`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1469 — `broadinstitute/warp`

Bounded repositories: `vladsavelyev/warp`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1471 — `alexj-lee/minimal-esm-training-loop`

Bounded repositories: `alexj-lee/minimal-esm-training-loop`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 2, code 2, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 4}`.

Privacy/data-governance flags: `{"human_genomics": 4}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 6, "assertion_as_validation": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1472 — `HelloWorldLTY/CVQVAE`

Bounded repositories: `HelloWorldLTY/CVQVAE`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 3, documentation 1, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1474 — `Charvijain16/PPML-for-Aneurysm-Rupture-`

Bounded repositories: `Charvijain16/PPML-for-Aneurysm-Rupture-`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 8, documentation 0, data 2, manifests 0.

Static security flags: `{"unsafe_deserialization": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 2, "hardcoded_absolute_path": 2, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1479 — `mkoretsky1/NSQIP_Reintubation`

Bounded repositories: `mkoretsky1/NSQIP_Reintubation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 9, code 8, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1481 — `jrschmidt2/periodic-NBO`

Bounded repositories: `Rasic2/periodic-NBO`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 6, code 6, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1482 — `HelloWorldLTY/Open-problems-for-single-cell-2022-Silver-medal-solution`

Bounded repositories: `HelloWorldLTY/Open-problems-for-single-cell-2022-Silver-medal-solution`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 9, documentation 1, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 31, "path_input": 30, "dynamic_code_execution": 13}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 10, "hardcoded_threshold": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1485 — `shaunporwal/geneplotlab`

Bounded repositories: `shaunporwal/geneplotlab`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 23, code 11, documentation 4, data 8, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1486 — `LieberInstitute/recount3`

Bounded repositories: `andrewsu/recount3`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1488 — `Chahat08/Brain-Tumor-Classification`

Bounded repositories: `Chahat08/Brain-Tumor-Classification`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1489 — `little2b/A-deep-learning-based-model-for-predicting-abnormal-liver-function-in-workers-in-the-automotive-manu`

Bounded repositories: `little2b/A-deep-learning-based-model-for-predicting-abnormal-liver-function-in-workers-in-the-automotive-manu`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 4, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1490 — `kexinhuang12345/clinicalBERT`

Bounded repositories: `kexinhuang12345/clinicalBERT`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 7, documentation 1, data 0, manifests 0.

Static security flags: `{"unsafe_deserialization": 2, "dynamic_code_execution": 1, "network_fetch": 1, "filesystem_mutation": 1, "path_input": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 18, "named_biomedical_cohort": 6}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 3, "assertion_as_validation": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1491 — `Sanat-Mishra/K562-cell-line-epigenetic-analysis`

Bounded repositories: `Sanat-Mishra/K562-cell-line-epigenetic-analysis`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 31, code 1, documentation 0, data 30, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1496 — `ddsjoberg/gtsummary`

Bounded repositories: `shaunporwal/gtsummary`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 43, code 43, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 20, "sql_string_construction": 5}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 3}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1500 — `drgmk/dd`

Bounded repositories: `drgmk/dd`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 17, code 10, documentation 4, data 1, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 6}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1505 — `jaybee84/microrna_variants`

Bounded repositories: `jaybee84/microrna_variants`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 14, code 3, documentation 2, data 2, manifests 6.

Static security flags: `{"mutable_remote_install": 5, "server_exposure": 1, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 9, "clinical_or_patient_data": 4, "upload_or_remote_transfer": 3}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 4}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1508 — `broadinstitute/gnomad_qc`

Bounded repositories: `vladsavelyev/gnomad_qc`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 2, documentation 0, data 0, manifests 1.

Static security flags: `{"sql_string_construction": 4}`.

Privacy/data-governance flags: `{"human_genomics": 14, "named_biomedical_cohort": 3}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1509 — `kexinhuang12345/MolTrans`

Bounded repositories: `kexinhuang12345/MolTrans`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 13, code 5, documentation 4, data 2, manifests 1.

Static security flags: `{"dynamic_code_execution": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1512 — `Sanat-Mishra/Imig-Lab`

Bounded repositories: `Sanat-Mishra/Imig-Lab`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 5, code 1, documentation 2, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
