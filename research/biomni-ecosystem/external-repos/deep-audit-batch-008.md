# External Deep Audit Batch 008

Observed at: `2026-08-24T04:45:04Z`

Scope: stable external-family queue orders `163`–`212`, inclusive.

## Result

This checkpoint closes 50 families containing 56 bounded repository records.

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 21 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 19 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 9 |
| `AUDIT_COMPLETE_NO_BIOMEDICAL_CAPABILITY` | 1 |
| **Total** | **50** |

The 21 substantive families preserve `change-000168`–`change-000196` and
`lineage-000061`–`lineage-000072`. Multiple independent branch/history
components produce 29 Change records. No Feature or Implementation ID is
allocated; direct adoption is rejected or deferred.

The canonical machine record is
`external-repos/deep-audit-batch-008-manifest.jsonl`.

## Evidence and queue integrity

- Ten MAP and ten verifier artifacts are SHA-bound; all 56 canonical identity
  rows byte-compare with current `repositories.jsonl`.
- GraphQL 502/error bodies are diagnostic-only and have evidence weight zero.
  Batch 008 exposed and fixed a cache bug that previously returned a 502 HTML
  body as false `200 cached=true`. Only fresh HTTP-200/no-errors results can now
  hit cache (`evidence-000198`).
- Verifier corrections override MAP wording/counts. No verifier requested a
  result-class reversal.
- Third-party code, tests, models, installers and workflows were not executed.
- Large child-fork sets remain explicitly bounded. Identity/SHA screening is not
  described as content audit where child repositories were outside
  `person_depth=1`.

## Substantive candidates

### Scientific and clinical workflows

- USD (`change-000173`) is an independent spatial-domain implementation with an
  invalid calibration contract, missing input/checkpoint provenance and unsafe
  pickle/NumPy/PyTorch loading; no license or independent validation is present.
- QueryPilot (`change-000171`) is a strong query/adapter implementation, but
  formal runs and adapters are external path+hash references and Spider Dev is
  repeatedly reused without an untouched test split.
- methods-graph (`change-000172`) retains a useful guardrail/evidence/replay
  concept, but replay fetches and evidence/scientific contracts are incomplete;
  nf-core observes HEAD yet lacks fetch-by-recorded-SHA clean replay.
- MRSi Resources (`change-000179`) presents disputed claims as educational
  evidence; all 12 remain usable and one population/CI/recency claim is retained,
  while GoatCounter contradicts its no-external-request posture.
- Dogma (`change-000180`) defaults its main API development command to
  `0.0.0.0`; writable-root scan/patch/stub-run, browser execution, workflow tool
  availability, URL handling and benchmark overcounting require strict
  deployment and scientific redesign.
- Med-Bench-Arena (`change-000181`, `lineage-000064`) retains one member scoring
  patch, but LLM-judge prompt injection, partial-criterion/sample failures and
  medical-data provider boundaries invalidate direct benchmark use.
- LazySlide PR 233 (`change-000183`, `lineage-000066`) contains organ-case,
  zero-range NaN, mutable equivalence clone and unpinned model risks. In the
  locked PyTorch 2.7 environment, unconditional pickle-RCE wording is not
  supported; the remaining risk is version-dependent deserialization plus model
  integrity/license uncertainty.
- CellTypeBias (`change-000187`–`000188`, `lineage-000069`) has hardcoded imports,
  zero-expression transforms, fork-multiprocessing RNG/null and dependent
  Stouffer/circular-null defects with no license.
- 0shotprot (`change-000189`–`000191`, `lineage-000070`) uses one AAV and seven
  TAPE tasks, fixed learned/additive oracles and adaptive generators. Adaptive
  overfitting is a risk rather than demonstrated proof; unpinned model code,
  unchecked archives and pickle remain blockers.
- ProSpero (`change-000192`, `lineage-000071`) is an orphan-style rewrite missing
  source license/environment/data/assets, with unpinned remote model code,
  unsafe result loading, unbounded unique-candidate loops and no wet-lab evidence.
- thyroid-quiz (`change-000194`–`000195`, `lineage-000072`) excludes uncertain
  cases from sensitivity/specificity denominators, relies on self-reported
  clinicians and has unsafe seed/export, image/data-governance and licensing
  boundaries.

