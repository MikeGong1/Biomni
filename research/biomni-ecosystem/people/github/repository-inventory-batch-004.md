# Public Repository Inventory for Code-visible People — Batch 004

Parent verification: `VERIFIED`. Scope:
`person-github-000032`–`000041`, all GitHub User accounts.

Fifteen successful serialized GraphQL responses returned all 500 public owner
repositories. Nine accounts fit on one page. The 100-node query for
shantanusharma was unstable, so the same full metadata surface was recovered in
six 50-node pages; the final page has `hasNextPage=false`, and the combined 277
nodes equal `totalCount`. Failed gateway and partial-transfer responses were
discarded. Requests remained sequential with two-second spacing. No repository
content or third-party code was executed.

## Coverage

| Person ID | Login | Public repositories | Existing IDs | New IDs | High | Possible | Low | Irrelevant | Cursor |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| person-github-000032 | SALhik | 14 | 1 | 13 | 3 | 2 | 0 | 9 | exhausted |
| person-github-000033 | sbonner0 | 27 | 1 | 26 | 5 | 1 | 18 | 3 | exhausted |
| person-github-000034 | serena2z | 6 | 0 | 6 | 2 | 1 | 0 | 3 | exhausted |
| person-github-000035 | shantanusharma | 277 | 1 | 276 | 41 | 37 | 141 | 58 | exhausted |
| person-github-000036 | shengyongniu | 36 | 1 | 35 | 16 | 3 | 2 | 15 | exhausted |
| person-github-000037 | shibahara-1113 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | exhausted |
| person-github-000038 | SnowLightPath | 4 | 1 | 3 | 2 | 1 | 0 | 1 | exhausted |
| person-github-000039 | th86 | 75 | 1 | 74 | 34 | 10 | 23 | 8 | exhausted |
| person-github-000040 | tuln128 | 8 | 1 | 7 | 5 | 3 | 0 | 0 | exhausted |
| person-github-000041 | vlln | 52 | 1 | 51 | 20 | 12 | 12 | 8 | exhausted |
| **Total** | **10 accounts** | **500** | **8** | **492** | **128** | **70** | **196** | **106** | **exhausted** |

Eight existing Biomni fork IDs are reused; serena2z and shibahara-1113 have no
current public Biomni owner fork in this batch. New repositories use contiguous
IDs `repo-001778`–`repo-002269`.

## Metadata screening

HIGH requires explicit biomedical, biological, omics, genetics, clinical, drug,
scientific-agent, MCP, Skills, benchmark, or matching scientific-infrastructure
metadata. POSSIBLE preserves uncertain adjacent entries. Generic ML/NLP/software
infrastructure without a domain signal is LOW; clearly unrelated sites, games,
templates, and utilities are IRRELEVANT.

The HIGH queue includes Biomni forks; biomedical NLP and knowledge-graph assets;
clinical, omics, genetics, single-cell, protein, drug and medical-imaging tools;
scientific agents/benchmarks; and directly named MCP or Skills infrastructure.
This is a breadth-first queue, not proof of feature uniqueness, stability, license
fitness, security, or integration value.

Metadata aggregate: 376 forks and 124 source repositories; none archived or
disabled; 12 expose a latest release; 125 have no affirmative SPDX object and 54
return `NOASSERTION`. All topic node counts equal `topics_total`. The 70
POSSIBLE entries remain pending bounded README disambiguation.

## Repository ledger

