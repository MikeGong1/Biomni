# Deduplication Policy

## Research unit and layers

The research unit is a `Unique Change Set`, not a GitHub page.

- `CHANGE`: a substantive Git patch or independently developed code change.
- `IMPLEMENTATION`: one concrete version of one or more features.
- `FEATURE`: a user-understandable independent capability.

A branch, PR, fork, merge commit, and cherry-pick may all expose one change. One
implementation may cover several features, and one feature may have several
implementations.

## Resolution pipeline

Use this order:

1. collect every public surface;
2. normalize identities and exact commit ancestry;
3. extract substantive unique changes;
4. decompose changes into implementations and features;
5. build the Git DAG and feature lineage;
6. compare function-level behavior and dependencies;
7. deduplicate equivalent changes; and
8. select a canonical implementation only after relevant collection is complete.

Exact SHA identity and ancestry are checked first. When SHAs differ, use patch ID,
diff similarity, function-level comparison, and semantic evidence as available.
Possible relations include `appears_in_branch`, `appears_in_pr`,
`appears_in_fork`, `duplicate_of`, `cherry_pick_of`, `rebased_from`,
`merged_as`, `derived_from`, `supersedes`, `superseded_by`, and
`alternative_to`.

## Classification

Every commit enters the inventory as one of `MERGE_ONLY`, `SYNC_ONLY`,
`DOC_ONLY`, `FORMAT_ONLY`, `DEPENDENCY_ONLY`, `BUG_FIX`, `FEATURE`, `REFACTOR`,
`REMOVAL`, `SECURITY`, `BENCHMARK`, `ENVIRONMENT`, or `UNKNOWN`. Merge, sync,
documentation, and formatting commits normally do not receive a separate deep
audit, but remain indexed for coverage.

If a commit belongs entirely to a PR, its deep analysis belongs to that PR
lineage rather than being counted again as a new feature.

## Version selection

Historical implementations with substantive unique code remain in lineage even
when merged, closed, abandoned, rewritten, or superseded. Each feature may have
different values for `first_public`, `latest_public`, `latest_stable`,
`latest_experimental`, and `canonical_for_integration`.

Date alone never selects the canonical implementation. Selection considers
functional completeness, maintenance, stability, tests, known bugs,
compatibility, license, dependency burden, security, integration cost, and
upstream acceptance.
