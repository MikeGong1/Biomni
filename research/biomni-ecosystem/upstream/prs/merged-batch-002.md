# Merged PR Inventory — Batch 002

Parent verification: `VERIFIED` at `2026-08-22T20:43:59Z`. Fresh official
Search API requests returned the same 11 unique page-2 PRs from #246 through
#268, followed by an empty page 3; both reported `total_count=111` and
`incomplete_results=false`. The merged-PR inventory denominator is exhausted.

- **Task ID:** `merged-pr-inventory-002`
- **Status:** `COMPLETE`
- **Scope/query/sort:** official GitHub Search API query `repo:snap-stanford/Biomni is:pr is:merged`; deterministic `sort=created&order=asc`; inventory request `per_page=100&page=2`; exhaustion check `per_page=100&page=3`.
- **Entities discovered globally:** 111 merged pull requests reported by both live requests.
- **Entities processed in batch:** 11 pull requests on page 2.
- **Entities processed cumulatively:** 111 pull requests (100 canonical page-1 records plus 11 page-2 records).
- **Pagination completed?:** Yes. Page 3 returned 0 records, with `total_count=111` and `incomplete_results=false`.
- **next page:** `null`
- **discovered_count:** `111`
- **processed_count:** `11`
- **cumulative_processed_count:** `111`
- **page_2_count:** `11`
- **page_3_count:** `0`
- **incomplete_results:** `false` on pages 2 and 3.
- **observed_at UTC:** `2026-08-22T20:40:48Z`
- **Claim/evidence posture:** PR metadata and pagination counts are `FACT` from Tier-1 official GitHub API responses. Classifications and feature leads are title-only `INFERENCE` pending diff-level validation.

## Completion status

The bounded merged-PR collection is complete at this observation snapshot: `discovered=111`, `cumulative processed=111`, and the next page is empty. The first canonical batch ended at PR #244 (created `2025-10-16T06:35:23Z`); this second batch begins at PR #246 (created `2025-10-22T01:58:27Z`), preserving ascending creation order without overlap.

## Batch summary

- Unique PRs: 11; all PR numbers are unique within this page.
- Unique authors: 6 — `andrewsu`, `kexinhuang12345`, `mickaelleclercq`, `nevergreendd`, `pre-commit-ci[bot]`, `serena2z`.
- Preliminary classification counts: `FEATURE=5`, `BUG_FIX=2`, `DEPENDENCY_ONLY=2`, `MERGE_ONLY=1`, `UNKNOWN=1`.
- The Search API response exposes `pull_request.merged_at` but not merge commit SHA, base ref/SHA, or head ref/SHA. No per-item expansion was performed.

## Per-PR inventory

