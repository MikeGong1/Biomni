# Public Repository Inventory for Code-visible People — Batch 002

Parent verification: `VERIFIED`. Scope: the next 10 canonical GitHub User
accounts in stable Person-ID order (`person-github-000011`–`000020`).

Thirteen serialized, error-free GraphQL responses returned all 587 public owner
repositories. HasanAldhahi, HelloWorldLTY, and jucor required and completed second
pages; every final `hasNextPage` is false and combined node counts equal each
account's `totalCount`. Heavier paired requests, two transient single-user 502s,
one TLS transport failure, and two parser-rejected page-2 requests were discarded;
only the recovered successful responses enter evidence. Requests remained queued
with two-second spacing. No repository content or third-party code was executed.

## Coverage

| Person ID | Login | Public repositories | Existing IDs | New IDs | High | Possible | Low | Irrelevant | Cursor |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| person-github-000011 | Edison-A-N | 49 | 1 | 48 | 8 | 17 | 9 | 15 | exhausted |
| person-github-000012 | evolu8 | 40 | 1 | 39 | 3 | 2 | 21 | 14 | exhausted |
| person-github-000013 | ginylil-tech | 2 | 0 | 2 | 0 | 0 | 1 | 1 | exhausted |
| person-github-000014 | HasanAldhahi | 157 | 1 | 156 | 7 | 8 | 26 | 116 | exhausted |
| person-github-000015 | HelloWorldLTY | 129 | 1 | 128 | 73 | 29 | 12 | 15 | exhausted |
| person-github-000016 | igor-sadalski | 5 | 1 | 4 | 1 | 2 | 1 | 1 | exhausted |
| person-github-000017 | jucor | 102 | 1 | 101 | 11 | 14 | 30 | 47 | exhausted |
| person-github-000018 | kexinhuang12345 | 43 | 0 | 43 | 15 | 6 | 10 | 12 | exhausted |
| person-github-000019 | kuanlinhuang | 30 | 0 | 30 | 19 | 7 | 3 | 1 | exhausted |
| person-github-000020 | lxasqjc | 30 | 1 | 29 | 6 | 7 | 8 | 9 | exhausted |
| **Total** | **10 accounts** | **587** | **7** | **580** | **143** | **92** | **121** | **231** | **exhausted** |

The seven overlaps are the existing Biomni forks owned by Edison-A-N, evolu8,
HasanAldhahi, HelloWorldLTY, igor-sadalski, jucor, and lxasqjc. Their canonical
IDs are reused; no duplicate repository entity was allocated. The 580 new
repositories use the contiguous range `repo-001001`–`repo-001580`.

## Metadata screening

This remains breadth-first metadata screening. HIGH requires explicit biomedical,
biological, omics, genetics, clinical, drug, scientific-agent, MCP, Skills,
scientific benchmark, or directly matching scientific-infrastructure metadata.
POSSIBLE preserves ambiguous adjacent repositories for README checks. Generic
ML/NLP/graph infrastructure is LOW without a domain signal; clearly unrelated
sites, tutorials, games, and utilities are IRRELEVANT.

Direct HIGH signals include MCP frameworks and inspection/adaptation tools;
EczemaNet and cardiac segmentation; Biomni variants and deployment; drug-
discovery and mental-health surfaces; extensive single-cell, spatial, multi-omics,
DNA/RNA foundation-model and perturbation repositories; scientific agents and
benchmarks; and known SNAP biomedical ecosystems. HIGH is only a deep-audit
queue—not proof of unique capability, integration value, maturity, license
fitness, or runtime correctness.

Metadata aggregate: 398 forks and 189 source repositories; two archived and none
disabled; 11 expose a latest release; 252 have no affirmative SPDX license object
and 123 return `NOASSERTION`. The 92 POSSIBLE repositories remain a bounded
README-disambiguation queue. Repository topics were complete: no
`topics_total` exceeded the returned node count.

## Repository ledger

