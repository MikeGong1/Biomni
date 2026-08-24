# External repository deep audit — Batch 038

Observed at: `2026-08-24T06:30:01Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1663–1712**.
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
| `DEEP_AUDIT_CANDIDATE` | 14 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 32 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 4 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 10 families for security-sensitive primitives, 8 for privacy/data-governance terms, and 8 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1663 | `NKalavros/arnie` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1664 | `tschaffter/portals` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1665 | `evolu8/EczemaNet` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1666 | `vladsavelyev/hmftools` | `DEEP_AUDIT_CANDIDATE` | 1 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1667 | `jucor/cBioPortalData`, `inodb/cBioPortalData` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1668 | `yarikoptic/nda-abcd-s3-downloader` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1669 | `yarikoptic/niicat` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1670 | `drgmk/ni` | `DEEP_AUDIT_CANDIDATE` | 0 | 11/7/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1671 | `yarikoptic/redirector` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1672 | `jaybee84/somatic-combiner` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1673 | `tschaffter/nlp-sandbox` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1674 | `yarikoptic/mriqc-sample1` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/2/6 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1675 | `lxasqjc/Foveation-for-Segmentation-of-Mega-pixel-Histology-Images` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1676 | `jaybee84/csbc-pson-dcc` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1677 | `tschaffter/i2b2_evaluation_scripts` | `DEEP_AUDIT_CANDIDATE` | 19 | 1/2/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1678 | `tschaffter/rocker-versioned` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1679 | `yarikoptic/ohbm2020-posters` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1680 | `jaybee84/SynapseShinyApp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1681 | `leezx/WGS_Pipeline_BestPractice` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1682 | `mickaelleclercq/TDM` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1683 | `jaybee84/synapseforms` | `DEEP_AUDIT_CANDIDATE` | 1 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1684 | `inodb/hotspots` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1685 | `changwn/WEVar` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1686 | `Sanat-Mishra/Multisample-VCF---PEDIA` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1687 | `amehrjou/lifelines` | `DEEP_AUDIT_CANDIDATE` | 1 | 4/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1688 | `andrewsu/biomedical-graph-visualizer` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1689 | `NKalavros/harmony` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1690 | `yarikoptic/bids-app-dummy` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/2/3 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1691 | `changwn/E-MTAB-6141` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1692 | `vladsavelyev/pyensembl` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1693 | `changwn/scATACseq-analysis-notes` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1694 | `tschaffter/COVID_diagnosis_baseline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1695 | `tschaffter/awesome-coronavirus` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1696 | `kexinhuang12345/SkipGNN` | `DEEP_AUDIT_CANDIDATE` | 0 | 10/2/16 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1697 | `NKalavros/scrinvex` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1698 | `yarikoptic/heudiconv-testdata` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 1699 | `vladsavelyev/gridss-purple-linx` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1700 | `vladsavelyev/MultiQC_bcbio` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1701 | `vladsavelyev/bcbio-nextgen` | `DEEP_AUDIT_CANDIDATE` | 4 | 2/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1702 | `changwn/RNA-seq-pipeline` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1703 | `KSUN63/DeepDTA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1704 | `yarikoptic/bisweb` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1705 | `andrewsu/Relay` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1706 | `Sanat-Mishra/PEDIA-workflow` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1707 | `inodb/cellBrowser` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1708 | `yarikoptic/tridesclous` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1709 | `vladsavelyev/ViFi` | `DEEP_AUDIT_CANDIDATE` | 1 | 7/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1710 | `vladsavelyev/polyidus` | `DEEP_AUDIT_CANDIDATE` | 2 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1711 | `changwn/tRFTarget` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1712 | `changwn/ICPS` | `DEEP_AUDIT_CANDIDATE` | 0 | 0/1/1 | REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead |

## Candidate and blocker details

### Order 1666 — `hartwigmedical/hmftools`

Bounded repositories: `vladsavelyev/hmftools`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 2, code 2, documentation 0, data 0, manifests 0.

Static security flags: `{"sql_string_construction": 1}`.

Privacy/data-governance flags: `{"human_genomics": 24}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1670 — `drgmk/ni`

Bounded repositories: `drgmk/ni`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 20, code 11, documentation 7, data 0, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 42}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 6}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1677 — `kotfic/i2b2_evaluation_scripts`

Bounded repositories: `tschaffter/i2b2_evaluation_scripts`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 8, code 1, documentation 2, data 2, manifests 3.

Static security flags: `{"dynamic_code_execution": 40, "mutable_remote_install": 2}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 46}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1681 — `leezx/WGS_Pipeline_BestPractice`

Bounded repositories: `leezx/WGS_Pipeline_BestPractice`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 9, code 7, documentation 2, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 125}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1683 — `Sage-Bionetworks/synapseforms`

Bounded repositories: `jaybee84/synapseforms`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 0, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1687 — `CamDavidsonPilon/lifelines`

Bounded repositories: `amehrjou/lifelines`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 4, code 4, documentation 0, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 6, "hardcoded_threshold": 3, "unseeded_randomness": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1690 — `yarikoptic/bids-app-dummy`

Bounded repositories: `yarikoptic/bids-app-dummy`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 8, code 1, documentation 2, data 3, manifests 1.

Static security flags: `{"shell_or_process_execution": 4, "filesystem_mutation": 1, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1692 — `openvax/pyensembl`

Bounded repositories: `vladsavelyev/pyensembl`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1696 — `kexinhuang12345/SkipGNN`

Bounded repositories: `kexinhuang12345/SkipGNN`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 30, code 10, documentation 2, data 16, manifests 1.

Static security flags: `{"dynamic_code_execution": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 6}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1699 — `vladsavelyev/gridss-purple-linx`

Bounded repositories: `vladsavelyev/gridss-purple-linx`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 10, code 7, documentation 1, data 0, manifests 1.

Static security flags: `{"mutable_remote_install": 4, "filesystem_mutation": 2, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"human_genomics": 42}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1701 — `bcbio/bcbio-nextgen`

Bounded repositories: `vladsavelyev/bcbio-nextgen`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 2, documentation 0, data 0, manifests 1.

Static security flags: `{"shell_or_process_execution": 5, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 21, "human_genomics": 9}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1709 — `namphuon/ViFi`

Bounded repositories: `vladsavelyev/ViFi`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 7, code 7, documentation 0, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 7, "network_fetch": 7, "dynamic_code_execution": 3, "path_input": 3, "filesystem_mutation": 1}`.

Privacy/data-governance flags: `{"human_genomics": 2}`.

Scientific/reproducibility flags: `{"hardcoded_absolute_path": 4}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1710 — `hoffmangroup/polyidus`

Bounded repositories: `vladsavelyev/polyidus`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{"shell_or_process_execution": 29, "network_fetch": 7}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1712 — `changwn/ICPS`

Bounded repositories: `changwn/ICPS`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 0, documentation 1, data 1, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
