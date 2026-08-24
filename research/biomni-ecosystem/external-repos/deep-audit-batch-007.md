# External Deep Audit Batch 007

Observed at: `2026-08-24T03:42:40Z`

Scope: stable external-family queue orders `113`–`162`, inclusive.

## Result

This checkpoint closes 50 families containing 53 bounded repository records.

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 19 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 26 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 5 |
| **Total** | **50** |

The 19 substantive families preserve `change-000140`–`change-000167` and
`lineage-000052`–`lineage-000060`. Selected repositories contain multiple
independent branch/history components, so 19 families yield 28 Change records.
No Feature or Implementation ID is allocated. Every direct-adoption path is
rejected or deferred.

The canonical machine record is
`external-repos/deep-audit-batch-007-manifest.jsonl`.

## Method and identity gate

- Ten MAP artifacts and ten verifier artifacts are SHA-bound in the manifest.
- Each order's repository ID, full name, family key/source, role and member count
  byte-compare equal to all current canonical `repositories.jsonl` rows carrying
  that queue order.
- Reverse member completeness and ID-to-order round trips are mandatory; literal
  worker IDs are not trusted as the authoritative set.
- Verifier corrections override MAP wording and counts. No verifier required a
  result-class reversal.
- Third-party code, tests, models, installers and workflows were not executed.
- Child forks outside the bounded person universe remain discovery leads. For
  example, the `obra/superpowers` family closes its one bounded member, but only
  the first 100 of 24,484 external child forks were sampled; the global child
  universe is not claimed complete.

## Substantive candidates

### Scientific agents and evaluation

- ScienceRAG (`change-000140`) is blocked by unauthenticated deployment/KG
  approval surfaces, unsafe joblib/NumPy/PyTorch artifact loading, a 31-sample
  calibration claim, external-corpus trust and unclear code/document/model asset
  rights.
- TruthSeq (`change-000141`) uses a biased/best-of-context null while its UI
  misstates the simulation contract. The same evidence claim is imported by
  Autism Atlas (`change-000158`, `lineage-000060`) without the underlying
  analysis.
- SciEvalKit adapter PRs (`change-000142`, `lineage-000052`) have useful mock/fake
  unit tests but no real-model/scientific validation; prompt and checkout
  differences confound cross-model comparison.
- Real-Twin PR 46 (`change-000143`, `lineage-000053`) changes the GEH objective to
  passing-link share but discards error magnitude above threshold; it is a
  traffic-simulation change, not a biomedical feature.
- SciAgentArena (`change-000161`) exposes unauthenticated code/upload execution,
  environment access, unsafe local paths/deserialization and plaintext
  clinical/omics job artifacts. Its evaluator and HVG contracts also fail
  statically, with no root license or runtime evidence.

### Biomedical models, databases and workflows

- ChromBPNet (`change-000152`–`000153`, `lineage-000056`) preserves nested
  6/54-commit multitask accessibility and nucleosome/cfDNA branches. Unsafe
  checkpoint/cache loading, shell/cloud/W&B boundaries, sensitive human inputs,
  incomplete orthogonal validation and negative cancer/minor-fraction results
  preclude clinical use.
- BixBench PR 2 (`change-000154`, `lineage-000057`) reports best-of-attempt
  success rather than Pass@1: 45 of 50 questions achieved a pass across 60
  attempts, while the canonical sweep was 34/46. Full-shell/holdout and inherited
  environment risks remain.
- Tao Shanghan Corpus (`change-000155`) has 8,541 structured records still
  pending review and zero manual reviews; transcript rights are mostly unstated,
  and its release archive lacks checksum/API release provenance.
- SpatialTis (`change-000157`) contains additional blocker defects: unordered
  hash values can be mapped into grids and Clark–Evans mixes squared nearest
  distances with a Euclidean expectation.
- ADCdb (`change-000162`) is retained only as a database lead after provenance,
  scientific validation, data terms and deployment controls are established.
