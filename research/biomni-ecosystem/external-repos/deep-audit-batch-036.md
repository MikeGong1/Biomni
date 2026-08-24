# External repository deep audit — Batch 036

Observed at: `2026-08-24T06:29:21Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1563–1612**.
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
| `DEEP_AUDIT_CANDIDATE` | 17 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 30 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 13 families for security-sensitive primitives, 10 for privacy/data-governance terms, and 6 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1563 | `kexinhuang12345/ml-genomics-resources` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1564 | `aevo98765/in-silico-proteome` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/0/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1565 | `Ali-Maq/shiny-server` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1566 | `zhanxw/MicrobiomeProfiler` | `DEEP_AUDIT_CANDIDATE` | 1 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1567 | `PabloCabaleiro/ProjectEyeliner` | `DEEP_AUDIT_CANDIDATE` | 0 | 20/3/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1568 | `gutendzx/dreem-learning-evaluation` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1569 | `DevinDeSilva/Pneaumonia_prediction_using_chest_xrays` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/6 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1570 | `vladsavelyev/gatk-sv` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1571 | `HelloWorldLTY/scib` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1572 | `amehrjou/wot` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1573 | `Sanat-Mishra/eclipdemux` | `DEEP_AUDIT_CANDIDATE` | 2 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1574 | `Vik-u/Enzyme-Promiscuity-Prediction` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1575 | `Mr-Milk/neighborhood_analysis` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1576 | `changwn/Kassandra` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1577 | `yarikoptic/HBN_BIDS` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1578 | `Vik-u/bio_embeddings` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1579 | `yarikoptic/niiview` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1580 | `jaybee84/NF-COVID-response` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1581 | `tschaffter/neuro-ner-phi-annotator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1582 | `Mr-Milk/configs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1583 | `HelloWorldLTY/scJoint` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1584 | `KalinNonchev/kipoiseq` | `DEEP_AUDIT_CANDIDATE` | 3 | 0/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1585 | `kexinhuang12345/chemprop` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1586 | `inodb/schematic` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1587 | `andrewsu/chp_metadata` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1588 | `andrewsu/minihackathons` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1589 | `jaybee84/synapse_analytical_utils` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1590 | `jaybee84/OpenPBTA-analysis` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1591 | `jaybee84/catalog` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1592 | `yarikoptic/dandiarchive` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1593 | `tschaffter/CovidCertificate-Documents` | `DEEP_AUDIT_CANDIDATE` | 12 | 0/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1594 | `zhuyitan/Enhanced_COXEN` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1595 | `Sanat-Mishra/Transcistor-2.0` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1596 | `jaybee84/challenge-analysis`, `tschaffter/challenge-analysis` | `DEEP_AUDIT_CANDIDATE` | 32 | 0/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1597 | `yarikoptic/bids-statsmodels-design-synthesizer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1598 | `yarikoptic/ds003647` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1599 | `Mr-Milk/circDraw` | `DEEP_AUDIT_CANDIDATE` | 0 | 23/8/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1600 | `jucor/ehr-predictions` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1601 | `changwn/pathview` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1602 | `Mr-Milk/circDraw-py` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/6/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1603 | `explorerwjy/ML_genomics` | `DEEP_AUDIT_CANDIDATE` | 0 | 14/2/8 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1604 | `yarikoptic/spikeextractors` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1605 | `vladsavelyev/hail` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1606 | `Mr-Milk/SpatialTis-Tutorial` | `DEEP_AUDIT_CANDIDATE` | 0 | 4/14/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1607 | `changwn/scGNN` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1608 | `Mr-Milk/KMexpress` | `DEEP_AUDIT_CANDIDATE` | 0 | 105/190/67 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1609 | `jaybee84/synExtra` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1610 | `inodb/annotation-tools` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1611 | `jaybee84/SomaticCombiner_docker` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1612 | `changwn/ICTD` | `DEEP_AUDIT_CANDIDATE` | 54 | 4/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 1564 — `aevo98765/in-silico-proteome`

