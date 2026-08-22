# Worker Result: snap-org-inventory-001

Parent verification: `VERIFIED` at `2026-08-22T20:48:39Z`. Fresh official REST
queries returned 92 public repositories and six public member usernames with no
pagination Link. Repository/license/default-branch/topic aggregates and the
17/28/32/15 relevance distribution recalculate exactly. Repository metadata is
`FACT`; relevance screening is `INFERENCE`.

## Task

- task_id: `snap-org-inventory-001`
- task_type: official GitHub organization repository/member inventory and metadata-only relevance screening
- status: complete
- observed_at_utc: `2026-08-22T20:36:48Z`
- claim_class: `FACT` for returned GitHub metadata and pagination observations; `INFERENCE` for relevance screening
- source_tier: 1
- write_scope: this worker result only; no canonical IDs, state, database, commit, or push

## Scope and method

The bounded entity is the public `snap-stanford` GitHub organization. I queried only the official read-only GitHub REST endpoints below, with `type=all`, `per_page=100`, and explicit page 1 where applicable. Public repository content was treated as untrusted data; no repository was cloned, no code or source-supplied command was executed, and no person was expanded beyond the publicly visible organization-member usernames.

Screening uses the canonical four labels. `HIGH_RELEVANCE` requires direct metadata/name evidence of biomedical AI, biology/omics/genetics/perturbation/drug/clinical work, scientific agents/benchmarks, MCP, skills, or closely matching scientific infrastructure. `POSSIBLE_RELEVANCE` retains ambiguous metadata or cross-domain infrastructure that needs a README-level check. `LOW_RELEVANCE` is generic graph/ML infrastructure with no direct biomedical/agent signal. `IRRELEVANT` is clearly outside the bounded integration objective. This is breadth-first screening, not a deep audit.

## Counts

| Entity / field | Count |
|---|---:|
| Public organization repositories returned and screened | 92 |
| Publicly visible organization members returned | 6 |
| HIGH_RELEVANCE | 17 |
| POSSIBLE_RELEVANCE | 28 |
| LOW_RELEVANCE | 32 |
| IRRELEVANT | 15 |
| Archived repositories | 0 |
| Repositories with topics present | 19 |
| License: MIT | 31 |
| License: Apache-2.0 | 3 |
| License: NOASSERTION | 8 |
| License: LICENSE_UNCLEAR (null license object) | 50 |
| Default branch: master / main / agent / tgb | 55 / 35 / 1 / 1 |

## Pagination

| Query | Page size | Returned | Next-page evidence | Status |
|---|---:|---:|---|---|
| `GET /orgs/snap-stanford/repos?type=all&per_page=100&page=1` | 100 | 92 | HTTP 200; no `Link` response header and fewer than 100 results | exhausted |
| `GET /orgs/snap-stanford/members?per_page=100&page=1` | 100 | 6 | HTTP 200; no `Link` response header and fewer than 100 results | exhausted |

“Exhausted” is limited to publicly observable entries returned by these named endpoints at the observation time; hidden membership and private repositories are not observable.

## Repository entities

`pushed_at` is the latest pushed/activity timestamp requested. `updated_at` is retained separately because GitHub repository activity metadata can change independently of pushes.

