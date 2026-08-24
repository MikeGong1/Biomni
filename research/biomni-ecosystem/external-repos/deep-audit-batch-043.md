# External repository deep audit — Batch 043

Observed at: `2026-08-24T06:31:54Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1913–1962**.
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
| `DEEP_AUDIT_CANDIDATE` | 17 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 28 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 4 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 1 |

Static-review flags were present in 12 families for security-sensitive primitives, 11 for privacy/data-governance terms, and 10 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1913 | `evolu8/SweepNet` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1914 | `shengyongniu/bulk_RNA_seq_count_base` | `DEEP_AUDIT_CANDIDATE` | 0 | 6/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1915 | `yarikoptic/module-FAIR-data` | `DOC_METADATA_MAINTENANCE_ONLY` | 5 | 0/4/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1916 | `drgmk/ALMA-RADMC-visibility-modelling` | `DEEP_AUDIT_CANDIDATE` | 0 | 9/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1917 | `jaybee84/RNAseq_cluster` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1918 | `jaybee84/agedbrain` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1919 | `vladsavelyev/concordance` | `DEEP_AUDIT_CANDIDATE` | 3 | 0/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1920 | `yarikoptic/lesson-template` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1921 | `yarikoptic/module-dataprocessing` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1922 | `yarikoptic/module-stats` | `DOC_METADATA_MAINTENANCE_ONLY` | 1 | 0/1/0 | CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated |
| 1923 | `kuanlinhuang/medtallk` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1924 | `yarikoptic/gears` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1925 | `andrewsu/Membrane-Protein-Mining` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1926 | `yarikoptic/papers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1927 | `kuanlinhuang/BioMine` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1928 | `vladsavelyev/goleft` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1929 | `yarikoptic/ds000114--demo-bet` | `EMPTY` | 0 | 0/0/0 | CLOSE_EMPTY_OR_UNAVAILABLE_ARTIFACT; no integration capability retained |
| 1930 | `yarikoptic/module-reproducible-basics` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1931 | `andrewsu/OBOFoundry.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1932 | `vladsavelyev/ipython-cluster-helper` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1933 | `yarikoptic/DartmouthMIND_tutorial` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1934 | `drgmk/classifier` | `DEEP_AUDIT_CANDIDATE` | 0 | 6/541/8 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1935 | `yarikoptic/nimh_repro_wrkshpAug2017` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1936 | `drgmk/imorbel` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1937 | `yarikoptic/dmptool` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1938 | `jaybee84/skimage-tutorials` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1939 | `drgmk/hd116434_51eri_excess` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/171/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1940 | `lxasqjc/OpenPNM-Examples` | `DEEP_AUDIT_CANDIDATE` | 86 | 0/18/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1941 | `yarikoptic/ndmg` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1942 | `vladsavelyev/exac_browser` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1943 | `vladsavelyev/genologics` | `DEEP_AUDIT_CANDIDATE` | 3 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1944 | `goodb/beacons` | `DEEP_AUDIT_CANDIDATE` | 0 | 69/31/18 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1945 | `zhanxw/FMAP` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1946 | `shengyongniu/igv` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1947 | `yarikoptic/BIDSonsetsWhichFear` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1948 | `kuanlinhuang/hotspot3d` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1949 | `NKalavros/sickle` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1950 | `PMK89/instrumentino` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1951 | `drgmk/ads_bibdesk` | `DEEP_AUDIT_CANDIDATE` | 3 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1952 | `andrewsu/PathogenTransmissionOntology` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1953 | `th86/ArduinoGoogleSheetAirQualityMonitor` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1954 | `zhanxw/ancestry` | `DEEP_AUDIT_CANDIDATE` | 0 | 80/2/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1955 | `yarikoptic/ds000114` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1956 | `drgmk/rzpsc` | `DEEP_AUDIT_CANDIDATE` | 0 | 5/27/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1957 | `inodb/biorhino-tools` | `DEEP_AUDIT_CANDIDATE` | 0 | 27/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1958 | `shengyongniu/ARGMap` | `DEEP_AUDIT_CANDIDATE` | 0 | 2/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1959 | `tschaffter/dm-docker` | `DEEP_AUDIT_CANDIDATE` | 0 | 16/13/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1960 | `yarikoptic/global2017` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1961 | `inodb/react-tooltip-test` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1962 | `yarikoptic/glumpy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 1914 — `shengyongniu/bulk_RNA_seq_count_base`