### Repository, data and benchmark infrastructure

- Bioconda history (`change-000168`–`000169`, `lineage-000061`) preserves two
  current-looking but superseded varcode/pybwa recipe branches; they are history,
  not integration sources.
- study-template PR 3 (`change-000170`, `lineage-000062`) is retained as a source
  PR candidate, not a fork-only implementation.
- letspill (`change-000174`) has an async authorization check without `await`,
  allowing a profile/viewing chain toward cross-user state/preferences, plus
  wildcard credentialed CORS, disabled CSRF, insecure cookies, no-verify DB TLS
  and no license.
- Four BIDS branches (`change-000175`–`000178`, `lineage-000063`) include small
  useful fixes and larger review leads; MEG sensor/electrode terminology,
  validator pseudo-file regression, memory/logging and BEP028 acceptance remain
  unresolved.
- labcams PR 4 (`change-000182`, `lineage-000065`) exposes a CLI-default reachable
  unauthenticated ZMQ `recv_pyobj` control surface; direct constructor default is
  safer and the distinction is retained.
- bids-copier (`change-000184`) remains an independent prototype with critical
  crafted-issue path traversal capable of arbitrary writable JSON overwrite and
  insufficient operational privacy controls.
- WeaveBench PR 23 (`change-000185`, `lineage-000067`) has host archive traversal,
  prompt-injectable secret-bearing judge and raw-score provenance gaps; host
  impact is conditional on deployment.
- DataLad history (`change-000186`, `lineage-000068`) preserves 75 native plus
  seven own-PR unique commits (82 union) across 23 source-unknown heads, including
  unsafe obsolete WIP. It is historical evidence, not current adoption code.
- Novae (`change-000193`) includes default admin/JWT conditions, arbitrary MCP
  host execution, shared service credentials and authenticated SSRF/provider
  egress risks with insufficient scientific evidence validation.
- bids-validator-derivative (`change-000196`) is a prototype with critical
  `../` output traversal enabling arbitrary writable JSON overwrite.

`clashskill` (order 208) is an independent but non-biomedical metadata false
positive. Its privileged downloads/controller/subscription/license risks are
recorded, but no biomedical Change or Feature is allocated.

## Complete family ledger

