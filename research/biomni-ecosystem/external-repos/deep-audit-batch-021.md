# External repository deep audit — Batch 021

Observed at: `2026-08-24T06:24:32Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **813–862**.
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
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 35 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 1 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 0 |

Static-review flags were present in 11 families for security-sensitive primitives, 8 for privacy/data-governance terms, and 7 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 813 | `dabulseco/ChemTSv2` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 814 | `psknlr/deepmind-research` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 815 | `yarikoptic/airoh-template` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 816 | `chaudhariatul/PA-LLaVA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 817 | `Rasic2/rdf_analysis` | `DEEP_AUDIT_CANDIDATE` | 3 | 0/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 818 | `Nigmat-future/diabeta-ai-insight` | `DEEP_AUDIT_CANDIDATE` | 0 | 68/5/4 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 819 | `Rakshitha-Ireddi/LeanAgent`, `yaswanth169/LeanAgent` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 820 | `yarikoptic/ohbm2025-reproducible-research` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 821 | `yarikoptic/Australian-Imaging-Service.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 822 | `Vik-u/ai-validation-feedback-loops` | `DOC_METADATA_MAINTENANCE_ONLY` | 0 | 0/1/0 | CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external |
| 823 | `Rasic2/AI4S-agent-tools` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 824 | `yarikoptic/MATLAB-support-for-Zarr-files` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 825 | `yarikoptic/PsyR` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 826 | `yarikoptic/Bidsificator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 827 | `yarikoptic/bids2openminds` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 828 | `yarikoptic/outreach` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 829 | `Ayushmaniar/Big-Data-Science-Drug-Protein-Interactions` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/0/10 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 830 | `yarikoptic/dandihub` | `DEEP_AUDIT_CANDIDATE` | 0 | 0/1/1 | REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead |
| 831 | `KalinNonchev/biomed_nccl_benchmark` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 832 | `Vik-u/mdapy` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 833 | `yarikoptic/mcp-use` | `DEEP_AUDIT_CANDIDATE` | 0 | 59/17/5 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 834 | `HelloWorldLTY/gene-embedding-benchmarks` | `DEEP_AUDIT_CANDIDATE` | 1 | 1/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 835 | `KSUN63/protein-vibe-coding` | `DEEP_AUDIT_CANDIDATE` | 0 | 1/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 836 | `yarikoptic/BrainEffeX` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 837 | `yarikoptic/physionet-build` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 838 | `yarikoptic/physionet` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 839 | `Ali-Maq/civic_extractor` | `DEEP_AUDIT_CANDIDATE` | 0 | 12/5/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 840 | `NKalavros/sequoia-pub` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 841 | `gutendzx/sleepfm-clinical` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 842 | `Ali-Maq/DeepTCR` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 843 | `Ali-Maq/Playbook-Workflow-Builder` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 844 | `yarikoptic/movement` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 845 | `yarikoptic/ndx-pose` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 846 | `yarikoptic/niimath` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 847 | `jaybee84/data-analysis-crow` | `DEEP_AUDIT_CANDIDATE` | 32 | 18/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 848 | `dabulseco/full_spectrum_bioinformatics` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 849 | `yarikoptic/containers` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 850 | `Vik-u/MetalDock` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 851 | `tangxuan82/Digital-Twin-based-system-for-pregnancy-risk-prevention-and-perinatal-care` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 852 | `samarth-kadaba/SMDPO` | `DEEP_AUDIT_CANDIDATE` | 0 | 26/2/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 853 | `anngvu/biocblog` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 854 | `Ali-Maq/IntegrAO` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 855 | `yarikoptic/SumarizeFmriprep` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 856 | `yarikoptic/modelcontextprotocol` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 857 | `anngvu/bioc-curation` | `DEEP_AUDIT_CANDIDATE` | 0 | 3/1/9 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 858 | `yarikoptic/napari` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 859 | `andrewsu/kgx` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 860 | `jaybee84/Health-Privacy-Challenge` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 861 | `kuanlinhuang/AI-Scientist-v2` | `DEEP_AUDIT_CANDIDATE` | 4 | 7/2/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 862 | `andrewsu/kg-registry` | `DEEP_AUDIT_CANDIDATE` | 0 | 28/695/13 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |

## Candidate and blocker details

### Order 817 — `yhpu/rdf_analysis`

Bounded repositories: `Rasic2/rdf_analysis`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 3, code 0, documentation 1, data 0, manifests 2.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 818 — `Nigmat-future/diabeta-ai-insight`

