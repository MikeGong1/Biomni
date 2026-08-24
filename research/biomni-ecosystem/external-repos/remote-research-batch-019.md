# 远程调研 Batch 019

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **713–762**；**50** 个 family；**52** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 52 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `DATASET_OR_BENCHMARK` | 5 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 13 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 19 |
| 分类 `LOW_INFORMATION_RECHECK` | 5 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 6 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `FORK_LINEAGE_REQUIRED` | 40 |
| 标记 `LICENSE_UNCLEAR` | 18 |
| 标记 `MULTI_MEMBER_FAMILY` | 2 |
| 标记 `RECENT_ACTIVE` | 50 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 713 | `aqlaboratory/openfold`<br>source=`aqlaboratory/openfold` | `repo-006113` `leizhou69/openfold`（REPRESENTATIVE；parent=aqlaboratory/openfold） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 714 | `upstash/context7`<br>source=`upstash/context7` | `repo-004596` `yarikoptic/context7`（REPRESENTATIVE；parent=upstash/context7） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 715 | `github/github-mcp-server`<br>source=`github/github-mcp-server` | `repo-004884` `yarikoptic/github-mcp-server`（REPRESENTATIVE；parent=github/github-mcp-server） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 716 | `venkateshhs/ecrf`<br>source=`venkateshhs/eCRF` | `repo-004778` `yarikoptic/eCRF`（REPRESENTATIVE；parent=venkateshhs/eCRF） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 717 | `yarikoptic/bids-validator-derivatives`<br>source=`yarikoptic/bids-validator-derivatives` | `repo-004473` `yarikoptic/bids-validator-derivatives`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 718 | `theislab/ehrapy`<br>source=`theislab/ehrapy` | `repo-002157` `th86/ehrapy`（REPRESENTATIVE；parent=theislab/ehrapy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 719 | `leezx/cancerllm`<br>source=`leezx/CancerLLM` | `repo-007179` `leezx/CancerLLM`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 720 | `macquarie-meg-research/biscuit`<br>source=`Macquarie-MEG-Research/Biscuit` | `repo-004489` `yarikoptic/Biscuit`（REPRESENTATIVE；parent=Macquarie-MEG-Research/Biscuit） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 721 | `broadinstitute/trexplorer-catalog`<br>source=`broadinstitute/trexplorer-catalog` | `repo-006120` `leizhou69/tandem-repeat-catalog`（REPRESENTATIVE；parent=broadinstitute/trexplorer-catalog） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 722 | `zenodo/zenodo-rdm`<br>source=`zenodo/zenodo-rdm` | `repo-005783` `yarikoptic/zenodo-rdm`（REPRESENTATIVE；parent=zenodo/zenodo-rdm） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 723 | `fmralign/fmralign`<br>source=`fmralign/fmralign` | `repo-004832` `yarikoptic/fmralign`（REPRESENTATIVE；parent=fmralign/fmralign） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 724 | `pulseq/pypulseq`<br>source=`pulseq/pypulseq` | `repo-005432` `yarikoptic/pypulseq`（REPRESENTATIVE；parent=pulseq/pypulseq） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 725 | `gao-lab/glue`<br>source=`gao-lab/GLUE` | `repo-001293` `HelloWorldLTY/GLUE`（REPRESENTATIVE；parent=gao-lab/GLUE） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 726 | `arcinstitute/state`<br>source=`ArcInstitute/state` | `repo-003934` `samarth-kadaba/state`（REPRESENTATIVE；parent=ArcInstitute/state）<br>`repo-002203` `th86/state_virtual_cell`（MEMBER；parent=ArcInstitute/state） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 727 | `marrlab/histogpt`<br>source=`marrlab/HistoGPT` | `repo-001303` `HelloWorldLTY/HistoGPT`（REPRESENTATIVE；parent=marrlab/HistoGPT） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 728 | `pyiron/pysqa`<br>source=`pyiron/pysqa` | `repo-005435` `yarikoptic/pysqa`（REPRESENTATIVE；parent=pyiron/pysqa） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 729 | `zaixizhang/rnagenesis`<br>source=`zaixizhang/RNAGenesis` | `repo-002047` `shantanusharma/RNAGenesis`（REPRESENTATIVE；parent=zaixizhang/RNAGenesis） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 730 | `bic-mni/mni-7t-dicom-to-bids`<br>source=`BIC-MNI/mni-7t-dicom-to-bids` | `repo-005116` `yarikoptic/MNI_7T_DICOM_to_BIDS`（REPRESENTATIVE；parent=BIC-MNI/mni-7t-dicom-to-bids） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 731 | `bic-mni/bic-mri-pipeline-util`<br>source=`BIC-MNI/bic-mri-pipeline-util` | `repo-004454` `yarikoptic/BIC_MRI_pipeline_util`（REPRESENTATIVE；parent=BIC-MNI/bic-mri-pipeline-util） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 732 | `citeproc-py/citeproc-py`<br>source=`citeproc-py/citeproc-py` | `repo-004550` `yarikoptic/citeproc-py`（REPRESENTATIVE；parent=citeproc-py/citeproc-py） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 733 | `motiwari/banditpam`<br>source=`motiwari/BanditPAM` | `repo-005800` `yaswanth169/BanditPAM`（REPRESENTATIVE；parent=motiwari/BanditPAM） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 734 | `salhik/dify_biomni_plugin`<br>source=`SALhik/dify_biomni_plugin` | `repo-001782` `SALhik/dify_biomni_plugin`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 735 | `hanlin-yang/future-bio-tech-stack`<br>source=`hanlin-yang/Future-Bio-Tech-Stack` | `repo-006569` `hanlin-yang/Future-Bio-Tech-Stack`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 736 | `peldom/papers_for_protein_design_using_dl`<br>source=`Peldom/papers_for_protein_design_using_DL` | `repo-002190` `th86/papers_for_protein_design_using_DL`（REPRESENTATIVE；parent=Peldom/papers_for_protein_design_using_DL） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 737 | `mpooja16/digital-twin-healthcare`<br>source=`mpooja16/digital-twin-healthcare` | `repo-006843` `tangxuan82/digital-twin-healthcare`（REPRESENTATIVE；parent=mpooja16/digital-twin-healthcare） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 738 | `poldracklab/fitlins`<br>source=`poldracklab/fitlins` | `repo-004825` `yarikoptic/fitlins`（REPRESENTATIVE；parent=poldracklab/fitlins） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 739 | `openneurodatasets/ds005256`<br>source=`OpenNeuroDatasets/ds005256` | `repo-004764` `yarikoptic/ds005256`（REPRESENTATIVE；parent=OpenNeuroDatasets/ds005256） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 740 | `ali-maq/oncodif_public`<br>source=`Ali-Maq/oncodif_public` | `repo-006342` `Ali-Maq/oncodif_public`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 741 | `fiveseasonsmedical/bcgnet`<br>source=`FiveSeasonsMedical/BCGNet` | `repo-006470` `gutendzx/BCGNet`（REPRESENTATIVE；parent=FiveSeasonsMedical/BCGNet） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 742 | `brain-score/vision`<br>source=`brain-score/vision` | `repo-005739` `yarikoptic/vision`（REPRESENTATIVE；parent=brain-score/vision） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 743 | `brain-score/language`<br>source=`brain-score/language` | `repo-005031` `yarikoptic/language`（REPRESENTATIVE；parent=brain-score/language） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 744 | `brain-score/brainio`<br>source=`brain-score/brainio` | `repo-004507` `yarikoptic/brainio`（REPRESENTATIVE；parent=brain-score/brainio） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 745 | `brain-score/core`<br>source=`brain-score/core` | `repo-004608` `yarikoptic/core`（REPRESENTATIVE；parent=brain-score/core） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 746 | `psych-ds/psychds-validator`<br>source=`psych-ds/psychds-validator` | `repo-005382` `yarikoptic/psychds-validator`（REPRESENTATIVE；parent=psych-ds/psychds-validator） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 747 | `felixphool/digital-twin-health-assistant`<br>source=`felixphool/Digital-Twin-Health-Assistant` | `repo-006842` `tangxuan82/Digital-Twin-Health-Assistant`（REPRESENTATIVE；parent=felixphool/Digital-Twin-Health-Assistant） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 748 | `bitbol-lab/proteomelm`<br>source=`Bitbol-Lab/ProteomeLM` | `repo-002194` `th86/ProteomeLM`（REPRESENTATIVE；parent=Bitbol-Lab/ProteomeLM） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 749 | `mic-dkfz/nnunet`<br>source=`MIC-DKFZ/nnUNet` | `repo-006639` `sszhu/nnUNet`（REPRESENTATIVE；parent=MIC-DKFZ/nnUNet） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 750 | `zou-group/virtual-lab`<br>source=`zou-group/virtual-lab` | `repo-006122` `leizhou69/virtual-lab`（REPRESENTATIVE；parent=zou-group/virtual-lab）<br>`repo-001714` `Pidem/virtual-lab`（MEMBER；parent=zou-group/virtual-lab） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 751 | `ncbi-nlp/geneagent`<br>source=`ncbi-nlp/GeneAgent` | `repo-002164` `th86/GeneAgent`（REPRESENTATIVE；parent=ncbi-nlp/GeneAgent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 752 | `plenoptic-org/plenoptic`<br>source=`plenoptic-org/plenoptic` | `repo-005347` `yarikoptic/plenoptic`（REPRESENTATIVE；parent=plenoptic-org/plenoptic） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 753 | `dabulseco/rfantibody-viewer`<br>source=`dabulseco/rfantibody-viewer` | `repo-005976` `dabulseco/rfantibody-viewer`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 754 | `alleninstitute/cell_type_mapper`<br>source=`AllenInstitute/cell_type_mapper` | `repo-003926` `samarth-kadaba/cell_type_mapper`（REPRESENTATIVE；parent=AllenInstitute/cell_type_mapper） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 755 | `facebookresearch/algonauts-2025`<br>source=`facebookresearch/algonauts-2025` | `repo-006937` `Vik-u/algonauts-2025`（REPRESENTATIVE；parent=facebookresearch/algonauts-2025） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 756 | `pydata/xarray`<br>source=`pydata/xarray` | `repo-005768` `yarikoptic/xarray`（REPRESENTATIVE；parent=pydata/xarray） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 757 | `stacklok/toolhive`<br>source=`stacklok/toolhive` | `repo-005698` `yarikoptic/toolhive`（REPRESENTATIVE；parent=stacklok/toolhive） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 758 | `thiraput01/qwenmed`<br>source=`Thiraput01/QwenMed` | `repo-004061` `Thiraput01/QwenMed`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 759 | `xinwuye/mmscibench-code`<br>source=`xinwuye/MMSciBench-code` | `repo-007564` `xinwuye/MMSciBench-code`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 760 | `kuanlinhuang/decentralizedimmunizationehr`<br>source=`kuanlinhuang/decentralizedImmunizationEHR` | `repo-001535` `kuanlinhuang/decentralizedImmunizationEHR`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 761 | `jaechang-hits/biomni_hits_test`<br>source=`jaechang-hits/biomni_hits_test` | `repo-002876` `jaechang-hits/biomni_hits_test`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 762 | `brainstem-org/brainstem_python_api_tools`<br>source=`brainstem-org/brainstem_python_api_tools` | `repo-004511` `yarikoptic/brainstem_python_api_tools`（REPRESENTATIVE；parent=brainstem-org/brainstem_python_api_tools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `713–762`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-019-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
