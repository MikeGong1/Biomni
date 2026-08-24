# External deep audit batch 004 — three awesome-list fork families

Observed at: `2026-08-23T17:06:34Z`

Batch status: **COMPLETE — STATIC_ONLY**

## Canonical decision

Queue orders 10–12 are three single-member forks of curated lists. Complete Git
normalization found no implementation, executable, model, dataset or scientific
method unique to a bounded fork:

| Queue | Source family | Result |
|---:|---|---|
| 10 | `zjlrock777/Awesome-LLM-Agents-Scientific-Discovery` | one merged and one open DOC_ONLY catalog PR |
| 11 | `Agents365-ai/awesome-ai-for-science-skills` | one open DOC_ONLY catalog PR |
| 12 | `G14nTDo4/Awesome-Pathology-Agents` | current fork is a source ancestor; two historical owner PRs are merged DOC_ONLY rows |

All three repository records are `DEEP_AUDITED` for the bounded fork/source
question and close as `RESOLVED_FORK_LINEAGE_NO_SUBSTANTIVE_UNIQUE_CODE`. No
Repository, Person, Change, Lineage, Feature or Implementation ID is allocated.
Outbound projects/papers are retained only as out-of-scope discovery leads.

## Acquisition and coverage

Acquisition was serialized and used no user token. Six current metadata documents
and six partial Git mirrors were frozen. All mirrors passed
`git fsck --full --strict` without diagnostics.

| Surface | LLM-agents list | AI-for-science Skills list | Pathology list |
|---|---:|---:|---:|
| Source heads / tags / pull refs | 1 / 0 / 18 | 1 / 0 / 6 | 1 / 0 / 5 |
| Source reported forks, outside `R` | 7 | 3 | 4 |
| Bounded fork heads / tags | 3 / 0 | 2 / 0 | 1 / 0 |
| Bounded fork PRs / releases / child forks | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| Heads/tags-only unique commits | 1 | 1 | 0 |
| Unique commits after source PR refs | 0 | 0 | 0 |

The three source anchors total three heads, zero tags and **29** pull refs, not
30: zjlrock777 contributes 18, Agents365 6 and G14nTDo4 5. Their 14 source-fork
networks remain outside the bounded people/repository universe. `refs/upstream`
matched each source ref name and SHA exactly; GitHub synthetic merge refs were not
treated as merges into main.

## Queue order 10 — LLM agents for scientific discovery list

The bounded fork has three heads and no tags. Default main
`3e079cd88b573556eba8bc0ef899ba7cee10ddf9` is a source ancestor, ahead 0 and
behind 10 from current source `bb3be5bc49dcc55de371f3d390c1ac0bf497e480`.

### Merged PR #11 — ClawBench row

Branch `add-clawbench-general-benchmark` SHA
`0b2fad557242c5114a9a3723a0e7fb961573b594` exactly equals source PR #11 head.
PR #11 merged as `cd12a4f0d4c2e3f5244423b1907d22426d8735ad`; both head and merge are ancestors
of current source main. The patch changes only README (+3/-1) and adds one general
web-agent benchmark entry.

The historical catalog row is not a reliable current identity record:

- its title, “A Comprehensive Benchmark for Evaluating AI Web Agents,” differs
  from official arXiv v2, “ClawBench: Can AI Agents Complete Everyday Online
  Tasks?”;
- its attribution string “Reacher et al.” does not match the names shown in the
  official arXiv record; no username-to-author mapping is inferred;
- 153 V1 and 130 V2 are paper-era counts; the current repository says two tasks
  were removed and ships 152/129;
- `github.com/reacher-z/ClawBench` now redirects to the same GitHub repository ID
  under `TIGER-AI-Lab/ClawBench`, not a second repository;
- the live target is Apache-2.0/Python and describes a general everyday browser
  benchmark, not a biomedical implementation.