Bounded repositories: `aevo98765/in-silico-proteome`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 6, code 2, documentation 0, data 4, manifests 0.

Static security flags: `{"network_fetch": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1566 — `YuLab-SMU/MicrobiomeProfiler`

Bounded repositories: `zhanxw/MicrobiomeProfiler`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 2, documentation 0, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1567 — `PabloCabaleiro/ProjectEyeliner`

Bounded repositories: `PabloCabaleiro/ProjectEyeliner`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 24, code 20, documentation 3, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1573 — `YeoLab/eclipdemux`

Bounded repositories: `Sanat-Mishra/eclipdemux`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1575 — `Mr-Milk/neighborhood_analysis`

Bounded repositories: `Mr-Milk/neighborhood_analysis`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 4, documentation 1, data 1, manifests 3.

Static security flags: `{"mutable_remote_install": 4}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 8}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 9}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1584 — `kipoi/kipoiseq`

Bounded repositories: `KalinNonchev/kipoiseq`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 0, documentation 1, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1589 — `jaybee84/synapse_analytical_utils`

Bounded repositories: `jaybee84/synapse_analytical_utils`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1593 — `admin-ch/CovidCertificate-Documents`

Bounded repositories: `tschaffter/CovidCertificate-Documents`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 0, documentation 1, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1594 — `zhuyitan/Enhanced_COXEN`

Bounded repositories: `zhuyitan/Enhanced_COXEN`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 2, documentation 4, data 0, manifests 1.

Static security flags: `{"mutable_remote_install": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"hardcoded_threshold": 4, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1595 — `Sanat-Mishra/Transcistor-2.0`

Bounded repositories: `Sanat-Mishra/Transcistor-2.0`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 2, data 0, manifests 0.

Static security flags: `{"path_input": 5}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1596 — `Sage-Bionetworks-Challenges/challenge-analysis-old`

Bounded repositories: `jaybee84/challenge-analysis`, `tschaffter/challenge-analysis`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 8, code 0, documentation 2, data 1, manifests 5.

Static security flags: `{"mutable_remote_install": 3}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1599 — `Mr-Milk/circDraw`

Bounded repositories: `Mr-Milk/circDraw`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 39, code 23, documentation 8, data 0, manifests 7.

Static security flags: `{"filesystem_mutation": 5}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 13, "human_genomics": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1602 — `Mr-Milk/circDraw-py`

Bounded repositories: `Mr-Milk/circDraw-py`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 19, code 8, documentation 6, data 3, manifests 1.

Static security flags: `{"mutable_remote_install": 4, "network_fetch": 3, "dynamic_code_execution": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 97, "human_genomics": 4}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 11}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1603 — `explorerwjy/ML_genomics`

Bounded repositories: `explorerwjy/ML_genomics`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 24, code 14, documentation 2, data 8, manifests 0.

Static security flags: `{"dynamic_code_execution": 10, "unsafe_deserialization": 6, "sql_string_construction": 4}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 2, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1606 — `Mr-Milk/SpatialTis-Tutorial`

Bounded repositories: `Mr-Milk/SpatialTis-Tutorial`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 18, code 4, documentation 14, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 17, "clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1608 — `Mr-Milk/KMexpress`

Bounded repositories: `Mr-Milk/KMexpress`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 366, code 105, documentation 190, data 67, manifests 0.

Static security flags: `{"dynamic_code_execution": 22, "mutable_remote_install": 15, "filesystem_mutation": 9, "sql_string_construction": 8, "hardcoded_secret_shape": 7, "path_input": 2, "browser_html_injection": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 422, "upload_or_remote_transfer": 197, "clinical_or_patient_data": 98, "human_genomics": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 3, "assertion_as_validation": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1612 — `zy26/ICTD`

Bounded repositories: `changwn/ICTD`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 9, code 4, documentation 2, data 1, manifests 1.

Static security flags: `{"mutable_remote_install": 10, "sql_string_construction": 4}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 2, "upload_or_remote_transfer": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