Bounded repositories: `shengyongniu/bulk_RNA_seq_count_base`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 7, code 6, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1916 — `drgmk/ALMA-RADMC-visibility-modelling`

Bounded repositories: `drgmk/ALMA-RADMC-visibility-modelling`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 11, code 9, documentation 1, data 0, manifests 1.

Static security flags: `{"shell_or_process_execution": 33, "path_input": 2, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 5}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 14, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1919 — `hammerlab/concordance`

Bounded repositories: `vladsavelyev/concordance`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 0, documentation 2, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 14}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1934 — `drgmk/classifier`

Bounded repositories: `drgmk/classifier`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 557, code 6, documentation 541, data 8, manifests 1.

Static security flags: `{"unsafe_deserialization": 2, "network_fetch": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 8, "hardcoded_absolute_path": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1936 — `drgmk/imorbel`

Bounded repositories: `drgmk/imorbel`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 3, documentation 1, data 0, manifests 0.

Static security flags: `{"path_input": 3, "sql_string_construction": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 61}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 19}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1939 — `drgmk/hd116434_51eri_excess`

Bounded repositories: `drgmk/hd116434_51eri_excess`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 172, code 1, documentation 171, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 85}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 1, "named_biomedical_cohort": 1, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1940 — `mrokhfrooz/OpenPNM-Examples`

Bounded repositories: `lxasqjc/OpenPNM-Examples`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 19, code 0, documentation 18, data 1, manifests 0.

Static security flags: `{"unsafe_deserialization": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1943 — `SciLifeLab/genologics`

Bounded repositories: `vladsavelyev/genologics`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1944 — `goodb/beacons`

Bounded repositories: `goodb/beacons`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 134, code 69, documentation 31, data 18, manifests 0.

Static security flags: `{"mutable_remote_install": 34, "dynamic_code_execution": 3}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 10, "human_genomics": 9}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 32}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1948 — `ding-lab/hotspot3d`

Bounded repositories: `kuanlinhuang/hotspot3d`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1951 — `jonathansick/ads_bibdesk`

Bounded repositories: `drgmk/ads_bibdesk`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 8, "dynamic_code_execution": 3, "filesystem_mutation": 3, "sql_string_construction": 3}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 7}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1954 — `zhanxw/ancestry`

Bounded repositories: `zhanxw/ancestry`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 85, code 80, documentation 2, data 3, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 68, "named_biomedical_cohort": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 22}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1956 — `drgmk/rzpsc`

Bounded repositories: `drgmk/rzpsc`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 37, code 5, documentation 27, data 5, manifests 0.

Static security flags: `{"shell_or_process_execution": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 10, "hardcoded_absolute_path": 7, "hardcoded_threshold": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1957 — `inodb/biorhino-tools`

Bounded repositories: `inodb/biorhino-tools`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 28, code 27, documentation 1, data 0, manifests 0.

Static security flags: `{"path_input": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 2}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1958 — `shengyongniu/ARGMap`

Bounded repositories: `shengyongniu/ARGMap`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 2, documentation 1, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1959 — `tschaffter/dm-docker`

Bounded repositories: `tschaffter/dm-docker`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 39, code 16, documentation 13, data 0, manifests 10.

Static security flags: `{"mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"named_biomedical_cohort": 32, "clinical_or_patient_data": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 8}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1961 — `inodb/react-tooltip-test`

Bounded repositories: `inodb/react-tooltip-test`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 3, documentation 4, data 0, manifests 1.

Static security flags: `{"mutable_remote_install": 6, "network_fetch": 3}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