| Order | Family source | Bounded repository IDs | Result | Change | Lineage |
|---:|---|---|---|---|---|
| 163 | `DearCaat/Awesome-Computational-Pathology-Papers` | repo-002950 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 164 | `bioconda/bioconda-recipes` | repo-001527, repo-002298, repo-002749, repo-004076, repo-006384 | DEEP_AUDIT_CANDIDATE | change-000168, change-000169 | lineage-000061 |
| 165 | `pynapple-org/pynapple` | repo-005423 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 166 | `brain-bbqs/study-template` | repo-005636 | DEEP_AUDIT_CANDIDATE | change-000170 | lineage-000062 |
| 167 | `hussius/deeplearning-biology` | repo-002998 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 168 | `fahadshamshad/awesome-transformers-in-medical-imaging` | repo-002984 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 169 | `maduc7/Histopathology-Datasets` | repo-003004 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 170 | `lulaiao/QueryPilot` | repo-003098 | DEEP_AUDIT_CANDIDATE | change-000171 | N/A |
| 171 | `web-arena-x/webarena` | repo-003905 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 172 | `manu-tej/methods-graph` | repo-007245 | DEEP_AUDIT_CANDIDATE | change-000172 | N/A |
| 173 | `HelloWorldLTY/USD` | repo-001367 | DEEP_AUDIT_CANDIDATE | change-000173 | N/A |
| 174 | `pfizer-opensource/scikit-digital-health` | repo-002056 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 175 | `marcosbolanos/letspill` | repo-001601 | DEEP_AUDIT_CANDIDATE | change-000174 | N/A |
| 176 | `bids-standard/bids-specification` | repo-004468 | DEEP_AUDIT_CANDIDATE | change-000175, change-000176, change-000177, change-000178 | lineage-000063 |
| 177 | `Future-House/paper-qa` | repo-006144, repo-007102 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 178 | `alexs42/MRSi-Resources` | repo-004196 | DEEP_AUDIT_CANDIDATE | change-000179 | N/A |
| 179 | `manu-tej/dogma` | repo-007235 | DEEP_AUDIT_CANDIDATE | change-000180 | N/A |
| 180 | `pariskang/Med-Bench-Arena` | repo-006612 | DEEP_AUDIT_CANDIDATE | change-000181 | lineage-000064 |
| 181 | `ESIPFed/science-on-schema.org` | repo-005548 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 182 | `bids-standard/bids-validator` | repo-004471 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 183 | `PridaLab/rippl-AI` | repo-005516 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 184 | `jcouto/labcams` | repo-005023 | DEEP_AUDIT_CANDIDATE | change-000182 | lineage-000065 |
| 185 | `ByteDance-Seed/WideSearch` | repo-003911 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 186 | `yuanzhang7/awesome-auto-research-landscape` | repo-003496 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 187 | `Peilin-FF/Awesome-Deep-Research` | repo-003533 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 188 | `rendeirolab/LazySlide` | repo-003007 | DEEP_AUDIT_CANDIDATE | change-000183 | lineage-000066 |
| 189 | `wgwang/awesome-LLM-benchmarks` | repo-003910 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 190 | `Halluminate/WebBench` | repo-003906 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 191 | `yarikoptic/bids-copier` | repo-004459 | DEEP_AUDIT_CANDIDATE | change-000184 | N/A |
| 192 | `NVIDIA/digital-biology-examples` | repo-005907 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 193 | `mahmoodlab/CORAL` | repo-001691 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 194 | `weavebench/WeaveBench` | repo-003904 | DEEP_AUDIT_CANDIDATE | change-000185 | lineage-000067 |
| 195 | `microsoft/WindowsAgentArena` | repo-003913 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 196 | `worldbench/awesome-ai-auto-research` | repo-003468 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 197 | `xu-hu-2002/Toward-Trustworthy-Computer-Use-Agent-A-Survey` | repo-003896 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 198 | `anthropics/life-sciences` | repo-001955, repo-006333 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 199 | `isaac-for-healthcare/i4h-workflows` | repo-001934 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 200 | `datalad/datalad` | repo-004664 | DEEP_AUDIT_CANDIDATE | change-000186 | lineage-000068 |
| 201 | `bids-standard/bids-website` | repo-004455 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 202 | `rendeirolab/lazyslide-tutorials` | repo-003009 | NO_UNIQUE_OR_SOURCE_LINEAGE | N/A | N/A |
| 203 | `ajannesari/awesome-single-cell-foundation-models-for-oncology` | repo-002978 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 204 | `explorerwjy/CellTypeBias_VIP` | repo-006048 | DEEP_AUDIT_CANDIDATE | change-000187, change-000188 | lineage-000069 |
| 205 | `marcosbolanos/0shotprot` | repo-001581 | DEEP_AUDIT_CANDIDATE | change-000189, change-000190, change-000191 | lineage-000070 |
| 206 | `szczurek-lab/ProSpero` | repo-001616 | DEEP_AUDIT_CANDIDATE | change-000192 | lineage-000071 |
| 207 | `AgenticHealthAI/Awesome-AI-Agents-for-Healthcare` | repo-003463 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |
| 208 | `vlln/clashskill` | repo-002231 | AUDIT_COMPLETE_NO_BIOMEDICAL_CAPABILITY | N/A | N/A |
| 209 | `Liripo/novae` | repo-003072 | DEEP_AUDIT_CANDIDATE | change-000193 | N/A |
| 210 | `Nigmat-future/thyroid-quiz` | repo-003205 | DEEP_AUDIT_CANDIDATE | change-000194, change-000195 | lineage-000072 |
| 211 | `yarikoptic/bids-validator-derivative` | repo-004472 | DEEP_AUDIT_CANDIDATE | change-000196 | N/A |
| 212 | `anthbapt/Spatial-Biology-Tools` | repo-003018 | DOC_METADATA_MAINTENANCE_ONLY | N/A | N/A |

## Canonical decision

Batch 008 raises deep-audited external families from 162 to 212 and bounded
repository records from 193 to 249. Unresolved external families fall from 1,907
to 1,857; queued HIGH records fall from 1,968 to 1,912. Stable queue orders are
not renumbered. The next accelerated shard is orders `213`–`262`.
