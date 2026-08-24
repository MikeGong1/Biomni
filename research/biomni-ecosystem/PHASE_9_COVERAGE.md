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
| `DEEP_AUDIT_CANDIDATE` families | 2 | 0 | 598 | ACTIVE |
| High-value reopening groups | 13 | 0 | 13 | PRIORITIZED |
| K-Dense/Kuan/BIDS/DataLad source surfaces | 14 | 0 | 14 | STATIC_BATCH_001_COMPLETE |
| Batch 001 provisional capability units | 21 | 0 | 21 | STATIC_BATCH_001_COMPLETE |
| SciAgent active Skills | 20 | 0 | 203 | STATIC_TRANCHE_001_COMPLETE |
| SciAgent previously retained leads | 20 | 0 | 125 | ACTIVE |
| Batch 002 SciAgent capability clusters | 17 | 0 | 17 | STATIC_BATCH_002_COMPLETE |
| Total provisional capability clusters/units | 38 | 0 | unknown | ACTIVE |
| Canonical Features | N/A | 0 | unknown | NOT_STARTED |
| Canonical Implementations | N/A | 0 | unknown | NOT_STARTED |

“Static normalized”表示已经拆出能力、完成初步语义边界和 Biomni gap 判断；“Canonical normalized”要求 Codex 完成代码级去重、provenance、验证和数据库 cross-reference。

## 3. Batch 001 静态结果

K-Dense/Kuan/BIDS/DataLad：21 个 provisional capability units。

Biomni gap：

- `BASELINE_EQUIVALENT_PRESENT`：6；
- `PARTIAL_OVERLAP`：4；
- `RELATED_OVERLAP_NOT_EQUIVALENT`：1；
- `CLEAR_GAP`：10。

Research disposition：

- `DUPLICATE_OR_SUPERSEDED`：6；
- `SOURCE_FIRST_WITH_REMEDIATION`：12；
- `REFERENCE_ONLY_BLOCKED`：3。

## 4. Batch 002 静态结果

SciAgent candidate tranche 001：20 个 Skills，17 个 capability clusters。

Cluster-level Biomni gap：

- `CLEAR_GAP`：10；
- `PARTIAL_OVERLAP`：4；
- `BASELINE_EQUIVALENT_PRESENT`：3。

Skill-level disposition：

- `SOURCE_FIRST_WITH_REMEDIATION`：16；
- `DUPLICATE_OR_SUPERSEDED`：4。

重要 identity reduction：

- pysam 与 samtools 是同一 HTS file-processing Feature 的两个 Implementation；
- Bakta 与 Prokka 是同一 prokaryotic-annotation Feature 的两个 Implementation；
- 两个 Biopython Skills 高度重复，必须拆分后只计一次；
- cBioPortal 与 ClinVar 已有 Biomni baseline Feature，不创建重复 Feature。

## 5. Runtime 和验证覆盖

| Validation | Completed | Current static scope | Status |
|---|---:|---:|---|
| Third-party runtime executions | 0 | 38 clusters/units | NOT_STARTED |
| Characterization-tested capabilities | 0 | 38 | CODEX_REQUIRED |
| Scientific runtime validations | 0 | 38 | CODEX_REQUIRED |
| Source-to-sink security validations | 0 | 38 | CODEX_REQUIRED |
| Privacy/data-flow validations | 0 | 38 | CODEX_REQUIRED |
| Publication review records | 0 | unknown | DEFERRED |

## 6. Commercial coverage

| Collection | Verified | Compared to OSS | Status |
|---|---:|---:|---|
| Grouped commercial behaviors | 17 | 0 | PARTIAL |
| Dated commercial events | 11 | N/A | PARTIAL |
| Commercial implementation internals | 0 | N/A | UNKNOWN |

## 7. Completion rule

Phase 9 只有在以下条件全部满足后才能标记 COMPLETE：

- 598 个 candidate family 全部归入 Feature、标记 duplicate/superseded，或保留为 reference-only；
- 203 个 SciAgent Skills 全部有 Phase 9 disposition；
- Batch 001 的 21 个 units 和 Batch 002 的 17 个 clusters 全部完成 Codex validation；
- `features.jsonl` 和 `implementations.jsonl` 有效且 cross-reference 完整；
- copied/adapted implementation 全部有 exact provenance；
- `CURRENT_FEATURE_CATALOG.md` 和 `INTEGRATION_CANDIDATES.md` 与数据库一致；
- 商业能力与 OSS baseline 的比较完成；
- 最终 coverage 和 integrity audit 通过。