- PACS (`change-000163`) continues after optimizer failure/parameter limits,
  writes FITS/SQLite and omits convergence fields from exports. Plain HTTP
  archives, fixed temporary paths, unsafe extraction/pickle, partial review data,
  absent environment lock and missing license block use.
- Autism data atlas (`change-000164`–`000166`) mixes a useful access catalog with
  irreproducible replication claims and an AlphaGenome wrapper lacking build and
  model versions. Familial genomic detail, command-line API keys, auto-install,
  DOM injection and absent license/provenance are material blockers.

### Infrastructure and selected fork histories

- cBioPortal (`change-000144`–`000147`, `lineage-000054`) preserves selected
  historical/source-PR and member branch evidence only. The discrete CNA branch
  silently bins floats; NaN falls through to amplification, while historical
  deployments contain obsolete or unsafe configuration. The other 114
  mixed-provenance member tips remain unaudited rather than bulk-promoted.
- ToolUniverse (`change-000148`–`000150`, `lineage-000055`) retains a narrow PHYKIT
  fix and skill-guidance changes but rejects the BixBench reproduction branch.
  Source-wide code execution, pickle/MCP/provider/PHI risks are inherited
  adoption context, not newly introduced by all five member-only commits.
- MiroFish (`change-000151`) is an independent simulation/agent platform with
  public debug/server and scientific-contract blockers; verifier-corrected scope
  is 44 changed files, not 46.
- grism (`change-000156`) treats `n<3` as normal, uses normality pretests and raw
  pairwise p-values without multiplicity correction, while remote use exposes
  query/style, resource and matplotlib thread-safety risks. No license or lock is
  present.
- sdb (`change-000159`–`000160`, `lineage-000058`) separates a modern astronomy
  identity/provenance core from unsafe legacy SQL/password tooling. It is outside
  biomedical scope and lacks a reuse license.
- scikit-bio PR 2494 (`change-000167`, `lineage-000059`) is retained as a
  diagnostic Python exception-message/test/changelog bug fix, not a documentation
  change.

## Complete family ledger