| PR | Title | Author | Created | Updated | Closed | Merged | Preliminary class | Merge/base/head details |
|---:|---|---|---|---|---|---|---|---|
| [#246](https://github.com/snap-stanford/Biomni/pull/246) | Feat/gpt5 mini support | [mickaelleclercq](https://github.com/mickaelleclercq) | 2025-10-22T01:58:27Z | 2025-10-27T05:16:50Z | 2025-10-27T05:16:50Z | 2025-10-27T05:16:50Z | FEATURE | Not returned by Search API |
| [#247](https://github.com/snap-stanford/Biomni/pull/247) | UI | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-10-25T22:17:06Z | 2025-10-27T05:43:37Z | 2025-10-27T05:43:37Z | 2025-10-27T05:43:36Z | UNKNOWN | Not returned by Search API |
| [#248](https://github.com/snap-stanford/Biomni/pull/248) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-10-27T18:24:17Z | 2025-10-27T19:54:50Z | 2025-10-27T19:54:50Z | 2025-10-27T19:54:50Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#249](https://github.com/snap-stanford/Biomni/pull/249) | Release/v0.0.8 | [serena2z](https://github.com/serena2z) | 2025-10-27T21:13:25Z | 2025-10-27T21:31:48Z | 2025-10-27T21:31:48Z | 2025-10-27T21:31:47Z | MERGE_ONLY | Not returned by Search API |
| [#251](https://github.com/snap-stanford/Biomni/pull/251) | protocol io integration | [serena2z](https://github.com/serena2z) | 2025-10-30T22:28:28Z | 2025-10-31T03:21:57Z | 2025-10-31T03:21:57Z | 2025-10-31T03:21:57Z | FEATURE | Not returned by Search API |
| [#252](https://github.com/snap-stanford/Biomni/pull/252) | know-how | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-11-03T06:10:55Z | 2025-11-06T01:39:20Z | 2025-11-06T01:39:20Z | 2025-11-06T01:39:20Z | FEATURE | Not returned by Search API |
| [#253](https://github.com/snap-stanford/Biomni/pull/253) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-11-03T18:36:37Z | 2026-01-15T04:23:09Z | 2026-01-15T04:23:09Z | 2026-01-15T04:23:09Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#256](https://github.com/snap-stanford/Biomni/pull/256) | minor fix | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-11-06T22:20:43Z | 2025-11-06T22:21:23Z | 2025-11-06T22:21:23Z | 2025-11-06T22:21:23Z | BUG_FIX | Not returned by Search API |
| [#259](https://github.com/snap-stanford/Biomni/pull/259) | added addgene/thermo protocols | [serena2z](https://github.com/serena2z) | 2025-11-13T03:08:32Z | 2026-01-15T04:23:43Z | 2026-01-15T04:23:43Z | 2026-01-15T04:23:43Z | FEATURE | Not returned by Search API |
| [#266](https://github.com/snap-stanford/Biomni/pull/266) | Add Western blot ROI detection tools | [nevergreendd](https://github.com/nevergreendd) | 2025-12-08T05:41:59Z | 2026-01-15T04:22:59Z | 2026-01-15T04:22:59Z | 2026-01-15T04:22:59Z | FEATURE | Not returned by Search API |
| [#268](https://github.com/snap-stanford/Biomni/pull/268) | Fix Gradio version compatibility issue | [andrewsu](https://github.com/andrewsu) | 2025-12-11T17:58:18Z | 2026-01-23T21:27:53Z | 2026-01-15T04:22:20Z | 2026-01-15T04:22:20Z | BUG_FIX | Not returned by Search API |

## Substantive changes

Title-level substantive leads:

- #246 advertises GPT-5 mini provider/model support.
- #247 appears UI-related, but the title is too terse to establish scope; it remains `UNKNOWN`.
- #251 advertises Protocols.io integration.
- #252 advertises a know-how change, but its exact feature boundaries are unknown.
- #259 advertises Addgene and Thermo protocol content.
- #266 advertises Western blot ROI-detection tools.
- #268 is a Gradio compatibility fix, not an independent capability by title.

## Potential duplicates and lineages

- #248 and #253 are repeated pre-commit autoupdate PRs and likely dependency-maintenance units, not independent features.
- #249 is a release aggregation and may contain changes already represented by earlier PR lineages.
- #251 and #259 both concern protocol capabilities and may be related, though one names Protocols.io integration and the other names Addgene/Thermo protocols.
- #247 (UI) and #268 (Gradio compatibility) may share a UI lineage, but this is not established by titles alone.
- #246 is potentially part of the existing multi-provider LLM lineage from page 1 rather than a standalone provider architecture.

## Potential feature leads

No canonical feature IDs were allocated. Provisional labels for parent normalization only:

- `LEAD_GPT5_MINI_SUPPORT` — #246
- `LEAD_UI_CHANGE_UNKNOWN_SCOPE` — #247
- `LEAD_PROTOCOLS_IO_INTEGRATION` — #251
- `LEAD_KNOW_HOW_CHANGE_UNKNOWN_SCOPE` — #252
- `LEAD_ADDGENE_THERMO_PROTOCOLS` — #259
- `LEAD_WESTERN_BLOT_ROI_DETECTION` — #266

## Evidence URLs

- Search UI: https://github.com/snap-stanford/Biomni/pulls?q=is%3Apr+is%3Amerged+sort%3Acreated-asc
- Page 2 API request: https://api.github.com/search/issues?q=repo%3Asnap-stanford%2FBiomni%20is%3Apr%20is%3Amerged&sort=created&order=asc&per_page=100&page=2
- Page 3 exhaustion request: https://api.github.com/search/issues?q=repo%3Asnap-stanford%2FBiomni%20is%3Apr%20is%3Amerged&sort=created&order=asc&per_page=100&page=3
- Every PR number in the table links to its Tier-1 GitHub PR page.

## SHAs

- Merge commit SHAs: `UNKNOWN_NOT_RETURNED_BY_SEARCH_API` for all 11 records.
- Base ref/SHA: `UNKNOWN_NOT_RETURNED_BY_SEARCH_API` for all 11 records.
- Head ref/SHA: `UNKNOWN_NOT_RETURNED_BY_SEARCH_API` for all 11 records.
- No SHA was inferred from dates, PR numbers, release labels, or the frozen main baseline.

## PR numbers

`246, 247, 248, 249, 251, 252, 253, 256, 259, 266, 268`

## Uncertainties

- GitHub search counts and indexing are time-dependent; completion is scoped to this exact UTC observation and query.
- Search pagination is offset-based rather than a frozen cursor. Concurrently created or reindexed records could theoretically shift pages between separate requests; ascending creation order, page-1 boundary comparison, matching totals, and an empty page 3 reduce but do not eliminate this observability limitation.
- Title-only classifications may misstate the actual patch, especially #247, #252, and #256.
- Search results do not establish merge method, exact commit ancestry, retained reachability from main, files/functions changed, or unique change sets.
- `merged_at` proves the API's merged state at observation time; it does not prove the advertised feature is present in frozen main SHA `400c1f366b96a35ca253e13c9b06c5076af41d65`.
- No PR bodies, comments, diffs, files, checks, or external links embedded in PR content were opened or executed.

## Unresolved questions

- What merge/base/head SHAs and unique patches correspond to these 11 PRs?
- Are #251 and #259 distinct protocol capabilities, sequential implementations, or overlapping content additions?
- What concrete changes are represented by #247 (`UI`) and #252 (`know-how`)?
- Is #246 a provider-route addition, a model-name/configuration update, or documentation-only behavior?
- Which page-2 changes remain reachable at the frozen baseline, particularly #268 whose public `updated_at` postdates its merge?

## Next action

Parent coordinator can normalize this page into canonical upstream PR records and mark the merged-PR breadth-first collection `COMPLETE` at 111/111. A separate bounded depth-audit phase should retrieve merge/base/head SHAs and diffs, resolve exact lineage/duplication, and allocate canonical feature IDs.
