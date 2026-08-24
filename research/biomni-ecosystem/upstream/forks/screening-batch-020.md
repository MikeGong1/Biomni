# Public Fork Unique-Change Screening — Batch 020

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query returned all 57 branch
refs without pagination. Five new unique head SHAs were compared serially with a
two-second interval; all comparisons succeeded, their heads matched the requested
OIDs, and the largest comparison contained five commits, so no compare pagination
was required. Analysis was static: no source, binary, hook, package, or test was
executed.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000697 | PraMamba/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000539 | hcui2/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000526 | murbachovski/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000525 | renato-umeton/BiomniA2 | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000524 | wei1540/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000521 | Yangwanyi1028/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000520 | zhangjiuri/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000530 | forcefield/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000533 | Bio-MingChen/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000531 | Yuzhifur/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000535 | zancmeresek/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000536 | Takshan/Biomni | User | 2 | 1 | 0 | 0 | 1 | IMAGE_ONLY_AUTOMATED_OPTIMIZATION |
| repo-000537 | hansen7/Biomni | User | 15 | 14 | 0 | 0 | 1 | DEPENDENCY_ONLY_AUTOMATED_SUPERSEDED |
| repo-000534 | deeplenk/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000538 | eqtylab/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000591 | SnowLightPath/Biomni | User | 3 | 3 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000555 | PabloCabaleiro/Biomni | User | 3 | 1 | 2 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000546 | th86/Biomni | User | 2 | 1 | 0 | 0 | 1 | UPSTREAM_PATCH_EQUIVALENT_PR_LINEAGE |
| repo-000545 | RasputinKaiser/Forkbiomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000544 | carden24/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000543 | cxcx816/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000542 | yaokaibb/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000540 | zaibaki/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000551 | bmegacoach/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000569 | evolu8/Biomni | User | 12 | 10 | 0 | 0 | 2 | DIVERGED_SUBSTANTIVE_COMPOSITE_WITH_REVERTED_STREAMING |

Classification counts: NO_UNIQUE_CHANGE=20, EXACT_PR_LINEAGE=1,
IMAGE_ONLY_AUTOMATED_OPTIMIZATION=1,
DEPENDENCY_ONLY_AUTOMATED_SUPERSEDED=1,
UPSTREAM_PATCH_EQUIVALENT_PR_LINEAGE=1, and
DIVERGED_SUBSTANTIVE_COMPOSITE_WITH_REVERTED_STREAMING=1.

## Retained historical change

### repo-000569 — evolu8/Biomni

- `message_popping@c4f2523...` is five ahead / 350 behind with merge base
  `a7d88fc...`. Four owner-authored commits form a side chain from an older
  upstream ancestor; the fifth commit merges `a7d88fc...`. The final net patch is
  one file, `biomni/agent/a1.py`, with three additions and one deletion.
- The final patch has two semantic components: an `A1` constructor parameter
  `temperature: float = 0.0` passed to `get_llm()`, and a
  `yield self.log, message` inside the existing synchronous `go()` loop. Retain
  the connected five-commit branch once for provenance, but do not count its
  streaming component as a second new implementation.
- The streaming hunk has stable patch ID
  `0c75291910d805c31023d09734f1a37cd4936edd`, exactly matching upstream PR #102
  head `b677959...`. PR #114 / `142c4dec...` then deletes that exact line. PR #122
  later implements streaming through a separate typed `go_stream()` method while
  preserving the synchronous `go()` contract.
- In Python, any `yield` makes the entire function a generator. Existing calls no
  longer receive `(log, final_text)` and do not execute until iterated. The old
  return tuple becomes `StopIteration.value`; each event instead carries the same
  growing mutable log plus a raw LangChain message. Callers can fail, stop work
  early, lose the final value, or expose non-serializable intermediate content.
- `A1` also shares `self.log`, graph state, and hard-coded thread ID `42` across
  calls. Longer-lived generators increase interleaving risk. Raw messages can
  contain prompts, tool arguments/outputs, generated code, paths, errors, or
  biomedical data; forwarding them without an explicit public event schema can
  leak internal or sensitive content.
