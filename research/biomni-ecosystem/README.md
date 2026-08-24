# Biomni Public Ecosystem Research Database

本目录保存 Biomni 及其相关生态的可追溯调研记录，包括人类可读报告和机器可读 JSONL。后续 GPT Pro／Codex 应从 Git 中恢复，而不是依赖聊天记忆。

## 当前恢复顺序

Phase 9 已开始。请按以下顺序读取：

1. `PHASE_9_STATE.md`
2. `PHASE_9_MASTER_INDEX.md`
3. `PHASE_9_COVERAGE.md`
4. `RESEARCH_FIRST_OVERRIDE.md`
5. `methodology/research-first-source-policy.md`
6. `phase-9/feature-taxonomy-v001.md`
7. `external-repos/research-first-reopen-manifest.jsonl`
8. 当前 workpack 或 batch report
9. `STATE.md`、`MASTER_INDEX.md`、`COVERAGE.md`，仅用于 Phase 8 历史细节

本地 Codex 全局入口：

- `CODEX_RESEARCH_FIRST_PROMPT.md`

当前代码级验证入口：

- `phase-9/CODEX_WORKPACK_001_KDENSE_KUAN.md`
- `phase-9/CODEX_WORKPACK_002_SCIAGENT_TRANCHE_001.md`

## 当前状态

- Phase 8：Batch 001–046 完成；
- external families：2,069／2,069；
- queued repository records：2,161／2,161；
- `DEEP_AUDIT_CANDIDATE`：598；
- Phase 9 statically normalized candidate families：2／598；
- SciAgent candidate Skills：20／125 静态归一化；
- provisional capability clusters/units：38；
- canonical Feature：0；
- canonical Implementation：0；
- third-party runtime executions：0；
- Phase 9：source-first Feature／Implementation normalization ACTIVE。

旧 `STATE.md`、`MASTER_INDEX.md` 和 `COVERAGE.md` 保留了完整执行历史，但其中部分中间段落仍含 Batch 009 未开始或旧累计数。当前状态以 `PHASE_9_*` 文件为准。

## 研究规则

- 范围与人员边界：`methodology/scope.md`
- Evidence：`methodology/evidence-policy.md`
- Deduplication：`methodology/deduplication-policy.md`
- Source-first 与 provenance：`methodology/research-first-source-policy.md`
- Static safety：`methodology/security-policy.md`
- Limitations：`methodology/limitations.md`

License 不再阻止功能发现，但仍作为 provenance 和后续 publication review 信息。科学、安全、隐私、临床、模型信任、数据治理和供应链风险不因科研用途而降低。

Canonical state、ID、Feature selection 和 JSONL cross-reference 由研究协调者维护；worker 输出在验证和归一化前均为 provisional。
