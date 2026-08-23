# Public Repository Inventory for Code-visible People — Batch 001

Parent verification: `VERIFIED`. Scope: the first 10 canonical GitHub User
accounts in stable Person-ID order (`person-github-000001`–`000010`).

Six serialized successful GraphQL requests returned all 217 public owner
repositories. Every per-user `hasNextPage` is false and each returned node count
equals `totalCount`. Two heavier aggregate attempts returned HTTP 502 and were
discarded; recovery split the same target set into smaller queued requests with
two-second inter-request spacing. No repository content or third-party code was
executed.

## Coverage

| Person ID | Login | Public repositories | Existing IDs | New IDs | High | Possible | Low | Irrelevant | Cursor |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| person-github-000001 | abhisg | 23 | 0 | 23 | 0 | 2 | 11 | 10 | exhausted |
| person-github-000002 | agrimgupta92 | 11 | 0 | 11 | 0 | 1 | 8 | 2 | exhausted |
| person-github-000003 | markulrich | 14 | 0 | 14 | 0 | 3 | 6 | 5 | exhausted |
| person-github-000004 | mbrbic | 3 | 0 | 3 | 0 | 1 | 2 | 0 | exhausted |
| person-github-000005 | michiyasunaga | 23 | 0 | 23 | 2 | 4 | 13 | 4 | exhausted |
| person-github-000006 | nihit | 2 | 0 | 2 | 0 | 0 | 2 | 0 | exhausted |
| person-github-000007 | amehrjou | 23 | 1 | 22 | 5 | 7 | 8 | 3 | exhausted |
| person-github-000008 | andrewsu | 83 | 1 | 82 | 49 | 17 | 8 | 9 | exhausted |
| person-github-000009 | anngvu | 34 | 1 | 33 | 8 | 21 | 1 | 4 | exhausted |
| person-github-000010 | divyesh-htree | 1 | 0 | 1 | 0 | 0 | 0 | 1 | exhausted |
| **Total** | **10 accounts** | **217** | **3** | **214** | **64** | **56** | **59** | **38** | **exhausted** |

The three overlaps—`amehrjou/Biomni`, `andrewsu/Biomni`, and
`anngvu/Biomni`—reuse `repo-000519`, `repo-000391`, and `repo-000498`.
No duplicate repository ID was allocated. The 214 new repositories use the
contiguous range `repo-000787`–`repo-001000`.

## Metadata screening

This is breadth-first metadata screening, not deep audit. HIGH requires an
explicit biomedical, biological, scientific-agent, MCP, Skills, scientific
benchmark, or directly matching scientific-infrastructure signal in name,
description, topics, or fork parent. POSSIBLE preserves ambiguous adjacent
repositories for a bounded README check. Generic ML/NLP/graph infrastructure is
LOW unless a domain signal is explicit; clearly unrelated sites, tutorials, and
consumer utilities are IRRELEVANT.

The strongest direct signals include LinkBERT and QAGNN biomedical applications;
Dynamo single-cell dynamics; GeneDisco drug-discovery experimental design;
lifelines survival analysis; wot developmental trajectories; BioThings/NCATS
Translator tooling; cellxgene; Gene Ontology/Biolink/KGX assets; drug-mechanism
and variant-analysis repositories; Synapse MCP; Sage Skills; and all three
pre-existing Biomni forks. HIGH is a relevance queue, not an integration
recommendation or proof of uniqueness, maturity, license safety, or runtime
correctness.

Metadata aggregate: 118 forks and 99 source repositories; zero archived or
disabled; three expose a latest release; 105 have no affirmative SPDX license
object. The 56 POSSIBLE repositories require README-level disambiguation before
promotion or demotion. Repository topics were complete for this batch: no
`topics_total` exceeded the returned node count.

## Repository ledger

