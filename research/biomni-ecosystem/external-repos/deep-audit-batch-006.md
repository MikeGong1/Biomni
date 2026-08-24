# External Deep Audit Batch 006

Observed at: `2026-08-24T02:43:36Z`

Scope: stable external-family queue orders `63`–`112`, inclusive.

## Result

This accelerated checkpoint closes 50 families containing 64 bounded repository
records.

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 21 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 26 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 3 |
| **Total** | **50** |

The 21 substantive families preserve `change-000114`–`change-000139` and
`lineage-000040`–`lineage-000051`. Several families contain more than one
independent branch/PR change, so 21 families yield 26 Change records. No Feature
or Implementation ID is allocated. Every direct-adoption path is rejected or
deferred pending later semantic comparison and scientific, security, privacy,
provenance or license remediation.

The canonical machine record is
`external-repos/deep-audit-batch-006-manifest.jsonl`.

## Identity correction and strengthened gate

The first structural reduction was rejected by the parent before canonical
write. A stale worker shard reused queue numbers `72/82/92/102/112` for unrelated
Biomni forks (`repo-000164/174/184/194/204`), and the reducer checked only that
those IDs existed. It also omitted the `ahueb/ai-nuggets` member
`repo-002424` from order 83.

The corrected identities are:

| Order | Authoritative bounded repository | Family |
|---:|---|---|
| 72 | `repo-002005` `shantanusharma/openfold-3` | `aqlaboratory/openfold-3` |
| 82 | `repo-002257` `vlln/plugin-registry` | `vlln/plugin-registry` |
| 92 | `repo-006613` `psknlr/NSCLC-Agent` | `psknlr/NSCLC-Agent` |
| 102 | `repo-003895` `reacher-z/torchgeo-bench` | `torchgeo/torchgeo-bench` |
| 112 | `repo-004990` `yarikoptic/isic-cli` | `ImageMarkup/isic-cli` |

The final G1–G10 gate requires, for every order, exact equality between the
manifest ID set and all canonical database rows carrying that queue order; ID to
order round trips; ID/name bijection; reverse member completeness; family-key,
role and count consistency; cross-order uniqueness; and verifier identity
binding. The final manifest contains exactly 64 canonical IDs and no stale
Biomni ID.

## Method and evidence boundary

- Ten mutually exclusive five-family MAP shards used SSH/local DAG and the pinned
  shared GitHub queue. Required PR/release/fork cursors reached terminal pages.
- Ten verification paths plus parent primary-artifact checks applied identity,
  DAG, scientific, severity, provenance and authentication corrections.
- A product write quota prevented two independent verifiers from persisting the
  corrected five-family verifier. The parent therefore recorded their completed
  analyses explicitly, then independently rechecked canonical identities,
  GraphQL viewer/limit evidence, retry metadata, branch-scoped licenses,
  patch-id intersections and durable PR objects.
- Third-party code, tests, models, installers, notebooks and workflows were not
  executed.
- Source owners and child forks outside the bounded person universe remained
  evidence-only leads and did not expand `person_depth=1`.

## Substantive candidates

### Biomedical analysis and clinical workflows

- HistoBistro (`change-000114`, `lineage-000040`) preserves a six-commit Mayo
  MSI/MSS experiment branch. Broken clinical-covariate code, unused class
  weighting, result-column defects, unresolved pseudonymous cohort
  redistribution and external experiment tracking block adoption.
- VISTA reproduction (`change-000115`) and spRefine (`change-000116`) are paper
  reproduction/model leads. The former lacks immutable implementation evidence;
  the latter uses validation as test/early stopping and lacks license, portable
  configuration and independent results.
- NSCLC-Agent v0.1/v0.2 (`change-000127`–`000128`, `lineage-000045`) is a
  substantive clinical research artifact, not a clinical tool. Arbitrary local
  image paths can be sent to providers, complete case data and journals cross
  privacy boundaries, evidence verification is incomplete, and the v0.2 tree has
  no license text.
- Pathogenic PD variants (`change-000132`) has ClinVar exact-string, gene
  substring, release mismatch, allele-normalization, non-random sampling and
  pseudonymous per-sample history/data-governance defects.
- TWEAKR (`change-000139`) contaminates empirical null panels by resampling real
  panel genes; large/small panel percentiles are therefore not comparably
  calibrated. License, environment and derived clinical-metadata terms are also
  absent.

### Agents, reproduction and evidence acquisition

- `plugin-registry` (`change-000118`) is a privileged plugin control plane.
  Package installation and agent tools need host authorization, CSRF/origin
  controls, human approval, source/signature policy, SSRF protection and a
  package sandbox.
