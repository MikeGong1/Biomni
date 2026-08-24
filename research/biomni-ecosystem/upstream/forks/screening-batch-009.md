# Public Fork Unique-Change Screening — Batch 009

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 95 branch refs without pagination.
Eleven new branch refs reduced to nine unique SHAs because two heads were shared
across surfaces. All nine unique heads were compared serially and succeeded; one
exact open-PR head was not re-compared.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000725 | wenliangz/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000548 | tpan6/Biomni-Grounded | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000261 | alexj-lee/Biomni | User | 33 | 31 | 0 | 2 | SUBSTANTIVE_PLUS_FORMAT_ONLY |
| repo-000264 | JiwaniZakir/Biomni | User | 34 | 32 | 0 | 2 | DOC_PLUS_FORMAT_ONLY |
| repo-000260 | adi-nar/biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000262 | zzgw/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000263 | Chanry1/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000265 | TaoDFang/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000459 | liamphenson/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000404 | xwang112358/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000269 | pengsihua2023/Biomni | User | 1 | 0 | 0 | 1 | DOC_ONLY |
| repo-000271 | rsflinn/Biomni | User | 2 | 1 | 1 | 0 | PR_LINEAGE_ONLY |
| repo-000266 | yguan001/Biomni02 | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000267 | Biodexic/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000272 | bo-wang813/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000273 | xiaoyu12/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000274 | mugpeng/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000275 | zlinghui/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000276 | chaizijun1/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000277 | shenxinggan/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000278 | wishyoulikebefore/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000279 | tingpeng17/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000280 | sunyolo/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000283 | Lancelot-Xie/Biomni | User | 4 | 0 | 0 | 4 | SUBSTANTIVE_LINEAGE |
| repo-000382 | KyleNeverGivesUp/Biomni | User | 2 | 0 | 0 | 2 | DIVERGED_SUBSTANTIVE |

Classification counts: DIVERGED_SUBSTANTIVE=1, DOC_ONLY=1,
DOC_PLUS_FORMAT_ONLY=1, NO_UNIQUE_CHANGE=19, PR_LINEAGE_ONLY=1,
SUBSTANTIVE_LINEAGE=1, SUBSTANTIVE_PLUS_FORMAT_ONLY=1.

## Substantive candidates

### repo-000261 — alexj-lee/Biomni

- `main`: two commits, three files, 0 behind.
- Redacts the printed API key, replaces a hard-coded `ChatAnthropic` code writer
  with configured `get_llm()`, and returns a typed fallback when Claude-only web
  search is requested with another model.
- A second commit requires visible `<think>` output in the agent system prompt.
  That can expose sensitive prompts, retrieved clinical material, secrets, or
  internal instructions and should not be integrated with the fixes as one block.
- The separate pre-commit branch is bot-authored maintenance and is excluded from
  the retained change.
- Preliminary type: `BUG_FIX` / security and provider compatibility.

### repo-000283 — Lancelot-Xie/Biomni

- Exact ancestry forms a strict chain:
  `fix-workflow-error-handling` (2 commits) ⊂ `add-task-history-storage` (5) ⊂
  `fix-history-refresh-issue` (8) ⊂ `main` (9).
- The change wraps generation, code execution, streaming, and Gradio paths in
  exception handling; adds JSONL conversation/history persistence and a sidebar;
  and reloads history choices on browser refresh. Main is the complete integration
  head; its final merge adds no visible tree delta beyond the eight-commit tip.
- Security/privacy: every Gradio user shares `~/.biomni/chat_history.jsonl` and
  one globally enumerable history selector. Full prompts, answers, execution
  traces, code, paths, metadata, and images can be retained indefinitely without
  per-user authorization, redaction, encryption, deletion, locking, or explicit
  restrictive permissions. Raw exception strings and tracebacks may also leak
  operational details.
- Preliminary type: `FEATURE` / workflow resilience and session history.

### repo-000382 — KyleNeverGivesUp/Biomni

- `dev` and `main` are exact duplicate surfaces of one head: 33 ahead / 9 behind,
  36 files, with merge base `c36e39f9202863bc7b0665563e74e97723862fa5`.
- Adds 21 domain `SKILL.md` catalogs, two-stage skill→tool retrieval, a separate
  retrieval LLM, token/debug logging, persistent retrieval caching, startup and
  post-retrieval dependency checks, structured PubMed results, and evaluation
  artifacts. Optional allowlisted pip auto-install mutates the active environment.
- Security/correctness: committed logs retain local/credential-adjacent fragments;
  debug output and shared disk caches require privacy review; global tool-name
  recovery can select the wrong module; unpinned runtime installs add supply-chain
  risk; and the PubMed return contract changes from string to heterogeneous lists.
  A partial stage-one selection can also silently exclude required tools.
- This is a diverged candidate. It is not assumed equivalent to the unrelated
  MyBiomni/WarpHelix Skills platform from `change-000025`.
- Preliminary type: `FEATURE` / Skills and agent retrieval architecture.

## Non-substantive and PR-lineage findings

- Nineteen repositories expose only upstream-known heads.
- alexj-lee and JiwaniZakir expose the exact same two-commit pre-commit update;
  it is one duplicate maintenance surface, not two owner changes.
- JiwaniZakir's other head adds a clinical RAG/agent safety checklist only. Its
  advice to retain full traces or chain-of-thought lacks PHI/secret controls.
- pengsihua2023 adds 34 documentation-only commits across 20 Chinese Markdown files.
- rsflinn's distinct branch is exact open PR #291; no duplicate change is created.

## Identity boundary

- New substantive User owners alexj-lee and Lancelot-Xie enter P.
- KyleNeverGivesUp was already in P as a PR author; its fork relationship is
  appended to the existing identity.
- JiwaniZakir and pengsihua2023 do not enter P because their unique owner-specific
  changes are documentation only. Shared bot maintenance does not establish entry.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 95 refs.
- Nine serialized comparisons against frozen main, all successful.
- Local exact-SHA comparison against the upstream DAG, canonical PR heads,
  previously screened heads, and canonical change commit sets.
- Commit-set membership proves the Lancelot branch chain and the exact shared
  surfaces; runtime behavior and third-party license terms remain unverified.

## Next action

Continue the next bounded active-fork batch. Retain the three changes and Lancelot
lineage for deep security/license audit and later feature decomposition.