The current repository publishes task/trace claims, but it was not deep-audited
because its owner is outside `P`; a list row and redirect do not add it to `R`.
PR #11 is `DOC_ONLY`, already upstream, and receives no canonical change ID.

### Open PR #14 — Dr. Claw row

Branch `add-dr-claw` SHA
`7fcbe89217da423d2a1563651747601c753a7794` exactly equals open PR #14 head and is
one commit ahead of source main. Its synthetic merge ref is not reachable from
main. The patch only adds one README row (+1/-1) linking `OpenLAIR/dr-claw`.

The row describes an end-to-end research workspace and 100+ skills. The current
outbound README makes similar claims, but no Dr. Claw code, Skill, model, result or
test is present in this fork. GitHub metadata reports JavaScript and SPDX
`NOASSERTION`; the outbound README describes a GPL-3.0/AGPL-3.0 split, which
requires file/origin-level review rather than a catalog badge. OpenLAIR is outside
the person boundary. PR #14 is `DOC_ONLY` and receives no ID.

## Queue order 11 — AI-for-science Skills list

Fork main `710783a792e200207e841f8b3171dd5c849a6563` exactly equals source main. Its
only other head, `add-dr-claw`
`4b52b8e1954e538bb4e9222977458384365a0821`, exactly equals open source PR #4 and
is ahead one. The patch replaces a README placeholder with one Dr. Claw row
(+1/-1); current source still lacks it.

PR #4 and queue-order-10 PR #14 are duplicate catalog surfaces for the same
outbound repository, not two capabilities or implementations. PR prose claims a
large runnable Skill suite, while the fork contains no `SKILL.md` from that suite.
The list's CC0 file applies to the list content only and cannot relicense Dr. Claw
or prove its runnability. This is `DOC_ONLY`; no ID is allocated.

## Queue order 12 — pathology agents list

Fork main `fac3ae861c814750559b6722d0388e2f9890b483` is a source-history ancestor,
ahead 0 and behind 21 from source main
`5b45640c90399349df8f56989756610fc835f70e`. It has no native unique head, tag,
pull, release or child fork.

Deleted fork branches nevertheless left two bounded-owner PR histories in source
main, so they are explicitly indexed rather than lost:

- merged PR #1 head `36caa4956194d9f068fb11f4e27b20ea52792c27`
  adds five README lines for DeepSpot, DeepSpot2Cell, DeepSpot-M and AESTETIK;
- merged PR #2 uses commits `1760ffc56b0caa2e155a4e32d8dfc029924ac367`
  and `d22ffccbd855d82d4248257272de02be7f10e02a` to add/link TCGA and HEST Xenium
  virtual-spatial-transcriptomics dataset rows.

Both are catalog metadata authored through the existing `KalinNonchev` GitHub
identity. They contain no paper text, dataset, model or project implementation;
the linked projects remain outside `R` and their claims/licenses were not audited.
Source and fork expose no root license. These merged PRs are `DOC_ONLY` and do not
warrant Change/Feature IDs.

## Identity, license and evidence boundary

Catalog ownership, PR user, raw commit display name, paper authors, claimed
represented maintainer and outbound repository organization are separate
identities. The shared raw email/display names in the two reacher-z forks do not
authorize a new real-name mapping. No external organization/member is added to
`P`.

License terms on a list apply to list text, not linked code, weights, datasets,
papers, APIs or services. The LLM-agents and Pathology lists have no root license;
the Skills list uses CC0; ClawBench currently reports Apache-2.0; Dr. Claw requires
dual-license origin review. None of these facts converts a catalog row into an
integration candidate.

The three-row machine reduction is
`deep-audit-batch-004-lineage-manifest.jsonl` (SHA-256
`049992af07fd9e468794e9b25bafd5e6712e01c0cc435ed0ed43a7e8b2a6bc7e`). Primary
evidence is `evidence-000169`–`evidence-000173`.

All findings are static. No list instruction, outbound repository, paper, dataset,
model, benchmark, test, installer or scientific code was executed.