| Order | Family source | Bounded repository IDs | Result | Change | Lineage |
|---:|---|---|---|---|---|
| 113 | `Irishaze/sciencerag` | repo-004212 | DEEP_AUDIT_CANDIDATE | change-000140 | N/A |
| 114 | `rsflinn/truthseq` | repo-003921 | DEEP_AUDIT_CANDIDATE | change-000141 | N/A |
| 115 | `InternScience/SciEvalKit` | repo-003873 | DEEP_AUDIT_CANDIDATE | change-000142 | lineage-000052 |
| 116 | `ORNL-Real-Sim/Real-Twin` | repo-003864 | DEEP_AUDIT_CANDIDATE | change-000143 | lineage-000053 |
| 117 | `cBioPortal/cbioportal` | repo-002301, repo-002758 | DEEP_AUDIT_CANDIDATE | change-000144, change-000145, change-000146, change-000147 | lineage-000054 |
| 118 | `mims-harvard/ToolUniverse` | repo-003025, repo-003161, repo-006365 | DEEP_AUDIT_CANDIDATE | change-000148, change-000149, change-000150 | lineage-000055 |
| 119 | `Irishaze/MiroFish` | repo-004211 | DEEP_AUDIT_CANDIDATE | change-000151 | N/A |
| 120 | `Research-Equality/awesome-ai-scientists` | repo-003488 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 121 | `pglira/awesome-science-communication` | repo-003708 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 122 | `EdwardLeeLPZ/Awesome-Auto-Research` | repo-003495 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 123 | `Harsh9005/awesome-scientific-ai-tools` | repo-003709 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 124 | `0x11c11e/awesome-ai-research-tools` | repo-003484 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 125 | `chchenhui/awesome-research-agents` | repo-003694 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 126 | `SUSTech-GenAI/awesome-researchclaw` | repo-003695 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 127 | `modelscope/Awesome-Vibe-Research` | repo-003735 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 128 | `writing-resources/awesome-scientific-writing` | repo-003711 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 129 | `kael-odin/awesome-academic-research-skills` | repo-003368 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 130 | `VoltAgent/awesome-ai-agent-papers` | repo-003901 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 131 | `huang-sh/awesome-ai4sci` | repo-003491 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 132 | `jd-coderepos/awesome-science-ai-agents` | repo-003707 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 133 | `kundajelab/chrombpnet` | repo-007035 | DEEP_AUDIT_CANDIDATE | change-000152, change-000153 | lineage-000056 |
| 134 | `omicverse/OmicOS-BixBench` | repo-003073 | DEEP_AUDIT_CANDIDATE | change-000154 | lineage-000057 |
| 135 | `psknlr/Tao-Shanghan-Corpus` | repo-006622 | DEEP_AUDIT_CANDIDATE | change-000155 | N/A |
| 136 | `obra/superpowers` | repo-002668 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 137 | `drgmk/grism` | repo-006779 | DEEP_AUDIT_CANDIDATE | change-000156 | N/A |
| 138 | `openbiox/awosome-bioinformatics` | repo-002987 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 139 | `Mr-Milk/SpatialTis-core` | repo-003154 | DEEP_AUDIT_CANDIDATE | change-000157 | N/A |
| 140 | `neurobagel/digest` | repo-004650 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 141 | `zhangleiniu/awesome-scientific-literature-retrieval` | repo-003710 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 142 | `webfuse-com/awesome-autoresearch` | repo-003501 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 143 | `aristoteleo/veckit` | repo-002210 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 144 | `rsflinn/autism-atlas-site` | repo-003918 | DEEP_AUDIT_CANDIDATE | change-000158 | lineage-000060 |
| 145 | `ai4s-research/awesome-ai-for-science` | repo-003481 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 146 | `drgmk/sdb` | repo-006789 | DEEP_AUDIT_CANDIDATE | change-000159, change-000160 | lineage-000058 |
| 147 | `yenanjing/awesome-ai-for-science` | repo-003480 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 148 | `HelloWorldLTY/SciAgentArena` | repo-001341 | DEEP_AUDIT_CANDIDATE | change-000161 | N/A |
| 149 | `leezx/ADCdb` | repo-007171 | DEEP_AUDIT_CANDIDATE | change-000162 | N/A |
| 150 | `drgmk/tldr_pacs` | repo-006792 | DEEP_AUDIT_CANDIDATE | change-000163 | N/A |
| 151 | `geniusrise/awesome-healthcare-datasets` | repo-002957 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 152 | `natnew/awesome-ai-scientists` | repo-003487 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 153 | `AI4Scientist/awesome-autoresearch` | repo-003500 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 154 | `openags/Awesome-AI-Scientist-Papers` | repo-003485 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 155 | `Marigoldwu/Awesome-Histopathology-to-Omics` | repo-002960 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 156 | `rsflinn/autism-data-atlas` | repo-003920 | DEEP_AUDIT_CANDIDATE | change-000164, change-000165, change-000166 | N/A |
| 157 | `vanandrew/warpkit` | repo-005749 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 158 | `Owais-CodeHub/MMIF-Review` | repo-003841 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 159 | `scikit-bio/scikit-bio` | repo-002938 | DEEP_AUDIT_CANDIDATE | change-000167 | lineage-000059 |
| 160 | `tsinghua-fib-lab/Awesome-AI-Scientists` | repo-003486 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 161 | `HKUST-KnowComp/Awesome-LLM-Scientific-Discovery` | repo-003640 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 162 | `handsome-rich/Awesome-Auto-Research-Tools` | repo-003497 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |

## Canonical decision

Batch 007 raises deep-audited external families from 112 to 162 and bounded
repository records from 140 to 193. Unresolved external families fall from 1,957
to 1,907; queued HIGH records fall from 2,021 to 1,968. Stable queue orders are
not renumbered. The next accelerated shard is orders `163`–`212`.