| Repository ID | Repository | Form | Language | Code license | Last push | Relevance |
|---|---|---|---|---|---|---|
| repo-001778 | SALhik/AutoPentester | source | Python | LICENSE_UNCLEAR | 2026-07-27 | IRRELEVANT |
| repo-001779 | SALhik/AutoPentester-fork-archive | fork | Python | LICENSE_UNCLEAR | 2026-03-11 | IRRELEVANT |
| repo-000493 | SALhik/Biomni | fork | Python | Apache-2.0 | 2025-08-25 | HIGH_RELEVANCE |
| repo-001780 | SALhik/Biomni_tests | source | Python | LICENSE_UNCLEAR | 2025-07-24 | HIGH_RELEVANCE |
| repo-001781 | SALhik/CueLight | source | Python | LICENSE_UNCLEAR | 2026-07-14 | IRRELEVANT |
| repo-001782 | SALhik/dify_biomni_plugin | source | Python | LICENSE_UNCLEAR | 2025-08-25 | HIGH_RELEVANCE |
| repo-001783 | SALhik/gemini-cli | fork | TypeScript | Apache-2.0 | 2026-04-29 | POSSIBLE_RELEVANCE |
| repo-001784 | SALhik/GeoFS-All-in-One-Addon_GeoFS-Nexus | source | JavaScript | MIT | 2026-04-06 | IRRELEVANT |
| repo-001785 | SALhik/kilocode | fork | TypeScript | Apache-2.0 | 2026-02-11 | POSSIBLE_RELEVANCE |
| repo-001786 | SALhik/kkv | source | — | LICENSE_UNCLEAR | 2025-07-10 | IRRELEVANT |
| repo-001787 | SALhik/personal-builds | fork | Dockerfile | GPL-3.0 | 2026-02-11 | IRRELEVANT |
| repo-001788 | SALhik/SALhik | source | TypeScript | LICENSE_UNCLEAR | 2026-02-10 | IRRELEVANT |
| repo-001789 | SALhik/The_Uni | fork | G-code | NOASSERTION | 2026-08-06 | IRRELEVANT |
| repo-001790 | SALhik/zhihu | fork | Python | NOASSERTION | 2026-07-30 | IRRELEVANT |
| repo-001791 | sbonner0/awesome-explainable-graph-reasoning | fork | — | Apache-2.0 | 2022-01-07 | LOW_RELEVANCE |
| repo-000704 | sbonner0/Biomni | fork | Python | Apache-2.0 | 2025-07-14 | HIGH_RELEVANCE |
| repo-001792 | sbonner0/boltz | fork | Python | MIT | 2026-03-29 | HIGH_RELEVANCE |
| repo-001793 | sbonner0/DeepTopologyClassification | source | Python | GPL-3.0 | 2020-11-25 | LOW_RELEVANCE |
| repo-001794 | sbonner0/dotfiles | source | Lua | LICENSE_UNCLEAR | 2026-07-05 | IRRELEVANT |
| repo-001795 | sbonner0/DynamicGEM | fork | Python | LICENSE_UNCLEAR | 2019-08-07 | LOW_RELEVANCE |
| repo-001796 | sbonner0/esm | fork | Python | MIT | 2021-10-22 | HIGH_RELEVANCE |
| repo-001797 | sbonner0/gae_in_pytorch | fork | Python | LICENSE_UNCLEAR | 2019-02-19 | LOW_RELEVANCE |
| repo-001798 | sbonner0/GFPX-GraphSimilarity | source | Scala | GPL-3.0 | 2020-10-24 | LOW_RELEVANCE |
| repo-001799 | sbonner0/GraphFingerprintComparison | source | Python | GPL-3.0 | 2020-10-12 | LOW_RELEVANCE |
| repo-001800 | sbonner0/hetionet | fork | HTML | LICENSE_UNCLEAR | 2025-04-17 | HIGH_RELEVANCE |
| repo-001801 | sbonner0/kge-jaxed | source | Python | LICENSE_UNCLEAR | 2026-06-11 | LOW_RELEVANCE |
| repo-001802 | sbonner0/NBFNet | fork | Python | MIT | 2022-07-27 | LOW_RELEVANCE |
| repo-001803 | sbonner0/NBFNet-PyG | fork | Python | MIT | 2023-06-02 | LOW_RELEVANCE |
| repo-001804 | sbonner0/Proteina-Complexa | fork | Python | NOASSERTION | 2026-07-11 | HIGH_RELEVANCE |
| repo-001805 | sbonner0/pykeen | fork | Python | MIT | 2025-04-29 | LOW_RELEVANCE |
| repo-001806 | sbonner0/pytorch-apex-experiment | fork | Python | MIT | 2019-09-03 | LOW_RELEVANCE |
| repo-001807 | sbonner0/pytorch_geometric | fork | Python | MIT | 2020-09-16 | LOW_RELEVANCE |
| repo-001808 | sbonner0/rexmex | fork | Python | LICENSE_UNCLEAR | 2023-06-02 | LOW_RELEVANCE |
| repo-001809 | sbonner0/RNNLogic | fork | Python | LICENSE_UNCLEAR | 2021-08-09 | LOW_RELEVANCE |
| repo-001810 | sbonner0/sbonner0 | source | — | LICENSE_UNCLEAR | 2021-11-09 | IRRELEVANT |
| repo-001811 | sbonner0/sbonner0.github.io | source | SCSS | MIT | 2026-07-29 | IRRELEVANT |
| repo-001812 | sbonner0/SemNetCon | source | Python | GPL-3.0 | 2016-05-04 | LOW_RELEVANCE |
| repo-001813 | sbonner0/skywalkR | fork | R | Apache-2.0 | 2022-02-23 | POSSIBLE_RELEVANCE |
| repo-001814 | sbonner0/temporal-neighbourhood-aggregation | source | Python | MIT | 2020-10-19 | LOW_RELEVANCE |
| repo-001815 | sbonner0/temporal-offset-reconstruction | source | Python | Apache-2.0 | 2020-06-26 | LOW_RELEVANCE |
| repo-001816 | sbonner0/unsupervised-graph-embedding | source | Python | MIT | 2020-10-19 | LOW_RELEVANCE |
| repo-001817 | serena2z/alc-website | source | TypeScript | MIT | 2025-05-06 | IRRELEVANT |
| repo-001818 | serena2z/medical-datasets | source | — | LICENSE_UNCLEAR | 2023-08-21 | HIGH_RELEVANCE |
| repo-001819 | serena2z/serena2z.github.io | source | JavaScript | LICENSE_UNCLEAR | 2024-06-09 | IRRELEVANT |
| repo-001820 | serena2z/skin_models | source | Python | MIT | 2025-02-04 | POSSIBLE_RELEVANCE |
| repo-001821 | serena2z/SkinGPT-4 | fork | Python | BSD-3-Clause | 2023-07-28 | HIGH_RELEVANCE |
| repo-001822 | serena2z/telephony | source | Python | LICENSE_UNCLEAR | 2024-04-03 | IRRELEVANT |
| repo-001823 | shantanusharma/A2A | fork | Shell | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-001824 | shantanusharma/adk-python | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001825 | shantanusharma/AFLplusplus | fork | C | AGPL-3.0 | 2026-08-22 | IRRELEVANT |
| repo-001826 | shantanusharma/agent-governance-toolkit | fork | Python | MIT | 2026-08-19 | LOW_RELEVANCE |
| repo-001827 | shantanusharma/agent-skills | fork | JavaScript | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-001828 | shantanusharma/Agentic_FinTech_Survey | fork | HTML | LICENSE_UNCLEAR | 2026-02-03 | IRRELEVANT |
| repo-001829 | shantanusharma/agentsmithy | fork | Python | Apache-2.0 | 2026-04-22 | LOW_RELEVANCE |
| repo-001830 | shantanusharma/ai-performance-engineering | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001831 | shantanusharma/AI-Scientist | fork | Jupyter Notebook | NOASSERTION | 2025-12-19 | HIGH_RELEVANCE |
| repo-001832 | shantanusharma/aider | fork | Python | Apache-2.0 | 2026-05-30 | LOW_RELEVANCE |
| repo-001833 | shantanusharma/ally-legal-assistant | fork | JavaScript | LICENSE_UNCLEAR | 2025-04-29 | IRRELEVANT |
| repo-001834 | shantanusharma/alphafold3 | fork | Python | Apache-2.0 | 2026-08-19 | HIGH_RELEVANCE |
| repo-001835 | shantanusharma/antigravity-cli | fork | — | LICENSE_UNCLEAR | 2026-07-24 | LOW_RELEVANCE |
| repo-001836 | shantanusharma/AP2 | fork | Python | Apache-2.0 | 2026-05-02 | IRRELEVANT |
| repo-001837 | shantanusharma/apisix | fork | Lua | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001838 | shantanusharma/arrow | fork | C++ | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001839 | shantanusharma/avro | fork | Java | Apache-2.0 | 2026-08-19 | IRRELEVANT |
| repo-001840 | shantanusharma/awesome-javascript | fork | — | LICENSE_UNCLEAR | 2026-08-19 | IRRELEVANT |
| repo-001841 | shantanusharma/Awesome-LLM-3D | fork | — | MIT | 2026-04-16 | LOW_RELEVANCE |
| repo-001842 | shantanusharma/awesome-mlops | fork | — | LICENSE_UNCLEAR | 2024-11-21 | LOW_RELEVANCE |
| repo-001843 | shantanusharma/awesome-nodejs | fork | — | CC0-1.0 | 2026-05-04 | IRRELEVANT |
| repo-001844 | shantanusharma/awesome-react | fork | — | LICENSE_UNCLEAR | 2026-08-22 | IRRELEVANT |
| repo-001845 | shantanusharma/awesome-scalability | fork | — | MIT | 2026-01-04 | IRRELEVANT |
| repo-001846 | shantanusharma/awsome-distributed-ai | fork | Shell | MIT-0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001847 | shantanusharma/azure-search-openai-demo | fork | Python | MIT | 2026-07-31 | LOW_RELEVANCE |
| repo-001848 | shantanusharma/beam | fork | Java | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001849 | shantanusharma/bedrock-chat | fork | TypeScript | MIT-0 | 2026-08-15 | LOW_RELEVANCE |
| repo-000549 | shantanusharma/Biomni | fork | Python | Apache-2.0 | 2026-01-18 | HIGH_RELEVANCE |
| repo-001850 | shantanusharma/bionemo-framework | fork | Python | LICENSE_UNCLEAR | 2026-08-23 | HIGH_RELEVANCE |
| repo-001851 | shantanusharma/blender | fork | C++ | NOASSERTION | 2026-08-22 | IRRELEVANT |
| repo-001852 | shantanusharma/boltz | fork | Python | MIT | 2025-10-03 | HIGH_RELEVANCE |
| repo-001853 | shantanusharma/brave-search-mcp-server | fork | TypeScript | MIT | 2026-08-22 | HIGH_RELEVANCE |
| repo-001854 | shantanusharma/calcite | fork | Java | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001855 | shantanusharma/ccxt | fork | Python | MIT | 2026-08-22 | IRRELEVANT |
| repo-001856 | shantanusharma/chainlit | fork | Python | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-001857 | shantanusharma/CHESS | fork | Python | Apache-2.0 | 2026-02-01 | LOW_RELEVANCE |
| repo-001858 | shantanusharma/claude-code | fork | Python | LICENSE_UNCLEAR | 2026-08-22 | LOW_RELEVANCE |
| repo-001859 | shantanusharma/claude-quickstarts | fork | Python | MIT | 2026-02-05 | LOW_RELEVANCE |
| repo-001860 | shantanusharma/clearml | fork | Python | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-001861 | shantanusharma/ClickHouse | fork | C++ | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001862 | shantanusharma/cline | fork | TypeScript | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001863 | shantanusharma/cluster-toolkit | fork | Go | Apache-2.0 | 2026-08-22 | HIGH_RELEVANCE |
| repo-001864 | shantanusharma/cog | fork | Go | Apache-2.0 | 2026-08-23 | LOW_RELEVANCE |
| repo-001865 | shantanusharma/cookbook | fork | Jupyter Notebook | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-001866 | shantanusharma/CoreNLP | fork | Java | GPL-3.0 | 2026-02-03 | LOW_RELEVANCE |
| repo-001867 | shantanusharma/crewAI | fork | Python | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-001868 | shantanusharma/crispr-gpt-pub | fork | Python | LICENSE_UNCLEAR | 2025-10-04 | HIGH_RELEVANCE |
| repo-001869 | shantanusharma/d3 | fork | Shell | ISC | 2025-12-02 | IRRELEVANT |
| repo-001870 | shantanusharma/datahub | fork | Python | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001871 | shantanusharma/DatawizzAI | fork | Python | MIT | 2024-10-29 | LOW_RELEVANCE |
| repo-001872 | shantanusharma/dbt-core | fork | Rust | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001873 | shantanusharma/dbt-utils | fork | Makefile | Apache-2.0 | 2026-01-13 | IRRELEVANT |
| repo-001874 | shantanusharma/deepagents | fork | Python | MIT | 2026-08-23 | LOW_RELEVANCE |
| repo-001875 | shantanusharma/deepchem | fork | Python | MIT | 2026-02-21 | HIGH_RELEVANCE |
| repo-001876 | shantanusharma/deepseek-harness | fork | TypeScript | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-001877 | shantanusharma/DeepSpeed | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001878 | shantanusharma/delta | fork | Scala | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001879 | shantanusharma/disruptor | fork | Java | Apache-2.0 | 2025-04-02 | IRRELEVANT |
| repo-001880 | shantanusharma/disruptor-rs | fork | Rust | MIT | 2026-08-15 | IRRELEVANT |
| repo-001881 | shantanusharma/dl-lowlat-infer | fork | Cuda | Apache-2.0 | 2026-04-13 | LOW_RELEVANCE |
| repo-001882 | shantanusharma/DORA | fork | TypeScript | NOASSERTION | 2026-01-07 | HIGH_RELEVANCE |
| repo-001883 | shantanusharma/dowhy | fork | Python | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001884 | shantanusharma/dspy | fork | Python | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-001885 | shantanusharma/duckdb | fork | C++ | MIT | 2026-08-22 | IRRELEVANT |
| repo-001886 | shantanusharma/dx | fork | Jupyter Notebook | AGPL-3.0 | 2025-04-05 | IRRELEVANT |
| repo-001887 | shantanusharma/electron | fork | C++ | MIT | 2026-08-22 | IRRELEVANT |
| repo-001888 | shantanusharma/eliza | fork | TypeScript | MIT | 2026-08-23 | LOW_RELEVANCE |
| repo-001889 | shantanusharma/evals | fork | Python | NOASSERTION | 2025-11-03 | HIGH_RELEVANCE |
| repo-001890 | shantanusharma/evo2 | fork | Jupyter Notebook | Apache-2.0 | 2026-06-21 | HIGH_RELEVANCE |
| repo-001891 | shantanusharma/excalidraw | fork | TypeScript | MIT | 2026-08-17 | IRRELEVANT |
| repo-001892 | shantanusharma/excalidraw-mcp | fork | TypeScript | LICENSE_UNCLEAR | 2026-03-24 | HIGH_RELEVANCE |
| repo-001893 | shantanusharma/fabric | fork | Go | Apache-2.0 | 2026-08-06 | LOW_RELEVANCE |
| repo-001894 | shantanusharma/fairseq | fork | Python | MIT | 2025-09-30 | LOW_RELEVANCE |
| repo-001895 | shantanusharma/faiss | fork | C++ | MIT | 2026-08-19 | LOW_RELEVANCE |
| repo-001896 | shantanusharma/fastai | fork | Jupyter Notebook | Apache-2.0 | 2026-08-15 | LOW_RELEVANCE |
| repo-001897 | shantanusharma/fastapi | fork | Python | MIT | 2026-08-19 | LOW_RELEVANCE |
| repo-001898 | shantanusharma/fastmcp | fork | Python | Apache-2.0 | 2026-08-22 | HIGH_RELEVANCE |
| repo-001899 | shantanusharma/feast | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001900 | shantanusharma/Finance-LLMs | fork | — | MIT | 2026-03-20 | IRRELEVANT |
| repo-001901 | shantanusharma/financial-services | fork | Python | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001902 | shantanusharma/FinGPT | fork | Jupyter Notebook | MIT | 2026-08-06 | IRRELEVANT |
| repo-001903 | shantanusharma/firecrawl | fork | TypeScript | AGPL-3.0 | 2026-08-23 | POSSIBLE_RELEVANCE |
| repo-001904 | shantanusharma/fish-shell | fork | Rust | NOASSERTION | 2026-08-22 | IRRELEVANT |
| repo-001905 | shantanusharma/flashinfer | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001906 | shantanusharma/flower | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001907 | shantanusharma/flyte | fork | Go | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001908 | shantanusharma/folly | fork | C++ | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001909 | shantanusharma/forem | fork | Ruby | AGPL-3.0 | 2026-08-22 | IRRELEVANT |
| repo-001910 | shantanusharma/ga-dev-tools | fork | TypeScript | NOASSERTION | 2026-01-29 | IRRELEVANT |
| repo-001911 | shantanusharma/garak | fork | Python | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001912 | shantanusharma/gatk | fork | Java | NOASSERTION | 2026-08-19 | HIGH_RELEVANCE |
| repo-001913 | shantanusharma/gemini-cli | fork | TypeScript | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001914 | shantanusharma/generative-ai | fork | Jupyter Notebook | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001915 | shantanusharma/generative-protein-binder-design | fork | Jupyter Notebook | NOASSERTION | 2026-07-18 | HIGH_RELEVANCE |
| repo-001916 | shantanusharma/generative-ui-demo | source | Python | Apache-2.0 | 2026-03-19 | LOW_RELEVANCE |
| repo-001917 | shantanusharma/generative-virtual-screening | fork | Jupyter Notebook | Apache-2.0 | 2025-11-07 | HIGH_RELEVANCE |
| repo-001918 | shantanusharma/gin | fork | Go | MIT | 2026-08-15 | LOW_RELEVANCE |
| repo-001919 | shantanusharma/glommio | fork | Rust | NOASSERTION | 2025-04-29 | LOW_RELEVANCE |
| repo-001920 | shantanusharma/google-research | fork | Jupyter Notebook | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001921 | shantanusharma/googletest | fork | C++ | BSD-3-Clause | 2026-08-22 | LOW_RELEVANCE |
| repo-001922 | shantanusharma/goose | fork | Rust | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001923 | shantanusharma/grafana | fork | TypeScript | AGPL-3.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001924 | shantanusharma/graphql-engine | fork | TypeScript | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-001925 | shantanusharma/Gymnasium | fork | Python | MIT | 2026-07-09 | LOW_RELEVANCE |
| repo-001926 | shantanusharma/h2o-3 | fork | Jupyter Notebook | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001927 | shantanusharma/h4cker | fork | Jupyter Notebook | MIT | 2026-08-15 | IRRELEVANT |
| repo-001928 | shantanusharma/haproxy | fork | C | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-001929 | shantanusharma/headroom | fork | Python | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001930 | shantanusharma/helm | fork | Python | Apache-2.0 | 2026-06-06 | HIGH_RELEVANCE |
| repo-001931 | shantanusharma/hudi | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001932 | shantanusharma/hyena-dna | fork | Assembly | Apache-2.0 | 2023-12-04 | HIGH_RELEVANCE |
| repo-001933 | shantanusharma/hyperlight | fork | Rust | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001934 | shantanusharma/i4h-workflows | fork | Python | Apache-2.0 | 2026-07-25 | HIGH_RELEVANCE |
| repo-001935 | shantanusharma/iceberg | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001936 | shantanusharma/immutable-js | fork | TypeScript | MIT | 2026-08-17 | LOW_RELEVANCE |
| repo-001937 | shantanusharma/Isaac-GR00T | fork | Python | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001938 | shantanusharma/istio | fork | Go | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001939 | shantanusharma/ivy | fork | Python | NOASSERTION | 2026-02-08 | LOW_RELEVANCE |
| repo-001940 | shantanusharma/jax | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001941 | shantanusharma/jena | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001942 | shantanusharma/johnsnowlabs | fork | Python | NOASSERTION | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001943 | shantanusharma/kafka | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001944 | shantanusharma/kaggle | source | Jupyter Notebook | Apache-2.0 | 2024-02-19 | IRRELEVANT |
| repo-001945 | shantanusharma/kubeflow | fork | — | Apache-2.0 | 2026-01-05 | LOW_RELEVANCE |
| repo-001946 | shantanusharma/kubernetes | fork | Go | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001947 | shantanusharma/lakeFS | fork | Go | Apache-2.0 | 2026-08-16 | LOW_RELEVANCE |
| repo-001948 | shantanusharma/lancedb | fork | Rust | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001949 | shantanusharma/langchain | fork | Python | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001950 | shantanusharma/latch | fork | Python | MIT | 2026-08-19 | HIGH_RELEVANCE |
| repo-001951 | shantanusharma/legend | fork | HTML | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-001952 | shantanusharma/leveldb | fork | C++ | BSD-3-Clause | 2026-03-11 | LOW_RELEVANCE |
| repo-001953 | shantanusharma/libevent | fork | C | NOASSERTION | 2026-07-31 | LOW_RELEVANCE |
| repo-001954 | shantanusharma/lidar | fork | Python | MIT | 2026-01-27 | HIGH_RELEVANCE |
| repo-001955 | shantanusharma/life-sciences | fork | Python | LICENSE_UNCLEAR | 2026-07-25 | HIGH_RELEVANCE |
| repo-001956 | shantanusharma/LightRAG | fork | Python | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001957 | shantanusharma/linux | fork | C | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-001958 | shantanusharma/litellm | fork | Python | NOASSERTION | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001959 | shantanusharma/liteparse | fork | Rust | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001960 | shantanusharma/livekit | fork | Go | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001961 | shantanusharma/llama.cpp | fork | C++ | MIT | 2026-08-23 | LOW_RELEVANCE |
| repo-001962 | shantanusharma/llama_index | fork | Python | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001963 | shantanusharma/LLaVA-Plus-Codebase | fork | Python | Apache-2.0 | 2026-02-08 | POSSIBLE_RELEVANCE |
| repo-001964 | shantanusharma/LLMs-in-Finance | fork | Jupyter Notebook | MIT | 2026-02-24 | IRRELEVANT |
| repo-001965 | shantanusharma/lm-evaluation-harness | fork | Python | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-001966 | shantanusharma/lorax | fork | Python | Apache-2.0 | 2026-02-08 | LOW_RELEVANCE |
| repo-001967 | shantanusharma/lxc | fork | C | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-001968 | shantanusharma/machine-learning-for-trading | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2024-08-18 | IRRELEVANT |
| repo-001969 | shantanusharma/MegaSparkDiff | fork | Scala | Apache-2.0 | 2025-06-17 | LOW_RELEVANCE |
| repo-001970 | shantanusharma/mem0 | fork | Python | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001971 | shantanusharma/mermaid | fork | TypeScript | MIT | 2026-08-22 | IRRELEVANT |
| repo-001972 | shantanusharma/mermaid-to-excalidraw | fork | TypeScript | MIT | 2026-03-24 | IRRELEVANT |
| repo-001973 | shantanusharma/metasploit-framework | fork | Ruby | NOASSERTION | 2026-08-22 | IRRELEVANT |
| repo-001974 | shantanusharma/milvus | fork | Go | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001975 | shantanusharma/mindsdb | fork | Makefile | MIT | 2026-07-13 | HIGH_RELEVANCE |
| repo-001976 | shantanusharma/mlflow | fork | Python | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001977 | shantanusharma/mlops-on-gcp | fork | Jupyter Notebook | Apache-2.0 | 2026-02-08 | LOW_RELEVANCE |
| repo-001978 | shantanusharma/moby | fork | Go | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001979 | shantanusharma/Model-Optimizer | fork | Python | Apache-2.0 | 2026-08-23 | LOW_RELEVANCE |
| repo-001980 | shantanusharma/modin | fork | Python | Apache-2.0 | 2026-02-12 | LOW_RELEVANCE |
| repo-001981 | shantanusharma/mujoco | fork | C++ | Apache-2.0 | 2026-08-22 | HIGH_RELEVANCE |
| repo-001982 | shantanusharma/n8n | fork | TypeScript | NOASSERTION | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001983 | shantanusharma/nanoGPT | fork | Python | MIT | 2025-11-12 | LOW_RELEVANCE |
| repo-001984 | shantanusharma/nebius-serverless-cookbook | fork | Python | MIT | 2026-05-16 | LOW_RELEVANCE |
| repo-001985 | shantanusharma/NeMo | fork | Python | Apache-2.0 | 2026-08-23 | LOW_RELEVANCE |
| repo-001986 | shantanusharma/NeMo-Agent-Toolkit | fork | Python | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001987 | shantanusharma/NeMo-Guardrails | fork | Python | NOASSERTION | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-001988 | shantanusharma/NemoClaw | fork | TypeScript | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001989 | shantanusharma/netty | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001990 | shantanusharma/neuralforecast | fork | Python | Apache-2.0 | 2026-08-17 | LOW_RELEVANCE |
| repo-001991 | shantanusharma/nifi | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001992 | shantanusharma/nix | fork | C++ | LGPL-2.1 | 2026-08-22 | LOW_RELEVANCE |
| repo-001993 | shantanusharma/nltk | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001994 | shantanusharma/node | fork | JavaScript | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-001995 | shantanusharma/notepad-plus-plus | fork | C++ | NOASSERTION | 2026-08-22 | IRRELEVANT |
| repo-001996 | shantanusharma/nuclei | fork | Go | MIT | 2026-08-22 | IRRELEVANT |
| repo-001997 | shantanusharma/numpy | fork | Python | NOASSERTION | 2026-08-22 | HIGH_RELEVANCE |
| repo-001998 | shantanusharma/NVFlare | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-001999 | shantanusharma/onnxruntime | fork | C++ | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-002000 | shantanusharma/openai | fork | Jupyter Notebook | MIT | 2026-02-01 | LOW_RELEVANCE |
| repo-002001 | shantanusharma/openai-agents-python | fork | Python | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002002 | shantanusharma/OpenBB | fork | Python | NOASSERTION | 2026-07-22 | IRRELEVANT |
| repo-002003 | shantanusharma/openclaw | fork | TypeScript | NOASSERTION | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002004 | shantanusharma/openfe | fork | Python | MIT | 2026-08-19 | HIGH_RELEVANCE |
| repo-002005 | shantanusharma/openfold-3 | fork | Python | Apache-2.0 | 2026-08-22 | HIGH_RELEVANCE |
| repo-002006 | shantanusharma/OpenHands | fork | TypeScript | MIT | 2026-08-22 | IRRELEVANT |
| repo-002007 | shantanusharma/OpenManus | fork | Python | MIT | 2026-02-11 | POSSIBLE_RELEVANCE |
| repo-002008 | shantanusharma/OpenShell | fork | Rust | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002009 | shantanusharma/opentrons | fork | Python | Apache-2.0 | 2026-08-22 | HIGH_RELEVANCE |
| repo-002010 | shantanusharma/openvino | fork | C++ | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002011 | shantanusharma/openvino_notebooks | fork | Jupyter Notebook | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002012 | shantanusharma/orientdb | fork | Java | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-002013 | shantanusharma/oss-fuzz-gen | fork | Python | Apache-2.0 | 2026-03-02 | IRRELEVANT |
| repo-002014 | shantanusharma/pandas | fork | Python | BSD-3-Clause | 2026-08-22 | LOW_RELEVANCE |
| repo-002015 | shantanusharma/pandoc | fork | Haskell | GPL-2.0 | 2026-08-22 | IRRELEVANT |
| repo-002016 | shantanusharma/pdf.js | fork | JavaScript | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-002017 | shantanusharma/phoenix | fork | Python | NOASSERTION | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002018 | shantanusharma/pinot | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002019 | shantanusharma/playwright | fork | TypeScript | Apache-2.0 | 2026-08-22 | IRRELEVANT |
| repo-002020 | shantanusharma/playwright-mcp | fork | TypeScript | Apache-2.0 | 2026-08-19 | HIGH_RELEVANCE |
| repo-002021 | shantanusharma/podman | fork | Go | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002022 | shantanusharma/polars | fork | Rust | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-002023 | shantanusharma/prefect | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002024 | shantanusharma/presto | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002025 | shantanusharma/promptfoo | fork | TypeScript | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002026 | shantanusharma/public-apis | fork | Python | MIT | 2026-08-19 | LOW_RELEVANCE |
| repo-002027 | shantanusharma/pydantic-ai | fork | Python | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002028 | shantanusharma/pylabrobot | fork | Python | MIT | 2026-08-22 | HIGH_RELEVANCE |
| repo-002029 | shantanusharma/python-training | fork | Jupyter Notebook | Apache-2.0 | 2024-07-17 | IRRELEVANT |
| repo-002030 | shantanusharma/pytorch | fork | Python | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-002031 | shantanusharma/pytorch-lightning | fork | Python | Apache-2.0 | 2026-08-15 | LOW_RELEVANCE |
| repo-002032 | shantanusharma/qiskit | fork | Python | Apache-2.0 | 2026-08-22 | HIGH_RELEVANCE |
| repo-002033 | shantanusharma/QuantLib | fork | C++ | NOASSERTION | 2026-08-22 | IRRELEVANT |
| repo-002034 | shantanusharma/quickfix | fork | C++ | NOASSERTION | 2026-05-30 | IRRELEVANT |
| repo-002035 | shantanusharma/quickfixj | fork | Java | NOASSERTION | 2026-08-17 | IRRELEVANT |
| repo-002036 | shantanusharma/rag | fork | Python | Apache-2.0 | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002037 | shantanusharma/rasa | fork | Python | Apache-2.0 | 2026-01-29 | LOW_RELEVANCE |
| repo-002038 | shantanusharma/ray | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002039 | shantanusharma/rdflib | fork | Python | BSD-3-Clause | 2026-05-07 | LOW_RELEVANCE |
| repo-002040 | shantanusharma/recipes | fork | JavaScript | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002041 | shantanusharma/recommenders | fork | Python | MIT | 2026-05-30 | LOW_RELEVANCE |
| repo-002042 | shantanusharma/redash | fork | Python | BSD-2-Clause | 2026-08-19 | LOW_RELEVANCE |
| repo-002043 | shantanusharma/redis | fork | C | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-002044 | shantanusharma/redpanda | fork | C++ | LICENSE_UNCLEAR | 2026-08-22 | LOW_RELEVANCE |
| repo-002045 | shantanusharma/reward_maximizing_ranking | fork | Python | GPL-3.0 | 2026-02-01 | LOW_RELEVANCE |
| repo-002046 | shantanusharma/rig | fork | Rust | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002047 | shantanusharma/RNAGenesis | fork | Jupyter Notebook | MIT | 2025-08-29 | HIGH_RELEVANCE |
| repo-002048 | shantanusharma/RNAPro | fork | Python | Apache-2.0 | 2026-01-17 | HIGH_RELEVANCE |
| repo-002049 | shantanusharma/rosetta | fork | C++ | NOASSERTION | 2026-08-19 | HIGH_RELEVANCE |
| repo-002050 | shantanusharma/rust | fork | Rust | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002051 | shantanusharma/rust-sdk | fork | Rust | NOASSERTION | 2026-08-22 | HIGH_RELEVANCE |
| repo-002052 | shantanusharma/rustdesk | fork | Rust | AGPL-3.0 | 2026-08-22 | IRRELEVANT |
| repo-002053 | shantanusharma/sam3 | fork | Python | NOASSERTION | 2026-08-15 | LOW_RELEVANCE |
| repo-002054 | shantanusharma/sample-agentic-insurance-claims-processing-eks | fork | Python | MIT-0 | 2025-11-26 | POSSIBLE_RELEVANCE |
| repo-002055 | shantanusharma/samtools | fork | C | NOASSERTION | 2026-08-22 | HIGH_RELEVANCE |
| repo-002056 | shantanusharma/scikit-digital-health | fork | Python | MIT | 2026-07-31 | HIGH_RELEVANCE |
| repo-002057 | shantanusharma/scikit-learn | fork | Python | BSD-3-Clause | 2026-08-22 | LOW_RELEVANCE |
| repo-002058 | shantanusharma/scylladb | fork | C++ | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-002059 | shantanusharma/seastar | fork | C++ | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-002060 | shantanusharma/servers | fork | TypeScript | NOASSERTION | 2026-08-19 | HIGH_RELEVANCE |
| repo-002061 | shantanusharma/sglang | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002062 | shantanusharma/shantanusharma | source | — | LICENSE_UNCLEAR | 2026-05-20 | IRRELEVANT |
| repo-002063 | shantanusharma/shantanusharma.github.io | source | HTML | LICENSE_UNCLEAR | 2025-12-24 | IRRELEVANT |
| repo-002064 | shantanusharma/skills | fork | Shell | MIT | 2026-08-22 | HIGH_RELEVANCE |
| repo-002065 | shantanusharma/snowflake-cli | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002066 | shantanusharma/snowpark-python | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002067 | shantanusharma/spaCy | fork | Python | MIT | 2026-05-30 | LOW_RELEVANCE |
| repo-002068 | shantanusharma/spark | fork | Scala | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002069 | shantanusharma/spark-nlp | fork | Scala | Apache-2.0 | 2026-07-09 | LOW_RELEVANCE |
| repo-002070 | shantanusharma/spec-kit | fork | Python | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-002071 | shantanusharma/squad | fork | TypeScript | MIT | 2026-08-22 | POSSIBLE_RELEVANCE |
| repo-002072 | shantanusharma/streamlit | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002073 | shantanusharma/Surprise | fork | Python | BSD-3-Clause | 2025-07-24 | LOW_RELEVANCE |
| repo-002074 | shantanusharma/SWE-agent | fork | Python | MIT | 2026-07-19 | POSSIBLE_RELEVANCE |
| repo-002075 | shantanusharma/TabPFN | fork | Python | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-002076 | shantanusharma/temporal | fork | Go | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-002077 | shantanusharma/tensorflow | fork | C++ | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002078 | shantanusharma/TensorRT-LLM | fork | Python | NOASSERTION | 2026-08-22 | LOW_RELEVANCE |
| repo-002079 | shantanusharma/thirdeye | fork | TypeScript | NOASSERTION | 2025-05-07 | LOW_RELEVANCE |
| repo-002080 | shantanusharma/thrift | fork | C++ | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002081 | shantanusharma/tokio | fork | Rust | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-002082 | shantanusharma/torch-sim | fork | Python | MIT | 2026-08-22 | HIGH_RELEVANCE |
| repo-002083 | shantanusharma/torchrec | fork | Python | BSD-3-Clause | 2026-08-22 | LOW_RELEVANCE |
| repo-002084 | shantanusharma/trade-surveillance-swarm | source | Python | MIT | 2026-02-06 | POSSIBLE_RELEVANCE |
| repo-002085 | shantanusharma/TradingAgents | fork | Python | Apache-2.0 | 2026-07-18 | POSSIBLE_RELEVANCE |
| repo-002086 | shantanusharma/transformers | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002087 | shantanusharma/triton | fork | MLIR | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-002088 | shantanusharma/trusted-agent-protocol | fork | Python | NOASSERTION | 2025-10-28 | POSSIBLE_RELEVANCE |
| repo-002089 | shantanusharma/typingmind | fork | HTML | NOASSERTION | 2026-07-25 | LOW_RELEVANCE |
| repo-002090 | shantanusharma/typst | fork | Rust | Apache-2.0 | 2026-08-17 | LOW_RELEVANCE |
| repo-002091 | shantanusharma/ultralytics | fork | Python | AGPL-3.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002092 | shantanusharma/unilm | fork | Python | MIT | 2026-01-23 | LOW_RELEVANCE |
| repo-002093 | shantanusharma/vertex-ai-samples | fork | Jupyter Notebook | Apache-2.0 | 2026-08-19 | LOW_RELEVANCE |
| repo-002094 | shantanusharma/vllm | fork | Python | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002095 | shantanusharma/vscode | fork | TypeScript | MIT | 2026-08-22 | IRRELEVANT |
| repo-002096 | shantanusharma/WindowsAppSDK | fork | C++ | MIT | 2026-08-19 | IRRELEVANT |
| repo-002097 | shantanusharma/wiremock | fork | Java | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002098 | shantanusharma/xgboost | fork | C++ | Apache-2.0 | 2026-08-22 | LOW_RELEVANCE |
| repo-002099 | shengyongniu/106-CD-project | fork | Yacc | LICENSE_UNCLEAR | 2018-06-11 | IRRELEVANT |
| repo-002100 | shengyongniu/agentgrade | source | Python | MIT | 2026-06-28 | POSSIBLE_RELEVANCE |
| repo-002101 | shengyongniu/ai-coscientist-protein | source | Python | MIT | 2026-07-08 | HIGH_RELEVANCE |
| repo-002102 | shengyongniu/ARGMap | source | Shell | LICENSE_UNCLEAR | 2017-02-05 | HIGH_RELEVANCE |
| repo-000646 | shengyongniu/Biomni | fork | Python | Apache-2.0 | 2025-08-16 | HIGH_RELEVANCE |
| repo-002103 | shengyongniu/bitcoinbook | fork | AsciiDoc | NOASSERTION | 2022-07-06 | IRRELEVANT |
| repo-002104 | shengyongniu/bulk_ATAC_seq | source | Shell | LICENSE_UNCLEAR | 2018-09-15 | HIGH_RELEVANCE |
| repo-002105 | shengyongniu/bulk_RNA_seq_count_base | source | R | LICENSE_UNCLEAR | 2017-11-15 | HIGH_RELEVANCE |
| repo-002106 | shengyongniu/bulk_rna_seq_tophat | source | R | LICENSE_UNCLEAR | 2018-09-15 | HIGH_RELEVANCE |
| repo-002107 | shengyongniu/cedb9569a64c7c97 | source | Python | LICENSE_UNCLEAR | 2026-03-16 | IRRELEVANT |
| repo-002108 | shengyongniu/cemba_data | fork | Python | MIT | 2018-12-29 | POSSIBLE_RELEVANCE |
| repo-002109 | shengyongniu/eQTL | fork | R | LICENSE_UNCLEAR | 2018-09-10 | HIGH_RELEVANCE |
| repo-002110 | shengyongniu/first-contributions | fork | JavaScript | MIT | 2018-04-16 | IRRELEVANT |
| repo-002111 | shengyongniu/google-maps-services-python | fork | Python | Apache-2.0 | 2020-04-27 | IRRELEVANT |
| repo-002112 | shengyongniu/igv | fork | Java | MIT | 2017-05-29 | HIGH_RELEVANCE |
| repo-002113 | shengyongniu/LearnPython | fork | Python | LICENSE_UNCLEAR | 2018-04-15 | IRRELEVANT |
| repo-002114 | shengyongniu/llm-serving-mlops | source | Python | MIT | 2026-06-29 | LOW_RELEVANCE |
| repo-002115 | shengyongniu/Machine-Learning-Interviews | fork | Jupyter Notebook | MIT | 2025-11-28 | IRRELEVANT |
| repo-002116 | shengyongniu/mcp.science | fork | Python | MIT | 2025-06-21 | HIGH_RELEVANCE |
| repo-002117 | shengyongniu/mergedna | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-05-18 | HIGH_RELEVANCE |
| repo-002118 | shengyongniu/MIMOSCA | fork | Jupyter Notebook | MIT | 2019-07-31 | HIGH_RELEVANCE |
| repo-002119 | shengyongniu/ML2ClinicalTrials | fork | Python | MIT | 2025-07-12 | HIGH_RELEVANCE |
| repo-002120 | shengyongniu/multimodal-rag | source | Python | LICENSE_UNCLEAR | 2026-07-07 | HIGH_RELEVANCE |
| repo-002121 | shengyongniu/neetcode-gpt | source | Python | LICENSE_UNCLEAR | 2026-08-03 | IRRELEVANT |
| repo-002122 | shengyongniu/practical-python | fork | Python | CC-BY-SA-4.0 | 2024-08-10 | IRRELEVANT |
| repo-002123 | shengyongniu/programming_language_cpp | source | C++ | LICENSE_UNCLEAR | 2017-10-26 | IRRELEVANT |
| repo-002124 | shengyongniu/robin | fork | Python | Apache-2.0 | 2025-06-14 | HIGH_RELEVANCE |
| repo-002125 | shengyongniu/rSeqTU | source | R | MIT | 2019-04-29 | HIGH_RELEVANCE |
| repo-002126 | shengyongniu/SeqTU | source | R | LICENSE_UNCLEAR | 2018-09-10 | HIGH_RELEVANCE |
| repo-002127 | shengyongniu/shengyongniu.github.io | source | JavaScript | MIT | 2020-07-30 | IRRELEVANT |
| repo-002128 | shengyongniu/stardew-vla | source | Python | LICENSE_UNCLEAR | 2026-07-07 | LOW_RELEVANCE |
| repo-002129 | shengyongniu/swarmtrainer | source | Python | MIT | 2026-07-07 | POSSIBLE_RELEVANCE |
| repo-002130 | shengyongniu/tahoe_hackathon | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-05-10 | IRRELEVANT |
| repo-002131 | shengyongniu/TorchCode | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2026-03-27 | IRRELEVANT |
| repo-002132 | shengyongniu/TorchLeet | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2026-01-19 | IRRELEVANT |
| repo-002133 | shengyongniu/v4 | fork | JavaScript | MIT | 2020-06-06 | IRRELEVANT |
| repo-002134 | shibahara-1113/pwl | source | Python | LICENSE_UNCLEAR | 2023-05-22 | IRRELEVANT |
| repo-000591 | SnowLightPath/Biomni | fork | Python | Apache-2.0 | 2025-08-03 | HIGH_RELEVANCE |
| repo-002135 | SnowLightPath/DDL | source | — | NOASSERTION | 2026-04-25 | IRRELEVANT |
| repo-002136 | SnowLightPath/extended-mind | source | JavaScript | MIT | 2026-04-05 | HIGH_RELEVANCE |
| repo-002137 | SnowLightPath/snow-light-place | source | — | Apache-2.0 | 2026-02-21 | POSSIBLE_RELEVANCE |
| repo-002138 | th86/agentskill-nyc-cameras | source | Python | LICENSE_UNCLEAR | 2026-06-10 | IRRELEVANT |
| repo-002139 | th86/AlexaLittleLight | source | Python | LICENSE_UNCLEAR | 2018-04-28 | POSSIBLE_RELEVANCE |
| repo-002140 | th86/andrej-karpathy-skills | fork | — | LICENSE_UNCLEAR | 2026-04-20 | LOW_RELEVANCE |
| repo-002141 | th86/ArduinoGoogleSheetAirQualityMonitor | source | Arduino | LICENSE_UNCLEAR | 2017-04-05 | HIGH_RELEVANCE |
| repo-002142 | th86/awesome-ai-agents-2026 | fork | — | NOASSERTION | 2026-03-26 | LOW_RELEVANCE |
| repo-002143 | th86/awesome-chatgpt-prompts | fork | JavaScript | CC0-1.0 | 2025-09-11 | LOW_RELEVANCE |
| repo-002144 | th86/awesome-single-cell | fork | — | MIT | 2018-03-14 | HIGH_RELEVANCE |
| repo-002145 | th86/awesome_bioinfo | source | — | LICENSE_UNCLEAR | 2025-09-15 | HIGH_RELEVANCE |
| repo-002146 | th86/BindCraft | fork | Python | MIT | 2025-08-12 | HIGH_RELEVANCE |
| repo-000546 | th86/Biomni | fork | Python | Apache-2.0 | 2025-07-29 | HIGH_RELEVANCE |
| repo-002147 | th86/BioSearch | source | JavaScript | LICENSE_UNCLEAR | 2016-10-12 | HIGH_RELEVANCE |
| repo-002148 | th86/bits-to-binders-resources | fork | — | LICENSE_UNCLEAR | 2024-08-24 | HIGH_RELEVANCE |
| repo-002149 | th86/cafr | fork | R | LICENSE_UNCLEAR | 2015-09-10 | POSSIBLE_RELEVANCE |
| repo-002150 | th86/CAR_T_TargetIdentification | fork | Jupyter Notebook | MIT | 2022-12-25 | HIGH_RELEVANCE |
| repo-002151 | th86/cell-eval2 | fork | Python | MIT | 2026-08-20 | HIGH_RELEVANCE |
| repo-002152 | th86/ColabFold | fork | Jupyter Notebook | MIT | 2025-08-26 | HIGH_RELEVANCE |
| repo-002153 | th86/concordanceIndex | source | C | LICENSE_UNCLEAR | 2019-02-03 | POSSIBLE_RELEVANCE |
| repo-002154 | th86/DC-Step-Up-Board | source | Eagle | LICENSE_UNCLEAR | 2015-11-13 | IRRELEVANT |
| repo-002155 | th86/DeterministicAttractor | source | R | LICENSE_UNCLEAR | 2014-06-28 | POSSIBLE_RELEVANCE |
| repo-002156 | th86/DrugDevAgent | source | JavaScript | LICENSE_UNCLEAR | 2026-02-12 | HIGH_RELEVANCE |
| repo-002157 | th86/ehrapy | fork | Python | Apache-2.0 | 2025-09-07 | HIGH_RELEVANCE |
| repo-002158 | th86/ESP8266RemoteController | source | Lua | LICENSE_UNCLEAR | 2015-09-06 | IRRELEVANT |
| repo-002159 | th86/ESP8266ServerMonitor | source | Lua | LICENSE_UNCLEAR | 2015-09-06 | IRRELEVANT |
| repo-002160 | th86/ezMA | source | R | LICENSE_UNCLEAR | 2013-12-06 | HIGH_RELEVANCE |
| repo-002161 | th86/freeagent | source | TypeScript | LICENSE_UNCLEAR | 2026-01-14 | POSSIBLE_RELEVANCE |
| repo-002162 | th86/freebot | source | TypeScript | LICENSE_UNCLEAR | 2026-01-14 | POSSIBLE_RELEVANCE |
| repo-002163 | th86/genagent | source | JavaScript | LICENSE_UNCLEAR | 2026-02-25 | LOW_RELEVANCE |
| repo-002164 | th86/GeneAgent | fork | Python | NOASSERTION | 2025-08-08 | HIGH_RELEVANCE |
| repo-002165 | th86/ggbio | source | R | LICENSE_UNCLEAR | 2013-05-22 | POSSIBLE_RELEVANCE |
| repo-002166 | th86/gislkit | source | R | LICENSE_UNCLEAR | 2018-10-09 | HIGH_RELEVANCE |
| repo-002167 | th86/gpt-oss | fork | Python | Apache-2.0 | 2025-08-05 | LOW_RELEVANCE |
| repo-002168 | th86/ImmuneBuilder | fork | Jupyter Notebook | BSD-3-Clause | 2025-01-28 | HIGH_RELEVANCE |
| repo-002169 | th86/knowledge-work-plugins | fork | Python | Apache-2.0 | 2026-02-04 | LOW_RELEVANCE |
| repo-002170 | th86/Large-Language-Model-Notebooks-Course | fork | Jupyter Notebook | MIT | 2025-05-19 | LOW_RELEVANCE |
| repo-002171 | th86/lfm2-web-search-agent | source | Python | LICENSE_UNCLEAR | 2026-06-29 | LOW_RELEVANCE |
| repo-002172 | th86/local_llm_agents | source | Python | LICENSE_UNCLEAR | 2025-11-11 | LOW_RELEVANCE |
| repo-002173 | th86/Mask_RCNN | fork | Jupyter Notebook | NOASSERTION | 2018-02-21 | LOW_RELEVANCE |
| repo-002174 | th86/MedCPT | fork | Python | NOASSERTION | 2024-03-24 | HIGH_RELEVANCE |
| repo-002175 | th86/minimind | fork | Python | Apache-2.0 | 2025-04-30 | LOW_RELEVANCE |
| repo-002176 | th86/mlx_llm_training | source | Python | LICENSE_UNCLEAR | 2026-06-03 | LOW_RELEVANCE |
| repo-002177 | th86/mobile-use | fork | Python | MIT | 2025-08-20 | LOW_RELEVANCE |
| repo-002178 | th86/Mods-for-mini-machine-shop | source | — | LICENSE_UNCLEAR | 2016-01-03 | IRRELEVANT |
| repo-002179 | th86/monocle-release | fork | R | LICENSE_UNCLEAR | 2017-11-29 | HIGH_RELEVANCE |
| repo-002180 | th86/multicoreR | source | R | LICENSE_UNCLEAR | 2014-12-16 | LOW_RELEVANCE |
| repo-002181 | th86/nanochat | fork | Python | MIT | 2026-01-11 | LOW_RELEVANCE |
| repo-002182 | th86/nanocoder | fork | TypeScript | LICENSE_UNCLEAR | 2025-08-15 | LOW_RELEVANCE |
| repo-002183 | th86/nanoGPT | fork | Python | MIT | 2024-12-09 | LOW_RELEVANCE |
| repo-002184 | th86/nemotron_finetune | fork | Python | LICENSE_UNCLEAR | 2026-04-27 | LOW_RELEVANCE |
| repo-002185 | th86/NYSubwayCountdownClock | source | Python | LICENSE_UNCLEAR | 2018-01-10 | IRRELEVANT |
| repo-002186 | th86/oagent | source | Python | LICENSE_UNCLEAR | 2026-04-28 | LOW_RELEVANCE |
| repo-002187 | th86/OpenClaw_Container | source | — | LICENSE_UNCLEAR | 2026-02-02 | LOW_RELEVANCE |
| repo-002188 | th86/OpenCode-ST | source | Python | LICENSE_UNCLEAR | 2026-01-22 | HIGH_RELEVANCE |
| repo-002189 | th86/OpenCode-TCRSeq-ML-pipeline | source | HTML | LICENSE_UNCLEAR | 2026-01-19 | HIGH_RELEVANCE |
| repo-002190 | th86/papers_for_protein_design_using_DL | fork | — | GPL-3.0 | 2025-08-23 | HIGH_RELEVANCE |
| repo-002191 | th86/parameter-golf | fork | Python | MIT | 2026-04-28 | LOW_RELEVANCE |
| repo-002192 | th86/predict-airr | fork | Python | LICENSE_UNCLEAR | 2025-11-04 | HIGH_RELEVANCE |
| repo-002193 | th86/progEval | source | R | LICENSE_UNCLEAR | 2013-06-28 | HIGH_RELEVANCE |
| repo-002194 | th86/ProteomeLM | fork | Jupyter Notebook | Apache-2.0 | 2025-08-15 | HIGH_RELEVANCE |
| repo-002195 | th86/pymutualinformation | source | Python | LICENSE_UNCLEAR | 2025-09-22 | HIGH_RELEVANCE |
| repo-002196 | th86/pytorch_ehr | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2024-01-22 | HIGH_RELEVANCE |
| repo-002197 | th86/RFdiffusion | fork | Python | NOASSERTION | 2025-07-16 | HIGH_RELEVANCE |
| repo-002198 | th86/SCUMIKit | source | Shell | MIT | 2015-12-12 | HIGH_RELEVANCE |
| repo-002199 | th86/seaad_task1 | source | Python | LICENSE_UNCLEAR | 2025-11-03 | POSSIBLE_RELEVANCE |
| repo-002200 | th86/seaad_task2 | source | Python | LICENSE_UNCLEAR | 2025-11-03 | POSSIBLE_RELEVANCE |
| repo-002201 | th86/seurat | fork | R | GPL-3.0 | 2019-11-19 | HIGH_RELEVANCE |
| repo-002202 | th86/smollm | fork | Python | Apache-2.0 | 2025-09-16 | LOW_RELEVANCE |
| repo-002203 | th86/state_virtual_cell | fork | Python | NOASSERTION | 2025-08-11 | HIGH_RELEVANCE |
| repo-002204 | th86/SurvivalCluster | source | R | LICENSE_UNCLEAR | 2013-07-02 | HIGH_RELEVANCE |
| repo-002205 | th86/Target2035_Aircheck_Utils | fork | Python | MIT | 2025-05-20 | POSSIBLE_RELEVANCE |
| repo-002206 | th86/TCGAfastlane | source | R | LICENSE_UNCLEAR | 2014-04-19 | HIGH_RELEVANCE |
| repo-002207 | th86/threadsbot | source | JavaScript | LICENSE_UNCLEAR | 2026-03-09 | IRRELEVANT |
| repo-002208 | th86/TimeCapsuleLLM | fork | Python | MIT | 2025-08-20 | LOW_RELEVANCE |
| repo-002209 | th86/transmeddatasets | source | — | LICENSE_UNCLEAR | 2018-03-01 | HIGH_RELEVANCE |
| repo-002210 | th86/veckit | fork | Python | MIT | 2026-08-10 | HIGH_RELEVANCE |
| repo-002211 | th86/vercel_demo | source | — | LICENSE_UNCLEAR | 2025-07-21 | IRRELEVANT |
| repo-002212 | tuln128/alde_forked | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2024-09-23 | HIGH_RELEVANCE |
| repo-000532 | tuln128/Biomni | fork | Python | Apache-2.0 | 2025-08-12 | HIGH_RELEVANCE |
| repo-002213 | tuln128/CloneBO | fork | Python | MIT | 2025-06-27 | POSSIBLE_RELEVANCE |
| repo-002214 | tuln128/epiLegosDNN | source | Jupyter Notebook | LICENSE_UNCLEAR | 2023-04-13 | HIGH_RELEVANCE |
| repo-002215 | tuln128/EvolvePro | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2024-10-14 | POSSIBLE_RELEVANCE |
| repo-002216 | tuln128/open_deep_research | fork | Python | MIT | 2025-06-23 | POSSIBLE_RELEVANCE |
| repo-002217 | tuln128/paper-bray2017 | fork | Shell | LICENSE_UNCLEAR | 2024-04-15 | HIGH_RELEVANCE |
| repo-002218 | tuln128/SGPO | fork | Jupyter Notebook | Apache-2.0 | 2026-07-16 | HIGH_RELEVANCE |
| repo-002219 | vlln/agent-client-protocol | fork | Rust | Apache-2.0 | 2026-07-29 | POSSIBLE_RELEVANCE |
| repo-002220 | vlln/agent-gui | source | Python | LICENSE_UNCLEAR | 2026-07-01 | POSSIBLE_RELEVANCE |
| repo-002221 | vlln/AgentChat | fork | JavaScript | MIT | 2026-07-30 | POSSIBLE_RELEVANCE |
| repo-002222 | vlln/AlphaConnectZero | source | Python | LICENSE_UNCLEAR | 2024-12-16 | IRRELEVANT |
| repo-002223 | vlln/anon-kode | fork | TypeScript | NOASSERTION | 2025-05-30 | POSSIBLE_RELEVANCE |
| repo-002224 | vlln/AutoFigure | fork | TypeScript | MIT | 2026-05-14 | HIGH_RELEVANCE |
| repo-002225 | vlln/autofigure-skill | source | Python | LICENSE_UNCLEAR | 2026-07-01 | HIGH_RELEVANCE |
| repo-002226 | vlln/autowiki | source | Python | MIT | 2026-06-23 | POSSIBLE_RELEVANCE |
| repo-002227 | vlln/background-task-skill | source | Shell | LICENSE_UNCLEAR | 2026-07-13 | HIGH_RELEVANCE |
| repo-002228 | vlln/bio-reproducer-loop | source | Python | LICENSE_UNCLEAR | 2026-08-22 | HIGH_RELEVANCE |
| repo-002229 | vlln/bio-skills | source | Python | LICENSE_UNCLEAR | 2026-07-01 | HIGH_RELEVANCE |
| repo-000512 | vlln/Biomni | fork | Python | Apache-2.0 | 2025-08-13 | HIGH_RELEVANCE |
| repo-002230 | vlln/camofox-browser | fork | JavaScript | MIT | 2026-05-13 | LOW_RELEVANCE |
| repo-002231 | vlln/clashskill | source | Shell | GPL-3.0 | 2026-07-22 | HIGH_RELEVANCE |
| repo-002232 | vlln/claude-replay | fork | JavaScript | MIT | 2026-07-20 | LOW_RELEVANCE |
| repo-002233 | vlln/devloop | source | — | LICENSE_UNCLEAR | 2026-07-26 | POSSIBLE_RELEVANCE |
| repo-002234 | vlln/dsh-loop | source | JavaScript | MIT | 2026-08-22 | LOW_RELEVANCE |
| repo-002235 | vlln/dsh-navbar | source | TypeScript | MIT | 2026-08-20 | LOW_RELEVANCE |
| repo-002236 | vlln/dsh-task-status | source | JavaScript | MIT | 2026-08-19 | LOW_RELEVANCE |
| repo-002237 | vlln/figure-extractor | fork | Python | LICENSE_UNCLEAR | 2025-01-05 | HIGH_RELEVANCE |
| repo-002238 | vlln/fpatch | source | Rust | LICENSE_UNCLEAR | 2026-05-15 | LOW_RELEVANCE |
| repo-002239 | vlln/grab | source | Go | LICENSE_UNCLEAR | 2026-07-01 | LOW_RELEVANCE |
| repo-002240 | vlln/hanwang-ai-pen-mapper | source | Python | LICENSE_UNCLEAR | 2026-07-15 | IRRELEVANT |
| repo-002241 | vlln/harness-adapter | source | TypeScript | LICENSE_UNCLEAR | 2026-07-25 | POSSIBLE_RELEVANCE |
| repo-002242 | vlln/homebrew-tap | source | Ruby | LICENSE_UNCLEAR | 2026-07-16 | LOW_RELEVANCE |
| repo-002243 | vlln/jlc-cli | fork | TypeScript | LICENSE_UNCLEAR | 2026-04-20 | IRRELEVANT |
| repo-002244 | vlln/llm-tty | source | Python | MIT | 2026-04-05 | POSSIBLE_RELEVANCE |
| repo-002245 | vlln/loopflow | source | Python | LICENSE_UNCLEAR | 2026-08-03 | POSSIBLE_RELEVANCE |
| repo-002246 | vlln/markdown-compressor | source | TypeScript | LICENSE_UNCLEAR | 2025-12-02 | LOW_RELEVANCE |
| repo-002247 | vlln/mineru-api-skill | source | Python | LICENSE_UNCLEAR | 2026-07-13 | HIGH_RELEVANCE |
| repo-002248 | vlln/mip | source | Go | MIT | 2026-07-16 | HIGH_RELEVANCE |
| repo-002249 | vlln/obsidian-harness | fork | TypeScript | Apache-2.0 | 2026-07-29 | POSSIBLE_RELEVANCE |
| repo-002250 | vlln/Obsidian_FolderBridge | fork | TypeScript | MIT | 2026-07-19 | IRRELEVANT |
| repo-002251 | vlln/paper2report | source | Python | Apache-2.0 | 2025-10-27 | HIGH_RELEVANCE |
| repo-002252 | vlln/paperutils | source | Python | LICENSE_UNCLEAR | 2026-07-13 | HIGH_RELEVANCE |
| repo-002253 | vlln/Partitioned-Wallpaper-Generator | source | HTML | GPL-3.0 | 2025-11-10 | IRRELEVANT |
| repo-002254 | vlln/paseo | fork | TypeScript | NOASSERTION | 2026-05-26 | POSSIBLE_RELEVANCE |
| repo-002255 | vlln/pdffigures-mcp-server | source | Python | Apache-2.0 | 2026-05-13 | HIGH_RELEVANCE |
| repo-002256 | vlln/pdffigures2-zig | source | Zig | Apache-2.0 | 2026-05-25 | HIGH_RELEVANCE |
| repo-002257 | vlln/plugin-registry | source | TypeScript | MIT | 2026-08-22 | HIGH_RELEVANCE |
| repo-002258 | vlln/quay-skill | source | Python | LICENSE_UNCLEAR | 2026-07-01 | HIGH_RELEVANCE |
| repo-002259 | vlln/relay | source | Go | LICENSE_UNCLEAR | 2026-08-03 | POSSIBLE_RELEVANCE |
| repo-002260 | vlln/remote-exec-skill | source | Shell | LICENSE_UNCLEAR | 2026-07-01 | HIGH_RELEVANCE |
| repo-002261 | vlln/skills-source | source | — | LICENSE_UNCLEAR | 2026-07-01 | HIGH_RELEVANCE |
| repo-002262 | vlln/skit | source | Go | MIT | 2026-07-13 | HIGH_RELEVANCE |
| repo-002263 | vlln/subagents-skill | source | Python | LICENSE_UNCLEAR | 2026-07-05 | HIGH_RELEVANCE |
| repo-002264 | vlln/Sudoku-RWKV | fork | Python | LICENSE_UNCLEAR | 2024-11-16 | IRRELEVANT |
| repo-002265 | vlln/system_prompts_leaks | fork | — | MIT | 2025-05-23 | LOW_RELEVANCE |
| repo-002266 | vlln/system_prompts_leaks_ | fork | JavaScript | LICENSE_UNCLEAR | 2025-06-04 | LOW_RELEVANCE |
| repo-002267 | vlln/tokscale | fork | Rust | MIT | 2026-07-28 | LOW_RELEVANCE |
| repo-002268 | vlln/whale-girl | source | JavaScript | MIT | 2026-08-19 | IRRELEVANT |
| repo-002269 | vlln/xiaomi-remote-voice-coding-adapter | source | Python | LICENSE_UNCLEAR | 2026-07-28 | IRRELEVANT |

## Identity and scope boundary

- Person depth remains one; contributors of these repositories do not enter P.
- Existing Biomni fork archaeology remains canonical for the eight overlaps.
- Fork status does not establish a unique change or feature.
- Public access and `LICENSE_UNCLEAR`/`NOASSERTION` do not grant reuse rights.
- External descriptions, topics, and repository content remain untrusted data.

## Evidence and limits

- GraphQL captured complete owner totals/cursors plus repository identity, parent,
  default head/date, language, topics, license, activity, state, and release.
- All 10 owner connections are exhausted at the observation time. Private,
  deleted, transferred, and later-created repositories remain unobservable.
- Labels are metadata-grounded INFERENCE. HIGH/POSSIBLE entries require source,
  license, security, and lineage verification before deep audit or ranking.
- Failed and incomplete network responses supplied no canonical metadata.

## Next action

Continue with `person-github-000042` and the following unprocessed User accounts,
preserving stable-ID order and explicit Bot boundaries.
