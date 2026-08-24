# Public Repository Inventory for Code-visible People — Batch 003

Parent verification: `VERIFIED`. Stable-ID scope is
`person-github-000021`–`000031`: 10 GitHub User accounts plus the intervening
`person-github-000029` Bot.

Ten serialized GraphQL requests returned all 205 public owner repositories for
the User accounts. Every repository connection fits in one page, every
`hasNextPage` is false, and returned nodes equal `totalCount`.
`pre-commit-ci[bot]` is explicitly `NOT_APPLICABLE_BOT`; no fictitious User
query or empty repository result is created. No repository content or third-party
code was executed.

## Coverage

| Person ID | Login | Account | Public repositories | Existing IDs | New IDs | High | Possible | Low | Irrelevant | Cursor |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| person-github-000021 | marcosbolanos | User | 48 | 1 | 47 | 20 | 10 | 8 | 10 | exhausted |
| person-github-000022 | mickaelleclercq | User | 13 | 0 | 13 | 5 | 3 | 3 | 2 | exhausted |
| person-github-000023 | MintaYLu | User | 9 | 1 | 8 | 3 | 5 | 0 | 1 | exhausted |
| person-github-000024 | MinxZ | User | 26 | 1 | 25 | 4 | 4 | 6 | 12 | exhausted |
| person-github-000025 | nevergreendd | User | 8 | 1 | 7 | 2 | 0 | 4 | 2 | exhausted |
| person-github-000026 | PabloPauling | User | 5 | 1 | 4 | 3 | 1 | 0 | 1 | exhausted |
| person-github-000027 | Pidem | User | 32 | 1 | 31 | 7 | 6 | 8 | 11 | exhausted |
| person-github-000028 | PLippmann | User | 12 | 1 | 11 | 1 | 2 | 6 | 3 | exhausted |
| person-github-000029 | pre-commit-ci[bot] | Bot | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not applicable |
| person-github-000030 | ryanDing26 | User | 33 | 1 | 32 | 6 | 7 | 5 | 15 | exhausted |
| person-github-000031 | RyanLi1028 | User | 19 | 0 | 19 | 1 | 3 | 4 | 11 | exhausted |
| **Total** | **11 accounts** | **10 User + 1 Bot** | **205** | **8** | **197** | **52** | **41** | **44** | **68** | **closed** |

The eight overlaps reuse existing Biomni lineage IDs for marcosbolanos, MintaYLu,
MinxZ, nevergreendd, PabloPauling, Pidem, PLippmann, and ryanDing26. The 197 new
repositories use contiguous IDs `repo-001581`–`repo-001777`.

## Metadata screening

HIGH requires an explicit biomedical, biological, scientific-agent, MCP, protein,
drug, clinical, omics, benchmark, or matching scientific-infrastructure signal.
POSSIBLE preserves metadata ambiguity for README review. Generic ML/NLP tooling
without a domain signal is LOW; unrelated sites, demos, games, and utilities are
IRRELEVANT.

Direct HIGH signals include protein-fitness optimization, DNA origami, BindCraft
and BoltzGen, pharmacology knowledge graphs, biomarker and omics tooling,
microRNA/RNA-seq utilities, clinical-trial prediction, molecule optimization,
variant-splicing prediction, molecular-pose MCP, biomolecular structure
prediction, spatial proteomics, medical LLM benchmarks, sepsis prediction,
whole-slide imaging, virtual scientific laboratories, diabetes and histopathology
models, and the eight existing Biomni lineages. HIGH is a deep-audit queue, not an
integration recommendation.

Metadata aggregate: 84 forks and 121 source repositories; none archived or
disabled; three expose a latest release; 115 have no affirmative SPDX license
object. All topic node counts equal `topics_total`. The 41 POSSIBLE entries await
bounded README disambiguation.

## Repository ledger