| Repository ID | Repository | Form | Language | Code license | Last push | Relevance |
|---|---|---|---|---|---|---|
| repo-001001 | Edison-A-N/1806 | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2018-12-20 | IRRELEVANT |
| repo-001002 | Edison-A-N/adk-python | fork | Python | Apache-2.0 | 2026-01-02 | POSSIBLE_RELEVANCE |
| repo-001003 | Edison-A-N/agent-garden | source | Python | MIT | 2025-11-30 | POSSIBLE_RELEVANCE |
| repo-001004 | Edison-A-N/agentmemory | fork | TypeScript | Apache-2.0 | 2026-05-09 | POSSIBLE_RELEVANCE |
| repo-001005 | Edison-A-N/ai-directories | fork | — | MIT | 2026-04-22 | IRRELEVANT |
| repo-001006 | Edison-A-N/autogen | fork | Python | CC-BY-4.0 | 2025-10-08 | POSSIBLE_RELEVANCE |
| repo-001007 | Edison-A-N/awesome-distributed-systems | fork | — | LICENSE_UNCLEAR | 2016-06-25 | LOW_RELEVANCE |
| repo-001008 | Edison-A-N/awesome-opencode | fork | JavaScript | CC0-1.0 | 2026-04-11 | POSSIBLE_RELEVANCE |
| repo-001009 | Edison-A-N/Best-README-Template | fork | — | MIT | 2020-10-06 | IRRELEVANT |
| repo-000565 | Edison-A-N/Biomni | fork | Python | Apache-2.0 | 2026-01-29 | HIGH_RELEVANCE |
| repo-001010 | Edison-A-N/Blog | source | — | LICENSE_UNCLEAR | 2021-02-01 | IRRELEVANT |
| repo-001011 | Edison-A-N/chatroom_network | source | Python | Apache-2.0 | 2025-12-28 | IRRELEVANT |
| repo-001012 | Edison-A-N/chinese-copywriting-formatter | source | TypeScript | LICENSE_UNCLEAR | 2023-09-14 | IRRELEVANT |
| repo-001013 | Edison-A-N/cursor-controller-skill | source | — | MIT | 2026-03-06 | HIGH_RELEVANCE |
| repo-001014 | Edison-A-N/deepagents-e2b | source | Python | MIT | 2026-05-18 | POSSIBLE_RELEVANCE |
| repo-001015 | Edison-A-N/DeepLearning-500-questions | fork | — | LICENSE_UNCLEAR | 2018-10-30 | IRRELEVANT |
| repo-001016 | Edison-A-N/django-orm-adapter | fork | Python | Apache-2.0 | 2021-05-20 | LOW_RELEVANCE |
| repo-001017 | Edison-A-N/django-storages | fork | Python | BSD-3-Clause | 2021-07-28 | LOW_RELEVANCE |
| repo-001018 | Edison-A-N/Edison-A-N | source | — | LICENSE_UNCLEAR | 2026-01-01 | IRRELEVANT |
| repo-001019 | Edison-A-N/Edison-A-N.github.io | source | — | LICENSE_UNCLEAR | 2026-06-02 | IRRELEVANT |
| repo-001020 | Edison-A-N/fastapi_mcp | fork | Python | MIT | 2025-10-21 | HIGH_RELEVANCE |
| repo-001021 | Edison-A-N/fastmcp | fork | Python | Apache-2.0 | 2025-10-20 | HIGH_RELEVANCE |
| repo-001022 | Edison-A-N/go-ddd | source | — | Apache-2.0 | 2022-08-31 | LOW_RELEVANCE |
| repo-001023 | Edison-A-N/go-ddd-kit | source | — | LICENSE_UNCLEAR | 2022-12-20 | LOW_RELEVANCE |
| repo-001024 | Edison-A-N/google.github.io | fork | HTML | LICENSE_UNCLEAR | 2018-09-18 | IRRELEVANT |
| repo-001025 | Edison-A-N/inspector | fork | TypeScript | MIT | 2026-02-07 | HIGH_RELEVANCE |
| repo-001026 | Edison-A-N/investment-research-os | source | Python | LICENSE_UNCLEAR | 2026-03-21 | IRRELEVANT |
| repo-001027 | Edison-A-N/KnowledgeGraphCourse | fork | — | LICENSE_UNCLEAR | 2020-06-24 | LOW_RELEVANCE |
| repo-001028 | Edison-A-N/langfuse-mcp | fork | Python | MIT | 2026-06-24 | HIGH_RELEVANCE |
| repo-001029 | Edison-A-N/langfuse-python | fork | Python | MIT | 2026-06-03 | POSSIBLE_RELEVANCE |
| repo-001030 | Edison-A-N/langgraph | fork | Python | MIT | 2025-12-31 | POSSIBLE_RELEVANCE |
| repo-001031 | Edison-A-N/lihang-code | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2018-12-17 | IRRELEVANT |
| repo-001032 | Edison-A-N/mcp-garden | source | Python | MIT | 2025-11-20 | HIGH_RELEVANCE |
| repo-001033 | Edison-A-N/mcpadapt | fork | Python | MIT | 2025-10-25 | HIGH_RELEVANCE |
| repo-001034 | Edison-A-N/my-page | source | TypeScript | LICENSE_UNCLEAR | 2024-08-03 | IRRELEVANT |
| repo-001035 | Edison-A-N/openagents | fork | Python | Apache-2.0 | 2026-06-19 | POSSIBLE_RELEVANCE |
| repo-001036 | Edison-A-N/opencode | fork | TypeScript | MIT | 2026-06-23 | POSSIBLE_RELEVANCE |
| repo-001037 | Edison-A-N/opencode-agent-memory | fork | TypeScript | MIT | 2026-03-21 | POSSIBLE_RELEVANCE |
| repo-001038 | Edison-A-N/opencode-preview | source | TypeScript | MIT | 2026-05-27 | POSSIBLE_RELEVANCE |
| repo-001039 | Edison-A-N/opencode-stat | source | TypeScript | LICENSE_UNCLEAR | 2026-07-06 | POSSIBLE_RELEVANCE |
| repo-001040 | Edison-A-N/opencode-worktree-memory-sync | source | TypeScript | MIT | 2026-03-20 | POSSIBLE_RELEVANCE |
| repo-001041 | Edison-A-N/OpenManus | fork | Python | MIT | 2025-09-07 | POSSIBLE_RELEVANCE |
| repo-001042 | Edison-A-N/patent_downloader | source | Python | MIT | 2026-04-03 | IRRELEVANT |
| repo-001043 | Edison-A-N/picoclaw | fork | Go | NOASSERTION | 2026-02-27 | POSSIBLE_RELEVANCE |
| repo-001044 | Edison-A-N/resumeCopy2S3 | source | — | LICENSE_UNCLEAR | 2019-06-20 | LOW_RELEVANCE |
| repo-001045 | Edison-A-N/smolagents | fork | Python | Apache-2.0 | 2025-10-28 | POSSIBLE_RELEVANCE |
| repo-001046 | Edison-A-N/SU4MLC | fork | Python | LICENSE_UNCLEAR | 2018-11-06 | LOW_RELEVANCE |
| repo-001047 | Edison-A-N/TensorFlow-Course | fork | Python | MIT | 2019-01-03 | IRRELEVANT |
| repo-001048 | Edison-A-N/tinykv | fork | Go | Apache-2.0 | 2022-12-30 | LOW_RELEVANCE |
| repo-001049 | evolu8/appscale | fork | Python | NOASSERTION | 2012-11-10 | LOW_RELEVANCE |
| repo-001050 | evolu8/appscale-tools | fork | Ruby | NOASSERTION | 2012-10-24 | LOW_RELEVANCE |
| repo-001051 | evolu8/asgard | fork | Groovy | LICENSE_UNCLEAR | 2012-06-25 | LOW_RELEVANCE |
| repo-001052 | evolu8/BEGAN-tensorflow | fork | Python | LICENSE_UNCLEAR | 2017-04-09 | LOW_RELEVANCE |
| repo-000569 | evolu8/Biomni | fork | Python | Apache-2.0 | 2025-07-27 | HIGH_RELEVANCE |
| repo-001053 | evolu8/BluetoothSerial | fork | Objective-C | NOASSERTION | 2014-11-12 | IRRELEVANT |
| repo-001054 | evolu8/bootcamp | fork | JavaScript | MIT | 2014-07-06 | IRRELEVANT |
| repo-001055 | evolu8/brain | fork | JavaScript | MIT | 2014-07-21 | LOW_RELEVANCE |
| repo-001056 | evolu8/CanvasCameraPlugin | fork | Objective-C | LICENSE_UNCLEAR | 2014-10-01 | IRRELEVANT |
| repo-001057 | evolu8/CapsNet-Keras | fork | Python | MIT | 2018-08-27 | LOW_RELEVANCE |
| repo-001058 | evolu8/chroma.js | fork | CoffeeScript | NOASSERTION | 2014-10-21 | IRRELEVANT |
| repo-001059 | evolu8/convnetjs | fork | JavaScript | MIT | 2014-06-30 | LOW_RELEVANCE |
| repo-001060 | evolu8/DeepBeliefSDK | fork | C++ | NOASSERTION | 2014-08-13 | LOW_RELEVANCE |
| repo-001061 | evolu8/EczemaNet | fork | Python | NOASSERTION | 2020-08-17 | HIGH_RELEVANCE |
| repo-001062 | evolu8/gdbn | fork | Python | NOASSERTION | 2014-06-20 | LOW_RELEVANCE |
| repo-001063 | evolu8/guided-diffusion | fork | Python | MIT | 2021-11-08 | LOW_RELEVANCE |
| repo-001064 | evolu8/IntuitNet | source | Jupyter Notebook | MIT | 2020-12-18 | POSSIBLE_RELEVANCE |
| repo-001065 | evolu8/Js2Py | fork | Python | LICENSE_UNCLEAR | 2014-12-12 | IRRELEVANT |
| repo-001066 | evolu8/jsfeat | fork | JavaScript | MIT | 2014-09-14 | LOW_RELEVANCE |
| repo-001067 | evolu8/macOS-eGPU | fork | Shell | NOASSERTION | 2019-05-17 | IRRELEVANT |
| repo-001068 | evolu8/neurolab | fork | Python | LICENSE_UNCLEAR | 2013-04-16 | LOW_RELEVANCE |
| repo-001069 | evolu8/nnet | fork | Python | MIT | 2014-09-11 | LOW_RELEVANCE |
| repo-001070 | evolu8/nnsandbox | fork | Python | LICENSE_UNCLEAR | 2013-05-24 | LOW_RELEVANCE |
| repo-001071 | evolu8/pix2pix-tensorflow | fork | Python | MIT | 2017-03-01 | LOW_RELEVANCE |
| repo-001072 | evolu8/plotform | source | — | LICENSE_UNCLEAR | 2017-01-27 | POSSIBLE_RELEVANCE |
| repo-001073 | evolu8/Repeat-after-you | source | — | MIT | 2026-05-30 | IRRELEVANT |
| repo-001074 | evolu8/sample-apps | fork | JavaScript | LICENSE_UNCLEAR | 2014-03-25 | IRRELEVANT |
| repo-001075 | evolu8/SegCaps | fork | Jupyter Notebook | Apache-2.0 | 2018-08-28 | LOW_RELEVANCE |
| repo-001076 | evolu8/seqwin | source | JavaScript | LICENSE_UNCLEAR | 2014-11-12 | IRRELEVANT |
| repo-001077 | evolu8/speech2gesture | fork | Python | LICENSE_UNCLEAR | 2019-08-01 | LOW_RELEVANCE |
| repo-001078 | evolu8/SpeechRecognizer | fork | Java | LICENSE_UNCLEAR | 2014-03-03 | IRRELEVANT |
| repo-001079 | evolu8/SweepNet | fork | Jupyter Notebook | MIT | 2017-11-22 | HIGH_RELEVANCE |
| repo-001080 | evolu8/TF-Vision-Lab | fork | Python | Apache-2.0 | 2018-10-01 | LOW_RELEVANCE |
| repo-001081 | evolu8/tfjs-react-seed | fork | JavaScript | LICENSE_UNCLEAR | 2018-06-14 | IRRELEVANT |
| repo-001082 | evolu8/togetherjs | fork | JavaScript | MPL-2.0 | 2014-07-01 | IRRELEVANT |
| repo-001083 | evolu8/tornado | fork | Python | Apache-2.0 | 2016-05-15 | LOW_RELEVANCE |
| repo-001084 | evolu8/WCT2 | fork | Python | MIT | 2019-10-28 | LOW_RELEVANCE |
| repo-001085 | evolu8/web-llm | fork | TypeScript | Apache-2.0 | 2026-04-24 | LOW_RELEVANCE |
| repo-001086 | evolu8/wikitude-phonegap | fork | Objective-C | LICENSE_UNCLEAR | 2014-11-10 | IRRELEVANT |
| repo-001087 | evolu8/wikitude-phonegap-samples | fork | JavaScript | LICENSE_UNCLEAR | 2014-10-17 | IRRELEVANT |
| repo-001088 | ginylil-tech/forked-OpenBB | fork | Python | NOASSERTION | 2025-07-17 | LOW_RELEVANCE |
| repo-001089 | ginylil-tech/python-console-snake | source | Python | MIT | 2025-08-29 | IRRELEVANT |
| repo-001090 | HasanAldhahi/agentq_gwdg | source | Python | MIT | 2025-06-28 | POSSIBLE_RELEVANCE |
| repo-001091 | HasanAldhahi/AI_LINKEDIN | source | Python | MIT | 2025-03-06 | IRRELEVANT |
| repo-001092 | HasanAldhahi/anthropic-cookbook | fork | Jupyter Notebook | MIT | 2025-01-23 | LOW_RELEVANCE |
| repo-001093 | HasanAldhahi/apollo_ammonites_lunar_landing_nmadl | fork | Python | LICENSE_UNCLEAR | 2021-08-24 | LOW_RELEVANCE |
| repo-001094 | HasanAldhahi/AssessmentChallengeReactTaskCrystalizeWeb3BootCamp | source | HTML | LICENSE_UNCLEAR | 2022-06-11 | IRRELEVANT |
| repo-001095 | HasanAldhahi/atchekegroup1lunarlanding | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2022-07-18 | LOW_RELEVANCE |
| repo-001096 | HasanAldhahi/awesome-ai-apps-and-agents | fork | Python | LICENSE_UNCLEAR | 2025-04-29 | POSSIBLE_RELEVANCE |
| repo-000563 | HasanAldhahi/Biomni | fork | Python | Apache-2.0 | 2025-07-23 | HIGH_RELEVANCE |
| repo-001097 | HasanAldhahi/biomni_agent | source | Python | Apache-2.0 | 2025-10-05 | HIGH_RELEVANCE |
| repo-001098 | HasanAldhahi/browser-use | fork | Python | MIT | 2024-11-24 | POSSIBLE_RELEVANCE |
| repo-001099 | HasanAldhahi/BurningManGame | source | JavaScript | LICENSE_UNCLEAR | 2022-05-20 | IRRELEVANT |
| repo-001100 | HasanAldhahi/chat-ai | fork | JavaScript | GPL-3.0 | 2026-08-11 | LOW_RELEVANCE |
| repo-001101 | HasanAldhahi/chatbot | source | JavaScript | LICENSE_UNCLEAR | 2024-08-08 | LOW_RELEVANCE |
| repo-001102 | HasanAldhahi/clarus-react | source | JavaScript | LICENSE_UNCLEAR | 2024-05-06 | IRRELEVANT |
| repo-001103 | HasanAldhahi/CLARUS_GNN | source | — | LICENSE_UNCLEAR | 2024-05-13 | LOW_RELEVANCE |
| repo-001104 | HasanAldhahi/cross-precision-llm-deployment-biomni | source | Python | Apache-2.0 | 2026-02-13 | HIGH_RELEVANCE |
| repo-001105 | HasanAldhahi/cv | fork | TypeScript | MIT | 2024-07-11 | IRRELEVANT |
| repo-001106 | HasanAldhahi/data-engineer-handbook | fork | Makefile | LICENSE_UNCLEAR | 2024-11-19 | LOW_RELEVANCE |
| repo-001107 | HasanAldhahi/DATA_FOREST | source | — | LICENSE_UNCLEAR | 2024-06-18 | LOW_RELEVANCE |
| repo-001108 | HasanAldhahi/DeepLearningExercise1 | source | — | LICENSE_UNCLEAR | 2022-10-29 | LOW_RELEVANCE |
| repo-001109 | HasanAldhahi/design_clarus | fork | JavaScript | LICENSE_UNCLEAR | 2022-11-12 | HIGH_RELEVANCE |
| repo-001110 | HasanAldhahi/drug-discovery-platform | source | — | LICENSE_UNCLEAR | 2025-04-01 | HIGH_RELEVANCE |
| repo-001111 | HasanAldhahi/DSA-OOPS-LLD | fork | Java | LICENSE_UNCLEAR | 2024-04-01 | IRRELEVANT |
| repo-001112 | HasanAldhahi/EXS | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2022-08-29 | IRRELEVANT |
| repo-001113 | HasanAldhahi/FLASK | source | — | LICENSE_UNCLEAR | 2021-11-28 | LOW_RELEVANCE |
| repo-001114 | HasanAldhahi/FlaskAPI | source | Python | LICENSE_UNCLEAR | 2021-11-28 | LOW_RELEVANCE |
| repo-001115 | HasanAldhahi/GNN_Counterfactuals | fork | HTML | LICENSE_UNCLEAR | 2023-12-16 | LOW_RELEVANCE |
| repo-001116 | HasanAldhahi/gwdg-ai-agents | source | Shell | LICENSE_UNCLEAR | 2026-04-22 | POSSIBLE_RELEVANCE |
| repo-001117 | HasanAldhahi/Hands-On-Large-Language-Models | fork | Jupyter Notebook | Apache-2.0 | 2025-04-25 | LOW_RELEVANCE |
| repo-001118 | HasanAldhahi/hpda | source | — | LICENSE_UNCLEAR | 2023-01-18 | IRRELEVANT |
| repo-001119 | HasanAldhahi/Launch-down-timer | source | CSS | LICENSE_UNCLEAR | 2021-10-02 | IRRELEVANT |
| repo-001120 | HasanAldhahi/layout_app | fork | TypeScript | LICENSE_UNCLEAR | 2026-02-18 | IRRELEVANT |
| repo-001121 | HasanAldhahi/librechat.ai | fork | MDX | MIT | 2024-12-26 | LOW_RELEVANCE |
| repo-001122 | HasanAldhahi/LiveData-KGE | fork | HTML | MIT | 2023-08-31 | POSSIBLE_RELEVANCE |
| repo-001123 | HasanAldhahi/Madlibs | source | JavaScript | LICENSE_UNCLEAR | 2022-05-17 | IRRELEVANT |
| repo-001124 | HasanAldhahi/my-first-git-assignment | source | — | LICENSE_UNCLEAR | 2022-03-23 | IRRELEVANT |
| repo-001125 | HasanAldhahi/my-repository-example | source | JavaScript | NOASSERTION | 2022-03-23 | IRRELEVANT |
| repo-001126 | HasanAldhahi/Netflix-Whatsapp-replica | source | — | LICENSE_UNCLEAR | 2022-05-20 | IRRELEVANT |
| repo-001127 | HasanAldhahi/nlp_Bert | source | — | LICENSE_UNCLEAR | 2023-09-02 | LOW_RELEVANCE |
| repo-001128 | HasanAldhahi/OpenAI-Reinforcement-Learning-with-Custom-Environment | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2021-01-10 | LOW_RELEVANCE |
| repo-001129 | HasanAldhahi/personal | source | JavaScript | LICENSE_UNCLEAR | 2022-12-20 | IRRELEVANT |
| repo-001130 | HasanAldhahi/phase-0-completing-assignments | fork | JavaScript | NOASSERTION | 2022-03-23 | IRRELEVANT |
| repo-001131 | HasanAldhahi/phase-0-css-fundamentals-lab | fork | HTML | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001132 | HasanAldhahi/phase-0-css-graffiti-lab | fork | CSS | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001133 | HasanAldhahi/phase-0-css-intro-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001134 | HasanAldhahi/phase-0-css-issue-bot-9000 | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001135 | HasanAldhahi/phase-0-css-kitten-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001136 | HasanAldhahi/phase-0-css-rainbow-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001137 | HasanAldhahi/phase-0-git-basics-lab | fork | JavaScript | NOASSERTION | 2022-03-23 | IRRELEVANT |
| repo-001138 | HasanAldhahi/phase-0-html-album-cover-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001139 | HasanAldhahi/phase-0-html-document-structure-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001140 | HasanAldhahi/phase-0-html-experiencing-html-lab | fork | JavaScript | NOASSERTION | 2022-03-23 | IRRELEVANT |
| repo-001141 | HasanAldhahi/phase-0-html-images-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001142 | HasanAldhahi/phase-0-html-issue-bot-9000-lab | fork | HTML | LICENSE_UNCLEAR | 2022-03-24 | IRRELEVANT |
| repo-001143 | HasanAldhahi/phase-0-html-link-tag-with-href | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001144 | HasanAldhahi/phase-0-html-lists-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001145 | HasanAldhahi/phase-0-html-riyadh-blog-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001146 | HasanAldhahi/phase-0-html-tables-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001147 | HasanAldhahi/phase-0-html-tag-lab | fork | JavaScript | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-001148 | HasanAldhahi/phase-0-intro-to-js-2-array-lab | fork | JavaScript | NOASSERTION | 2022-04-06 | IRRELEVANT |
| repo-001149 | HasanAldhahi/phase-0-intro-to-js-2-looping-code-along | fork | JavaScript | NOASSERTION | 2022-04-08 | IRRELEVANT |
| repo-001150 | HasanAldhahi/phase-0-intro-to-js-2-objects-lab | fork | JavaScript | NOASSERTION | 2022-04-07 | IRRELEVANT |
| repo-001151 | HasanAldhahi/phase-0-javascript-events-acting-on-events-lab | fork | JavaScript | NOASSERTION | 2021-12-30 | IRRELEVANT |
| repo-001152 | HasanAldhahi/phase-0-javascript-events-event-listening-lab | fork | JavaScript | NOASSERTION | 2022-06-03 | IRRELEVANT |
| repo-001153 | HasanAldhahi/phase-0-pac-3-arithmetic-lab | fork | JavaScript | NOASSERTION | 2022-04-05 | IRRELEVANT |
| repo-001154 | HasanAldhahi/phase-0-pac-3-function-parameters-lab | fork | JavaScript | NOASSERTION | 2022-04-05 | IRRELEVANT |
| repo-001155 | HasanAldhahi/phase-0-pac-3-intro-to-functions-lab | fork | JavaScript | NOASSERTION | 2022-04-05 | IRRELEVANT |
| repo-001156 | HasanAldhahi/phase-0-pac-3-what-is-a-test | fork | JavaScript | NOASSERTION | 2022-04-04 | IRRELEVANT |
| repo-001157 | HasanAldhahi/phase-0-pac-3-what-is-a-test-lab | fork | JavaScript | NOASSERTION | 2022-04-04 | IRRELEVANT |
| repo-001158 | HasanAldhahi/phase-0-the-dom-editing-lab | fork | JavaScript | NOASSERTION | 2022-06-03 | IRRELEVANT |
| repo-001159 | HasanAldhahi/phase-0-the-dom-modifying-elements-lab | fork | JavaScript | NOASSERTION | 2022-05-12 | IRRELEVANT |
| repo-001160 | HasanAldhahi/phase-1-adding-behavior-with-methods | fork | JavaScript | NOASSERTION | 2022-06-17 | IRRELEVANT |
| repo-001161 | HasanAldhahi/phase-1-algorithms-has-target-sum | fork | JavaScript | NOASSERTION | 2022-06-12 | IRRELEVANT |
| repo-001162 | HasanAldhahi/phase-1-algorithms-has-target-sum-solution | fork | JavaScript | NOASSERTION | 2022-06-12 | IRRELEVANT |
| repo-001163 | HasanAldhahi/phase-1-algorithms-palindrome | fork | JavaScript | NOASSERTION | 2022-06-10 | IRRELEVANT |
| repo-001164 | HasanAldhahi/phase-1-algorithms-palindrome-solution-1 | fork | JavaScript | NOASSERTION | 2022-06-10 | IRRELEVANT |
| repo-001165 | HasanAldhahi/phase-1-algorithms-palindrome-solution-2 | fork | JavaScript | NOASSERTION | 2022-06-10 | IRRELEVANT |
| repo-001166 | HasanAldhahi/phase-1-arithmetic-lab | fork | JavaScript | NOASSERTION | 2022-04-08 | IRRELEVANT |
| repo-001167 | HasanAldhahi/phase-1-array-filter-method-lab | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001168 | HasanAldhahi/phase-1-array-find-method-lab | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001169 | HasanAldhahi/phase-1-array-map-method-lab | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001170 | HasanAldhahi/phase-1-arrow-functions | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001171 | HasanAldhahi/phase-1-class-extension-lab | fork | JavaScript | NOASSERTION | 2022-06-18 | IRRELEVANT |
| repo-001172 | HasanAldhahi/phase-1-constructor-functions-lab | fork | JavaScript | NOASSERTION | 2022-06-18 | IRRELEVANT |
| repo-001173 | HasanAldhahi/phase-1-context-lab | fork | JavaScript | NOASSERTION | 2022-06-12 | IRRELEVANT |
| repo-001174 | HasanAldhahi/phase-1-control-flow-lab | fork | JavaScript | NOASSERTION | 2022-04-07 | IRRELEVANT |
| repo-001175 | HasanAldhahi/phase-1-destructuring-assignment | fork | JavaScript | NOASSERTION | 2022-04-28 | IRRELEVANT |
| repo-001176 | HasanAldhahi/phase-1-domcontentloaded | fork | JavaScript | NOASSERTION | 2022-06-06 | IRRELEVANT |
| repo-001177 | HasanAldhahi/phase-1-fetch-lab | fork | JavaScript | NOASSERTION | 2022-06-04 | IRRELEVANT |
| repo-001178 | HasanAldhahi/phase-1-first-class-functions | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001179 | HasanAldhahi/phase-1-first-class-functions-lab | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001180 | HasanAldhahi/phase-1-functions-lab | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001181 | HasanAldhahi/phase-1-getter-and-setter-methods | fork | JavaScript | NOASSERTION | 2022-06-17 | IRRELEVANT |
| repo-001182 | HasanAldhahi/phase-1-initializing-instances | fork | JavaScript | NOASSERTION | 2022-06-17 | IRRELEVANT |
| repo-001183 | HasanAldhahi/phase-1-intro-to-context | fork | JavaScript | NOASSERTION | 2022-06-18 | IRRELEVANT |
| repo-001184 | HasanAldhahi/phase-1-javascript-functional-library-project | fork | JavaScript | NOASSERTION | 2022-06-12 | IRRELEVANT |
| repo-001185 | HasanAldhahi/phase-1-javascript-functions-continued | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001186 | HasanAldhahi/phase-1-javascript-variables-lab | fork | JavaScript | NOASSERTION | 2022-04-07 | IRRELEVANT |
| repo-001187 | HasanAldhahi/phase-1-js-fetch-on-demand-with-forms | fork | HTML | NOASSERTION | 2022-06-04 | IRRELEVANT |
| repo-001188 | HasanAldhahi/phase-1-object-ball | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001189 | HasanAldhahi/phase-1-object-oriented-methods-lab | fork | JavaScript | NOASSERTION | 2022-06-18 | IRRELEVANT |
| repo-001190 | HasanAldhahi/phase-1-review-strings-lab | fork | JavaScript | NOASSERTION | 2022-04-08 | IRRELEVANT |
| repo-001191 | HasanAldhahi/phase-1-scope-lab | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001192 | HasanAldhahi/phase-1-sending-data-with-fetch | fork | JavaScript | NOASSERTION | 2022-06-10 | IRRELEVANT |
| repo-001193 | HasanAldhahi/phase-1-static-methods-lab | fork | JavaScript | NOASSERTION | 2022-06-18 | IRRELEVANT |
| repo-001194 | HasanAldhahi/phase-1-stitching-together-the-three-pillars | fork | JavaScript | NOASSERTION | 2022-06-06 | IRRELEVANT |
| repo-001195 | HasanAldhahi/phase-1-super-lab | fork | JavaScript | NOASSERTION | 2022-06-18 | IRRELEVANT |
| repo-001196 | HasanAldhahi/phase-1-tasklister-mini-project | fork | HTML | NOASSERTION | 2022-05-23 | IRRELEVANT |
| repo-001197 | HasanAldhahi/phase-1-using-array-reduce | fork | JavaScript | NOASSERTION | 2022-04-23 | IRRELEVANT |
| repo-001198 | HasanAldhahi/phase-1-using-json-server-and-postman | fork | — | NOASSERTION | 2022-06-04 | IRRELEVANT |
| repo-001199 | HasanAldhahi/precourse | fork | Jupyter Notebook | MIT | 2022-01-25 | POSSIBLE_RELEVANCE |
| repo-001200 | HasanAldhahi/RAG | source | — | LICENSE_UNCLEAR | 2024-07-16 | LOW_RELEVANCE |
| repo-001201 | HasanAldhahi/rag-from-scratch | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2024-05-03 | LOW_RELEVANCE |
| repo-001202 | HasanAldhahi/Rag-project | fork | Python | LICENSE_UNCLEAR | 2025-03-19 | LOW_RELEVANCE |
| repo-001203 | HasanAldhahi/RAG2 | source | JavaScript | LICENSE_UNCLEAR | 2024-07-18 | LOW_RELEVANCE |
| repo-001204 | HasanAldhahi/react-hooks-component-props-mini-project | fork | JavaScript | LICENSE_UNCLEAR | 2022-07-17 | IRRELEVANT |
| repo-001205 | HasanAldhahi/react-hooks-components-basics | fork | HTML | NOASSERTION | 2022-05-20 | IRRELEVANT |
| repo-001206 | HasanAldhahi/react-hooks-components-basics-lab | fork | HTML | NOASSERTION | 2022-07-07 | IRRELEVANT |
| repo-001207 | HasanAldhahi/react-hooks-dq-components | source | CSS | LICENSE_UNCLEAR | 2022-06-02 | IRRELEVANT |
| repo-001208 | HasanAldhahi/react-hooks-dq-lifting-state | fork | JavaScript | LICENSE_UNCLEAR | 2021-01-04 | IRRELEVANT |
| repo-001209 | HasanAldhahi/react-hooks-event-handling-lab | fork | JavaScript | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001210 | HasanAldhahi/react-hooks-forms | fork | HTML | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001211 | HasanAldhahi/react-hooks-forms-lab | fork | JavaScript | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001212 | HasanAldhahi/react-hooks-hogwild | fork | JavaScript | LICENSE_UNCLEAR | 2022-07-17 | IRRELEVANT |
| repo-001213 | HasanAldhahi/react-hooks-import-export | fork | HTML | NOASSERTION | 2022-05-20 | IRRELEVANT |
| repo-001214 | HasanAldhahi/react-hooks-import-export-lab | fork | JavaScript | NOASSERTION | 2022-07-07 | IRRELEVANT |
| repo-001215 | HasanAldhahi/react-hooks-information-flow-code-along | fork | CSS | NOASSERTION | 2022-06-03 | IRRELEVANT |
| repo-001216 | HasanAldhahi/react-hooks-information-flow-lab | fork | JavaScript | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001217 | HasanAldhahi/react-hooks-lists-and-keys-lab | fork | JavaScript | NOASSERTION | 2022-07-11 | IRRELEVANT |
| repo-001218 | HasanAldhahi/react-hooks-npm-lab | fork | JavaScript | NOASSERTION | 2022-06-08 | IRRELEVANT |
| repo-001219 | HasanAldhahi/react-hooks-props-basics | fork | HTML | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001220 | HasanAldhahi/react-hooks-props-basics-lab | fork | JavaScript | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001221 | HasanAldhahi/react-hooks-react-app-example | fork | JavaScript | NOASSERTION | 2022-06-08 | IRRELEVANT |
| repo-001222 | HasanAldhahi/react-hooks-react-router-code-along | fork | JavaScript | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001223 | HasanAldhahi/react-hooks-react-router-dynamic-routes | fork | JavaScript | LICENSE_UNCLEAR | 2022-07-17 | IRRELEVANT |
| repo-001224 | HasanAldhahi/react-hooks-react-router-programmatic-navigation | fork | JavaScript | NOASSERTION | 2022-03-11 | IRRELEVANT |
| repo-001225 | HasanAldhahi/react-hooks-react-router-routes-lab | fork | JavaScript | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001226 | HasanAldhahi/react-hooks-running-tests | fork | HTML | LICENSE_UNCLEAR | 2022-06-08 | IRRELEVANT |
| repo-001227 | HasanAldhahi/react-hooks-state-and-events-lab | fork | JavaScript | NOASSERTION | 2022-07-17 | IRRELEVANT |
| repo-001228 | HasanAldhahi/react-hooks-state-events-mini-project | fork | JavaScript | LICENSE_UNCLEAR | 2022-07-17 | IRRELEVANT |
| repo-001229 | HasanAldhahi/react-hooks-state-events-pairing | fork | HTML | LICENSE_UNCLEAR | 2022-02-03 | IRRELEVANT |
| repo-001230 | HasanAldhahi/react-query-1 | fork | JavaScript | LICENSE_UNCLEAR | 2022-06-16 | IRRELEVANT |
| repo-001231 | HasanAldhahi/ReinforcementLearningCourse | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2022-01-22 | LOW_RELEVANCE |
| repo-001232 | HasanAldhahi/Resume-Portfolio-Starter-pack | fork | JavaScript | LICENSE_UNCLEAR | 2025-02-25 | IRRELEVANT |
| repo-001233 | HasanAldhahi/SDE | source | JavaScript | MIT | 2023-12-18 | IRRELEVANT |
| repo-001234 | HasanAldhahi/SDE_Final_Project | source | JavaScript | LICENSE_UNCLEAR | 2024-02-21 | IRRELEVANT |
| repo-001235 | HasanAldhahi/smartcity_task1 | source | Python | MIT | 2024-05-11 | LOW_RELEVANCE |
| repo-001236 | HasanAldhahi/StableBaselinesRL | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2021-03-10 | LOW_RELEVANCE |
| repo-001237 | HasanAldhahi/start-llms | fork | — | MIT | 2024-05-22 | LOW_RELEVANCE |
| repo-001238 | HasanAldhahi/stats-preview-component | source | — | LICENSE_UNCLEAR | 2021-08-08 | IRRELEVANT |
| repo-001239 | HasanAldhahi/Trentino_weather_climate_change | source | — | Apache-2.0 | 2023-10-23 | HIGH_RELEVANCE |
| repo-001240 | HasanAldhahi/tum-traffic-dataset-dev-kit | fork | Python | MIT | 2024-05-02 | HIGH_RELEVANCE |
| repo-001241 | HasanAldhahi/U-KAN | fork | Python | LICENSE_UNCLEAR | 2024-06-06 | POSSIBLE_RELEVANCE |
| repo-001242 | HasanAldhahi/vaping_bad | source | JavaScript | MIT | 2026-06-08 | POSSIBLE_RELEVANCE |
| repo-001243 | HasanAldhahi/weekly | source | Python | LICENSE_UNCLEAR | 2024-12-14 | IRRELEVANT |
| repo-001244 | HasanAldhahi/word-alliance_debug | fork | Python | Apache-2.0 | 2023-09-04 | LOW_RELEVANCE |
| repo-001245 | HasanAldhahi/xAI-Shiny-App | fork | R | LICENSE_UNCLEAR | 2023-02-15 | LOW_RELEVANCE |
| repo-001246 | HelloWorldLTY/ai-deadlines | fork | HTML | MIT | 2021-01-30 | IRRELEVANT |
| repo-001247 | HelloWorldLTY/APPFL | fork | Python | MIT | 2024-02-20 | POSSIBLE_RELEVANCE |
| repo-001248 | HelloWorldLTY/ARIEL | source | Python | LICENSE_UNCLEAR | 2026-06-21 | POSSIBLE_RELEVANCE |
| repo-001249 | HelloWorldLTY/AT-504 | source | Jupyter Notebook | LICENSE_UNCLEAR | 2021-06-25 | IRRELEVANT |
| repo-001250 | HelloWorldLTY/AT-505 | source | Python | MIT | 2021-08-15 | IRRELEVANT |
| repo-001251 | HelloWorldLTY/attention_flow | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2021-09-09 | LOW_RELEVANCE |
| repo-001252 | HelloWorldLTY/autoresearch | fork | Python | LICENSE_UNCLEAR | 2026-03-26 | HIGH_RELEVANCE |
| repo-001253 | HelloWorldLTY/Awesome-Bioinformatics-Papers | source | — | LICENSE_UNCLEAR | 2021-12-14 | HIGH_RELEVANCE |
| repo-001254 | HelloWorldLTY/awesome-deep-learning-single-cell-papers | fork | — | Apache-2.0 | 2023-09-15 | HIGH_RELEVANCE |
| repo-001255 | HelloWorldLTY/Awesome-DNA-Language-Modelling | source | — | LICENSE_UNCLEAR | 2024-09-21 | HIGH_RELEVANCE |
| repo-001256 | HelloWorldLTY/AWGAN | source | Jupyter Notebook | MIT | 2023-02-09 | HIGH_RELEVANCE |
| repo-001257 | HelloWorldLTY/BAITSAO | source | Python | LICENSE_UNCLEAR | 2025-11-17 | HIGH_RELEVANCE |
| repo-001258 | HelloWorldLTY/BEND | fork | Python | BSD-3-Clause | 2024-08-26 | HIGH_RELEVANCE |
| repo-001259 | HelloWorldLTY/BiAE | source | Jupyter Notebook | MIT | 2021-12-13 | HIGH_RELEVANCE |
| repo-001260 | HelloWorldLTY/Bioinfor_researchers_atlas | fork | — | LICENSE_UNCLEAR | 2022-01-02 | HIGH_RELEVANCE |
| repo-000690 | HelloWorldLTY/Biomni | fork | Python | Apache-2.0 | 2025-09-28 | HIGH_RELEVANCE |
| repo-001261 | HelloWorldLTY/brainbridge | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-05-11 | POSSIBLE_RELEVANCE |
| repo-001262 | HelloWorldLTY/CellForge | fork | Python | LICENSE_UNCLEAR | 2026-02-12 | HIGH_RELEVANCE |
| repo-001263 | HelloWorldLTY/CS225-DataStructure-inpython | source | Jupyter Notebook | LICENSE_UNCLEAR | 2020-11-15 | IRRELEVANT |
| repo-001264 | HelloWorldLTY/CVQVAE | source | Python | LICENSE_UNCLEAR | 2022-12-26 | HIGH_RELEVANCE |
| repo-001265 | HelloWorldLTY/damo-creformer | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2025-01-06 | POSSIBLE_RELEVANCE |
| repo-001266 | HelloWorldLTY/dance | fork | Python | BSD-2-Clause | 2024-03-31 | HIGH_RELEVANCE |
| repo-001267 | HelloWorldLTY/DANCE_NIPS2024 | fork | Python | LICENSE_UNCLEAR | 2024-10-12 | HIGH_RELEVANCE |
| repo-001268 | HelloWorldLTY/DanQ_pytorch | source | Python | LICENSE_UNCLEAR | 2025-01-10 | POSSIBLE_RELEVANCE |
| repo-001269 | HelloWorldLTY/DeepCTR | fork | Python | Apache-2.0 | 2024-01-31 | LOW_RELEVANCE |
| repo-001270 | HelloWorldLTY/DeepDDs | fork | — | LICENSE_UNCLEAR | 2021-07-05 | POSSIBLE_RELEVANCE |
| repo-001271 | HelloWorldLTY/deeprare_reproduce | source | Python | LICENSE_UNCLEAR | 2026-06-27 | POSSIBLE_RELEVANCE |
| repo-001272 | HelloWorldLTY/DeepRobust | fork | Python | MIT | 2024-04-04 | LOW_RELEVANCE |
| repo-001273 | HelloWorldLTY/Deepsynergy_pytorch | source | Python | LICENSE_UNCLEAR | 2025-07-22 | POSSIBLE_RELEVANCE |
| repo-001274 | HelloWorldLTY/Delphi | fork | Jupyter Notebook | MIT | 2025-11-07 | HIGH_RELEVANCE |
| repo-001275 | HelloWorldLTY/depression_detection | source | — | LICENSE_UNCLEAR | 2026-07-07 | HIGH_RELEVANCE |
| repo-001276 | HelloWorldLTY/DNABERT_S | fork | Python | LICENSE_UNCLEAR | 2024-08-27 | HIGH_RELEVANCE |
| repo-001277 | HelloWorldLTY/DNACLIP | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-07-21 | HIGH_RELEVANCE |
| repo-001278 | HelloWorldLTY/drugplayground | source | Python | MIT | 2026-01-05 | HIGH_RELEVANCE |
| repo-001279 | HelloWorldLTY/ECE385-PNG-WAV-processing | fork | Python | MIT | 2018-05-04 | IRRELEVANT |
| repo-001280 | HelloWorldLTY/EEPRS_analysis | fork | Shell | LICENSE_UNCLEAR | 2025-07-20 | POSSIBLE_RELEVANCE |
| repo-001281 | HelloWorldLTY/enformer-pytorch | fork | Python | MIT | 2024-12-04 | HIGH_RELEVANCE |
| repo-001282 | HelloWorldLTY/ENVI | fork | Jupyter Notebook | MIT | 2024-04-08 | HIGH_RELEVANCE |
| repo-001283 | HelloWorldLTY/EPInformer | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2024-09-12 | HIGH_RELEVANCE |
| repo-001284 | HelloWorldLTY/evaluate | fork | Python | Apache-2.0 | 2024-09-11 | LOW_RELEVANCE |
| repo-001285 | HelloWorldLTY/evo2 | fork | Jupyter Notebook | Apache-2.0 | 2025-03-11 | HIGH_RELEVANCE |
| repo-001286 | HelloWorldLTY/EvoAgentX | fork | Python | NOASSERTION | 2025-10-04 | POSSIBLE_RELEVANCE |
| repo-001287 | HelloWorldLTY/GEARS | fork | Python | MIT | 2024-07-10 | HIGH_RELEVANCE |
| repo-001288 | HelloWorldLTY/gene-embedding-benchmarks | fork | Python | BSD-3-Clause | 2025-06-07 | HIGH_RELEVANCE |
| repo-001289 | HelloWorldLTY/GeneCompass | fork | Python | LICENSE_UNCLEAR | 2024-10-01 | HIGH_RELEVANCE |
| repo-001290 | HelloWorldLTY/GenesTroBot | source | — | LICENSE_UNCLEAR | 2024-12-16 | HIGH_RELEVANCE |
| repo-001291 | HelloWorldLTY/Geneverse | source | Python | LICENSE_UNCLEAR | 2024-10-21 | HIGH_RELEVANCE |
| repo-001292 | HelloWorldLTY/GigaTIME | fork | Jupyter Notebook | NOASSERTION | 2025-12-12 | HIGH_RELEVANCE |
| repo-001293 | HelloWorldLTY/GLUE | fork | Python | MIT | 2025-09-03 | HIGH_RELEVANCE |
| repo-001294 | HelloWorldLTY/GNN | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2022-08-10 | LOW_RELEVANCE |
| repo-001295 | HelloWorldLTY/gorilla | fork | Python | Apache-2.0 | 2026-07-30 | POSSIBLE_RELEVANCE |
| repo-001296 | HelloWorldLTY/GPFM | fork | Python | LICENSE_UNCLEAR | 2024-10-04 | POSSIBLE_RELEVANCE |
| repo-001297 | HelloWorldLTY/GR | fork | TeX | CC-BY-SA-4.0 | 2019-01-19 | POSSIBLE_RELEVANCE |
| repo-001298 | HelloWorldLTY/grammar_samples | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2025-07-21 | HIGH_RELEVANCE |
| repo-001299 | HelloWorldLTY/gReLU | fork | Python | MIT | 2024-10-24 | HIGH_RELEVANCE |
| repo-001300 | HelloWorldLTY/guidance | fork | Jupyter Notebook | MIT | 2024-03-29 | POSSIBLE_RELEVANCE |
| repo-001301 | HelloWorldLTY/handbook | fork | HTML | LICENSE_UNCLEAR | 2022-05-28 | IRRELEVANT |
| repo-001302 | HelloWorldLTY/HelloWorldLTY.github.io | source | JavaScript | MIT | 2026-08-10 | IRRELEVANT |
| repo-001303 | HelloWorldLTY/HistoGPT | fork | Jupyter Notebook | Apache-2.0 | 2025-08-31 | HIGH_RELEVANCE |
| repo-001304 | HelloWorldLTY/hygieia | source | Python | LICENSE_UNCLEAR | 2026-04-30 | HIGH_RELEVANCE |
| repo-001305 | HelloWorldLTY/InternAgent | fork | Python | NOASSERTION | 2025-07-22 | HIGH_RELEVANCE |
| repo-001306 | HelloWorldLTY/juntang-zhuang | fork | — | LICENSE_UNCLEAR | 2022-07-10 | POSSIBLE_RELEVANCE |
| repo-001307 | HelloWorldLTY/LAMDNA | source | Python | LICENSE_UNCLEAR | 2026-07-09 | HIGH_RELEVANCE |
| repo-001308 | HelloWorldLTY/ldsc | fork | Python | GPL-3.0 | 2024-08-16 | HIGH_RELEVANCE |
| repo-001309 | HelloWorldLTY/Lihang | fork | Python | LICENSE_UNCLEAR | 2020-04-01 | IRRELEVANT |
| repo-001310 | HelloWorldLTY/LiveCodeBench | fork | Python | MIT | 2025-07-16 | IRRELEVANT |
| repo-001311 | HelloWorldLTY/LLaVA | fork | Python | Apache-2.0 | 2024-08-12 | POSSIBLE_RELEVANCE |
| repo-001312 | HelloWorldLTY/LucaOneApp | fork | Python | Apache-2.0 | 2024-09-20 | POSSIBLE_RELEVANCE |
| repo-001313 | HelloWorldLTY/mae | fork | Python | NOASSERTION | 2022-04-22 | LOW_RELEVANCE |
| repo-001314 | HelloWorldLTY/MAJAR | fork | R | NOASSERTION | 2022-12-12 | HIGH_RELEVANCE |
| repo-001315 | HelloWorldLTY/MiniCPM-V | fork | Python | Apache-2.0 | 2024-06-27 | POSSIBLE_RELEVANCE |
| repo-001316 | HelloWorldLTY/mixtime | source | Python | LICENSE_UNCLEAR | 2026-06-04 | POSSIBLE_RELEVANCE |
| repo-001317 | HelloWorldLTY/mnnpy | fork | Python | BSD-3-Clause | 2021-08-28 | LOW_RELEVANCE |
| repo-001318 | HelloWorldLTY/MOK | source | Python | Apache-2.0 | 2024-05-15 | LOW_RELEVANCE |
| repo-001319 | HelloWorldLTY/MuSe-GNN | source | Python | MIT | 2025-07-02 | HIGH_RELEVANCE |
| repo-001320 | HelloWorldLTY/MUSK | fork | Python | LICENSE_UNCLEAR | 2025-09-01 | POSSIBLE_RELEVANCE |
| repo-001321 | HelloWorldLTY/Myblog | source | — | LICENSE_UNCLEAR | 2022-08-30 | IRRELEVANT |
| repo-001322 | HelloWorldLTY/nenlp.github.io | fork | HTML | LICENSE_UNCLEAR | 2025-03-05 | IRRELEVANT |
| repo-001323 | HelloWorldLTY/neurips2021_multimodal_topmethods | fork | Python | MIT | 2022-01-21 | HIGH_RELEVANCE |
| repo-001324 | HelloWorldLTY/Open-problems-for-single-cell-2022-Silver-medal-solution | source | Jupyter Notebook | LICENSE_UNCLEAR | 2022-11-19 | HIGH_RELEVANCE |
| repo-001325 | HelloWorldLTY/openproblems | fork | Python | MIT | 2024-10-14 | HIGH_RELEVANCE |
| repo-001326 | HelloWorldLTY/Orthrus | fork | Python | MIT | 2024-10-29 | HIGH_RELEVANCE |
| repo-001327 | HelloWorldLTY/pascient | fork | Jupyter Notebook | NOASSERTION | 2024-12-06 | HIGH_RELEVANCE |
| repo-001328 | HelloWorldLTY/PertBench | fork | Python | LICENSE_UNCLEAR | 2026-02-01 | HIGH_RELEVANCE |
| repo-001329 | HelloWorldLTY/processing_severity | source | — | LICENSE_UNCLEAR | 2025-04-26 | POSSIBLE_RELEVANCE |
| repo-001330 | HelloWorldLTY/propr_python | source | Python | LICENSE_UNCLEAR | 2024-07-03 | POSSIBLE_RELEVANCE |
| repo-001331 | HelloWorldLTY/pytorch_geometric | fork | Python | MIT | 2022-08-25 | LOW_RELEVANCE |
| repo-001332 | HelloWorldLTY/regLM | fork | Jupyter Notebook | MIT | 2025-03-13 | HIGH_RELEVANCE |
| repo-001333 | HelloWorldLTY/RobustCell | source | Jupyter Notebook | LICENSE_UNCLEAR | 2024-11-24 | HIGH_RELEVANCE |
| repo-001334 | HelloWorldLTY/RPCL | source | Python | LICENSE_UNCLEAR | 2025-01-25 | LOW_RELEVANCE |
| repo-001335 | HelloWorldLTY/scAAnet | fork | Jupyter Notebook | MIT | 2022-05-27 | HIGH_RELEVANCE |
| repo-001336 | HelloWorldLTY/scDeepSort | fork | Python | GPL-3.0 | 2022-06-22 | HIGH_RELEVANCE |
| repo-001337 | HelloWorldLTY/scDRS | fork | Jupyter Notebook | MIT | 2024-08-11 | HIGH_RELEVANCE |
| repo-001338 | HelloWorldLTY/scELMo | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-01-31 | HIGH_RELEVANCE |
| repo-001339 | HelloWorldLTY/scEval | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-06-28 | HIGH_RELEVANCE |
| repo-001340 | HelloWorldLTY/scFoundation | fork | Jupyter Notebook | Apache-2.0 | 2024-07-26 | HIGH_RELEVANCE |
| repo-001341 | HelloWorldLTY/SciAgentArena | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-08-09 | HIGH_RELEVANCE |
| repo-001342 | HelloWorldLTY/scib | fork | Python | MIT | 2021-09-16 | HIGH_RELEVANCE |
| repo-001343 | HelloWorldLTY/scJoint | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2021-08-09 | HIGH_RELEVANCE |
| repo-001344 | HelloWorldLTY/scLLMExplorer | source | Python | LICENSE_UNCLEAR | 2023-12-20 | LOW_RELEVANCE |
| repo-001345 | HelloWorldLTY/scover | fork | HTML | MIT | 2025-01-09 | POSSIBLE_RELEVANCE |
| repo-001346 | HelloWorldLTY/sctransform | fork | R | GPL-3.0 | 2023-01-29 | HIGH_RELEVANCE |
| repo-001347 | HelloWorldLTY/scTransformer | source | Jupyter Notebook | LICENSE_UNCLEAR | 2022-03-28 | HIGH_RELEVANCE |
| repo-001348 | HelloWorldLTY/scvi-tools | fork | Python | BSD-3-Clause | 2024-05-07 | HIGH_RELEVANCE |
| repo-001349 | HelloWorldLTY/slime | fork | Python | Apache-2.0 | 2026-07-16 | POSSIBLE_RELEVANCE |
| repo-001350 | HelloWorldLTY/SpaIM | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2025-10-27 | HIGH_RELEVANCE |
| repo-001351 | HelloWorldLTY/spEMO | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-05-09 | HIGH_RELEVANCE |
| repo-001352 | HelloWorldLTY/sprefine | source | Python | LICENSE_UNCLEAR | 2025-01-10 | HIGH_RELEVANCE |
| repo-001353 | HelloWorldLTY/squidpy | fork | Python | BSD-3-Clause | 2023-09-25 | HIGH_RELEVANCE |
| repo-001354 | HelloWorldLTY/STAT542-Statistical-Learning | source | HTML | MIT | 2021-12-27 | IRRELEVANT |
| repo-001355 | HelloWorldLTY/stg | fork | Python | MIT | 2024-12-31 | LOW_RELEVANCE |
| repo-001356 | HelloWorldLTY/STPath | fork | Python | LICENSE_UNCLEAR | 2025-07-27 | HIGH_RELEVANCE |
| repo-001357 | HelloWorldLTY/SuperGLUE | source | Python | LICENSE_UNCLEAR | 2025-07-22 | HIGH_RELEVANCE |
| repo-001358 | HelloWorldLTY/Tangram | fork | Jupyter Notebook | BSD-3-Clause | 2024-12-14 | HIGH_RELEVANCE |
| repo-001359 | HelloWorldLTY/Tangram_v2 | source | Python | LICENSE_UNCLEAR | 2023-11-07 | HIGH_RELEVANCE |
| repo-001360 | HelloWorldLTY/task-dge-perturbation-prediction-analysis | fork | Jupyter Notebook | MIT | 2024-10-30 | HIGH_RELEVANCE |
| repo-001361 | HelloWorldLTY/task_batch_integration | fork | Python | MIT | 2025-01-27 | HIGH_RELEVANCE |
| repo-001362 | HelloWorldLTY/TeamPath | source | Python | LICENSE_UNCLEAR | 2026-07-21 | POSSIBLE_RELEVANCE |
| repo-001363 | HelloWorldLTY/transformGamPoi-Paper | fork | HTML | GPL-3.0 | 2023-05-04 | POSSIBLE_RELEVANCE |
| repo-001364 | HelloWorldLTY/trl | fork | Python | Apache-2.0 | 2025-08-23 | POSSIBLE_RELEVANCE |
| repo-001365 | HelloWorldLTY/UKBioLM | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-05-09 | HIGH_RELEVANCE |
| repo-001366 | HelloWorldLTY/UNICORN | source | Python | LICENSE_UNCLEAR | 2025-12-13 | POSSIBLE_RELEVANCE |
| repo-001367 | HelloWorldLTY/USD | source | Python | LICENSE_UNCLEAR | 2026-08-01 | HIGH_RELEVANCE |
| repo-001368 | HelloWorldLTY/UTMOST | fork | Python | LICENSE_UNCLEAR | 2023-08-07 | HIGH_RELEVANCE |
| repo-001369 | HelloWorldLTY/VISTA | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-12-17 | POSSIBLE_RELEVANCE |
| repo-001370 | HelloWorldLTY/VISTA_reproduce | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-02-17 | HIGH_RELEVANCE |
| repo-001371 | HelloWorldLTY/WM8731-Audio-CODEC | fork | Verilog | LICENSE_UNCLEAR | 2020-12-25 | IRRELEVANT |
| repo-001372 | HelloWorldLTY/Yale-Notes | fork | TeX | LICENSE_UNCLEAR | 2022-01-31 | IRRELEVANT |
| repo-001373 | HelloWorldLTY/YCSGP.github.io | fork | HTML | MIT | 2025-03-11 | IRRELEVANT |
| repo-000481 | igor-sadalski/Biomni | fork | Python | Apache-2.0 | 2025-10-27 | HIGH_RELEVANCE |
| repo-001374 | igor-sadalski/Hopper_Hardware | source | C | LICENSE_UNCLEAR | 2022-09-10 | LOW_RELEVANCE |
| repo-001375 | igor-sadalski/igor-sadalski.github.io | source | HTML | MIT | 2026-03-11 | IRRELEVANT |
| repo-001376 | igor-sadalski/popV | fork | Python | MIT | 2025-09-09 | POSSIBLE_RELEVANCE |
| repo-001377 | igor-sadalski/Scaling-up-measurement-noise-scaling-laws | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-07-28 | POSSIBLE_RELEVANCE |
| repo-001378 | jucor/12-HelmholtzTorch | source | Lua | LICENSE_UNCLEAR | 2013-08-06 | POSSIBLE_RELEVANCE |
| repo-001379 | jucor/AJR | source | Shell | LICENSE_UNCLEAR | 2013-09-18 | POSSIBLE_RELEVANCE |
| repo-001380 | jucor/anki_field_sorter | source | Python | LICENSE_UNCLEAR | 2025-07-14 | IRRELEVANT |
| repo-001381 | jucor/anki_notes | source | Shell | LICENSE_UNCLEAR | 2025-06-13 | IRRELEVANT |
| repo-001382 | jucor/audiobookshelf | fork | JavaScript | GPL-3.0 | 2026-05-10 | IRRELEVANT |
| repo-001383 | jucor/audiobookshelf-app | fork | Vue | GPL-3.0 | 2026-06-23 | IRRELEVANT |
| repo-001384 | jucor/baal | fork | Python | Apache-2.0 | 2021-12-07 | LOW_RELEVANCE |
| repo-001385 | jucor/ban-the-scan-remake | source | HTML | MIT | 2026-07-01 | IRRELEVANT |
| repo-001386 | jucor/bats | fork | Shell | MIT | 2016-05-11 | IRRELEVANT |
| repo-000701 | jucor/Biomni | fork | Python | Apache-2.0 | 2025-07-10 | HIGH_RELEVANCE |
| repo-001387 | jucor/box.com-downloader | fork | Python | GPL-3.0 | 2026-04-21 | IRRELEVANT |
| repo-001388 | jucor/cBioPortalData | fork | R | LICENSE_UNCLEAR | 2020-07-12 | HIGH_RELEVANCE |
| repo-001389 | jucor/chattr | fork | R | NOASSERTION | 2023-12-21 | POSSIBLE_RELEVANCE |
| repo-001390 | jucor/chron | source | R | LICENSE_UNCLEAR | 2013-08-08 | LOW_RELEVANCE |
| repo-001391 | jucor/claude-code-lsp-skill | source | — | MIT | 2026-03-04 | HIGH_RELEVANCE |
| repo-001392 | jucor/claude-plugins-official | fork | Python | LICENSE_UNCLEAR | 2026-03-03 | POSSIBLE_RELEVANCE |
| repo-001393 | jucor/clearml-docs | fork | JavaScript | NOASSERTION | 2023-03-28 | LOW_RELEVANCE |
| repo-001394 | jucor/clojure-lsp-plugin | source | — | Apache-2.0 | 2026-03-03 | POSSIBLE_RELEVANCE |
| repo-001395 | jucor/conda | fork | Python | NOASSERTION | 2021-05-28 | LOW_RELEVANCE |
| repo-001396 | jucor/conda-bash-completion-feedstock | fork | Shell | BSD-3-Clause | 2022-11-17 | LOW_RELEVANCE |
| repo-001397 | jucor/conda-forge-pinning-feedstock | fork | Python | BSD-3-Clause | 2023-12-27 | LOW_RELEVANCE |
| repo-001398 | jucor/cubox-installer-scripts | fork | Shell | LICENSE_UNCLEAR | 2013-09-18 | IRRELEVANT |
| repo-001399 | jucor/cunn | fork | Lua | LICENSE_UNCLEAR | 2014-06-12 | LOW_RELEVANCE |
| repo-001400 | jucor/denon-remote | fork | HTML | LICENSE_UNCLEAR | 2026-07-05 | IRRELEVANT |
| repo-001401 | jucor/docker-transmission-openvpn | fork | Shell | GPL-3.0 | 2025-11-29 | IRRELEVANT |
| repo-001402 | jucor/ehr-predictions | fork | Python | Apache-2.0 | 2021-05-05 | HIGH_RELEVANCE |
| repo-001403 | jucor/ffjm-2026-codex | source | — | LICENSE_UNCLEAR | 2026-02-08 | POSSIBLE_RELEVANCE |
| repo-001404 | jucor/ffjm-quarts-2026-par-ia-apres-fermeture | source | — | LICENSE_UNCLEAR | 2026-02-08 | IRRELEVANT |
| repo-001405 | jucor/firefly-theme-zed | fork | — | Apache-2.0 | 2026-05-23 | IRRELEVANT |
| repo-001406 | jucor/Flipper-IRDB | fork | — | LICENSE_UNCLEAR | 2022-12-24 | IRRELEVANT |
| repo-001407 | jucor/fsv | fork | C | LGPL-2.1 | 2013-07-17 | IRRELEVANT |
| repo-001408 | jucor/ggmcmc | fork | R | LICENSE_UNCLEAR | 2013-08-04 | HIGH_RELEVANCE |
| repo-001409 | jucor/Google-Calendar-Guests-Can-Modify-Event-By-Default | fork | JavaScript | LICENSE_UNCLEAR | 2014-11-27 | IRRELEVANT |
| repo-001410 | jucor/graphicsmagick | fork | Lua | LICENSE_UNCLEAR | 2013-06-01 | LOW_RELEVANCE |
| repo-001411 | jucor/grid-docs | fork | — | LICENSE_UNCLEAR | 2021-10-04 | LOW_RELEVANCE |
| repo-001412 | jucor/gtestExample | source | C++ | LICENSE_UNCLEAR | 2013-07-10 | IRRELEVANT |
| repo-001413 | jucor/hermes-agent | fork | Python | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001414 | jucor/HighRes-net | fork | Jupyter Notebook | NOASSERTION | 2020-02-21 | HIGH_RELEVANCE |
| repo-001415 | jucor/image | fork | C | LICENSE_UNCLEAR | 2015-02-20 | LOW_RELEVANCE |
| repo-001416 | jucor/IPython-notebook-extensions | fork | HTML | NOASSERTION | 2015-12-21 | LOW_RELEVANCE |
| repo-001417 | jucor/katex-github-chrome-extension | fork | JavaScript | MIT | 2022-03-15 | IRRELEVANT |
| repo-001418 | jucor/krippendorff | source | R | NOASSERTION | 2024-11-13 | HIGH_RELEVANCE |
| repo-001419 | jucor/llama | fork | Python | GPL-3.0 | 2023-03-03 | LOW_RELEVANCE |
| repo-001420 | jucor/logroll | fork | Lua | LICENSE_UNCLEAR | 2013-08-01 | IRRELEVANT |
| repo-001421 | jucor/lua---ffmpeg | fork | Lua | LICENSE_UNCLEAR | 2013-02-06 | LOW_RELEVANCE |
| repo-001422 | jucor/lua-fs-0.3 | fork | C | LICENSE_UNCLEAR | 2013-01-03 | IRRELEVANT |
| repo-001423 | jucor/lua-pprint | fork | Lua | LICENSE_UNCLEAR | 2013-08-01 | IRRELEVANT |
| repo-001424 | jucor/lua-sci | source | Lua | NOASSERTION | 2014-08-05 | POSSIBLE_RELEVANCE |
| repo-001425 | jucor/lua-signal | fork | C | NOASSERTION | 2014-07-24 | IRRELEVANT |
| repo-001426 | jucor/lua-util | fork | Lua | LICENSE_UNCLEAR | 2013-03-19 | IRRELEVANT |
| repo-001427 | jucor/lua-xsys | source | Lua | LICENSE_UNCLEAR | 2013-08-05 | IRRELEVANT |
| repo-001428 | jucor/luatrace | fork | Lua | MIT | 2013-02-10 | IRRELEVANT |
| repo-001429 | jucor/metal-defect-detection | fork | Jupyter Notebook | NOASSERTION | 2021-04-04 | LOW_RELEVANCE |
| repo-001430 | jucor/mlconf-dlp | source | Python | LICENSE_UNCLEAR | 2025-10-24 | LOW_RELEVANCE |
| repo-001431 | jucor/models | fork | Python | Apache-2.0 | 2017-03-19 | LOW_RELEVANCE |
| repo-001432 | jucor/moneymanagerex | fork | C | GPL-2.0 | 2016-10-23 | IRRELEVANT |
| repo-001433 | jucor/openai-ratelimiter | fork | Python | MIT | 2023-06-20 | POSSIBLE_RELEVANCE |
| repo-001434 | jucor/optim | fork | Lua | LICENSE_UNCLEAR | 2013-08-06 | LOW_RELEVANCE |
| repo-001435 | jucor/pdfbook | source | Shell | LICENSE_UNCLEAR | 2023-11-12 | IRRELEVANT |
| repo-001436 | jucor/planning-with-files | fork | — | MIT | 2026-01-03 | HIGH_RELEVANCE |
| repo-001437 | jucor/plotnine | fork | Python | GPL-2.0 | 2021-11-10 | LOW_RELEVANCE |
| repo-001438 | jucor/polis | fork | JavaScript | AGPL-3.0 | 2026-07-27 | LOW_RELEVANCE |
| repo-001439 | jucor/pymc | fork | Python | NOASSERTION | 2024-07-10 | HIGH_RELEVANCE |
| repo-001440 | jucor/python_koans | fork | Python | MIT | 2016-07-25 | IRRELEVANT |
| repo-001441 | jucor/pytorch-examples | fork | Python | BSD-3-Clause | 2017-04-26 | LOW_RELEVANCE |
| repo-001442 | jucor/rclient | source | Lua | LICENSE_UNCLEAR | 2013-11-29 | POSSIBLE_RELEVANCE |
| repo-001443 | jucor/reshape | fork | R | LICENSE_UNCLEAR | 2013-11-27 | LOW_RELEVANCE |
| repo-001444 | jucor/rocks | fork | Lua | LICENSE_UNCLEAR | 2014-03-26 | LOW_RELEVANCE |
| repo-001445 | jucor/scikit-learn | fork | Python | NOASSERTION | 2017-08-07 | LOW_RELEVANCE |
| repo-001446 | jucor/Scumm-theDocs | fork | — | LICENSE_UNCLEAR | 2024-08-24 | IRRELEVANT |
| repo-001447 | jucor/sensemaking-tools | fork | TypeScript | Apache-2.0 | 2025-01-23 | POSSIBLE_RELEVANCE |
| repo-001448 | jucor/Simple-Chrome-Extension-Content-Script-Skeleton | fork | JavaScript | LICENSE_UNCLEAR | 2012-11-07 | IRRELEVANT |
| repo-001449 | jucor/skypilot | fork | Python | Apache-2.0 | 2024-09-03 | POSSIBLE_RELEVANCE |
| repo-001450 | jucor/spearmint | fork | Python | LICENSE_UNCLEAR | 2013-06-17 | POSSIBLE_RELEVANCE |
| repo-001451 | jucor/spotty | fork | Python | MIT | 2021-04-13 | LOW_RELEVANCE |
| repo-001452 | jucor/spr | fork | Go | MIT | 2026-06-10 | IRRELEVANT |
| repo-001453 | jucor/tagtime-vis | fork | R | LICENSE_UNCLEAR | 2015-02-09 | IRRELEVANT |
| repo-001454 | jucor/test-public | source | — | LICENSE_UNCLEAR | 2017-01-26 | IRRELEVANT |
| repo-001455 | jucor/themes | fork | JavaScript | LICENSE_UNCLEAR | 2016-11-07 | IRRELEVANT |
| repo-001456 | jucor/todo.txt-graph | fork | Python | LICENSE_UNCLEAR | 2017-01-20 | IRRELEVANT |
| repo-001457 | jucor/todotxt.net | fork | C# | NOASSERTION | 2021-04-30 | IRRELEVANT |
| repo-001458 | jucor/tomdoc.lua | source | — | LICENSE_UNCLEAR | 2013-01-19 | IRRELEVANT |
| repo-001459 | jucor/topydo | fork | Python | GPL-3.0 | 2017-01-24 | IRRELEVANT |
| repo-001460 | jucor/torch | fork | C | NOASSERTION | 2013-11-13 | LOW_RELEVANCE |
| repo-001461 | jucor/torch-cdflib | source | Fortran | LICENSE_UNCLEAR | 2024-11-13 | POSSIBLE_RELEVANCE |
| repo-001462 | jucor/torch-datasets | fork | Lua | LICENSE_UNCLEAR | 2013-04-29 | LOW_RELEVANCE |
| repo-001463 | jucor/torch-doc-template | source | CSS | LICENSE_UNCLEAR | 2016-06-24 | IRRELEVANT |
| repo-001464 | jucor/torch-graph | fork | Lua | LICENSE_UNCLEAR | 2013-03-07 | LOW_RELEVANCE |
| repo-001465 | jucor/torch-gsl | source | Lua | LICENSE_UNCLEAR | 2012-12-18 | HIGH_RELEVANCE |
| repo-001466 | jucor/torch-prepend-path | source | Lua | LICENSE_UNCLEAR | 2013-05-23 | IRRELEVANT |
| repo-001467 | jucor/torch7 | fork | C | LICENSE_UNCLEAR | 2015-02-19 | LOW_RELEVANCE |
| repo-001468 | jucor/tweetokenize | fork | Python | BSD-3-Clause | 2018-03-31 | LOW_RELEVANCE |
| repo-001469 | jucor/vc | source | Awk | LICENSE_UNCLEAR | 2013-09-16 | IRRELEVANT |
| repo-001470 | jucor/vim-lua-inspect | fork | Lua | LICENSE_UNCLEAR | 2011-11-24 | IRRELEVANT |
| repo-001471 | jucor/vim-sleuth | fork | Vim Script | LICENSE_UNCLEAR | 2017-07-23 | IRRELEVANT |
| repo-001472 | jucor/vpn-configs-contrib | fork | Shell | GPL-3.0 | 2025-12-07 | IRRELEVANT |
| repo-001473 | jucor/werkzeug | fork | Python | NOASSERTION | 2017-09-19 | IRRELEVANT |
| repo-001474 | jucor/whatfreewords | fork | HTML | LICENSE_UNCLEAR | 2020-08-29 | IRRELEVANT |
| repo-001475 | jucor/whombat | fork | TypeScript | GPL-3.0 | 2025-05-20 | LOW_RELEVANCE |
| repo-001476 | jucor/yt-dlp | fork | Python | Unlicense | 2024-06-29 | IRRELEVANT |
| repo-001477 | jucor/ZeroBraneStudio | fork | Lua | NOASSERTION | 2013-04-26 | IRRELEVANT |
| repo-001478 | jucor/zotero-scipdf | fork | TypeScript | AGPL-3.0 | 2026-02-28 | HIGH_RELEVANCE |
| repo-001479 | kexinhuang12345/amplify-vite-react-template | source | TypeScript | MIT-0 | 2025-05-07 | IRRELEVANT |
| repo-001480 | kexinhuang12345/anomaly-detection-resources | fork | Python | AGPL-3.0 | 2021-04-13 | LOW_RELEVANCE |
| repo-001481 | kexinhuang12345/ApaperAday | source | — | LICENSE_UNCLEAR | 2019-06-14 | POSSIBLE_RELEVANCE |
| repo-001482 | kexinhuang12345/Basic-Algorithm | source | Java | LICENSE_UNCLEAR | 2017-12-06 | IRRELEVANT |
| repo-001483 | kexinhuang12345/CASTER | source | Jupyter Notebook | LICENSE_UNCLEAR | 2020-10-28 | HIGH_RELEVANCE |
| repo-001484 | kexinhuang12345/chemprop | fork | Python | MIT | 2021-07-29 | HIGH_RELEVANCE |
| repo-001485 | kexinhuang12345/clinicalBERT | source | Jupyter Notebook | LICENSE_UNCLEAR | 2022-10-17 | HIGH_RELEVANCE |
| repo-001486 | kexinhuang12345/Coursera_Machine_Learning_Andrew | source | MATLAB | LICENSE_UNCLEAR | 2017-08-14 | IRRELEVANT |
| repo-001487 | kexinhuang12345/CS102_Data_Structure | source | Java | LICENSE_UNCLEAR | 2017-08-14 | IRRELEVANT |
| repo-001488 | kexinhuang12345/cs107test | source | Python | LICENSE_UNCLEAR | 2020-10-26 | IRRELEVANT |
| repo-001489 | kexinhuang12345/CS201_Computer_System_Organization | source | C | LICENSE_UNCLEAR | 2017-08-14 | IRRELEVANT |
| repo-001490 | kexinhuang12345/CS224N | source | Jupyter Notebook | LICENSE_UNCLEAR | 2018-01-06 | LOW_RELEVANCE |
| repo-001491 | kexinhuang12345/CS231N_Stanford | source | Jupyter Notebook | LICENSE_UNCLEAR | 2017-11-07 | LOW_RELEVANCE |
| repo-001492 | kexinhuang12345/data_analysis | source | Jupyter Notebook | LICENSE_UNCLEAR | 2018-10-10 | IRRELEVANT |
| repo-001493 | kexinhuang12345/data_process | source | Python | LICENSE_UNCLEAR | 2023-08-21 | POSSIBLE_RELEVANCE |
| repo-001494 | kexinhuang12345/DeepPurpose | source | Jupyter Notebook | BSD-3-Clause | 2024-06-10 | HIGH_RELEVANCE |
| repo-001495 | kexinhuang12345/drug-bert | source | — | LICENSE_UNCLEAR | 2020-02-06 | HIGH_RELEVANCE |
| repo-001496 | kexinhuang12345/DrugDataResource | source | — | BSD-3-Clause | 2020-08-22 | HIGH_RELEVANCE |
| repo-001497 | kexinhuang12345/ESPF | source | Jupyter Notebook | LICENSE_UNCLEAR | 2019-10-30 | HIGH_RELEVANCE |
| repo-001498 | kexinhuang12345/experiment-data-llm | source | — | BSD-3-Clause | 2024-04-12 | POSSIBLE_RELEVANCE |
| repo-001499 | kexinhuang12345/github-issue-templates | fork | — | LICENSE_UNCLEAR | 2021-05-05 | IRRELEVANT |
| repo-001500 | kexinhuang12345/GNNPapers | fork | — | LICENSE_UNCLEAR | 2020-11-25 | LOW_RELEVANCE |
| repo-001501 | kexinhuang12345/hub-docs | fork | Svelte | Apache-2.0 | 2023-01-20 | LOW_RELEVANCE |
| repo-001502 | kexinhuang12345/intro_ml_nyu | source | Jupyter Notebook | LICENSE_UNCLEAR | 2018-05-25 | IRRELEVANT |
| repo-001503 | kexinhuang12345/leetcode | source | Java | LICENSE_UNCLEAR | 2019-06-04 | IRRELEVANT |
| repo-001504 | kexinhuang12345/logd74 | fork | — | LICENSE_UNCLEAR | 2017-11-23 | HIGH_RELEVANCE |
| repo-001505 | kexinhuang12345/mitotic_spindle | source | MATLAB | LICENSE_UNCLEAR | 2018-11-11 | HIGH_RELEVANCE |
| repo-001506 | kexinhuang12345/ml-genomics-resources | source | — | BSD-3-Clause | 2021-11-02 | HIGH_RELEVANCE |
| repo-001507 | kexinhuang12345/MolDesigner-Public | source | Python | BSD-3-Clause | 2020-11-27 | HIGH_RELEVANCE |
| repo-001508 | kexinhuang12345/MolTrans | source | Jupyter Notebook | BSD-3-Clause | 2022-07-15 | HIGH_RELEVANCE |
| repo-001509 | kexinhuang12345/nextjs-ai-bio-assistant | source | TypeScript | NOASSERTION | 2025-01-20 | HIGH_RELEVANCE |
| repo-001510 | kexinhuang12345/NLP | source | Jupyter Notebook | LICENSE_UNCLEAR | 2017-11-02 | LOW_RELEVANCE |
| repo-001511 | kexinhuang12345/Numerical_Analysis | source | MATLAB | LICENSE_UNCLEAR | 2017-10-17 | LOW_RELEVANCE |
| repo-001512 | kexinhuang12345/Operating_System | source | Java | LICENSE_UNCLEAR | 2017-08-14 | IRRELEVANT |
| repo-001513 | kexinhuang12345/playground | fork | Python | LICENSE_UNCLEAR | 2020-09-14 | IRRELEVANT |
| repo-001514 | kexinhuang12345/readthedocs.org | fork | Python | MIT | 2021-09-02 | LOW_RELEVANCE |
| repo-001515 | kexinhuang12345/robustness-gym | fork | Python | Apache-2.0 | 2021-01-14 | POSSIBLE_RELEVANCE |
| repo-001516 | kexinhuang12345/scGNN | source | Jupyter Notebook | BSD-3-Clause | 2020-10-22 | HIGH_RELEVANCE |
| repo-001517 | kexinhuang12345/SkipGNN | source | Jupyter Notebook | BSD-3-Clause | 2020-05-09 | HIGH_RELEVANCE |
| repo-001518 | kexinhuang12345/SkyRL | fork | Python | Apache-2.0 | 2025-08-31 | POSSIBLE_RELEVANCE |
| repo-001519 | kexinhuang12345/staged-recipes | fork | Python | BSD-3-Clause | 2020-12-24 | POSSIBLE_RELEVANCE |
| repo-001520 | kexinhuang12345/toxic-comment-detection | source | Jupyter Notebook | LICENSE_UNCLEAR | 2018-07-20 | LOW_RELEVANCE |
| repo-001521 | kexinhuang12345/transformers | fork | Python | Apache-2.0 | 2021-02-06 | LOW_RELEVANCE |
| repo-001522 | kuanlinhuang/AD_SPI1_project | source | R | LICENSE_UNCLEAR | 2018-06-19 | HIGH_RELEVANCE |
| repo-001523 | kuanlinhuang/agentic_coding_starter | source | — | LICENSE_UNCLEAR | 2025-06-16 | POSSIBLE_RELEVANCE |
| repo-001524 | kuanlinhuang/AgentReplication | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-12-20 | POSSIBLE_RELEVANCE |
| repo-001525 | kuanlinhuang/AI-Scientist-v2 | fork | Python | Apache-2.0 | 2025-05-09 | HIGH_RELEVANCE |
| repo-001526 | kuanlinhuang/awesome-machine-learning | fork | Python | LICENSE_UNCLEAR | 2015-04-08 | LOW_RELEVANCE |
| repo-001527 | kuanlinhuang/bioconda-recipes | fork | Shell | MIT | 2026-08-03 | HIGH_RELEVANCE |
| repo-001528 | kuanlinhuang/BioMine | fork | Python | NOASSERTION | 2017-09-20 | HIGH_RELEVANCE |
| repo-001529 | kuanlinhuang/Biomni-Lite | source | Python | Apache-2.0 | 2026-02-28 | HIGH_RELEVANCE |
| repo-001530 | kuanlinhuang/Biomni_AD_ADA_entries | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-02-23 | HIGH_RELEVANCE |
| repo-001531 | kuanlinhuang/boltz | fork | Python | MIT | 2026-04-02 | HIGH_RELEVANCE |
| repo-001532 | kuanlinhuang/claude-scientific-skills | fork | Python | MIT | 2026-03-03 | HIGH_RELEVANCE |
| repo-001533 | kuanlinhuang/claw-code | fork | Rust | LICENSE_UNCLEAR | 2026-04-06 | POSSIBLE_RELEVANCE |
| repo-001534 | kuanlinhuang/claw-code-parity | fork | Rust | LICENSE_UNCLEAR | 2026-04-02 | POSSIBLE_RELEVANCE |
| repo-001535 | kuanlinhuang/decentralizedImmunizationEHR | source | — | LICENSE_UNCLEAR | 2025-08-01 | HIGH_RELEVANCE |
| repo-001536 | kuanlinhuang/efficient-evolution | fork | Python | MIT | 2025-03-24 | HIGH_RELEVANCE |
| repo-001537 | kuanlinhuang/genome | fork | Perl | LGPL-3.0 | 2015-02-21 | HIGH_RELEVANCE |
| repo-001538 | kuanlinhuang/GetFreeCopyV2 | source | TypeScript | LICENSE_UNCLEAR | 2025-08-24 | IRRELEVANT |
| repo-001539 | kuanlinhuang/graph-storyteller | source | TypeScript | LICENSE_UNCLEAR | 2025-08-07 | POSSIBLE_RELEVANCE |
| repo-001540 | kuanlinhuang/Growth | source | CSS | LICENSE_UNCLEAR | 2016-04-05 | LOW_RELEVANCE |
| repo-001541 | kuanlinhuang/hotspot3d | fork | Perl | MIT | 2017-05-15 | HIGH_RELEVANCE |
| repo-001542 | kuanlinhuang/HumanProof | source | Python | GPL-3.0 | 2026-07-03 | POSSIBLE_RELEVANCE |
| repo-001543 | kuanlinhuang/JRNLClub_Public | source | — | LICENSE_UNCLEAR | 2025-11-30 | LOW_RELEVANCE |
| repo-001544 | kuanlinhuang/medtallk | fork | JavaScript | LICENSE_UNCLEAR | 2017-10-21 | HIGH_RELEVANCE |
| repo-001545 | kuanlinhuang/paperclip | fork | Python | Apache-2.0 | 2026-05-22 | HIGH_RELEVANCE |
| repo-001546 | kuanlinhuang/PDXNatComm2017 | source | R | LICENSE_UNCLEAR | 2018-01-11 | HIGH_RELEVANCE |
| repo-001547 | kuanlinhuang/PopularGenes | source | R | LICENSE_UNCLEAR | 2018-03-25 | HIGH_RELEVANCE |
| repo-001548 | kuanlinhuang/STELLA | fork | Python | LICENSE_UNCLEAR | 2025-10-01 | HIGH_RELEVANCE |
| repo-001549 | kuanlinhuang/VarCrawl | fork | TypeScript | MIT | 2026-04-19 | POSSIBLE_RELEVANCE |
| repo-001550 | kuanlinhuang/vcf2tsv | source | Python | GPL-3.0 | 2023-01-20 | HIGH_RELEVANCE |
| repo-001551 | kuanlinhuang/WikiPathways_GeneSet_R | fork | R | GPL-2.0 | 2015-06-25 | HIGH_RELEVANCE |
| repo-001552 | lxasqjc/Andrew_Machine_Learning_Programming_Assignments | source | MATLAB | MIT | 2018-08-09 | IRRELEVANT |
| repo-001553 | lxasqjc/Assignments_cs231 | source | Jupyter Notebook | MIT | 2019-05-02 | IRRELEVANT |
| repo-000634 | lxasqjc/Biomni | fork | Python | Apache-2.0 | 2026-04-10 | HIGH_RELEVANCE |
| repo-001554 | lxasqjc/chenjin-academic | source | Jupyter Notebook | MIT | 2026-02-10 | POSSIBLE_RELEVANCE |
| repo-001555 | lxasqjc/cpython | fork | Python | NOASSERTION | 2018-07-17 | LOW_RELEVANCE |
| repo-001556 | lxasqjc/CS231_Assignments_2018 | source | — | LICENSE_UNCLEAR | 2018-08-10 | IRRELEVANT |
| repo-001557 | lxasqjc/Deeper-Image-Quality-Transfer-Training-Low-Memory-Neural-Networks-for-3D-Images | fork | Python | LICENSE_UNCLEAR | 2018-09-14 | HIGH_RELEVANCE |
| repo-001558 | lxasqjc/Deformation-Segmentation | source | C | NOASSERTION | 2022-12-24 | LOW_RELEVANCE |
| repo-001559 | lxasqjc/dlib | fork | C++ | LICENSE_UNCLEAR | 2018-03-31 | LOW_RELEVANCE |
| repo-001560 | lxasqjc/Foveation-for-Segmentation-of-Mega-pixel-Histology-Images | source | — | LICENSE_UNCLEAR | 2020-07-10 | HIGH_RELEVANCE |
| repo-001561 | lxasqjc/Foveation-Segmentation | source | Python | MIT | 2022-01-24 | POSSIBLE_RELEVANCE |
| repo-001562 | lxasqjc/ibd-expert-poll | source | HTML | LICENSE_UNCLEAR | 2026-08-12 | POSSIBLE_RELEVANCE |
| repo-001563 | lxasqjc/lbpcascade_animeface | fork | — | LICENSE_UNCLEAR | 2018-07-25 | IRRELEVANT |
| repo-001564 | lxasqjc/learn-downsample.github.io | source | HTML | LICENSE_UNCLEAR | 2022-03-17 | POSSIBLE_RELEVANCE |
| repo-001565 | lxasqjc/MCPL | source | — | LICENSE_UNCLEAR | 2024-05-27 | POSSIBLE_RELEVANCE |
| repo-001566 | lxasqjc/MedICSS_2021 | source | — | LICENSE_UNCLEAR | 2021-07-15 | POSSIBLE_RELEVANCE |
| repo-001567 | lxasqjc/my_git_test | source | HTML | LICENSE_UNCLEAR | 2018-08-19 | IRRELEVANT |
| repo-001568 | lxasqjc/Numerical-Analysis-Examples | fork | C# | MIT | 2018-09-10 | LOW_RELEVANCE |
| repo-001569 | lxasqjc/numSCAL_basic | fork | C++ | NOASSERTION | 2018-10-03 | HIGH_RELEVANCE |
| repo-001570 | lxasqjc/OpenCV2-Python-Tutorials | fork | Python | LICENSE_UNCLEAR | 2018-09-15 | IRRELEVANT |
| repo-001571 | lxasqjc/OpenPNM | fork | Python | MIT | 2017-11-24 | HIGH_RELEVANCE |
| repo-001572 | lxasqjc/OpenPNM-Examples | fork | Python | MIT | 2017-07-05 | HIGH_RELEVANCE |
| repo-001573 | lxasqjc/pysc2 | fork | Python | Apache-2.0 | 2018-10-15 | LOW_RELEVANCE |
| repo-001574 | lxasqjc/s2client-api | fork | C++ | MIT | 2018-07-16 | LOW_RELEVANCE |
| repo-001575 | lxasqjc/s2client-proto | fork | Python | MIT | 2018-10-17 | LOW_RELEVANCE |
| repo-001576 | lxasqjc/Sleep-Switch | source | Python | LICENSE_UNCLEAR | 2018-10-07 | IRRELEVANT |
| repo-001577 | lxasqjc/STEGO | fork | Jupyter Notebook | MIT | 2023-03-24 | LOW_RELEVANCE |
| repo-001578 | lxasqjc/test | source | — | LICENSE_UNCLEAR | 2018-04-01 | IRRELEVANT |
| repo-001579 | lxasqjc/vlm-private | fork | Python | LICENSE_UNCLEAR | 2025-05-07 | POSSIBLE_RELEVANCE |
| repo-001580 | lxasqjc/website_detector | fork | Python | GPL-3.0 | 2020-03-16 | IRRELEVANT |

## Identity and scope boundary

- These repositories are owned by existing P accounts; their contributors do not
  expand P. Person depth remains exactly one.
- Fork-parent metadata is recorded, but fork status does not prove a unique change
  or feature. Existing Biomni fork archaeology remains canonical for the seven
  overlaps.
- `LICENSE_UNCLEAR` and `NOASSERTION` are not reuse permission.
- Metadata and repository content remain untrusted research data.

## Evidence and limits

- GraphQL captured owner totals/cursors, repository identity, fork/parent, default
  head/date, language, topics, license object, activity, archive/disabled state,
  stars/forks, disk usage, and latest public release.
- All 10 owner collections are exhausted at the observation time. Private,
  deleted, transferred, and subsequently created repositories are unobservable.
- Metadata relevance is an INFERENCE. HIGH and POSSIBLE entries still require
  source/README verification, deduplication, license review, and static security
  analysis before deep audit or integration ranking.
- Failed transport, gateway, and parser responses supplied no canonical metadata
  and are retained only as recovery context, not evidence.

## Next action

Continue the next stable-ID account batch, beginning with
`person-github-000021`–`000030`. Defer README disambiguation until broader
person-repository coverage advances.