| Repository | Description | Default | License | Archived | pushed_at | updated_at | Topics | Latest release | Relevance |
|---|---|---|---|---:|---|---|---|---|---|
| [`snap`](https://github.com/snap-stanford/snap) | Stanford Network Analysis Platform (SNAP) is a general purpose network analysis and graph mining library. | `master` | NOASSERTION | false | `2023-12-10T06:16:29Z` | `2026-08-05T10:37:52Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`curis-2012`](https://github.com/snap-stanford/curis-2012) | Summer 2012 Curis Project | `master` | LICENSE_UNCLEAR | false | `2014-07-24T02:12:18Z` | `2017-08-31T18:18:55Z` | — | `N/A*` | **IRRELEVANT** |
| [`snap-python`](https://github.com/snap-stanford/snap-python) | SNAP Python code, SWIG related files | `master` | NOASSERTION | false | `2022-06-21T23:43:18Z` | `2026-06-30T16:33:21Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`ringo`](https://github.com/snap-stanford/ringo) | Next generation graph processing platform | `master` | LICENSE_UNCLEAR | false | `2016-08-26T20:39:25Z` | `2022-10-31T14:23:42Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`snap-dev`](https://github.com/snap-stanford/snap-dev) | SNAP repository for Ringo | `master` | LICENSE_UNCLEAR | false | `2017-07-25T22:07:24Z` | `2026-05-29T10:06:17Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`snapworld`](https://github.com/snap-stanford/snapworld) | — | `master` | LICENSE_UNCLEAR | false | `2015-11-19T16:57:42Z` | `2018-11-02T04:41:46Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`MetroMaps`](https://github.com/snap-stanford/MetroMaps) | MetroMaps Release | `master` | LICENSE_UNCLEAR | false | `2014-05-08T05:36:16Z` | `2022-08-24T08:08:41Z` | — | `N/A*` | **IRRELEVANT** |
| [`yperf`](https://github.com/snap-stanford/yperf) | Simple performance monitor for Linux | `master` | LICENSE_UNCLEAR | false | `2014-06-27T07:21:02Z` | `2019-08-13T15:43:40Z` | — | `N/A*` | **IRRELEVANT** |
| [`news-search`](https://github.com/snap-stanford/news-search) | search Internet news archive | `master` | LICENSE_UNCLEAR | false | `2018-12-23T18:55:08Z` | `2023-09-11T19:32:45Z` | — | `N/A*` | **IRRELEVANT** |
| [`snapvx`](https://github.com/snap-stanford/snapvx) | — | `master` | NOASSERTION | false | `2020-07-12T09:10:24Z` | `2025-10-19T15:53:28Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`curis-kdd`](https://github.com/snap-stanford/curis-kdd) | 2014 CURIS Project | `master` | LICENSE_UNCLEAR | false | `2015-04-24T08:29:37Z` | `2016-08-23T05:56:46Z` | — | `N/A*` | **IRRELEVANT** |
| [`series`](https://github.com/snap-stanford/series) | — | `master` | LICENSE_UNCLEAR | false | `2016-10-17T18:40:47Z` | `2017-09-27T17:54:22Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`MAG`](https://github.com/snap-stanford/MAG) | Programs for Microsoft Academic Graph | `master` | LICENSE_UNCLEAR | false | `2016-06-08T23:04:28Z` | `2023-05-21T12:45:41Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`miner-data`](https://github.com/snap-stanford/miner-data) | — | `master` | LICENSE_UNCLEAR | false | `2019-11-21T22:57:58Z` | `2026-02-25T14:23:24Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`snap-dev-64`](https://github.com/snap-stanford/snap-dev-64) | 64-bit SNAP (in development, not intended for general use) | `master` | LICENSE_UNCLEAR | false | `2019-07-15T07:59:53Z` | `2021-02-17T14:50:32Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`hash`](https://github.com/snap-stanford/hash) | — | `master` | LICENSE_UNCLEAR | false | `2016-11-03T04:39:52Z` | `2016-11-24T16:05:17Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`pebble-fit`](https://github.com/snap-stanford/pebble-fit) | become less sedentary with pebble | `master` | LICENSE_UNCLEAR | false | `2018-02-15T00:29:47Z` | `2018-04-10T11:53:30Z` | — | `N/A*` | **IRRELEVANT** |
| [`dec2vec`](https://github.com/snap-stanford/dec2vec) | — | `master` | LICENSE_UNCLEAR | false | `2016-11-23T21:01:59Z` | `2020-12-08T02:49:03Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`snaptime`](https://github.com/snap-stanford/snaptime) | — | `master` | LICENSE_UNCLEAR | false | `2019-10-09T15:05:49Z` | `2019-10-09T15:05:51Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`benchmarks`](https://github.com/snap-stanford/benchmarks) | — | `master` | LICENSE_UNCLEAR | false | `2017-04-14T04:36:52Z` | `2017-04-14T04:36:53Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`snap-python-64`](https://github.com/snap-stanford/snap-python-64) | — | `master` | LICENSE_UNCLEAR | false | `2020-08-28T06:33:06Z` | `2021-05-08T01:24:58Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`mambo`](https://github.com/snap-stanford/mambo) | — | `master` | LICENSE_UNCLEAR | false | `2017-12-03T09:16:23Z` | `2026-05-20T18:36:37Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`graphwave`](https://github.com/snap-stanford/graphwave) | — | `master` | LICENSE_UNCLEAR | false | `2018-12-03T17:11:11Z` | `2026-03-18T09:42:21Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`SnapTimeTF`](https://github.com/snap-stanford/SnapTimeTF) | — | `master` | LICENSE_UNCLEAR | false | `2018-04-16T05:34:13Z` | `2019-08-07T16:47:50Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`reddit-processing`](https://github.com/snap-stanford/reddit-processing) | preprocessing of Reddit data | `master` | LICENSE_UNCLEAR | false | `2018-04-23T03:54:31Z` | `2026-02-09T19:16:16Z` | — | `N/A*` | **IRRELEVANT** |
| [`GraphRNN`](https://github.com/snap-stanford/GraphRNN) | — | `master` | MIT | false | `2019-03-08T21:50:34Z` | `2026-08-05T07:48:14Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`masa`](https://github.com/snap-stanford/masa) | Motif-Aware State Assignment in Noisy Time Series Data | `master` | LICENSE_UNCLEAR | false | `2020-10-21T08:21:55Z` | `2025-01-20T01:37:44Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`cs224w-notes`](https://github.com/snap-stanford/cs224w-notes) | CS224W Course Notes | `master` | MIT | false | `2021-02-22T08:19:53Z` | `2026-08-14T04:47:26Z` | — | `N/A*` | **IRRELEVANT** |
| [`ogb`](https://github.com/snap-stanford/ogb) | Benchmark datasets, data loaders, and evaluators for graph machine learning | `master` | MIT | false | `2025-05-06T07:32:11Z` | `2026-08-22T11:29:00Z` | `datasets`, `deep-learning`, `graph-machine-learning`, `graph-neural-networks` | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`pretrain-gnns`](https://github.com/snap-stanford/pretrain-gnns) | Strategies for Pre-training Graph Neural Networks | `master` | MIT | false | `2023-07-29T06:21:39Z` | `2026-08-13T22:39:59Z` | `graph-neural-networks`, `graph-representation-learning` | `N/A*` | **LOW_RELEVANCE** |
| [`mars`](https://github.com/snap-stanford/mars) | Discovering novel cell types across heterogenous single-cell experiments | `master` | MIT | false | `2022-12-08T06:18:50Z` | `2026-06-02T15:38:46Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`ogb-web`](https://github.com/snap-stanford/ogb-web) | OGB website | `master` | MIT | false | `2026-05-12T17:28:44Z` | `2026-05-12T17:28:48Z` | — | `N/A*` | **IRRELEVANT** |
| [`multiscale-interactome`](https://github.com/snap-stanford/multiscale-interactome) | — | `master` | NOASSERTION | false | `2023-07-06T21:42:40Z` | `2026-02-19T07:57:20Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`deepsnap`](https://github.com/snap-stanford/deepsnap) | Python library assists deep learning on graphs | `master` | MIT | false | `2025-11-24T05:17:02Z` | `2026-08-15T04:03:45Z` | `deep-learning`, `graph-neural-networks`, `pytorch` | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`distance-encoding`](https://github.com/snap-stanford/distance-encoding) | Distance Encoding for GNN Design | `master` | MIT | false | `2021-03-20T22:00:33Z` | `2026-05-11T08:58:09Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`GIB`](https://github.com/snap-stanford/GIB) | Graph Information Bottleneck (GIB) for learning minimal sufficient structural and feature information using GNNs | `master` | MIT | false | `2022-11-29T05:51:44Z` | `2026-07-17T02:21:14Z` | `graph-neural-networks`, `information-bottleneck`, `node-classification`, `representation-learning`, `robustness` | `N/A*` | **LOW_RELEVANCE** |
| [`covid-mobility`](https://github.com/snap-stanford/covid-mobility) | — | `master` | LICENSE_UNCLEAR | false | `2020-11-15T02:07:48Z` | `2026-08-12T19:20:36Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`neural-subgraph-learning-GNN`](https://github.com/snap-stanford/neural-subgraph-learning-GNN) | — | `master` | LICENSE_UNCLEAR | false | `2024-06-25T05:22:07Z` | `2026-07-01T19:33:37Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`comet`](https://github.com/snap-stanford/comet) | [ICLR 2021] Concept Learners for Few-Shot Learning | `master` | NOASSERTION | false | `2023-06-06T17:43:56Z` | `2025-01-29T13:22:33Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`GraphGym`](https://github.com/snap-stanford/GraphGym) | Platform for designing and evaluating Graph Neural Networks (GNN) | `master` | NOASSERTION | false | `2023-11-10T05:37:18Z` | `2026-08-22T10:58:27Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`KGReasoning`](https://github.com/snap-stanford/KGReasoning) | Multi-Hop Logical Reasoning in Knowledge Graphs | `main` | MIT | false | `2022-03-27T20:05:19Z` | `2026-07-09T20:24:57Z` | `embedding`, `knowledge-base`, `knowledge-graph`, `reasoning` | `N/A*` | **LOW_RELEVANCE** |
| [`CAW`](https://github.com/snap-stanford/CAW) | — | `master` | MIT | false | `2022-09-27T15:19:06Z` | `2026-05-11T14:02:09Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`crust`](https://github.com/snap-stanford/crust) | [NeurIPS 2020] Coresets for Robust Training of Neural Networks against Noisy Labels | `master` | MIT | false | `2021-05-02T09:11:25Z` | `2026-03-12T11:24:57Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`F-FADE`](https://github.com/snap-stanford/F-FADE) | — | `master` | LICENSE_UNCLEAR | false | `2021-01-12T14:59:41Z` | `2026-05-18T11:44:10Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`covid-mobility-tool`](https://github.com/snap-stanford/covid-mobility-tool) | — | `main` | LICENSE_UNCLEAR | false | `2021-02-20T19:47:05Z` | `2026-06-11T02:38:45Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`lego`](https://github.com/snap-stanford/lego) | — | `main` | LICENSE_UNCLEAR | false | `2021-06-09T06:31:14Z` | `2022-06-23T03:23:49Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`stellar`](https://github.com/snap-stanford/stellar) | — | `main` | MIT | false | `2023-01-18T13:47:42Z` | `2026-07-30T02:25:39Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`ConE`](https://github.com/snap-stanford/ConE) | — | `main` | MIT | false | `2021-11-03T03:08:23Z` | `2026-03-27T13:45:23Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`GreaseLM`](https://github.com/snap-stanford/GreaseLM) | [ICLR 2022 spotlight]GreaseLM: Graph REASoning Enhanced Language Models for Question Answering | `main` | MIT | false | `2025-04-23T23:52:08Z` | `2026-05-06T14:12:01Z` | `biomedical-ques`, `commonsense-reasoning`, `graph-neural-networks`, `knowledge-graph`, `language-model`, `question-answering` | `N/A*` | **HIGH_RELEVANCE** |
| [`GEARS`](https://github.com/snap-stanford/GEARS) | GEARS is a geometric deep learning model that predicts outcomes of novel multi-gene perturbations | `master` | MIT | false | `2025-02-01T09:35:37Z` | `2026-08-18T07:39:27Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`orca`](https://github.com/snap-stanford/orca) | [ICLR 2022] Open-World Semi-Supervised Learning | `main` | LICENSE_UNCLEAR | false | `2022-02-17T04:35:15Z` | `2026-07-17T17:39:02Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`bc-emb`](https://github.com/snap-stanford/bc-emb) | — | `main` | LICENSE_UNCLEAR | false | `2022-06-27T16:11:59Z` | `2026-03-20T06:55:40Z` | — | `N/A*` | **IRRELEVANT** |
| [`GNN-reading-group`](https://github.com/snap-stanford/GNN-reading-group) | — | `main` | LICENSE_UNCLEAR | false | `2022-09-27T21:45:59Z` | `2025-05-28T00:59:37Z` | — | `N/A*` | **IRRELEVANT** |
| [`roland`](https://github.com/snap-stanford/roland) | — | `master` | NOASSERTION | false | `2023-11-05T12:02:24Z` | `2026-05-25T15:18:00Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`covid-spillovers`](https://github.com/snap-stanford/covid-spillovers) | — | `main` | LICENSE_UNCLEAR | false | `2022-12-14T17:24:30Z` | `2025-02-09T02:14:44Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`le_pde`](https://github.com/snap-stanford/le_pde) | LE-PDE accelerates PDEs' forward simulation and inverse optimization via latent global evolution, achieving significant speedup with SOTA accuracy | `master` | MIT | false | `2024-01-30T14:29:46Z` | `2026-07-23T02:22:25Z` | `accelerate`, `deep-learning`, `inverse-optimization`, `latent-space`, `pde`, `surrogate-models` | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`zeroc`](https://github.com/snap-stanford/zeroc) | ZeroC is a neuro-symbolic method that trained with elementary visual concepts and relations, can zero-shot recognize and acquire more complex, hierarchical concepts, even across domains | `master` | MIT | false | `2023-05-08T23:06:13Z` | `2025-12-01T03:51:38Z` | `concept-learning`, `energy-based-model`, `generalization`, `hierarchical`, `neuro-symbolic`, `zero-shot-learning` | `N/A*` | **LOW_RELEVANCE** |
| [`ViRel`](https://github.com/snap-stanford/ViRel) | ViRel: Unsupervised Visual Relations Discovery with Graph-level Analogy | `master` | LICENSE_UNCLEAR | false | `2024-08-10T04:22:11Z` | `2026-07-21T20:53:48Z` | `graph`, `graph-neural-networks`, `machine-learning`, `reasoning`, `representation-learning`, `unsupervised-learning` | `N/A*` | **LOW_RELEVANCE** |
| [`csr`](https://github.com/snap-stanford/csr) | — | `main` | Apache-2.0 | false | `2023-07-06T16:57:12Z` | `2026-05-29T11:14:59Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`tuneup`](https://github.com/snap-stanford/tuneup) | — | `main` | LICENSE_UNCLEAR | false | `2023-11-04T03:39:25Z` | `2023-11-04T03:24:37Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`SATURN`](https://github.com/snap-stanford/SATURN) | — | `main` | MIT | false | `2024-07-03T02:00:59Z` | `2026-08-19T11:30:33Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`lamp`](https://github.com/snap-stanford/lamp) | [ICLR23] First deep learning-based surrogate model that jointly learns the evolution model and optimizes computational cost via remeshing | `master` | MIT | false | `2024-01-30T14:29:08Z` | `2025-12-09T15:35:26Z` | `controllable`, `learned-simulation`, `mesh-based`, `multi-resolution`, `physics-simulation`, `reinforcement-learning` | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`med-flamingo`](https://github.com/snap-stanford/med-flamingo) | — | `master` | LICENSE_UNCLEAR | false | `2023-08-23T18:03:37Z` | `2026-08-14T00:03:23Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`planet`](https://github.com/snap-stanford/planet) | PlaNet: Predicting population response to drugs via clinical knowledge graph | `main` | MIT | false | `2025-03-13T22:22:56Z` | `2026-03-17T16:30:07Z` | `biomedicine`, `graph-neural-networks`, `knowledge-graph`, `language-model` | `N/A*` | **HIGH_RELEVANCE** |
| [`supply-chains`](https://github.com/snap-stanford/supply-chains) | — | `tgb` | LICENSE_UNCLEAR | false | `2025-02-25T23:16:59Z` | `2026-08-20T05:19:15Z` | — | `N/A*` | **IRRELEVANT** |
| [`prodigy`](https://github.com/snap-stanford/prodigy) | — | `main` | LICENSE_UNCLEAR | false | `2023-07-12T23:16:37Z` | `2026-07-16T07:10:16Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`llm-social-network`](https://github.com/snap-stanford/llm-social-network) | — | `agent` | LICENSE_UNCLEAR | false | `2025-06-30T19:55:02Z` | `2026-08-10T03:07:50Z` | — | `N/A*` | **IRRELEVANT** |
| [`ipf-network-inference`](https://github.com/snap-stanford/ipf-network-inference) | — | `master` | LICENSE_UNCLEAR | false | `2024-06-18T18:14:24Z` | `2024-06-18T18:14:27Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`exposure-segregation`](https://github.com/snap-stanford/exposure-segregation) | — | `main` | LICENSE_UNCLEAR | false | `2023-11-28T20:36:37Z` | `2026-02-24T15:09:56Z` | — | `N/A*` | **IRRELEVANT** |
| [`MLAgentBench`](https://github.com/snap-stanford/MLAgentBench) | — | `main` | MIT | false | `2024-06-19T13:53:23Z` | `2026-08-12T00:46:41Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`conformalized-gnn`](https://github.com/snap-stanford/conformalized-gnn) | Uncertainty Quantification over Graph with Conformalized Graph Neural Networks (NeurIPS 2023) | `master` | LICENSE_UNCLEAR | false | `2023-09-27T00:58:55Z` | `2026-07-10T18:29:00Z` | `calibration`, `conformal-prediction`, `gnn`, `graph`, `graph-neural-networks`, `uncertainty-quantification` | `N/A*` | **LOW_RELEVANCE** |
| [`UCE`](https://github.com/snap-stanford/UCE) | UCE is a zero-shot foundation model for single-cell gene expression data | `main` | MIT | false | `2026-07-08T17:49:55Z` | `2026-08-21T17:19:28Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`plato`](https://github.com/snap-stanford/plato) | — | `main` | MIT | false | `2024-03-22T06:17:10Z` | `2026-03-08T23:39:43Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`AutoTransfer`](https://github.com/snap-stanford/AutoTransfer) | — | `main` | NOASSERTION | false | `2024-01-29T00:42:06Z` | `2026-01-22T05:19:13Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`caml`](https://github.com/snap-stanford/caml) | — | `main` | LICENSE_UNCLEAR | false | `2024-01-23T00:48:38Z` | `2026-05-12T16:17:21Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`UCE_decoder`](https://github.com/snap-stanford/UCE_decoder) | — | `main` | LICENSE_UNCLEAR | false | `2024-02-02T20:54:42Z` | `2024-02-02T20:52:02Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`BioDiscoveryAgent`](https://github.com/snap-stanford/BioDiscoveryAgent) | BioDiscoveryAgent is an LLM-based AI agent for closed-loop design of genetic perturbation experiments | `master` | MIT | false | `2025-07-06T20:16:52Z` | `2026-08-19T04:53:56Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`stark`](https://github.com/snap-stanford/stark) | (NeurIPS D&B 2024) STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases  | `main` | MIT | false | `2026-02-06T06:08:54Z` | `2026-08-07T20:17:09Z` | `graph`, `information-retrieval`, `knowledge-base`, `llm`, `multimodal`, `nlp`, `semi-structured-data` | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`KGWAS`](https://github.com/snap-stanford/KGWAS) | KGWAS: novel genetics discovery enabled by massive functional genomics knowledge graph | `master` | MIT | false | `2025-03-07T06:09:48Z` | `2026-02-16T11:02:10Z` | `ai`, `functional-genomics`, `genetics`, `knowledge-graph` | `N/A*` | **HIGH_RELEVANCE** |
| [`relbench-user-study`](https://github.com/snap-stanford/relbench-user-study) | — | `main` | LICENSE_UNCLEAR | false | `2024-08-07T23:01:04Z` | `2026-04-29T02:41:32Z` | — | `N/A*` | **IRRELEVANT** |
| [`precice`](https://github.com/snap-stanford/precice) | — | `main` | LICENSE_UNCLEAR | false | `2026-01-26T13:20:56Z` | `2026-02-16T11:01:34Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`POPPER`](https://github.com/snap-stanford/POPPER) | Automated Hypothesis Testing with Agentic Sequential Falsifications | `main` | LICENSE_UNCLEAR | false | `2025-05-14T03:19:14Z` | `2026-08-18T03:35:04Z` | `agent`, `ai-for-science`, `hypothesis-testing`, `llm` | `N/A*` | **HIGH_RELEVANCE** |
| [`Biomni`](https://github.com/snap-stanford/Biomni) | Biomni: a general-purpose biomedical AI agent | `main` | Apache-2.0 | false | `2026-08-17T19:17:40Z` | `2026-08-22T19:35:41Z` | `agent`, `ai`, `biomedicine` | `N/A*` | **HIGH_RELEVANCE** |
| [`relgt`](https://github.com/snap-stanford/relgt) | Relational Graph Transformer | `main` | MIT | false | `2025-07-10T16:16:41Z` | `2026-08-01T16:29:39Z` | `graph-neural-networks`, `graph-transformer`, `relational-databases`, `relational-deep-learning`, `transformers` | `N/A*` | **LOW_RELEVANCE** |
| [`stage-gnn`](https://github.com/snap-stanford/stage-gnn) | — | `master` | MIT | false | `2025-06-12T01:38:19Z` | `2026-07-23T02:39:53Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`RelGNN`](https://github.com/snap-stanford/RelGNN) | [ICML 2025] RelGNN: Composite Message Passing for Relational Deep Learning | `main` | MIT | false | `2025-06-12T19:09:17Z` | `2026-07-17T02:16:21Z` | — | `N/A*` | **LOW_RELEVANCE** |
| [`optimas`](https://github.com/snap-stanford/optimas) | (ICLR 2026) Optimas: Optimizing Compound AI Systems | `main` | Apache-2.0 | false | `2026-02-06T06:12:06Z` | `2026-07-21T19:11:08Z` | `compound-ai-systems`, `multiagent-systems`, `optimization`, `reward-learning` | `N/A*` | **POSSIBLE_RELEVANCE** |
| [`PULSAR`](https://github.com/snap-stanford/PULSAR) | PULSAR: a Foundation Model for Multi-scale and Multicellular Biology | `main` | MIT | false | `2026-03-01T00:07:34Z` | `2026-08-14T14:01:34Z` | `ai`, `foundation-models`, `genetics`, `single-cell`, `virtual-cell` | `N/A*` | **HIGH_RELEVANCE** |
| [`UCE-brain`](https://github.com/snap-stanford/UCE-brain) | — | `main` | LICENSE_UNCLEAR | false | `2026-05-26T23:09:58Z` | `2026-07-13T23:39:27Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`perturb-hd`](https://github.com/snap-stanford/perturb-hd) | — | `main` | LICENSE_UNCLEAR | false | `2026-05-01T22:38:54Z` | `2026-07-17T12:57:16Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`snap-skills`](https://github.com/snap-stanford/snap-skills) | — | `main` | LICENSE_UNCLEAR | false | `2026-07-30T20:11:50Z` | `2026-07-30T20:12:38Z` | — | `N/A*` | **HIGH_RELEVANCE** |
| [`memorilla`](https://github.com/snap-stanford/memorilla) | — | `main` | LICENSE_UNCLEAR | false | `2026-08-11T05:03:40Z` | `2026-08-11T05:03:43Z` | — | `N/A*` | **POSSIBLE_RELEVANCE** |

`N/A*`: latest release was not collected. It is not included in the organization-list REST payload, and no authenticated GitHub GraphQL/CLI batch route was available in this environment. The value means “not batch-accessible in this collection,” not “no release exists.” `LICENSE_UNCLEAR` means the API returned a null license object; `NOASSERTION` is GitHub’s returned SPDX value and is not treated as affirmative reuse permission.

## Relevance evidence and interpretation

Direct HIGH triggers visible in official metadata include single-cell/cell-type work (`mars`, `UCE`, `PULSAR`), interactome/genomics/genetics and perturbation (`multiscale-interactome`, `GEARS`, `KGWAS`, `BioDiscoveryAgent`, `perturb-hd`), biomedical/clinical/drug systems (`GreaseLM`, `med-flamingo`, `planet`, `Biomni`), and scientific-agent/benchmark/skills capabilities (`MLAgentBench`, `POPPER`, `snap-skills`). `UCE_decoder` and `UCE-brain` are retained HIGH by their explicit UCE lineage/name, but their missing descriptions make that inference weaker than the description-backed entries.

The 28 POSSIBLE entries should not be promoted based on organization proximity. Several have no description or topics; others are general benchmarks, graph infrastructure, COVID/public-health analyses, or scientific simulation whose independent Biomni value requires a bounded README/code-surface screen. LOW and IRRELEVANT entries remain inventoried for coverage and are not deep-audit recommendations.

## Public member entities

Only the public GitHub username and profile URL are recorded. No real-name or institutional identity mapping is inferred.

| GitHub username | Public profile |
|---|---|
| `abhisg` | https://github.com/abhisg |
| `agrimgupta92` | https://github.com/agrimgupta92 |
| `markulrich` | https://github.com/markulrich |
| `mbrbic` | https://github.com/mbrbic |
| `michiyasunaga` | https://github.com/michiyasunaga |
| `nihit` | https://github.com/nihit |

## Evidence

- Repository inventory: https://api.github.com/orgs/snap-stanford/repos?type=all&per_page=100&page=1
- Public-member inventory: https://api.github.com/orgs/snap-stanford/members?per_page=100&page=1
- Repository evidence fields used: `name`, `html_url`, `description`, `default_branch`, `license.spdx_id`, `archived`, `pushed_at`, `updated_at`, and `topics`.
- Response evidence: both endpoints returned HTTP 200; captured response headers contained no pagination `Link` header.
- Observation time applies to both endpoint results: `2026-08-22T20:36:48Z`.

## Uncertainties and limitations

- Public GitHub endpoints cannot reveal private repositories or hidden organization membership.
- Metadata-only screening cannot establish code capability, runtime correctness, feature uniqueness, lineage, dependency burden, security, or component-level licensing.
- GitHub repository `updated_at` may reflect non-code events; `pushed_at` is not a verified latest-commit SHA/date.
- Repositories with missing descriptions/topics, especially POSSIBLE entries, require bounded README inspection before promotion or demotion.
- Latest release is unknown for every repository in this batch for the batch-accessibility reason stated above.
- Repository and member inventories are time-dependent; “all” means all publicly returned entries under the documented queries at the observation time.

## Next actions

1. Parent coordinator verifies and normalizes these provisional entities into canonical records and assigns IDs.
2. Deep-audit the 17 HIGH_RELEVANCE repositories only after canonical prioritization/deduplication; start with description-backed direct biomedical/scientific-agent matches.
3. Perform a bounded README-level disambiguation pass on the 28 POSSIBLE_RELEVANCE repositories, especially missing-description entries, before deciding whether any enter deep audit.
4. Treat the six usernames only as repository-discovery entry points under `person_depth = 1`; do not infer identity or expand through their collaborators.
