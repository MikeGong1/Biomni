# Phase 9 Master Index

状态：**PHASE 9A COMPLETE; PHASE 9B READY**

## Authoritative controls

| File | Status | Purpose |
|---|---|---|
| `PHASE_9_STATE.md` | AUTHORITATIVE | 当前阶段和边界 |
| `PHASE_9_COVERAGE.md` | AUTHORITATIVE | 静态覆盖和 Codex 缺口 |
| `phase-9/PHASE9_STATIC_COMPLETION_SUMMARY.md` | COMPLETE | Phase 9A 完成汇总 |
| `CURRENT_FEATURE_CATALOG.md` | COMPLETE_STATIC | provisional Feature 目录 |
| `INTEGRATION_CANDIDATES.md` | COMPLETE_STATIC | 集成研究优先级 |
| `phase-9/CODEX_PHASE9_VALIDATION_QUEUE.md` | READY | Codex cluster 验证入口 |

## Machine-readable outputs

| File | Rows / status |
|---|---:|
| `phase-9/candidate-family-static-normalization.jsonl` | 598 |
| `phase-9/sciagent-phase9-all-skills.jsonl` | 203 |
| `phase-9/provisional-features.jsonl` | 91 |
| `phase-9/provisional-implementations.jsonl` | 801 |
| `phase-9/commercial-oss-gap-static.jsonl` | 17 |
| `phase-9/codex-phase9-validation-queue.jsonl` | 91 |

## Historical evidence retained

Phase 8 Batch 001–046、Change／Lineage／Evidence、旧控制文件和所有 detailed audit reports 继续保留，不重跑、不删除。

## Canonical databases

`database/features.jsonl` 和 `database/implementations.jsonl` 仍为空。只有 Codex 完成 Phase 9B 验证和 cross-reference 后才允许写入正式 ID。
