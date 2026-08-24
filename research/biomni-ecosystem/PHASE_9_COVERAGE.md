# Phase 9 Coverage

状态：**ACTIVE**

## 1. Phase 8 发现覆盖

| Collection | Complete | Total | Status |
|---|---:|---:|---|
| External families | 2,069 | 2,069 | COMPLETE |
| Queued repository records | 2,161 | 2,161 | COMPLETE |
| External deep-audit batches | 46 | 46 | COMPLETE |
| Biomni fork identities screened | 694 | 694 | COMPLETE |
| Main commits indexed | 487 | 487 | COMPLETE |
| Open PRs inventoried | 38 | 38 | COMPLETE |
| Merged PRs inventoried | 111 | 111 | COMPLETE |
| Closed-unmerged PRs inventoried | 33 | 33 | COMPLETE |

## 2. Phase 9 功能归一化覆盖

| Collection | Static normalized | Canonical normalized | Total | Status |
|---|---:|---:|---:|---|
| `DEEP_AUDIT_CANDIDATE` families | 1 | 0 | 598 | ACTIVE |
| High-value reopening groups | 13 | 0 | 13 | PRIORITIZED |
| K-Dense/Kuan/BIDS/DataLad source surfaces | 14 | 0 | 14 | STATIC_BATCH_001_COMPLETE |
| Provisional capability units from Batch 001 | 21 | 0 | 21 | STATIC_BATCH_001_COMPLETE |
| SciAgent active Skills | 0 | 0 | 203 | NOT_STARTED_PHASE_9_NORMALIZATION |
| SciAgent previously retained leads | 0 | 0 | 125 | QUEUED |
| Canonical Features | N/A | 0 | unknown | NOT_STARTED |
| Canonical Implementations | N/A | 0 | unknown | NOT_STARTED |

“Static normalized”表示已经拆出能力、完成初步语义边界和 Biomni gap 判断；“Canonical normalized”要求 Codex 完成代码级去重、provenance、验证和数据库 cross-reference。

## 3. Batch 001 静态结果

21 个 provisional capability units：

- `BASELINE_EQUIVALENT_PRESENT`：6；
- `PARTIAL_OVERLAP`：4；
- `RELATED_OVERLAP_NOT_EQUIVALENT`：1；
- `CLEAR_GAP`：10。

Research disposition：

- `DUPLICATE_OR_SUPERSEDED`：6；
- `SOURCE_FIRST_WITH_REMEDIATION`：12；
- `REFERENCE_ONLY_BLOCKED`：3。

## 4. Runtime 和验证覆盖

| Validation | Completed | Total | Status |
|---|---:|---:|---|
| Third-party runtime executions | 0 | unknown | NOT_STARTED |
| Characterization-tested provisional capabilities | 0 | 21 | CODEX_REQUIRED |
| Scientific runtime validations | 0 | 21 | CODEX_REQUIRED |
| Source-to-sink security validations | 0 | 21 | CODEX_REQUIRED |
| Privacy/data-flow validations | 0 | 21 | CODEX_REQUIRED |
| Publication review records | 0 | unknown | DEFERRED |

## 5. Commercial coverage

| Collection | Verified | Compared to OSS | Status |
|---|---:|---:|---|
| Grouped commercial behaviors | 17 | 0 | PARTIAL |
| Dated commercial events | 11 | N/A | PARTIAL |
| Commercial implementation internals | 0 | N/A | UNKNOWN |

## 6. Completion rule

Phase 9 只有在以下条件全部满足后才能标记 COMPLETE：

- 598 个 candidate family 全部归入 Feature、标记 duplicate/superseded，或保留为 reference-only；
- 203 个 SciAgent Skills 全部有 Phase 9 disposition；
- K-Dense/Kuan/BIDS/DataLad 的 21 个 capability units 全部完成 Codex validation；
- `features.jsonl` 和 `implementations.jsonl` 有效且 cross-reference 完整；
- copied/adapted implementation 全部有 exact provenance；
- `CURRENT_FEATURE_CATALOG.md` 和 `INTEGRATION_CANDIDATES.md` 与数据库一致；
- 商业能力与 OSS baseline 的比较完成；
- 最终 coverage 和 integrity audit 通过。