- `ai-nuggets` (`change-000119`) is a biomedical literature automation source,
  but unreviewed LLM publication, listener tracking and absent root license block
  direct use.
- `bio-reproducer-loop` (`change-000120`–`000121`, `lineage-000042`) has useful
  bundle/private-oracle/VM architecture. Ordinary use still executes external
  paper code on the host, uploads PDFs, uses mutable installers and unrestricted
  guest egress; develop derives circular ClaroAI oracles.
- The MoBi agent branch (`change-000122`, `lineage-000043`) spans 171 unique
  commits. Mass balance is hard-coded, convergence and Pharmpy/VPC contracts are
  false or broken, BLOCK does not roll back, study windows drift, model data can
  leave for an LLM, and mixed/vendored licenses remain unresolved.
- CRC atlas (`change-000123`), ADC acquisition (`change-000124`) and the aptamer
  pipeline (`change-000125`) retain design leads only. Missing immutable source
  provenance, approval/host/path boundaries, secret handling, self-generated
  controls, stub modalities and data/service terms prevent reuse.

### Benchmarks, evaluation and platforms

- TorchSim PR 454 (`change-000117`, `lineage-000041`) is historical numerical
  bug-fix evidence superseded by upstream refactor 439; its `1e-17` float64 test
  rounds to equality and does not exercise the claimed distinct-close case.
- Terminal-Bench-Science (`change-000126`, `lineage-000044`) preserves six
  closed synthetic benchmark proposals. Public reference truth contaminates
  evaluation, and the CT/MRI task uses phantoms rather than clinical validation.
- `cell-eval2` (`change-000129`, `lineage-000046`) has unusually strong metric
  documentation and tests, but `allow_pickle=True`, unvalidated v2 metrics and an
  unlicensed real H5AD fixture block direct adoption.
- cBioPortal branches (`change-000130`–`000131`, `lineage-000047`) use mutable
  remote embeddings and expose a network-bound development proxy; potential DOM
  injection, permissive CORS/hosts and clinical-backend bridging require
  rejection.
- TorchGeo DEO residue (`change-000133`, `lineage-000048`) has nine commits
  absent from current refs; eight match PR 239 development patch IDs and one is a
  member-only residual. PR 239 merged, PR 243 remains open with normalization and
  result fixes. Excluded Slurm/plot/mock-test artifacts are preserved as history,
  not an owner Feature.
- NexLAB (`change-000134`–`000135`, `lineage-000049`) contains laboratory
  notebook/education concepts, but stored-XSS, function authorization/quota,
  absent Firebase rules, and invalid statistics/privacy boundaries block use.
- VLMEvalKit PRs (`change-000136`, `lineage-000050`) normalize to open source PRs
  1634–1645. OmniDoc prediction/reference misalignment and unreachable MMMU
  sentence splitting can invalidate metrics; sandbox, model and dataset terms
  remain inherited blockers.
- ASD_Circuits (`change-000137`–`000138`, `lineage-000051`) preserves main and a
  26-commit PD/HD validation branch. The branch has no result artifacts or key
  matrices and contains conflicting gene-set definitions, so numerical claims
  remain unreproducible prose evidence.

## Complete family ledger

