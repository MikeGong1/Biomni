# Phase 9 Research State

状态：**PHASE 9A STATIC RESEARCH COMPLETE; PHASE 9B CODEX VALIDATION READY**

生效日期：`2026-08-24`

研究分支：`research/biomni-ecosystem-audit`

## Phase 8

- Batch 001–046：完成；
- external families：2,069／2,069；
- queued repository records：2,161／2,161；
- `DEEP_AUDIT_CANDIDATE`：598；
- 第三方代码运行：0。

## Phase 9A 已完成

- 598／598 个 candidate family 完成 family-level static normalization；
- 203／203 个 SciAgent Skill 有 Phase 9 disposition；
- 125／125 个 SciAgent candidate lead 完成静态 Feature cluster 映射；
- K-Dense／Kuan／BIDS／DataLad 的 21 个详细 capability unit 已纳入总目录；
- 形成 91 个 provisional Feature cluster；
- 形成 801 个 provisional Implementation record；
- 17／17 个已验证 commercial behavior 完成 bounded OSS 静态比较；
- 形成 91 个 Codex validation cluster；
- 已生成 `CURRENT_FEATURE_CATALOG.md` 和 `INTEGRATION_CANDIDATES.md`。

## 当前权威产物

1. `phase-9/PHASE9_STATIC_COMPLETION_SUMMARY.md`
2. `CURRENT_FEATURE_CATALOG.md`
3. `INTEGRATION_CANDIDATES.md`
4. `phase-9/provisional-features.jsonl`
5. `phase-9/provisional-implementations.jsonl`
6. `phase-9/candidate-family-static-normalization.jsonl`
7. `phase-9/sciagent-phase9-all-skills.jsonl`
8. `phase-9/commercial-oss-gap-static.md`
9. `phase-9/codex-phase9-validation-queue.jsonl`
10. `phase-9/CODEX_PHASE9_VALIDATION_QUEUE.md`

## Phase 9B 必须由 Codex 完成

- clone/fetch exact source SHA；
- code／symbol／AST／patch-level semantic dedup；
- characterization tests；
- scientific runtime validation；
- source-to-sink security analysis；
- privacy/data-flow validation；
- copied/adapted provenance ledger；
- canonical `features.jsonl` 和 `implementations.jsonl` 写入；
- final JSONL cross-reference 和 repository-integrity audit。

## 解释规则

Phase 9A 的 `COMPLETE_STATIC_RESEARCH` 不等于 runtime verified。Canonical Feature 和 Implementation 仍为 0，直到 Phase 9B 验证门通过。

License 不作为功能研究淘汰条件；科学、安全、隐私、临床、模型和供应链阻断项继续生效。
