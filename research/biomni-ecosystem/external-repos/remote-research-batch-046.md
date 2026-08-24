# 远程调研 Batch 046

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **2063–2069**；**7** 个 family；**7** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 7 |
| Bounded repository records | 7 |
| Identity note families | 0 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 3 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 1 |
| 分类 `LOW_INFORMATION_RECHECK` | 3 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `FORK_LINEAGE_REQUIRED` | 3 |
| 标记 `LICENSE_UNCLEAR` | 6 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 2063 | `inodb/snakemake-uppmax-demo`<br>source=`inodb/snakemake-uppmax-demo` | `repo-002860` `inodb/snakemake-uppmax-demo`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2064 | `smathot/qnotero`<br>source=`smathot/qnotero` | `repo-005465` `yarikoptic/qnotero`（REPRESENTATIVE；parent=smathot/qnotero） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2065 | `fperez/nipy-notebooks`<br>source=`fperez/nipy-notebooks` | `repo-005225` `yarikoptic/nipy-notebooks`（REPRESENTATIVE；parent=fperez/nipy-notebooks） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2066 | `hannes-brt/flowvb`<br>source=`hannes-brt/FlowVB` | `repo-007517` `hannes-brt/FlowVB`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2067 | `yarikoptic/nipy-suite`<br>source=`yarikoptic/nipy-suite` | `repo-005227` `yarikoptic/nipy-suite`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2068 | `yarikoptic/nipy-old`<br>source=`yarikoptic/NiPy-OLD` | `repo-005226` `yarikoptic/NiPy-OLD`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2069 | `stefanv/scipy3`<br>source=`stefanv/scipy3` | `repo-005553` `yarikoptic/scipy3`（REPRESENTATIVE；parent=stefanv/scipy3） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `2063–2069`，共 `7` 个 family。
- 机器可读记录位于 `remote-research-batch-046-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