| Repository ID | Repository | Form | Language | Code license | Last push | Relevance |
|---|---|---|---|---|---|---|
| repo-001581 | marcosbolanos/0shotprot | source | Python | GPL-3.0 | 2026-07-23 | HIGH_RELEVANCE |
| repo-001582 | marcosbolanos/3dna | source | Python | MIT | 2026-03-10 | HIGH_RELEVANCE |
| repo-001583 | marcosbolanos/acap | fork | C++ | LICENSE_UNCLEAR | 2023-09-13 | HIGH_RELEVANCE |
| repo-001584 | marcosbolanos/Apple-USB-Ethernet-Adapter-Windows-Driver | fork | Batchfile | LICENSE_UNCLEAR | 2020-01-27 | IRRELEVANT |
| repo-001585 | marcosbolanos/ariana | fork | TypeScript | LICENSE_UNCLEAR | 2026-02-24 | POSSIBLE_RELEVANCE |
| repo-001586 | marcosbolanos/autorigami | source | Python | LICENSE_UNCLEAR | 2026-07-22 | POSSIBLE_RELEVANCE |
| repo-001587 | marcosbolanos/autorigami- | source | Python | LICENSE_UNCLEAR | 2026-03-26 | HIGH_RELEVANCE |
| repo-001588 | marcosbolanos/awesome-node-backend | source | TypeScript | LICENSE_UNCLEAR | 2025-12-05 | LOW_RELEVANCE |
| repo-001589 | marcosbolanos/BindCraft | fork | Python | MIT | 2025-11-19 | HIGH_RELEVANCE |
| repo-000570 | marcosbolanos/Biomni | fork | Python | Apache-2.0 | 2025-09-02 | HIGH_RELEVANCE |
| repo-001590 | marcosbolanos/boltzgen | fork | Jupyter Notebook | MIT | 2026-01-09 | HIGH_RELEVANCE |
| repo-001591 | marcosbolanos/Case-Lucis | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-06-30 | HIGH_RELEVANCE |
| repo-001592 | marcosbolanos/Cheminformatics_molecule_property_project | fork | Python | LICENSE_UNCLEAR | 2025-10-01 | HIGH_RELEVANCE |
| repo-001593 | marcosbolanos/Curie | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-06-02 | POSSIBLE_RELEVANCE |
| repo-001594 | marcosbolanos/devcontainer-features | source | Shell | MIT | 2025-11-21 | LOW_RELEVANCE |
| repo-001595 | marcosbolanos/devcontainers.github.io | fork | HTML | MIT | 2026-01-05 | LOW_RELEVANCE |
| repo-001596 | marcosbolanos/dsa | source | C | LICENSE_UNCLEAR | 2025-11-28 | IRRELEVANT |
| repo-001597 | marcosbolanos/fitness-landscapes | source | Python | LICENSE_UNCLEAR | 2026-05-13 | HIGH_RELEVANCE |
| repo-001598 | marcosbolanos/FrenchPharmaKG | source | Python | LICENSE_UNCLEAR | 2025-06-22 | HIGH_RELEVANCE |
| repo-001599 | marcosbolanos/graphics_c | source | C | LICENSE_UNCLEAR | 2025-11-22 | IRRELEVANT |
| repo-001600 | marcosbolanos/kaggle_medicalPremiums | source | Jupyter Notebook | LICENSE_UNCLEAR | 2024-11-05 | HIGH_RELEVANCE |
| repo-001601 | marcosbolanos/letspill | source | — | LICENSE_UNCLEAR | 2026-07-30 | HIGH_RELEVANCE |
| repo-001602 | marcosbolanos/letspill-backend | source | JavaScript | LICENSE_UNCLEAR | 2026-03-09 | POSSIBLE_RELEVANCE |
| repo-001603 | marcosbolanos/marcode | source | Python | LICENSE_UNCLEAR | 2026-06-20 | IRRELEVANT |
| repo-001604 | marcosbolanos/marcos-bolanos.github.io | source | — | LICENSE_UNCLEAR | 2025-03-15 | IRRELEVANT |
| repo-001605 | marcosbolanos/mats_practice | source | Python | LICENSE_UNCLEAR | 2026-06-18 | IRRELEVANT |
| repo-001606 | marcosbolanos/MeshTree | source | Python | LICENSE_UNCLEAR | 2024-11-16 | HIGH_RELEVANCE |
| repo-001607 | marcosbolanos/mlbionetw | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-12-27 | HIGH_RELEVANCE |
| repo-001608 | marcosbolanos/Muse | fork | Python | MIT | 2026-05-04 | POSSIBLE_RELEVANCE |
| repo-001609 | marcosbolanos/my-dev-container-setup | source | Dockerfile | LICENSE_UNCLEAR | 2025-10-10 | LOW_RELEVANCE |
| repo-001610 | marcosbolanos/notemakr | source | Python | LICENSE_UNCLEAR | 2025-10-27 | LOW_RELEVANCE |
| repo-001611 | marcosbolanos/pairwise-representations | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-05-11 | POSSIBLE_RELEVANCE |
| repo-001612 | marcosbolanos/pariwise-representations | source | — | LICENSE_UNCLEAR | 2026-05-11 | POSSIBLE_RELEVANCE |
| repo-001613 | marcosbolanos/ped-t1d-model | source | R | LICENSE_UNCLEAR | 2025-02-25 | HIGH_RELEVANCE |
| repo-001614 | marcosbolanos/pgvector-age | source | Python | LICENSE_UNCLEAR | 2025-06-11 | LOW_RELEVANCE |
| repo-001615 | marcosbolanos/pjepa | source | — | LICENSE_UNCLEAR | 2026-03-24 | LOW_RELEVANCE |
| repo-001616 | marcosbolanos/ProSpero | fork | Python | GPL-3.0 | 2026-07-23 | HIGH_RELEVANCE |
| repo-001617 | marcosbolanos/ProSST | fork | Python | NOASSERTION | 2026-06-08 | HIGH_RELEVANCE |
| repo-001618 | marcosbolanos/RLBind | source | Python | LICENSE_UNCLEAR | 2026-02-09 | POSSIBLE_RELEVANCE |
| repo-001619 | marcosbolanos/SaaS-Foundations | fork | HTML | MIT | 2024-09-11 | IRRELEVANT |
| repo-001620 | marcosbolanos/sandbot | source | Dockerfile | LICENSE_UNCLEAR | 2025-08-01 | POSSIBLE_RELEVANCE |
| repo-001621 | marcosbolanos/supernova-dx | source | Just | Apache-2.0 | 2026-06-29 | POSSIBLE_RELEVANCE |
| repo-001622 | marcosbolanos/surface-filling-curve-flows | fork | C++ | MIT | 2026-03-26 | LOW_RELEVANCE |
| repo-001623 | marcosbolanos/synth | source | Python | LICENSE_UNCLEAR | 2026-07-30 | IRRELEVANT |
| repo-001624 | marcosbolanos/t1diab-sadm-mk2 | fork | R | LICENSE_UNCLEAR | 2024-12-27 | HIGH_RELEVANCE |
| repo-001625 | marcosbolanos/valentines-snake | source | JavaScript | LICENSE_UNCLEAR | 2025-02-27 | IRRELEVANT |
| repo-001626 | marcosbolanos/Virtual-Cell-Challenge | fork | — | LICENSE_UNCLEAR | 2025-09-15 | HIGH_RELEVANCE |
| repo-001627 | marcosbolanos/vital | fork | C++ | GPL-3.0 | 2023-05-25 | IRRELEVANT |
| repo-001628 | mickaelleclercq/aurora | source | Python | NOASSERTION | 2026-08-17 | IRRELEVANT |
| repo-001629 | mickaelleclercq/AutoFigure-Edit | source | Python | MIT | 2026-04-13 | HIGH_RELEVANCE |
| repo-001630 | mickaelleclercq/bioAgent | source | Python | LICENSE_UNCLEAR | 2025-09-22 | HIGH_RELEVANCE |
| repo-001631 | mickaelleclercq/BioDiscML | source | Java | GPL-3.0 | 2025-07-18 | HIGH_RELEVANCE |
| repo-001632 | mickaelleclercq/caustic_water_removal | source | Python | LICENSE_UNCLEAR | 2026-03-26 | LOW_RELEVANCE |
| repo-001633 | mickaelleclercq/CUMAb-pipeline | source | HTML | LICENSE_UNCLEAR | 2026-04-02 | POSSIBLE_RELEVANCE |
| repo-001634 | mickaelleclercq/glass | source | JavaScript | GPL-3.0 | 2026-04-27 | POSSIBLE_RELEVANCE |
| repo-001635 | mickaelleclercq/mesotox | source | HTML | LICENSE_UNCLEAR | 2026-04-16 | POSSIBLE_RELEVANCE |
| repo-001636 | mickaelleclercq/mirdup | source | Java | LICENSE_UNCLEAR | 2019-11-15 | HIGH_RELEVANCE |
| repo-001637 | mickaelleclercq/mock_data | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-10-07 | IRRELEVANT |
| repo-001638 | mickaelleclercq/seafloor_3d | source | Python | LICENSE_UNCLEAR | 2026-03-27 | LOW_RELEVANCE |
| repo-001639 | mickaelleclercq/stereo_measure | source | Python | LICENSE_UNCLEAR | 2025-08-22 | LOW_RELEVANCE |
| repo-001640 | mickaelleclercq/TDM | fork | R | BSD-3-Clause | 2020-06-22 | HIGH_RELEVANCE |
| repo-001641 | MintaYLu/Best-README-Template | fork | — | MIT | 2021-01-15 | IRRELEVANT |
| repo-000623 | MintaYLu/Biomni | fork | Python | Apache-2.0 | 2025-09-27 | HIGH_RELEVANCE |
| repo-001642 | MintaYLu/claude-code-haha | fork | TypeScript | LICENSE_UNCLEAR | 2026-04-01 | POSSIBLE_RELEVANCE |
| repo-001643 | MintaYLu/clinical-trial-outcome-prediction | fork | Python | LICENSE_UNCLEAR | 2023-07-17 | HIGH_RELEVANCE |
| repo-001644 | MintaYLu/COT | source | Jupyter Notebook | MIT | 2022-03-29 | POSSIBLE_RELEVANCE |
| repo-001645 | MintaYLu/DDN | source | Python | MIT | 2024-01-18 | POSSIBLE_RELEVANCE |
| repo-001646 | MintaYLu/DDN-R | source | HTML | MIT | 2023-04-19 | POSSIBLE_RELEVANCE |
| repo-001647 | MintaYLu/MIMOSA | fork | Python | LICENSE_UNCLEAR | 2023-07-17 | HIGH_RELEVANCE |
| repo-001648 | MintaYLu/QA_benchmark | source | — | LICENSE_UNCLEAR | 2025-11-20 | POSSIBLE_RELEVANCE |
| repo-001649 | MinxZ/ai_challenger_2018 | source | Jupyter Notebook | MIT | 2018-05-23 | LOW_RELEVANCE |
| repo-001650 | MinxZ/assignment | source | MATLAB | LICENSE_UNCLEAR | 2017-07-31 | IRRELEVANT |
| repo-001651 | MinxZ/ChatGPT-Next-Web | fork | TypeScript | MIT | 2023-07-20 | IRRELEVANT |
| repo-001652 | MinxZ/circle | source | Python | MIT | 2019-09-18 | IRRELEVANT |
| repo-000541 | MinxZ/dleader_agent | fork | Python | Apache-2.0 | 2026-02-02 | HIGH_RELEVANCE |
| repo-001653 | MinxZ/Dog-Breed-Identification | source | Jupyter Notebook | MIT | 2018-03-05 | LOW_RELEVANCE |
| repo-001654 | MinxZ/etf-rotation-lab | source | Python | MIT | 2026-08-19 | IRRELEVANT |
| repo-001655 | MinxZ/fashion_mnist | source | Jupyter Notebook | MIT | 2019-12-10 | LOW_RELEVANCE |
| repo-001656 | MinxZ/FinGenius | fork | Python | GPL-3.0 | 2025-07-29 | IRRELEVANT |
| repo-001657 | MinxZ/flask-hello-world | source | Python | LICENSE_UNCLEAR | 2024-06-04 | IRRELEVANT |
| repo-001658 | MinxZ/flask-hello-world2 | source | Python | LICENSE_UNCLEAR | 2024-06-04 | IRRELEVANT |
| repo-001659 | MinxZ/Gemini | source | Jupyter Notebook | MIT | 2023-07-19 | POSSIBLE_RELEVANCE |
| repo-001660 | MinxZ/homework | fork | Python | MIT | 2018-12-08 | IRRELEVANT |
| repo-001661 | MinxZ/Invasive-Species-Monitoring | source | Jupyter Notebook | LICENSE_UNCLEAR | 2017-11-29 | HIGH_RELEVANCE |
| repo-001662 | MinxZ/learn_programming | source | Python | MIT | 2024-12-10 | IRRELEVANT |
| repo-001663 | MinxZ/loopfittingproblem | source | Python | Apache-2.0 | 2026-01-22 | POSSIBLE_RELEVANCE |
| repo-001664 | MinxZ/minxz.github.io | source | — | LICENSE_UNCLEAR | 2021-03-18 | IRRELEVANT |
| repo-001665 | MinxZ/MMSplice_MTSplice | fork | Jupyter Notebook | MIT | 2026-01-28 | HIGH_RELEVANCE |
| repo-001666 | MinxZ/multi_label | source | Python | MIT | 2019-12-10 | LOW_RELEVANCE |
| repo-001667 | MinxZ/s2orc-doc2json | fork | Python | Apache-2.0 | 2024-04-11 | HIGH_RELEVANCE |
| repo-001668 | MinxZ/streamlit-agent | fork | TypeScript | Apache-2.0 | 2023-12-14 | POSSIBLE_RELEVANCE |
| repo-001669 | MinxZ/streamlit-auth0 | fork | Python | MIT | 2024-08-19 | LOW_RELEVANCE |
| repo-001670 | MinxZ/Streamlit-Authenticator | fork | Python | NOASSERTION | 2024-08-18 | LOW_RELEVANCE |
| repo-001671 | MinxZ/summary_all | fork | TypeScript | GPL-3.0 | 2023-09-13 | IRRELEVANT |
| repo-001672 | MinxZ/templet | source | — | MIT | 2022-05-05 | IRRELEVANT |
| repo-001673 | MinxZ/yougeng-ai | source | Python | LICENSE_UNCLEAR | 2023-11-26 | POSSIBLE_RELEVANCE |
| repo-000395 | nevergreendd/Biomni | fork | Python | Apache-2.0 | 2025-12-08 | HIGH_RELEVANCE |
| repo-001674 | nevergreendd/fl_study3 | source | Jupyter Notebook | MIT | 2023-11-16 | LOW_RELEVANCE |
| repo-001675 | nevergreendd/LookSo.Jr | fork | C++ | LICENSE_UNCLEAR | 2017-04-05 | IRRELEVANT |
| repo-001676 | nevergreendd/Massive-PotreeConverter | fork | Python | Apache-2.0 | 2019-04-29 | LOW_RELEVANCE |
| repo-001677 | nevergreendd/MolGrapher | fork | Python | MIT | 2025-03-26 | HIGH_RELEVANCE |
| repo-001678 | nevergreendd/opengv | fork | C++ | NOASSERTION | 2020-03-16 | LOW_RELEVANCE |
| repo-001679 | nevergreendd/swift-transformers | fork | Swift | Apache-2.0 | 2024-04-20 | LOW_RELEVANCE |
| repo-001680 | nevergreendd/zshsettings | fork | Shell | LICENSE_UNCLEAR | 2021-05-15 | IRRELEVANT |
| repo-000575 | PabloPauling/Biomni | fork | Python | Apache-2.0 | 2025-11-24 | HIGH_RELEVANCE |
| repo-001681 | PabloPauling/gemini-cli | fork | TypeScript | Apache-2.0 | 2025-08-22 | POSSIBLE_RELEVANCE |
| repo-001682 | PabloPauling/PabloPauling | source | — | LICENSE_UNCLEAR | 2026-03-27 | IRRELEVANT |
| repo-001683 | PabloPauling/posebusters-mcp-server | source | Python | BSD-3-Clause | 2025-07-14 | HIGH_RELEVANCE |
| repo-001684 | PabloPauling/Protenix | fork | Python | Apache-2.0 | 2026-04-09 | HIGH_RELEVANCE |
| repo-001685 | Pidem/amazon-bedrock-agentcore-samples | fork | Jupyter Notebook | Apache-2.0 | 2025-07-18 | POSSIBLE_RELEVANCE |
| repo-001686 | Pidem/amazon-sagemaker-examples | fork | Jupyter Notebook | Apache-2.0 | 2025-02-13 | LOW_RELEVANCE |
| repo-001687 | Pidem/beaker-kernel | fork | Vue | MIT | 2025-06-23 | POSSIBLE_RELEVANCE |
| repo-000361 | Pidem/Biomni | fork | Python | Apache-2.0 | 2026-02-03 | HIGH_RELEVANCE |
| repo-001688 | Pidem/CloudFormation-Deep-Dive | fork | JavaScript | LICENSE_UNCLEAR | 2021-06-09 | IRRELEVANT |
| repo-001689 | Pidem/cloudformation-studio-domain | fork | — | MIT-0 | 2024-07-01 | IRRELEVANT |
| repo-001690 | Pidem/Columbia_AI_course_CS | source | Python | LICENSE_UNCLEAR | 2017-07-07 | IRRELEVANT |
| repo-001691 | Pidem/CORAL | fork | Python | NOASSERTION | 2026-07-27 | HIGH_RELEVANCE |
| repo-001692 | Pidem/DataHarmonizationAgent | source | Python | LICENSE_UNCLEAR | 2025-07-18 | POSSIBLE_RELEVANCE |
| repo-001693 | Pidem/DeepLearning-Tensorflow2 | source | Jupyter Notebook | LICENSE_UNCLEAR | 2021-02-16 | IRRELEVANT |
| repo-001694 | Pidem/equiformer-trainium | source | Python | LICENSE_UNCLEAR | 2026-05-15 | POSSIBLE_RELEVANCE |
| repo-001695 | Pidem/facenet | fork | Python | MIT | 2020-05-02 | IRRELEVANT |
| repo-001696 | Pidem/HCLSBenchmarks | source | — | LICENSE_UNCLEAR | 2026-06-02 | HIGH_RELEVANCE |
| repo-001697 | Pidem/insightface | fork | Python | MIT | 2020-08-26 | IRRELEVANT |
| repo-001698 | Pidem/Machine_Learning_Research | source | — | LICENSE_UNCLEAR | 2019-06-13 | LOW_RELEVANCE |
| repo-001699 | Pidem/MachineLearning101 | source | R | LICENSE_UNCLEAR | 2017-11-09 | IRRELEVANT |
| repo-001700 | Pidem/medmarks | fork | Python | MIT | 2026-07-01 | HIGH_RELEVANCE |
| repo-001701 | Pidem/mgp-tcn | fork | Python | BSD-3-Clause | 2021-02-16 | HIGH_RELEVANCE |
| repo-001702 | Pidem/ml-specialized-hardware | fork | Jupyter Notebook | MIT-0 | 2025-02-16 | LOW_RELEVANCE |
| repo-001703 | Pidem/MobileNet-SSD | fork | Python | MIT | 2018-12-21 | LOW_RELEVANCE |
| repo-001704 | Pidem/models | fork | Python | Apache-2.0 | 2019-07-12 | LOW_RELEVANCE |
| repo-001705 | Pidem/MongoDB-and-SQL | source | Python | LICENSE_UNCLEAR | 2017-10-26 | IRRELEVANT |
| repo-001706 | Pidem/neuron-performance-book | source | Python | LICENSE_UNCLEAR | 2026-07-17 | LOW_RELEVANCE |
| repo-001707 | Pidem/Person_reID_baseline_pytorch | fork | Python | MIT | 2020-05-21 | LOW_RELEVANCE |
| repo-001708 | Pidem/PharmaCommercialDemo | source | Python | LICENSE_UNCLEAR | 2025-10-29 | POSSIBLE_RELEVANCE |
| repo-001709 | Pidem/Pidem.github.io | source | SCSS | LICENSE_UNCLEAR | 2026-07-08 | IRRELEVANT |
| repo-001710 | Pidem/tensorrt | fork | Python | Apache-2.0 | 2019-07-15 | LOW_RELEVANCE |
| repo-001711 | Pidem/tf2_course | fork | Jupyter Notebook | Apache-2.0 | 2019-06-23 | IRRELEVANT |
| repo-001712 | Pidem/TRIDENT | fork | Python | NOASSERTION | 2025-02-24 | HIGH_RELEVANCE |
| repo-001713 | Pidem/verifiers | fork | Python | MIT | 2026-06-02 | POSSIBLE_RELEVANCE |
| repo-001714 | Pidem/virtual-lab | fork | Jupyter Notebook | MIT | 2025-05-28 | HIGH_RELEVANCE |
| repo-001715 | Pidem/yoloface | fork | Python | MIT | 2019-11-04 | IRRELEVANT |
| repo-001716 | PLippmann/atropos | fork | Python | MIT | 2026-01-31 | POSSIBLE_RELEVANCE |
| repo-001717 | PLippmann/AwesomeAnimeResearch | fork | — | LICENSE_UNCLEAR | 2024-12-03 | IRRELEVANT |
| repo-000700 | PLippmann/Biomni | fork | Python | Apache-2.0 | 2025-07-21 | HIGH_RELEVANCE |
| repo-001718 | PLippmann/disaster-tweet-jax | source | Jupyter Notebook | Apache-2.0 | 2024-10-21 | LOW_RELEVANCE |
| repo-001719 | PLippmann/gemma3-jax-fast | source | Python | LICENSE_UNCLEAR | 2025-08-19 | LOW_RELEVANCE |
| repo-001720 | PLippmann/llama-ft | source | Python | LICENSE_UNCLEAR | 2025-01-10 | LOW_RELEVANCE |
| repo-001721 | PLippmann/multimodal-manga-translation | source | Jupyter Notebook | MIT | 2024-12-03 | IRRELEVANT |
| repo-001722 | PLippmann/nanochat | fork | Python | MIT | 2026-01-16 | LOW_RELEVANCE |
| repo-001723 | PLippmann/nanogpt-jax | source | Python | MIT | 2025-01-03 | LOW_RELEVANCE |
| repo-001724 | PLippmann/nomos-lean | fork | Python | MIT | 2026-03-29 | POSSIBLE_RELEVANCE |
| repo-001725 | PLippmann/PLippmann.github.io | source | HTML | LICENSE_UNCLEAR | 2026-07-22 | IRRELEVANT |
| repo-001726 | PLippmann/s1 | fork | Python | Apache-2.0 | 2025-02-13 | LOW_RELEVANCE |
| repo-001727 | ryanDing26/aging-theories | source | Python | LICENSE_UNCLEAR | 2025-10-23 | HIGH_RELEVANCE |
| repo-001728 | ryanDing26/AS-Resource-Guide | source | HTML | LICENSE_UNCLEAR | 2023-10-21 | POSSIBLE_RELEVANCE |
| repo-001729 | ryanDing26/asgs-webmaster-challenge | source | JavaScript | LICENSE_UNCLEAR | 2026-01-03 | IRRELEVANT |
| repo-000507 | ryanDing26/Biomni | fork | Python | Apache-2.0 | 2025-10-19 | HIGH_RELEVANCE |
| repo-001730 | ryanDing26/Career-GPT | source | TypeScript | LICENSE_UNCLEAR | 2024-09-10 | IRRELEVANT |
| repo-001731 | ryanDing26/Convolutional-Semantic-Segmentation | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-02-17 | LOW_RELEVANCE |
| repo-001732 | ryanDing26/Diabetes-Classifier | source | Python | LICENSE_UNCLEAR | 2025-04-29 | HIGH_RELEVANCE |
| repo-001733 | ryanDing26/diffpath | source | Python | LICENSE_UNCLEAR | 2025-11-10 | POSSIBLE_RELEVANCE |
| repo-001734 | ryanDing26/diffusion | source | Python | LICENSE_UNCLEAR | 2025-12-03 | LOW_RELEVANCE |
| repo-001735 | ryanDing26/emDNA-GPU | source | Python | LICENSE_UNCLEAR | 2025-11-03 | HIGH_RELEVANCE |
| repo-001736 | ryanDing26/graph-transformers | source | Python | LICENSE_UNCLEAR | 2025-10-27 | LOW_RELEVANCE |
| repo-001737 | ryanDing26/Hackaging-team-Ryan | source | Python | LICENSE_UNCLEAR | 2025-10-23 | HIGH_RELEVANCE |
| repo-001738 | ryanDing26/HistoPath | source | Jupyter Notebook | MIT | 2025-11-08 | HIGH_RELEVANCE |
| repo-001739 | ryanDing26/Housing-Price-Predictor | source | Jupyter Notebook | LICENSE_UNCLEAR | 2024-06-26 | IRRELEVANT |
| repo-001740 | ryanDing26/JDRE-agent | source | Python | LICENSE_UNCLEAR | 2025-11-08 | POSSIBLE_RELEVANCE |
| repo-001741 | ryanDing26/Kumo-AI-Hackathon | source | TypeScript | LICENSE_UNCLEAR | 2025-08-18 | LOW_RELEVANCE |
| repo-001742 | ryanDing26/LatentTarget | source | Python | LICENSE_UNCLEAR | 2025-10-21 | POSSIBLE_RELEVANCE |
| repo-001743 | ryanDing26/LeetCoding | source | Python | LICENSE_UNCLEAR | 2024-08-24 | IRRELEVANT |
| repo-001744 | ryanDing26/lumaa-spring-2025-ai-ml | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2025-02-24 | IRRELEVANT |
| repo-001745 | ryanDing26/NBA-Salary-Analysis | source | Jupyter Notebook | LICENSE_UNCLEAR | 2024-03-21 | IRRELEVANT |
| repo-001746 | ryanDing26/pantry-tracker | source | JavaScript | LICENSE_UNCLEAR | 2024-08-17 | IRRELEVANT |
| repo-001747 | ryanDing26/paper-processing | source | Python | LICENSE_UNCLEAR | 2026-01-22 | POSSIBLE_RELEVANCE |
| repo-001748 | ryanDing26/personal-website | source | CSS | LICENSE_UNCLEAR | 2024-10-16 | IRRELEVANT |
| repo-001749 | ryanDing26/portfolio-tracker | source | JavaScript | LICENSE_UNCLEAR | 2025-10-22 | IRRELEVANT |
| repo-001750 | ryanDing26/remit | source | JavaScript | LICENSE_UNCLEAR | 2026-01-03 | IRRELEVANT |
| repo-001751 | ryanDing26/reprogramming | source | Python | LICENSE_UNCLEAR | 2025-12-16 | POSSIBLE_RELEVANCE |
| repo-001752 | ryanDing26/ryanDing26 | source | — | LICENSE_UNCLEAR | 2025-10-19 | IRRELEVANT |
| repo-001753 | ryanDing26/Software-Tools-Labs | source | Java | LICENSE_UNCLEAR | 2024-06-26 | IRRELEVANT |
| repo-001754 | ryanDing26/splitwise | source | JavaScript | LICENSE_UNCLEAR | 2026-01-03 | IRRELEVANT |
| repo-001755 | ryanDing26/teaching-programming-portfolio | source | HTML | LICENSE_UNCLEAR | 2026-04-07 | IRRELEVANT |
| repo-001756 | ryanDing26/Tech-Layoff-Modeling | fork | Jupyter Notebook | GPL-2.0 | 2024-06-25 | IRRELEVANT |
| repo-001757 | ryanDing26/Transformer-Sentiment-Analyzer | source | Python | LICENSE_UNCLEAR | 2025-02-16 | LOW_RELEVANCE |
| repo-001758 | ryanDing26/YuGilsonLab-DataAnalysis | fork | Python | LICENSE_UNCLEAR | 2023-10-24 | POSSIBLE_RELEVANCE |
| repo-001759 | RyanLi1028/2021-GGJ | source | JavaScript | LICENSE_UNCLEAR | 2021-02-13 | IRRELEVANT |
| repo-001760 | RyanLi1028/Biomni-SkyRL | fork | Python | Apache-2.0 | 2025-09-15 | HIGH_RELEVANCE |
| repo-001761 | RyanLi1028/cs149gpt | fork | Python | LICENSE_UNCLEAR | 2023-11-29 | IRRELEVANT |
| repo-001762 | RyanLi1028/CS236-Final-Project | source | Jupyter Notebook | LICENSE_UNCLEAR | 2023-12-13 | IRRELEVANT |
| repo-001763 | RyanLi1028/cybench | fork | HTML | LICENSE_UNCLEAR | 2024-09-19 | POSSIBLE_RELEVANCE |
| repo-001764 | RyanLi1028/docs | fork | Python | NOASSERTION | 2021-04-03 | LOW_RELEVANCE |
| repo-001765 | RyanLi1028/DubHacks2020 | fork | JavaScript | LICENSE_UNCLEAR | 2020-10-19 | IRRELEVANT |
| repo-001766 | RyanLi1028/DubLease | source | JavaScript | LICENSE_UNCLEAR | 2023-02-06 | IRRELEVANT |
| repo-001767 | RyanLi1028/DubLeaseApp | fork | JavaScript | LICENSE_UNCLEAR | 2023-05-04 | IRRELEVANT |
| repo-001768 | RyanLi1028/GPT-3 | source | JavaScript | LICENSE_UNCLEAR | 2020-11-27 | LOW_RELEVANCE |
| repo-001769 | RyanLi1028/lab_website | fork | HTML | LICENSE_UNCLEAR | 2021-02-10 | IRRELEVANT |
| repo-001770 | RyanLi1028/misinfo_believability | source | Python | LICENSE_UNCLEAR | 2024-03-04 | POSSIBLE_RELEVANCE |
| repo-001771 | RyanLi1028/NegotiationArena | fork | Python | LICENSE_UNCLEAR | 2025-04-28 | POSSIBLE_RELEVANCE |
| repo-001772 | RyanLi1028/PI2-NL-Interactive-Visualization-Interface-Generation-from-Natural-Language-Tasks | source | TeX | LICENSE_UNCLEAR | 2022-07-28 | LOW_RELEVANCE |
| repo-001773 | RyanLi1028/Sketch2Code | fork | Jupyter Notebook | MIT | 2024-03-06 | LOW_RELEVANCE |
| repo-001774 | RyanLi1028/socket.io | fork | JavaScript | MIT | 2021-01-08 | IRRELEVANT |
| repo-001775 | RyanLi1028/sync-endpoint-web-ui | fork | Java | Apache-2.0 | 2021-05-21 | IRRELEVANT |
| repo-001776 | RyanLi1028/temp | source | — | LICENSE_UNCLEAR | 2024-10-23 | IRRELEVANT |
| repo-001777 | RyanLi1028/Web-Games | source | JavaScript | LICENSE_UNCLEAR | 2020-09-29 | IRRELEVANT |

## Identity and scope boundary

- Person depth remains one; repository contributors do not enter P.
- The Bot is retained in P but has no User repository connection to enumerate.
- Fork metadata does not prove a unique change. Existing Biomni archaeology stays
  canonical for all eight overlaps.
- Public availability and `LICENSE_UNCLEAR`/`NOASSERTION` are not reuse
  permission. External metadata remains untrusted research data.
- The unresolved `RyanLi1028` versus raw `RyanLi0802` identity caution remains;
  this repository inventory does not merge them.

## Evidence and limits

- GraphQL captured complete owner totals/cursors and repository metadata including
  fork parent, default head/date, topics, license object, activity, state, and
  latest public release.
- All 10 User owner connections are exhausted at the observation time. Private,
  deleted, transferred, and later-created repositories remain unobservable.
- Relevance labels are metadata-grounded INFERENCE and require source, license,
  security, and lineage verification before deep audit or integration ranking.

## Next action

Continue with the next unprocessed User accounts after
`person-github-000031`, while marking any intervening Bot account not applicable
instead of silently skipping it.