- Temperature passthrough was technically compatible with the then-current
  `get_llm()` signature, but it silently changes the effective default from 0.7
  to 0.0, has no range/provider validation, and is absent from configuration,
  documentation, and tests. Temperature alone does not establish reproducibility
  without seed, model/provider version, prompt, tool/data snapshot, environment,
  and run provenance.
- Upstream PR #161 later exposes `BiomniConfig.temperature` and
  `BIOMNI_TEMPERATURE` with the established 0.7 default, while PR #122 provides the
  separate streaming API. These are conceptually fuller successors; no part of
  this stale branch should be cherry-picked directly.
- No dependency, dataset, asset, endpoint, or license file changes. Apache-2.0
  provenance remains, and all five branch commits map directly to existing person
  `evolu8` / `person-github-000012`. Preserve attribution for the temperature
  experiment and point streaming provenance to PR #102.

## Patch-equivalent and non-substantive findings

### repo-000546 — th86/Biomni

- `main@805d5f6...` adds only `deepseek` to Ollama model-name detection.
- It and upstream `a252ebc...` have the same parent `6afa5c1...`, same resulting
  tree and `llm.py` blob, byte-identical hunk, and stable patch ID
  `e896b73adfa4a84490bd64646f6b9d52e711f63d`.
- `a252ebc...` is the human commit in merged PR #106; the PR head `2cfa886...`
  only adds pre-commit formatting. This fork head is an exact patch-equivalent
  sibling/precursor, not a new change. `th86` is already
  `person-github-000039` through PR #106.
- The substring heuristic can still misroute unspecified hosted DeepSeek names to
  Ollama, although explicit `source` and `base_url` take precedence. That is a
  canonical PR behavior to review, not a fork-only capability.

### Automated maintenance

- `Takshan:imgbot@54546b8...` is one ImgBot-authored binary logo optimization.
  The commit claims 95.33 KiB to 23.99 KiB, but the binary patch is omitted and the
  target blob is unavailable locally, so pixel, dimension, color-profile, and
  metadata preservation are unverified. It changes no code and is excluded.
- `hansen7:pre-commit-ci-update-config@89ef517...` bumps Biome 2.1.2→2.1.3
  and Ruff 0.12.5→0.12.7. `evolu8:pre-commit-ci-update-config@9fd4d14...`
  bumps Biome 2.1.1→2.1.2 and Ruff 0.12.3→0.12.4. Both are bot-authored,
  different from each other and from upstream update patches, and superseded by
  frozen main's Biome 2.3.10, Ruff 0.14.11, and pre-commit-hooks 6.0.0.
- Hook tags are not immutable commit pins. No historical release safety was
  verified, so these stale maintenance heads should be regenerated from current
  configuration rather than reused. They add no vendored code or new license.

## Exact PR and no-unique findings

- Twenty repositories expose only upstream-known heads.
- `PabloCabaleiro:generalize_get_llm@cd595a1...` is exact closed-unmerged draft
  PR #95. `PabloCabaleiro:refactoring_get_llm@897211f...` is exact
  closed-unmerged PR #107. Neither receives a duplicate change ID.

## Identity boundary

- No new person record is allocated. `evolu8`, `th86`, `PabloCabaleiro`, and
  `pre-commit-ci[bot]` already exist in P; only `evolu8` gains a substantive-fork
  relation through this batch.
- ImgBotApp is a bot on a non-substantive image-only surface and does not enter P.
  Takshan and hansen7 have no direct authorship on retained substantive changes.
- Upstream-only and exact-PR-only owners do not enter through this batch.

## Evidence and limits

- Authenticated GraphQL inventory covered 25 repositories and all 57 refs.
- Five serialized comparisons against frozen main succeeded; head identity,
  commit count, file count, and lack of pagination were independently checked.
- Local immutable Git objects prove both stable patch identities, th86's same
  parent/tree/blob relationship, PR #102 ancestry, PR #114 deletion, and later
  PR #122/#161 canonical designs.
- No binary rendering, hook execution, model call, test, package install, or
  third-party code execution was performed.

## Next action

Continue the next bounded active-fork batch. Retain one historical change and one
lineage, already resolved as compatibility-blocked or superseded by upstream
PRs #114, #122, and #161; do not promote it as a direct integration candidate.