| Order | Family source | Bounded repository IDs | Result | Change | Lineage |
|---:|---|---|---|---|---|
| 63 | `DigitalSlideArchive/HistomicsTK` | repo-004952 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 64 | `priyanka9991/HistoBistro` | repo-006156 | DEEP_AUDIT_CANDIDATE | change-000114 | lineage-000040 |
| 65 | `bunnelab/virtues` | repo-006907 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 66 | `HelloWorldLTY/VISTA_reproduce` | repo-001370 | DEEP_AUDIT_CANDIDATE | change-000115 | N/A |
| 67 | `SCAU-AnimalGenetics/OmiGA` | repo-004274 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 68 | `HelloWorldLTY/sprefine` | repo-001352 | DEEP_AUDIT_CANDIDATE | change-000116 | N/A |
| 69 | `TorchSim/torch-sim` | repo-002082 | DEEP_AUDIT_CANDIDATE | change-000117 | lineage-000041 |
| 70 | `GoogleCloudPlatform/cluster-toolkit` | repo-001863, repo-004956 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 71 | `brave/brave-search-mcp-server` | repo-001853 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 72 | `aqlaboratory/openfold-3` | repo-002005 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 73 | `modelcontextprotocol/rust-sdk` | repo-002051 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 74 | `numpy/numpy` | repo-001997 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 75 | `Opentrons/opentrons` | repo-002009 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 76 | `samtools/samtools` | repo-002055 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 77 | `mattpocock/skills` | repo-002064, repo-002416, repo-005983 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 78 | `PyLabRobot/pylabrobot` | repo-002028, repo-007000 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 79 | `Qiskit/qiskit` | repo-002032 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 80 | `google-deepmind/mujoco` | repo-001981 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 81 | `PrefectHQ/fastmcp` | repo-001021, repo-001898, repo-005915 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 82 | `vlln/plugin-registry` | repo-002257 | DEEP_AUDIT_CANDIDATE | change-000118 | N/A |
| 83 | `andrewsu/ai-nuggets` | repo-000891, repo-002424 | DEEP_AUDIT_CANDIDATE | change-000119 | N/A |
| 84 | `vlln/bio-reproducer-loop` | repo-002228 | DEEP_AUDIT_CANDIDATE | change-000120, change-000121 | lineage-000042 |
| 85 | `Open-Systems-Pharmacology/MoBi` | repo-002730 | DEEP_AUDIT_CANDIDATE | change-000122 | lineage-000043 |
| 86 | `leezx/crc-unmet-need-therapeutic-atlas` | repo-007188 | DEEP_AUDIT_CANDIDATE | change-000123 | N/A |
| 87 | `leezx/adc-acquisition` | repo-007170 | DEEP_AUDIT_CANDIDATE | change-000124 | N/A |
| 88 | `chaudhariatul/apta-switch-multi-agent-pipeline` | repo-006418 | DEEP_AUDIT_CANDIDATE | change-000125 | N/A |
| 89 | `seandavi/awesome-single-cell` | repo-002144, repo-002574, repo-002974, repo-007051 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 90 | `codeocean/codeocean-sdk-python` | repo-004578 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 91 | `harbor-framework/terminal-bench-science` | repo-003886, repo-005655 | DEEP_AUDIT_CANDIDATE | change-000126 | lineage-000044 |
| 92 | `psknlr/NSCLC-Agent` | repo-006613 | DEEP_AUDIT_CANDIDATE | change-000127, change-000128 | lineage-000045 |
| 93 | `ArcInstitute/cell-eval2` | repo-002151 | DEEP_AUDIT_CANDIDATE | change-000129 | lineage-000046 |
| 94 | `modelcontextprotocol/servers` | repo-002060 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 95 | `microsoft/playwright-mcp` | repo-002020 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 96 | `RosettaCommons/rosetta` | repo-002049 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 97 | `OpenFreeEnergy/openfe` | repo-002004 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 98 | `google-deepmind/alphafold3` | repo-001834 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 99 | `broadinstitute/gatk` | repo-001912, repo-007077 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 100 | `cBioPortal/cbioportal-frontend` | repo-002763 | DEEP_AUDIT_CANDIDATE | change-000130, change-000131 | lineage-000047 |
| 101 | `mkoretsky1/pathogenic_pd_variants` | repo-003108 | DEEP_AUDIT_CANDIDATE | change-000132 | N/A |
| 102 | `torchgeo/torchgeo-bench` | repo-003895 | DEEP_AUDIT_CANDIDATE | change-000133 | lineage-000048 |
| 103 | `Institute-for-Future-Intelligence/nexlab` | repo-005949 | DEEP_AUDIT_CANDIDATE | change-000134, change-000135 | lineage-000049 |
| 104 | `scverse/ecosystem-packages` | repo-002999, repo-003125 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 105 | `mapping-commons/sssom` | repo-005625 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 106 | `open-compass/VLMEvalKit` | repo-003900 | DEEP_AUDIT_CANDIDATE | change-000136 | lineage-000050 |
| 107 | `WaterFutures/WaterBenchmarkHub` | repo-003903 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 108 | `explorerwjy/ASD_Circuits` | repo-006045 | DEEP_AUDIT_CANDIDATE | change-000137, change-000138 | lineage-000051 |
| 109 | `Graphify-Labs/graphify` | repo-005919, repo-007333 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 110 | `leezx/TWEAKR-OncoPlacental` | repo-007209 | DEEP_AUDIT_CANDIDATE | change-000139 | N/A |
| 111 | `ImageMarkup/isic-metadata` | repo-004991 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 112 | `ImageMarkup/isic-cli` | repo-004990 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |

## Canonical decision

Batch 006 raises deep-audited external families from 62 to 112 and bounded
repository records from 76 to 140. Unresolved external families fall from 2,007
to 1,957; queued HIGH records fall from 2,085 to 2,021. Stable queue orders are
not renumbered. The next accelerated shard is orders `113`–`162`.