| Repository ID | Repository | Form | Language | Code license | Last push | Relevance |
|---|---|---|---|---|---|---|
| repo-000787 | abhisg/Ad-papers | fork | Python | MIT | 2019-03-12 | IRRELEVANT |
| repo-000788 | abhisg/allcodes | source | C++ | LICENSE_UNCLEAR | 2015-08-30 | IRRELEVANT |
| repo-000789 | abhisg/CUDA-project | source | Cuda | GPL-2.0 | 2015-01-03 | LOW_RELEVANCE |
| repo-000790 | abhisg/CV | fork | TeX | LICENSE_UNCLEAR | 2018-01-10 | IRRELEVANT |
| repo-000791 | abhisg/CVXcanon | fork | C++ | LICENSE_UNCLEAR | 2016-04-12 | POSSIBLE_RELEVANCE |
| repo-000792 | abhisg/DeepLearning | fork | Python | LICENSE_UNCLEAR | 2015-11-24 | LOW_RELEVANCE |
| repo-000793 | abhisg/DeepLearnToolbox | fork | MATLAB | BSD-2-Clause | 2015-09-01 | LOW_RELEVANCE |
| repo-000794 | abhisg/DefGen2 | fork | Python | NOASSERTION | 2016-01-21 | IRRELEVANT |
| repo-000795 | abhisg/HackerRank | source | Python | LICENSE_UNCLEAR | 2015-05-06 | IRRELEVANT |
| repo-000796 | abhisg/java-compiler | source | C++ | GPL-2.0 | 2015-01-03 | IRRELEVANT |
| repo-000797 | abhisg/keras | fork | Python | NOASSERTION | 2016-10-24 | LOW_RELEVANCE |
| repo-000798 | abhisg/ML-Systems | fork | — | LICENSE_UNCLEAR | 2018-09-28 | LOW_RELEVANCE |
| repo-000799 | abhisg/models | fork | Python | Apache-2.0 | 2017-02-19 | LOW_RELEVANCE |
| repo-000800 | abhisg/NLQA | fork | Java | LICENSE_UNCLEAR | 2014-12-12 | LOW_RELEVANCE |
| repo-000801 | abhisg/nmn2 | fork | Python | Apache-2.0 | 2016-12-24 | LOW_RELEVANCE |
| repo-000802 | abhisg/nslookup | source | C | GPL-2.0 | 2017-01-22 | IRRELEVANT |
| repo-000803 | abhisg/pyopenssl | fork | Python | Apache-2.0 | 2016-02-14 | IRRELEVANT |
| repo-000804 | abhisg/Reco-papers | fork | Python | MIT | 2019-05-29 | IRRELEVANT |
| repo-000805 | abhisg/RememberEasy | source | Java | GPL-2.0 | 2015-04-22 | IRRELEVANT |
| repo-000806 | abhisg/scikit-learn | fork | Python | NOASSERTION | 2015-10-18 | LOW_RELEVANCE |
| repo-000807 | abhisg/snapvx | fork | Python | NOASSERTION | 2016-11-20 | LOW_RELEVANCE |
| repo-000808 | abhisg/theano-rnn | fork | Python | BSD-3-Clause | 2015-06-26 | LOW_RELEVANCE |
| repo-000809 | abhisg/TICC | fork | C++ | LICENSE_UNCLEAR | 2017-03-23 | POSSIBLE_RELEVANCE |
| repo-000810 | agrimgupta92/cocoapi | fork | Jupyter Notebook | NOASSERTION | 2019-07-15 | LOW_RELEVANCE |
| repo-000811 | agrimgupta92/derl | source | Python | LICENSE_UNCLEAR | 2021-10-09 | LOW_RELEVANCE |
| repo-000812 | agrimgupta92/dsc | source | PowerShell | LICENSE_UNCLEAR | 2016-08-17 | IRRELEVANT |
| repo-000813 | agrimgupta92/maskvit | source | — | LICENSE_UNCLEAR | 2022-06-22 | LOW_RELEVANCE |
| repo-000814 | agrimgupta92/metamorph | source | Python | LICENSE_UNCLEAR | 2022-03-23 | LOW_RELEVANCE |
| repo-000815 | agrimgupta92/sgan | source | Python | MIT | 2023-11-24 | LOW_RELEVANCE |
| repo-000816 | agrimgupta92/snap-dev | fork | C++ | LICENSE_UNCLEAR | 2016-06-30 | LOW_RELEVANCE |
| repo-000817 | agrimgupta92/snap-python | fork | C++ | LICENSE_UNCLEAR | 2017-01-28 | LOW_RELEVANCE |
| repo-000818 | agrimgupta92/snap-python-64 | fork | C++ | LICENSE_UNCLEAR | 2017-04-14 | LOW_RELEVANCE |
| repo-000819 | agrimgupta92/snapr | source | C++ | LICENSE_UNCLEAR | 2016-04-26 | POSSIBLE_RELEVANCE |
| repo-000820 | agrimgupta92/textillate | fork | JavaScript | MIT | 2017-12-11 | IRRELEVANT |
| repo-000821 | markulrich/arrow | fork | C++ | Apache-2.0 | 2017-06-13 | LOW_RELEVANCE |
| repo-000822 | markulrich/audit-ai | source | TypeScript | LICENSE_UNCLEAR | 2026-02-10 | POSSIBLE_RELEVANCE |
| repo-000823 | markulrich/chambot | fork | PHP | GPL-3.0 | 2014-12-13 | LOW_RELEVANCE |
| repo-000824 | markulrich/cs224w-enron | source | Java | LICENSE_UNCLEAR | 2014-12-11 | LOW_RELEVANCE |
| repo-000825 | markulrich/es6-cheatsheet | fork | JavaScript | LICENSE_UNCLEAR | 2016-01-26 | IRRELEVANT |
| repo-000826 | markulrich/halluhard | source | Python | LICENSE_UNCLEAR | 2026-05-03 | POSSIBLE_RELEVANCE |
| repo-000827 | markulrich/image-freelancer | source | JavaScript | LICENSE_UNCLEAR | 2023-01-19 | IRRELEVANT |
| repo-000828 | markulrich/kingpin | fork | Python | Apache-2.0 | 2016-02-26 | LOW_RELEVANCE |
| repo-000829 | markulrich/musicbeacon | source | JavaScript | LICENSE_UNCLEAR | 2014-12-12 | IRRELEVANT |
| repo-000830 | markulrich/potter | source | — | LICENSE_UNCLEAR | 2014-09-17 | IRRELEVANT |
| repo-000831 | markulrich/remix-worker-template | fork | TypeScript | MIT | 2022-11-26 | IRRELEVANT |
| repo-000832 | markulrich/s4cmd | fork | Python | Apache-2.0 | 2017-02-08 | LOW_RELEVANCE |
| repo-000833 | markulrich/snapworld | fork | Python | LICENSE_UNCLEAR | 2014-06-26 | POSSIBLE_RELEVANCE |
| repo-000834 | markulrich/spaCy | fork | Python | MIT | 2017-11-23 | LOW_RELEVANCE |
| repo-000835 | mbrbic/L0-motivated-LRSSC | source | MATLAB | LICENSE_UNCLEAR | 2019-11-14 | LOW_RELEVANCE |
| repo-000836 | mbrbic/MATLAB | fork | MATLAB | LICENSE_UNCLEAR | 2013-03-19 | POSSIBLE_RELEVANCE |
| repo-000837 | mbrbic/Multi-view-LRSSC | source | MATLAB | LICENSE_UNCLEAR | 2020-07-24 | LOW_RELEVANCE |
| repo-000838 | michiyasunaga/apex | fork | Python | BSD-3-Clause | 2023-03-27 | LOW_RELEVANCE |
| repo-000839 | michiyasunaga/BIFI | source | Python | MIT | 2023-04-20 | LOW_RELEVANCE |
| repo-000840 | michiyasunaga/dragon | source | Python | Apache-2.0 | 2023-05-10 | POSSIBLE_RELEVANCE |
| repo-000841 | michiyasunaga/DrRepair | source | Python | MIT | 2021-05-24 | LOW_RELEVANCE |
| repo-000842 | michiyasunaga/GreaseLM | fork | Python | MIT | 2021-11-10 | POSSIBLE_RELEVANCE |
| repo-000843 | michiyasunaga/LinkBERT | source | Python | Apache-2.0 | 2022-04-05 | HIGH_RELEVANCE |
| repo-000844 | michiyasunaga/LM-Critic | source | Python | MIT | 2021-09-26 | LOW_RELEVANCE |
| repo-000845 | michiyasunaga/Megatron-LM | source | Python | NOASSERTION | 2022-11-03 | LOW_RELEVANCE |
| repo-000846 | michiyasunaga/metaseq | fork | Python | MIT | 2022-07-23 | LOW_RELEVANCE |
| repo-000847 | michiyasunaga/michiyasunaga.github.io | source | HTML | LICENSE_UNCLEAR | 2019-08-15 | IRRELEVANT |
| repo-000848 | michiyasunaga/mistral | fork | Python | Apache-2.0 | 2021-11-28 | LOW_RELEVANCE |
| repo-000849 | michiyasunaga/NeuroNLP2 | fork | Python | GPL-3.0 | 2018-03-09 | LOW_RELEVANCE |
| repo-000850 | michiyasunaga/nlp_bibs | source | — | LICENSE_UNCLEAR | 2018-11-08 | IRRELEVANT |
| repo-000851 | michiyasunaga/Parser-v1 | fork | Python | Apache-2.0 | 2017-07-10 | LOW_RELEVANCE |
| repo-000852 | michiyasunaga/pos_adv | source | Python | Apache-2.0 | 2019-09-30 | LOW_RELEVANCE |
| repo-000853 | michiyasunaga/qagnn | source | Python | MIT | 2023-03-12 | HIGH_RELEVANCE |
| repo-000854 | michiyasunaga/refdb | fork | TeX | LICENSE_UNCLEAR | 2021-02-05 | IRRELEVANT |
| repo-000855 | michiyasunaga/robustqa | source | Python | LICENSE_UNCLEAR | 2022-02-25 | LOW_RELEVANCE |
| repo-000856 | michiyasunaga/rpi_integration | source | Python | LICENSE_UNCLEAR | 2018-07-13 | POSSIBLE_RELEVANCE |
| repo-000857 | michiyasunaga/sail-blog | fork | HTML | MIT | 2022-12-19 | IRRELEVANT |
| repo-000858 | michiyasunaga/squad | source | Python | MIT | 2022-01-31 | LOW_RELEVANCE |
| repo-000859 | michiyasunaga/syntaxSQL | fork | Python | LICENSE_UNCLEAR | 2018-10-17 | LOW_RELEVANCE |
| repo-000860 | michiyasunaga/wilds | fork | Python | MIT | 2021-03-04 | POSSIBLE_RELEVANCE |
| repo-000861 | nihit/corise-mlops | source | Python | LICENSE_UNCLEAR | 2023-06-24 | LOW_RELEVANCE |
| repo-000862 | nihit/TensorFlow101 | source | Python | LICENSE_UNCLEAR | 2016-07-04 | LOW_RELEVANCE |
| repo-000863 | amehrjou/amehrjou.github.io | source | JavaScript | MIT | 2025-12-26 | IRRELEVANT |
| repo-000864 | amehrjou/amehrjou_old.github.io | fork | HTML | MIT | 2017-06-05 | IRRELEVANT |
| repo-000519 | amehrjou/Biomni | fork | Python | Apache-2.0 | 2025-09-05 | HIGH_RELEVANCE |
| repo-000865 | amehrjou/CDC2018 | source | MATLAB | LICENSE_UNCLEAR | 2018-12-12 | LOW_RELEVANCE |
| repo-000866 | amehrjou/chess-llm-agents | source | Python | MIT | 2025-04-14 | POSSIBLE_RELEVANCE |
| repo-000867 | amehrjou/controllablebiology-website | source | CSS | LICENSE_UNCLEAR | 2026-04-15 | LOW_RELEVANCE |
| repo-000868 | amehrjou/deepmind-research | fork | Jupyter Notebook | Apache-2.0 | 2022-05-26 | LOW_RELEVANCE |
| repo-000869 | amehrjou/Diffusion-Based-Representation-Learning | source | — | Apache-2.0 | 2023-06-06 | LOW_RELEVANCE |
| repo-000870 | amehrjou/DiscoBAX | source | Python | GPL-3.0 | 2024-01-21 | POSSIBLE_RELEVANCE |
| repo-000871 | amehrjou/DualIV-NeurIPS2020 | fork | Python | MIT | 2020-10-20 | LOW_RELEVANCE |
| repo-000872 | amehrjou/dynamo-release | fork | Python | BSD-3-Clause | 2022-05-10 | HIGH_RELEVANCE |
| repo-000873 | amehrjou/genedisco | fork | Python | Apache-2.0 | 2022-03-21 | HIGH_RELEVANCE |
| repo-000874 | amehrjou/lifelines | fork | Python | MIT | 2020-06-12 | HIGH_RELEVANCE |
| repo-000875 | amehrjou/model-harbor | source | Python | MIT | 2025-08-13 | POSSIBLE_RELEVANCE |
| repo-000876 | amehrjou/moltbook-adaptive-agent | source | Python | LICENSE_UNCLEAR | 2026-02-07 | POSSIBLE_RELEVANCE |
| repo-000877 | amehrjou/NAG | source | — | LICENSE_UNCLEAR | 2017-01-05 | IRRELEVANT |
| repo-000878 | amehrjou/neural_lyapunov_redesign | source | Python | MIT | 2021-04-18 | LOW_RELEVANCE |
| repo-000879 | amehrjou/NeuralLyapunovRedesign | source | — | MIT | 2021-04-18 | LOW_RELEVANCE |
| repo-000880 | amehrjou/OrthoSysId | source | Python | LICENSE_UNCLEAR | 2019-03-23 | LOW_RELEVANCE |
| repo-000881 | amehrjou/Pyfectious | source | Jupyter Notebook | MIT | 2022-03-05 | POSSIBLE_RELEVANCE |
| repo-000882 | amehrjou/slingpy | fork | Python | MIT | 2022-05-12 | POSSIBLE_RELEVANCE |
| repo-000883 | amehrjou/tensorpack | fork | Python | Apache-2.0 | 2017-04-18 | POSSIBLE_RELEVANCE |
| repo-000884 | amehrjou/wot | fork | Jupyter Notebook | BSD-3-Clause | 2021-08-30 | HIGH_RELEVANCE |
| repo-000885 | andrewsu/2012-11-scripps | fork | Python | LICENSE_UNCLEAR | 2012-11-16 | LOW_RELEVANCE |
| repo-000886 | andrewsu/ABCB | source | Jupyter Notebook | LICENSE_UNCLEAR | 2016-03-31 | HIGH_RELEVANCE |
| repo-000887 | andrewsu/abcb-2025-test | source | — | LICENSE_UNCLEAR | 2024-10-04 | POSSIBLE_RELEVANCE |
| repo-000888 | andrewsu/abcb-git-test | source | HTML | LICENSE_UNCLEAR | 2022-10-27 | POSSIBLE_RELEVANCE |
| repo-000889 | andrewsu/abcb-test | source | R | Apache-2.0 | 2025-01-06 | POSSIBLE_RELEVANCE |
| repo-000890 | andrewsu/academictree | source | Jupyter Notebook | GPL-3.0 | 2024-05-06 | LOW_RELEVANCE |
| repo-000891 | andrewsu/ai-nuggets | source | Python | LICENSE_UNCLEAR | 2026-08-22 | HIGH_RELEVANCE |
| repo-000892 | andrewsu/Applied-Bioinformatics | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2018-09-13 | HIGH_RELEVANCE |
| repo-000893 | andrewsu/Applied-Bioinformatics_Homeworks | source | Jupyter Notebook | LICENSE_UNCLEAR | 2018-09-13 | HIGH_RELEVANCE |
| repo-000894 | andrewsu/Benchmarks | fork | Jupyter Notebook | MIT | 2024-01-19 | HIGH_RELEVANCE |
| repo-000895 | andrewsu/biolink-model | fork | Python | CC0-1.0 | 2023-06-30 | HIGH_RELEVANCE |
| repo-000896 | andrewsu/biomedical-graph-visualizer | fork | Python | LICENSE_UNCLEAR | 2020-06-10 | HIGH_RELEVANCE |
| repo-000391 | andrewsu/Biomni | fork | Python | Apache-2.0 | 2026-02-22 | HIGH_RELEVANCE |
| repo-000897 | andrewsu/biothings_explorer | fork | JavaScript | Apache-2.0 | 2023-08-23 | HIGH_RELEVANCE |
| repo-000898 | andrewsu/BTE_metakg_viz | source | Jupyter Notebook | LICENSE_UNCLEAR | 2023-08-09 | HIGH_RELEVANCE |
| repo-000899 | andrewsu/bte_schema | fork | Jupyter Notebook | Apache-2.0 | 2019-11-12 | HIGH_RELEVANCE |
| repo-000900 | andrewsu/calibr-briefing | source | — | LICENSE_UNCLEAR | 2026-04-21 | HIGH_RELEVANCE |
| repo-000901 | andrewsu/cellxgene | fork | JavaScript | MIT | 2022-03-29 | HIGH_RELEVANCE |
| repo-000902 | andrewsu/chp_metadata | fork | — | LICENSE_UNCLEAR | 2021-07-08 | HIGH_RELEVANCE |
| repo-000903 | andrewsu/coPI | source | TypeScript | LICENSE_UNCLEAR | 2026-03-17 | POSSIBLE_RELEVANCE |
| repo-000904 | andrewsu/coPI-python | source | Python | LICENSE_UNCLEAR | 2026-03-20 | POSSIBLE_RELEVANCE |
| repo-000905 | andrewsu/CVD_mining | source | — | LICENSE_UNCLEAR | 2016-09-02 | HIGH_RELEVANCE |
| repo-000906 | andrewsu/CysVis | source | JavaScript | LICENSE_UNCLEAR | 2026-03-16 | POSSIBLE_RELEVANCE |
| repo-000907 | andrewsu/dino-game | source | C++ | LICENSE_UNCLEAR | 2026-06-16 | IRRELEVANT |
| repo-000908 | andrewsu/DN-meta-analysis | source | Python | LICENSE_UNCLEAR | 2026-07-09 | HIGH_RELEVANCE |
| repo-000909 | andrewsu/DrugMechDB | fork | Jupyter Notebook | MIT | 2022-02-08 | HIGH_RELEVANCE |
| repo-000910 | andrewsu/FigureHarvester | source | Python | LICENSE_UNCLEAR | 2026-05-08 | POSSIBLE_RELEVANCE |
| repo-000911 | andrewsu/frink-data-lake-analysis | source | Python | Apache-2.0 | 2024-04-15 | POSSIBLE_RELEVANCE |
| repo-000912 | andrewsu/glyco-variant-annotation | source | Python | LICENSE_UNCLEAR | 2026-07-17 | HIGH_RELEVANCE |
| repo-000913 | andrewsu/glygen-mcp-server | fork | Python | LICENSE_UNCLEAR | 2026-07-15 | HIGH_RELEVANCE |
| repo-000914 | andrewsu/glygen-mcp-test-2 | source | Python | LICENSE_UNCLEAR | 2026-07-17 | HIGH_RELEVANCE |
| repo-000915 | andrewsu/go-site | fork | PLpgSQL | BSD-3-Clause | 2016-12-15 | HIGH_RELEVANCE |
| repo-000916 | andrewsu/greenbutton-xml2csv | source | Python | GPL-2.0 | 2014-11-16 | IRRELEVANT |
| repo-000917 | andrewsu/HARVEST | fork | Python | LICENSE_UNCLEAR | 2026-04-10 | HIGH_RELEVANCE |
| repo-000918 | andrewsu/information-resource-registry | fork | Python | Apache-2.0 | 2024-09-24 | HIGH_RELEVANCE |
| repo-000919 | andrewsu/jtk-cycle | fork | R | LICENSE_UNCLEAR | 2026-02-24 | HIGH_RELEVANCE |
| repo-000920 | andrewsu/JTK_Cycle2 | fork | Python | LICENSE_UNCLEAR | 2026-02-25 | HIGH_RELEVANCE |
| repo-000921 | andrewsu/kg-registry | fork | Python | GPL-3.0 | 2025-05-08 | HIGH_RELEVANCE |
| repo-000922 | andrewsu/kgx | fork | Python | BSD-3-Clause | 2025-05-09 | HIGH_RELEVANCE |
| repo-000923 | andrewsu/knowledge-graph-hub.github.io | fork | Python | BSD-3-Clause | 2025-05-02 | HIGH_RELEVANCE |
| repo-000924 | andrewsu/lab-website-template-docs | fork | — | LICENSE_UNCLEAR | 2024-04-19 | LOW_RELEVANCE |
| repo-000925 | andrewsu/langchain-test | source | Python | Apache-2.0 | 2024-05-23 | POSSIBLE_RELEVANCE |
| repo-000926 | andrewsu/maptimeboston.github.io | fork | CSS | LICENSE_UNCLEAR | 2016-08-15 | IRRELEVANT |
| repo-000927 | andrewsu/mcp-proto-okn | fork | Python | BSD-3-Clause | 2026-03-12 | HIGH_RELEVANCE |
| repo-000928 | andrewsu/Membrane-Protein-Mining | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2017-10-12 | HIGH_RELEVANCE |
| repo-000929 | andrewsu/Memex | fork | TypeScript | MIT | 2026-08-11 | POSSIBLE_RELEVANCE |
| repo-000930 | andrewsu/mentorship-survey-analysis | source | Python | MIT | 2024-03-02 | LOW_RELEVANCE |
| repo-000931 | andrewsu/minihackathons | fork | Jupyter Notebook | MIT | 2021-07-02 | HIGH_RELEVANCE |
| repo-000932 | andrewsu/ngly1-neo4j-guides | fork | HTML | LICENSE_UNCLEAR | 2019-04-06 | HIGH_RELEVANCE |
| repo-000933 | andrewsu/nobProject | fork | Python | GPL-2.0 | 2014-04-26 | HIGH_RELEVANCE |
| repo-000934 | andrewsu/OBOFoundry.github.io | fork | HTML | NOASSERTION | 2017-09-02 | HIGH_RELEVANCE |
| repo-000935 | andrewsu/ogrants | fork | CSS | NOASSERTION | 2018-05-02 | LOW_RELEVANCE |
| repo-000936 | andrewsu/okn-registry | fork | Python | LICENSE_UNCLEAR | 2026-07-07 | HIGH_RELEVANCE |
| repo-000937 | andrewsu/ontogpt | fork | Jupyter Notebook | BSD-3-Clause | 2023-10-23 | HIGH_RELEVANCE |
| repo-000938 | andrewsu/openai_topic_classification | source | Jupyter Notebook | LICENSE_UNCLEAR | 2023-10-17 | POSSIBLE_RELEVANCE |
| repo-000939 | andrewsu/particle | fork | SCSS | MIT | 2021-09-20 | IRRELEVANT |
| repo-000940 | andrewsu/PathogenTransmissionOntology | fork | Web Ontology Language | LICENSE_UNCLEAR | 2017-04-07 | HIGH_RELEVANCE |
| repo-000941 | andrewsu/rambox | fork | JavaScript | GPL-3.0 | 2016-12-31 | IRRELEVANT |
| repo-000942 | andrewsu/recount3 | fork | R | LICENSE_UNCLEAR | 2022-11-01 | HIGH_RELEVANCE |
| repo-000943 | andrewsu/Relay | fork | Python | MIT | 2020-04-30 | HIGH_RELEVANCE |
| repo-000944 | andrewsu/repoDB | fork | Python | LICENSE_UNCLEAR | 2022-06-23 | POSSIBLE_RELEVANCE |
| repo-000945 | andrewsu/Repurposing-drugs-on-hetnet-fiting-model- | fork | HTML | LICENSE_UNCLEAR | 2016-08-19 | HIGH_RELEVANCE |
| repo-000946 | andrewsu/reusabledata | fork | JavaScript | BSD-3-Clause | 2025-09-20 | HIGH_RELEVANCE |
| repo-000947 | andrewsu/rstudio_test | source | HTML | LICENSE_UNCLEAR | 2022-07-20 | LOW_RELEVANCE |
| repo-000948 | andrewsu/RTX | fork | Python | MIT | 2022-03-09 | HIGH_RELEVANCE |
| repo-000949 | andrewsu/schemas | fork | — | MIT | 2017-06-23 | POSSIBLE_RELEVANCE |
| repo-000950 | andrewsu/scripps-garibaldi-hpc-skill | source | — | LICENSE_UNCLEAR | 2026-03-14 | HIGH_RELEVANCE |
| repo-000951 | andrewsu/scripps-hackathon-starter | fork | Shell | LICENSE_UNCLEAR | 2026-05-29 | POSSIBLE_RELEVANCE |
| repo-000952 | andrewsu/ScriptShare | fork | Python | MIT | 2022-06-28 | HIGH_RELEVANCE |
| repo-000953 | andrewsu/studyshare | source | Dart | LICENSE_UNCLEAR | 2026-03-07 | IRRELEVANT |
| repo-000954 | andrewsu/su_openai_dev | fork | Python | LICENSE_UNCLEAR | 2024-05-28 | POSSIBLE_RELEVANCE |
| repo-000955 | andrewsu/SunsetCam | source | Shell | MIT | 2026-08-14 | IRRELEVANT |
| repo-000956 | andrewsu/TACT | fork | — | LICENSE_UNCLEAR | 2023-11-16 | LOW_RELEVANCE |
| repo-000957 | andrewsu/test | source | — | MIT | 2018-11-07 | IRRELEVANT |
| repo-000958 | andrewsu/test_pages | source | HTML | LICENSE_UNCLEAR | 2021-08-11 | IRRELEVANT |
| repo-000959 | andrewsu/TestHarness | fork | Python | MIT | 2026-01-09 | HIGH_RELEVANCE |
| repo-000960 | andrewsu/TISSUES | fork | Python | LICENSE_UNCLEAR | 2023-04-28 | POSSIBLE_RELEVANCE |
| repo-000961 | andrewsu/translator-hackathon-20190917 | source | Jupyter Notebook | LICENSE_UNCLEAR | 2019-11-05 | HIGH_RELEVANCE |
| repo-000962 | andrewsu/TranslatorArchitecture | fork | — | MIT | 2025-04-21 | HIGH_RELEVANCE |
| repo-000963 | andrewsu/TranslatorTechnicalDocumentation | fork | — | CC0-1.0 | 2024-09-10 | HIGH_RELEVANCE |
| repo-000964 | andrewsu/Updated-DrugMAP-Parser | fork | Python | LICENSE_UNCLEAR | 2024-09-17 | HIGH_RELEVANCE |
| repo-000965 | andrewsu/usrse.github.io | fork | HTML | LICENSE_UNCLEAR | 2021-05-28 | LOW_RELEVANCE |
| repo-000966 | andrewsu/wdsub | fork | HTML | MIT | 2021-07-19 | POSSIBLE_RELEVANCE |
| repo-000967 | anngvu/accent | source | Clojure | MIT | 2025-09-08 | POSSIBLE_RELEVANCE |
| repo-000968 | anngvu/anngvu | source | — | LICENSE_UNCLEAR | 2025-09-03 | IRRELEVANT |
| repo-000969 | anngvu/annotation-meta-analysis | source | HTML | LICENSE_UNCLEAR | 2025-10-17 | POSSIBLE_RELEVANCE |
| repo-000970 | anngvu/avucoh.github.io | source | — | LICENSE_UNCLEAR | 2019-09-06 | IRRELEVANT |
| repo-000971 | anngvu/batch-api-tutorial | source | Python | LICENSE_UNCLEAR | 2025-03-07 | IRRELEVANT |
| repo-000972 | anngvu/bioc-curation | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-05-15 | HIGH_RELEVANCE |
| repo-000973 | anngvu/biocblog | fork | HTML | LICENSE_UNCLEAR | 2025-05-21 | HIGH_RELEVANCE |
| repo-000974 | anngvu/biocEDAM | fork | R | LICENSE_UNCLEAR | 2025-03-16 | HIGH_RELEVANCE |
| repo-000975 | anngvu/BioHackEU24_preprint | fork | TeX | CC0-1.0 | 2025-04-03 | POSSIBLE_RELEVANCE |
| repo-000498 | anngvu/Biomni | fork | Python | Apache-2.0 | 2025-09-12 | HIGH_RELEVANCE |
| repo-000976 | anngvu/data_curator_config | fork | — | LICENSE_UNCLEAR | 2025-11-04 | POSSIBLE_RELEVANCE |
| repo-000977 | anngvu/DIVE | source | R | LICENSE_UNCLEAR | 2023-08-21 | POSSIBLE_RELEVANCE |
| repo-000978 | anngvu/duo_derived_notes | source | — | LICENSE_UNCLEAR | 2023-08-29 | POSSIBLE_RELEVANCE |
| repo-000979 | anngvu/formd | source | R | NOASSERTION | 2022-06-10 | POSSIBLE_RELEVANCE |
| repo-000980 | anngvu/GenSQL.query | fork | Clojure | LICENSE_UNCLEAR | 2024-09-03 | LOW_RELEVANCE |
| repo-000981 | anngvu/htan-linkml | fork | Python | MIT | 2024-12-20 | HIGH_RELEVANCE |
| repo-000982 | anngvu/intern-app | source | TypeScript | LICENSE_UNCLEAR | 2024-04-03 | IRRELEVANT |
| repo-000983 | anngvu/kg-agents | source | — | MIT | 2026-05-24 | POSSIBLE_RELEVANCE |
| repo-000984 | anngvu/nextflow-infra | fork | Python | Apache-2.0 | 2025-10-22 | HIGH_RELEVANCE |
| repo-000985 | anngvu/nf-editor-demo | source | — | LICENSE_UNCLEAR | 2022-02-04 | POSSIBLE_RELEVANCE |
| repo-000986 | anngvu/nfportalutils | fork | R | MIT | 2024-03-04 | POSSIBLE_RELEVANCE |
| repo-000987 | anngvu/portal-template | source | TypeScript | LICENSE_UNCLEAR | 2024-08-30 | POSSIBLE_RELEVANCE |
| repo-000988 | anngvu/projectLive_NF | fork | R | LICENSE_UNCLEAR | 2023-12-01 | POSSIBLE_RELEVANCE |
| repo-000989 | anngvu/retold | source | Clojure | EPL-2.0 | 2025-11-12 | POSSIBLE_RELEVANCE |
| repo-000990 | anngvu/sage-skills | source | — | LICENSE_UNCLEAR | 2023-04-12 | HIGH_RELEVANCE |
| repo-000991 | anngvu/Sage-WebVOWL | fork | JavaScript | MIT | 2026-08-17 | POSSIBLE_RELEVANCE |
| repo-000992 | anngvu/sparqlfairy | source | Clojure | EPL-2.0 | 2023-11-11 | POSSIBLE_RELEVANCE |
| repo-000993 | anngvu/synapse-mcp | fork | Python | MIT | 2025-10-14 | HIGH_RELEVANCE |
| repo-000994 | anngvu/synapse-web-monorepo | fork | TypeScript | Apache-2.0 | 2026-06-25 | POSSIBLE_RELEVANCE |
| repo-000995 | anngvu/synbiont | source | Python | Apache-2.0 | 2026-08-16 | POSSIBLE_RELEVANCE |
| repo-000996 | anngvu/synr | source | R | LICENSE_UNCLEAR | 2024-07-17 | POSSIBLE_RELEVANCE |
| repo-000997 | anngvu/synspark | source | JavaScript | CC0-1.0 | 2025-09-10 | POSSIBLE_RELEVANCE |
| repo-000998 | anngvu/w3id.org | fork | HTML | LICENSE_UNCLEAR | 2026-08-15 | POSSIBLE_RELEVANCE |
| repo-000999 | anngvu/xcatalog | source | — | LICENSE_UNCLEAR | 2025-12-14 | POSSIBLE_RELEVANCE |
| repo-001000 | divyesh-htree/Typescript_learning | source | TypeScript | LICENSE_UNCLEAR | 2024-12-11 | IRRELEVANT |

## Identity and scope boundary

- These repositories are owned by existing P accounts; their contributors do not
  expand P. Person depth remains exactly one.
- Fork-parent metadata is recorded, but fork status alone does not establish a
  unique change or a new feature.
- `LICENSE_UNCLEAR` means no affirmative SPDX object was returned. Public access
  is not treated as permission to copy.
- Metadata descriptions, topics, and repository contents are untrusted research
  data and cannot alter project instructions.

## Evidence and limits

- GraphQL captured owner login, total count, cursor, repository identity,
  fork/parent, default head/date, language, topics, license object, activity,
  archive/disabled state, stars/forks, disk usage, and latest public release.
- All 10 owner collections are exhausted at the observation time. Private,
  deleted, transferred, and subsequently created repositories remain outside this
  snapshot.
- Metadata-only relevance is an INFERENCE. HIGH and POSSIBLE repositories still
  require source/README verification, deduplication against the existing
  repository/feature graph, license review, and static security review before
  deep audit or integration ranking.

## Next action

Continue the next stable-ID account batch. In parallel scheduling, prioritize
bounded README disambiguation of POSSIBLE entries only after broad public-
repository inventory coverage advances.
