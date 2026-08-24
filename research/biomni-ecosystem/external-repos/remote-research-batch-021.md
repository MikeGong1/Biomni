# 远程调研 Batch 021

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **813–862**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `DATASET_OR_BENCHMARK` | 6 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 9 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 20 |
| 分类 `LOW_INFORMATION_RECHECK` | 3 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 10 |
| 标记 `CHILD_FORK_SURFACE` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 42 |
| 标记 `LICENSE_UNCLEAR` | 18 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RECENT_ACTIVE` | 50 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 813 | `molecule-generator-collection/chemtsv2`<br>source=`molecule-generator-collection/ChemTSv2` | `repo-005893` `dabulseco/ChemTSv2`（REPRESENTATIVE；parent=molecule-generator-collection/ChemTSv2） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 814 | `google-deepmind/deepmind-research`<br>source=`google-deepmind/deepmind-research` | `repo-006606` `psknlr/deepmind-research`（REPRESENTATIVE；parent=google-deepmind/deepmind-research） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 815 | `airoh-pipeline/airoh-template`<br>source=`airoh-pipeline/airoh-template` | `repo-004373` `yarikoptic/airoh-template`（REPRESENTATIVE；parent=airoh-pipeline/airoh-template） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 816 | `ddw2aigroup2cqupt/pa-llava`<br>source=`ddw2AIGROUP2CQUPT/PA-LLaVA` | `repo-006443` `chaudhariatul/PA-LLaVA`（REPRESENTATIVE；parent=ddw2AIGROUP2CQUPT/PA-LLaVA） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 817 | `yhpu/rdf_analysis`<br>source=`yhpu/rdf_analysis` | `repo-007425` `Rasic2/rdf_analysis`（REPRESENTATIVE；parent=yhpu/rdf_analysis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 818 | `nigmat-future/diabeta-ai-insight`<br>source=`Nigmat-future/diabeta-ai-insight` | `repo-003182` `Nigmat-future/diabeta-ai-insight`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 819 | `lean-dojo/leanagent`<br>source=`lean-dojo/LeanAgent` | `repo-003273` `Rakshitha-Ireddi/LeanAgent`（REPRESENTATIVE；parent=lean-dojo/LeanAgent）<br>`repo-005829` `yaswanth169/LeanAgent`（MEMBER；parent=lean-dojo/LeanAgent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 820 | `sina-mansour/ohbm2025-reproducible-research`<br>source=`sina-mansour/ohbm2025-reproducible-research` | `repo-005264` `yarikoptic/ohbm2025-reproducible-research`（REPRESENTATIVE；parent=sina-mansour/ohbm2025-reproducible-research） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 821 | `australian-imaging-service/australian-imaging-service.github.io`<br>source=`Australian-Imaging-Service/Australian-Imaging-Service.github.io` | `repo-004412` `yarikoptic/Australian-Imaging-Service.github.io`（REPRESENTATIVE；parent=Australian-Imaging-Service/Australian-Imaging-Service.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 822 | `vik-u/ai-validation-feedback-loops`<br>source=`Vik-u/ai-validation-feedback-loops` | `repo-006935` `Vik-u/ai-validation-feedback-loops`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 823 | `deepmodeling/ai4s-agent-tools`<br>source=`deepmodeling/AI4S-agent-tools` | `repo-007403` `Rasic2/AI4S-agent-tools`（REPRESENTATIVE；parent=deepmodeling/AI4S-agent-tools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 824 | `mathworks/matlab-support-for-zarr-files`<br>source=`mathworks/MATLAB-support-for-Zarr-files` | `repo-005081` `yarikoptic/MATLAB-support-for-Zarr-files`（REPRESENTATIVE；parent=mathworks/MATLAB-support-for-Zarr-files） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 825 | `garner-code/psyr`<br>source=`garner-code/PsyR` | `repo-005386` `yarikoptic/PsyR`（REPRESENTATIVE；parent=garner-code/PsyR） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 826 | `hip-infrastructure/bidsificator`<br>source=`HIP-infrastructure/Bidsificator` | `repo-004480` `yarikoptic/Bidsificator`（REPRESENTATIVE；parent=HIP-infrastructure/Bidsificator） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 827 | `openmetadatainitiative/bids2openminds`<br>source=`openMetadataInitiative/bids2openminds` | `repo-004476` `yarikoptic/bids2openminds`（REPRESENTATIVE；parent=openMetadataInitiative/bids2openminds） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 828 | `openneuropet/outreach`<br>source=`openneuropet/outreach` | `repo-005305` `yarikoptic/outreach`（REPRESENTATIVE；parent=openneuropet/outreach） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 829 | `ayushmaniar/big-data-science-drug-protein-interactions`<br>source=`Ayushmaniar/Big-Data-Science-Drug-Protein-Interactions` | `repo-002436` `Ayushmaniar/Big-Data-Science-Drug-Protein-Interactions`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 830 | `dandi/dandi-hub`<br>source=`dandi/dandi-hub` | `repo-004644` `yarikoptic/dandihub`（REPRESENTATIVE；parent=dandi/dandi-hub） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 831 | `kalinnonchev/biomed_nccl_benchmark`<br>source=`KalinNonchev/biomed_nccl_benchmark` | `repo-002990` `KalinNonchev/biomed_nccl_benchmark`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 832 | `mushroomfire/mdapy`<br>source=`mushroomfire/mdapy` | `repo-006977` `Vik-u/mdapy`（REPRESENTATIVE；parent=mushroomfire/mdapy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 833 | `mcp-use/mcp-use`<br>source=`mcp-use/mcp-use` | `repo-005085` `yarikoptic/mcp-use`（REPRESENTATIVE；parent=mcp-use/mcp-use） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 834 | `ylaboratory/gene-embedding-benchmarks`<br>source=`ylaboratory/gene-embedding-benchmarks` | `repo-001288` `HelloWorldLTY/gene-embedding-benchmarks`（REPRESENTATIVE；parent=ylaboratory/gene-embedding-benchmarks） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 835 | `ksun63/protein-vibe-coding`<br>source=`KSUN63/protein-vibe-coding` | `repo-007163` `KSUN63/protein-vibe-coding`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 836 | `neuroprismlab/braineffex`<br>source=`neuroprismlab/BrainEffeX` | `repo-004505` `yarikoptic/BrainEffeX`（REPRESENTATIVE；parent=neuroprismlab/BrainEffeX） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 837 | `mit-lcp/physionet-build`<br>source=`MIT-LCP/physionet-build` | `repo-005334` `yarikoptic/physionet-build`（REPRESENTATIVE；parent=MIT-LCP/physionet-build） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 838 | `mit-lcp/physionet`<br>source=`MIT-LCP/physionet` | `repo-005333` `yarikoptic/physionet`（REPRESENTATIVE；parent=MIT-LCP/physionet） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 839 | `ali-maq/civic_extractor`<br>source=`Ali-Maq/civic_extractor` | `repo-006306` `Ali-Maq/civic_extractor`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 840 | `gevaertlab/sequoia-pub`<br>source=`gevaertlab/sequoia-pub` | `repo-007293` `NKalavros/sequoia-pub`（REPRESENTATIVE；parent=gevaertlab/sequoia-pub） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 841 | `zou-group/sleepfm-clinical`<br>source=`zou-group/sleepfm-clinical` | `repo-006536` `gutendzx/sleepfm-clinical`（REPRESENTATIVE；parent=zou-group/sleepfm-clinical） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 842 | `sidhomj/deeptcr`<br>source=`sidhomj/DeepTCR` | `repo-006317` `Ali-Maq/DeepTCR`（REPRESENTATIVE；parent=sidhomj/DeepTCR） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 843 | `maayanlab/playbook-workflow-builder`<br>source=`MaayanLab/Playbook-Workflow-Builder` | `repo-006346` `Ali-Maq/Playbook-Workflow-Builder`（REPRESENTATIVE；parent=MaayanLab/Playbook-Workflow-Builder） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 844 | `neuroinformatics-unit/movement`<br>source=`neuroinformatics-unit/movement` | `repo-005128` `yarikoptic/movement`（REPRESENTATIVE；parent=neuroinformatics-unit/movement） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 845 | `rly/ndx-pose`<br>source=`rly/ndx-pose` | `repo-005160` `yarikoptic/ndx-pose`（REPRESENTATIVE；parent=rly/ndx-pose） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 846 | `rordenlab/niimath`<br>source=`rordenlab/niimath` | `repo-005215` `yarikoptic/niimath`（REPRESENTATIVE；parent=rordenlab/niimath） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 847 | `future-house/finch`<br>source=`Future-House/finch` | `repo-007067` `jaybee84/data-analysis-crow`（REPRESENTATIVE；parent=Future-House/finch） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 848 | `zaneveld/full_spectrum_bioinformatics`<br>source=`zaneveld/full_spectrum_bioinformatics` | `repo-005916` `dabulseco/full_spectrum_bioinformatics`（REPRESENTATIVE；parent=zaneveld/full_spectrum_bioinformatics） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 849 | `repronim/containers`<br>source=`ReproNim/containers` | `repo-004594` `yarikoptic/containers`（REPRESENTATIVE；parent=ReproNim/containers） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 850 | `matthijshak/metaldock`<br>source=`MatthijsHak/MetalDock` | `repo-006978` `Vik-u/MetalDock`（REPRESENTATIVE；parent=MatthijsHak/MetalDock） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 851 | `virginiaanton/digital-twin-based-system-for-pregnancy-risk-prevention-and-perinatal-care`<br>source=`virginiaanton/Digital-Twin-based-system-for-pregnancy-risk-prevention-and-perinatal-care` | `repo-006841` `tangxuan82/Digital-Twin-based-system-for-pregnancy-risk-prevention-and-perinatal-care`（REPRESENTATIVE；parent=virginiaanton/Digital-Twin-based-system-for-pregnancy-risk-prevention-and-perinatal-care） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 852 | `samarth-kadaba/smdpo`<br>source=`samarth-kadaba/SMDPO` | `repo-003933` `samarth-kadaba/SMDPO`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 853 | `vjcitn/biocblog`<br>source=`vjcitn/biocblog` | `repo-000973` `anngvu/biocblog`（REPRESENTATIVE；parent=vjcitn/biocblog） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 854 | `bowang-lab/integrao`<br>source=`bowang-lab/IntegrAO` | `repo-006328` `Ali-Maq/IntegrAO`（REPRESENTATIVE；parent=bowang-lab/IntegrAO） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 855 | `repronim/sumarizefmriprep`<br>source=`ReproNim/SumarizeFmriprep` | `repo-005641` `yarikoptic/SumarizeFmriprep`（REPRESENTATIVE；parent=ReproNim/SumarizeFmriprep） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 856 | `modelcontextprotocol/modelcontextprotocol`<br>source=`modelcontextprotocol/modelcontextprotocol` | `repo-005118` `yarikoptic/modelcontextprotocol`（REPRESENTATIVE；parent=modelcontextprotocol/modelcontextprotocol） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 857 | `anngvu/bioc-curation`<br>source=`anngvu/bioc-curation` | `repo-000972` `anngvu/bioc-curation`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 858 | `napari/napari`<br>source=`napari/napari` | `repo-005150` `yarikoptic/napari`（REPRESENTATIVE；parent=napari/napari） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 859 | `biolink/kgx`<br>source=`biolink/kgx` | `repo-000922` `andrewsu/kgx`（REPRESENTATIVE；parent=biolink/kgx） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 860 | `pmbio/health-privacy-challenge`<br>source=`PMBio/Health-Privacy-Challenge` | `repo-007082` `jaybee84/Health-Privacy-Challenge`（REPRESENTATIVE；parent=PMBio/Health-Privacy-Challenge） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 861 | `sakanaai/ai-scientist-v2`<br>source=`SakanaAI/AI-Scientist-v2` | `repo-001525` `kuanlinhuang/AI-Scientist-v2`（REPRESENTATIVE；parent=SakanaAI/AI-Scientist-v2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 862 | `knowledge-graph-hub/kg-registry`<br>source=`Knowledge-Graph-Hub/kg-registry` | `repo-000921` `andrewsu/kg-registry`（REPRESENTATIVE；parent=Knowledge-Graph-Hub/kg-registry） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `813–862`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-021-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