Bounded repositories: `Nigmat-future/diabeta-ai-insight`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 79, code 68, documentation 5, data 4, manifests 2.

Static security flags: `{"network_fetch": 4, "sql_string_construction": 1, "browser_html_injection": 1}`.

Privacy/data-governance flags: `{"human_genomics": 64, "clinical_or_patient_data": 2}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 829 — `Ayushmaniar/Big-Data-Science-Drug-Protein-Interactions`

Bounded repositories: `Ayushmaniar/Big-Data-Science-Drug-Protein-Interactions`.

Immutable acquisition: IMMUTABLE_GIT_TREE_SELECTED_BLOBS; files read 11, code 1, documentation 0, data 10, manifests 0.

Static security flags: `{"sql_string_construction": 2}`.

Privacy/data-governance flags: `{"human_genomics": 32}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 3}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 830 — `dandi/dandi-hub`

Bounded repositories: `yarikoptic/dandihub`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 0, documentation 1, data 1, manifests 1.

Static security flags: `{"filesystem_mutation": 3, "hardcoded_secret_shape": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead**.

### Order 831 — `KalinNonchev/biomed_nccl_benchmark`

Bounded repositories: `KalinNonchev/biomed_nccl_benchmark`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 3, code 1, documentation 1, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 1}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 833 — `mcp-use/mcp-use`

Bounded repositories: `yarikoptic/mcp-use`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 88, code 59, documentation 17, data 5, manifests 5.

Static security flags: `{"hardcoded_secret_shape": 11, "shell_or_process_execution": 8, "mutable_remote_install": 7, "filesystem_mutation": 4, "network_fetch": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 166, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 834 — `ylaboratory/gene-embedding-benchmarks`

Bounded repositories: `HelloWorldLTY/gene-embedding-benchmarks`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 1, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 835 — `KSUN63/protein-vibe-coding`

Bounded repositories: `KSUN63/protein-vibe-coding`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 4, code 1, documentation 1, data 0, manifests 1.

Static security flags: `{"network_fetch": 1, "path_input": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 839 — `Ali-Maq/civic_extractor`

Bounded repositories: `Ali-Maq/civic_extractor`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 19, code 12, documentation 5, data 2, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{"human_genomics": 29, "clinical_or_patient_data": 14, "upload_or_remote_transfer": 1}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 847 — `Future-House/finch`

Bounded repositories: `jaybee84/data-analysis-crow`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 23, code 18, documentation 2, data 1, manifests 2.

Static security flags: `{"filesystem_mutation": 6, "mutable_remote_install": 3, "unsafe_deserialization": 2, "hardcoded_secret_shape": 2, "dynamic_code_execution": 1, "shell_or_process_execution": 1, "path_input": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 63}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 3, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 852 — `samarth-kadaba/SMDPO`

Bounded repositories: `samarth-kadaba/SMDPO`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 28, code 26, documentation 2, data 0, manifests 0.

Static security flags: `{"dynamic_code_execution": 9, "unsafe_deserialization": 1, "network_fetch": 1, "sql_string_construction": 1}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 10, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 11, "hardcoded_threshold": 7, "assertion_as_validation": 4}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 857 — `anngvu/bioc-curation`

Bounded repositories: `anngvu/bioc-curation`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 13, code 3, documentation 1, data 9, manifests 0.

Static security flags: `{"network_fetch": 2, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 45, "clinical_or_patient_data": 12, "named_biomedical_cohort": 4}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 861 — `SakanaAI/AI-Scientist-v2`

Bounded repositories: `kuanlinhuang/AI-Scientist-v2`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 10, code 7, documentation 2, data 1, manifests 0.

Static security flags: `{"shell_or_process_execution": 24, "filesystem_mutation": 15, "dynamic_code_execution": 4, "network_fetch": 4, "path_input": 3, "hardcoded_secret_shape": 3, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"human_genomics": 11}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 6}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 862 — `Knowledge-Graph-Hub/kg-registry`

Bounded repositories: `andrewsu/kg-registry`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 747, code 28, documentation 695, data 13, manifests 6.

Static security flags: `{"mutable_remote_install": 32, "network_fetch": 9, "path_input": 6, "dynamic_code_execution": 1, "unsafe_deserialization": 1, "browser_html_injection": 1}`.

Privacy/data-governance flags: `{"human_genomics": 161, "clinical_or_patient_data": 68, "named_biomedical_cohort": 13}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 10}`.

Direct-adoption blockers:

- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
