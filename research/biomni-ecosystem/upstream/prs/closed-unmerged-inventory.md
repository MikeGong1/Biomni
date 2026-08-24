# Closed-Unmerged Pull Request Inventory

Parent verification: `VERIFIED` at `2026-08-22T20:42:21Z`. A fresh official
Search API query returned 33 unique records with `incomplete_results=false`; the
worker table contains the same set and 33 complete base/head SHA pairs. Separate
official PR resources confirm #289 and #290 share base SHA, head repository/ref,
and head SHA. This remains a PR-surface duplicate candidate, not a resolved unique
change identity.

task_id: `closed-unmerged-pr-inventory-001`
scope: official GitHub results for `repo:snap-stanford/Biomni is:pr is:closed is:unmerged`
repository: `snap-stanford/Biomni`
observed_at_utc: `2026-08-22T20:36:23Z`
claim_class: `FACT` for API metadata; `INFERENCE` for preliminary class, relevance, and lineage flags
source_tier: `1`
execution_boundary: static metadata inventory only; no PR code or third-party content executed

## Count and pagination

- kickoff_count: `33`
- official_search_total_count: `33`
- official_search_incomplete_results: `false`
- recorded_pr_count: `33`
- count_reconciliation: `33 kickoff = 33 API total = 33 recorded`
- pagination: `EXHAUSTED`
- search_page_1: `33` items with `per_page=100`
- search_page_2: `0` items; explicit terminal-page check
- metadata_cross-check: closed-PR REST listing pages contained `100`, `44`, and `0` items; all 33 search-result PR numbers were found, and every matched item had `merged_at=null`

No result was excluded. GitHub search ordering at observation time was newest-created
first. All labels were empty. Only PR #95 was a draft.

## PR inventory

Preliminary class and relevance are title/branch-metadata triage, not code-level
conclusions. `HIGH` means prioritize for a later static diff audit; `POSSIBLE`
means retain as a potentially substantive lead; `LOW` means apparently
documentation-only from current metadata.

| PR | Title | Author | Created (UTC) | Updated (UTC) | Closed (UTC) | Draft | Labels | Preliminary class | Relevance |
|---:|---|---|---|---|---|---|---|---|---|
| [#327](https://github.com/snap-stanford/Biomni/pull/327) | Fix LangChain tool schema dropping optional parameters | `QING1105` | 2026-08-20T03:20:22Z | 2026-08-20T03:29:03Z | 2026-08-20T03:29:02Z | no | none | `BUG_FIX` | `HIGH` |
| [#326](https://github.com/snap-stanford/Biomni/pull/326) | Fix custom LLM env var name mismatch between docs and config.py | `QING1105` | 2026-08-20T03:02:26Z | 2026-08-20T03:29:55Z | 2026-08-20T03:29:55Z | no | none | `BUG_FIX` | `HIGH` |
| [#300](https://github.com/snap-stanford/Biomni/pull/300) | update dependencies | `Liripo` | 2026-05-30T02:53:13Z | 2026-06-12T07:16:19Z | 2026-06-12T07:16:19Z | no | none | `DEPENDENCY_ONLY` | `POSSIBLE` |
| [#297](https://github.com/snap-stanford/Biomni/pull/297) | Add libinvent tool and update template_tools | `lulaiao` | 2026-04-15T13:57:01Z | 2026-07-16T16:13:45Z | 2026-07-16T16:13:45Z | no | none | `FEATURE` | `HIGH` |
| [#296](https://github.com/snap-stanford/Biomni/pull/296) | Bedrock client factory | `xhaaix` | 2026-04-09T11:09:30Z | 2026-04-09T11:09:52Z | 2026-04-09T11:09:52Z | no | none | `REFACTOR` | `HIGH` |
| [#294](https://github.com/snap-stanford/Biomni/pull/294) | add clinvar validation code and links | `mkoretsky1` | 2026-03-26T19:53:59Z | 2026-03-26T19:54:09Z | 2026-03-26T19:54:09Z | no | none | `FEATURE` | `HIGH` |
| [#290](https://github.com/snap-stanford/Biomni/pull/290) | merge from dev | `KyleNeverGivesUp` | 2026-03-14T22:46:34Z | 2026-03-14T22:47:15Z | 2026-03-14T22:46:52Z | no | none | `SYNC_ONLY` | `POSSIBLE` |
| [#289](https://github.com/snap-stanford/Biomni/pull/289) | Dev | `KyleNeverGivesUp` | 2026-03-14T22:40:47Z | 2026-03-14T22:47:16Z | 2026-03-14T22:42:24Z | no | none | `UNKNOWN` | `POSSIBLE` |
| [#287](https://github.com/snap-stanford/Biomni/pull/287) | Test | `Chahat08` | 2026-03-05T23:16:21Z | 2026-03-09T17:18:28Z | 2026-03-09T17:18:28Z | no | none | `UNKNOWN` | `POSSIBLE` |
| [#279](https://github.com/snap-stanford/Biomni/pull/279) | Feature/logging token count | `Ayushmaniar` | 2026-02-11T07:32:49Z | 2026-02-11T07:33:18Z | 2026-02-11T07:33:18Z | no | none | `FEATURE` | `HIGH` |
| [#274](https://github.com/snap-stanford/Biomni/pull/274) | Transform Biomni into MathMind: A Mathematical Modeling AI Agent | `Harrydirk41` | 2026-01-20T08:06:58Z | 2026-01-20T08:09:11Z | 2026-01-20T08:09:11Z | no | none | `FEATURE` | `POSSIBLE` |
| [#270](https://github.com/snap-stanford/Biomni/pull/270) | Resource filter | `jaechang-hits` | 2025-12-19T08:32:25Z | 2025-12-19T08:33:01Z | 2025-12-19T08:32:30Z | no | none | `FEATURE` | `HIGH` |
| [#269](https://github.com/snap-stanford/Biomni/pull/269) | Sandbox | `jaechang-hits` | 2025-12-19T08:13:40Z | 2025-12-19T08:14:43Z | 2025-12-19T08:13:48Z | no | none | `SECURITY` | `HIGH` |
| [#265](https://github.com/snap-stanford/Biomni/pull/265) | Memory feature added | `hklee-hits` | 2025-12-02T01:53:47Z | 2025-12-02T01:56:53Z | 2025-12-02T01:56:53Z | no | none | `FEATURE` | `HIGH` |
| [#263](https://github.com/snap-stanford/Biomni/pull/263) | Sop recomendation | `jaechang-hits` | 2025-11-25T00:48:14Z | 2025-11-28T06:54:25Z | 2025-11-28T06:54:24Z | no | none | `FEATURE` | `HIGH` |
| [#262](https://github.com/snap-stanford/Biomni/pull/262) | Feature/start from upstream 20251116 | `kuanlinhuang` | 2025-11-17T22:37:56Z | 2025-11-17T22:41:00Z | 2025-11-17T22:41:00Z | no | none | `SYNC_ONLY` | `POSSIBLE` |
| [#243](https://github.com/snap-stanford/Biomni/pull/243) | fix: update query_reactome() to use current 2025 Reactome API endpoints | `divyesh-htree` | 2025-10-16T06:18:36Z | 2025-10-16T06:33:10Z | 2025-10-16T06:33:10Z | no | none | `BUG_FIX` | `HIGH` |
| [#239](https://github.com/snap-stanford/Biomni/pull/239) | Biomni eval 1 | `kexinhuang12345` | 2025-10-13T06:10:12Z | 2025-10-13T06:10:39Z | 2025-10-13T06:10:39Z | no | none | `BENCHMARK` | `HIGH` |
| [#197](https://github.com/snap-stanford/Biomni/pull/197) | _ | `samarth-kadaba` | 2025-09-04T23:26:03Z | 2025-09-04T23:29:12Z | 2025-09-04T23:26:13Z | no | none | `REFACTOR` | `POSSIBLE` |
| [#196](https://github.com/snap-stanford/Biomni/pull/196) | _ | `samarth-kadaba` | 2025-09-04T22:10:12Z | 2025-09-04T23:28:47Z | 2025-09-04T22:10:59Z | no | none | `ENVIRONMENT` | `POSSIBLE` |
| [#158](https://github.com/snap-stanford/Biomni/pull/158) | Add nnU-Net segmentation module under bioimaging tools | `MintaYLu` | 2025-08-17T00:28:51Z | 2025-09-14T21:25:18Z | 2025-09-14T21:25:18Z | no | none | `FEATURE` | `HIGH` |
| [#155](https://github.com/snap-stanford/Biomni/pull/155) | feat: Add data preprocessing tools for biomedical research | `MinxZ` | 2025-08-15T08:16:47Z | 2025-08-17T00:57:06Z | 2025-08-17T00:57:06Z | no | none | `FEATURE` | `HIGH` |
| [#151](https://github.com/snap-stanford/Biomni/pull/151) | Add MSeeP.ai badge | `lwsinclair` | 2025-08-14T01:50:52Z | 2025-08-15T03:18:32Z | 2025-08-15T03:18:31Z | no | none | `DOC_ONLY` | `LOW` |
| [#121](https://github.com/snap-stanford/Biomni/pull/121) | add apac. and eu. as prefix for bedrock model | `MinxZ` | 2025-08-05T06:11:38Z | 2025-08-05T06:20:35Z | 2025-08-05T06:19:50Z | no | none | `BUG_FIX` | `HIGH` |
| [#111](https://github.com/snap-stanford/Biomni/pull/111) | Missing gcc and unzip in setup.sh | `MinxZ` | 2025-08-01T06:28:06Z | 2025-08-14T07:05:09Z | 2025-08-14T07:05:09Z | no | none | `ENVIRONMENT` | `HIGH` |
| [#107](https://github.com/snap-stanford/Biomni/pull/107) | Refactor configuration management | `PabloCabaleiro` | 2025-07-30T10:14:52Z | 2025-08-18T20:44:41Z | 2025-08-18T20:44:41Z | no | none | `REFACTOR` | `HIGH` |
| [#95](https://github.com/snap-stanford/Biomni/pull/95) | Using `get_llm` in database.py to get the model | `PabloCabaleiro` | 2025-07-25T13:10:28Z | 2025-08-02T05:40:37Z | 2025-08-02T05:40:37Z | yes | none | `REFACTOR` | `HIGH` |
| [#80](https://github.com/snap-stanford/Biomni/pull/80) | Feat/openfda integration | `lxasqjc` | 2025-07-22T10:11:21Z | 2025-08-04T05:57:47Z | 2025-08-04T05:57:47Z | no | none | `FEATURE` | `HIGH` |
| [#71](https://github.com/snap-stanford/Biomni/pull/71) | Add AWS Bedrock Support for Database files | `JinL0` | 2025-07-20T23:36:44Z | 2025-07-27T22:48:02Z | 2025-07-27T22:48:01Z | no | none | `FEATURE` | `HIGH` |
| [#51](https://github.com/snap-stanford/Biomni/pull/51) | Implement MCPAdapter and ToolLoader for dynamic tool loading and remote function handling | `Shindevrp` | 2025-07-15T17:17:36Z | 2025-08-03T05:19:45Z | 2025-08-03T05:19:45Z | no | none | `FEATURE` | `HIGH` |
| [#36](https://github.com/snap-stanford/Biomni/pull/36) | MCP Integration | `Shindevrp` | 2025-07-12T18:03:07Z | 2025-08-03T05:20:28Z | 2025-08-03T05:20:27Z | no | none | `FEATURE` | `HIGH` |
| [#35](https://github.com/snap-stanford/Biomni/pull/35) | Integrate ToolUniverse as Optional Tool Backend for Biomni Agents | `lxasqjc` | 2025-07-12T15:46:17Z | 2025-07-23T05:41:55Z | 2025-07-23T05:41:54Z | no | none | `FEATURE` | `HIGH` |
| [#2](https://github.com/snap-stanford/Biomni/pull/2) | docs: Fix typo in README (expectly-&gt;expertly) | `erhuve` | 2025-06-03T04:47:01Z | 2025-07-09T05:12:49Z | 2025-07-09T05:12:48Z | no | none | `DOC_ONLY` | `LOW` |

## SHA metadata

All SHAs below are full 40-character values reported by GitHub's official Pulls
REST resource at the observation time. Base SHA is the base commit recorded for
the PR, not the current default-branch HEAD.

| PR | Base repository/ref | Base SHA | Head repository/label/ref | Head SHA |
|---:|---|---|---|---|
| #327 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | `QING1105/Biomni` / `QING1105:fix/langchain-optional-params` | `2750a5d33d5b5c5caa05cdedeb45a07b3e9be8d5` |
| #326 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | `QING1105/Biomni` / `QING1105:fix/env-var-mismatch-custom-llm` | `397f422e2a4925c47083e1986bc0a37ccfa89354` |
| #300 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | unavailable / `Liripo:patch-1` | `fa46e3d45b258220eb53da638b981adc19a216a5` |
| #297 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | unavailable / `zhuwangjulia:jiangyu` | `c2414f26b9978532a259821eafb7ac24d2ddd7ba` |
| #296 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | `vladsavelyev/Biomni` / `vladsavelyev:bedrock-client-factory` | `dbbd39f303a8b6b8a3bde423aad10e77233872e1` |
| #294 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | unavailable / `mkoretsky1:clinvar-validation` | `a30f715858e8f62a48b737f4f41f44f5f1a1054a` |
| #290 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | `KyleNeverGivesUp/Biomni` / `KyleNeverGivesUp:dev` | `9d22e6f627b6d5a2892a9426029942c994bdb2c3` |
| #289 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | `KyleNeverGivesUp/Biomni` / `KyleNeverGivesUp:dev` | `9d22e6f627b6d5a2892a9426029942c994bdb2c3` |
| #287 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | unavailable / `nyu-vis-krueger-group:test` | `7b370452aeb5ad126afdf6cd6dba60ed9c41dbf7` |
| #279 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | `siavashre/amplicon-repo-agentai` / `siavashre:feature/logging-token-count` | `aa627ab1a6da0de8e090f0ddb59a661b06d8d8af` |
| #274 | `snap-stanford/Biomni` / `main` | `400c1f366b96a35ca253e13c9b06c5076af41d65` | unavailable / `Harrydirk41:claude/math-modeling-agent-BoHcj` | `66bea3e77b038b22e8ec47df3c52476e4be31187` |
| #270 | `snap-stanford/Biomni` / `main` | `c36e39f9202863bc7b0665563e74e97723862fa5` | unavailable / `jaechang-hits:resource_filter` | `5de9bd04fd2b0fae49d7e41e65da048472649efd` |
| #269 | `snap-stanford/Biomni` / `main` | `c36e39f9202863bc7b0665563e74e97723862fa5` | unavailable / `jaechang-hits:sandbox` | `42b77daa1b9cb5fcc7760d972b433c2b3c081d7a` |
| #265 | `snap-stanford/Biomni` / `main` | `c36e39f9202863bc7b0665563e74e97723862fa5` | unavailable / `jaechang-hits:hklee_merck` | `1127a409b89b8812348ab81e3d807bb5119665ba` |
| #263 | `snap-stanford/Biomni` / `main` | `c36e39f9202863bc7b0665563e74e97723862fa5` | unavailable / `jaechang-hits:sop_recomendation` | `8c34a2aa8bd5b805b80d5e2064fa6d608cadcf9b` |
| #262 | `snap-stanford/Biomni` / `main` | `c36e39f9202863bc7b0665563e74e97723862fa5` | `Kaimen-Inc/Biomni-AD` / `Kaimen-Inc:feature/start-from-upstream-20251116` | `c99c4684a6059fc7bc453d789ce16ebc2ee1973f` |
| #243 | `snap-stanford/Biomni` / `main` | `8fd7b218c43b78538f79cd93d05db43d8a8073c6` | `hplustree/AI_Agentic_Biomni` / `hplustree:fix/reactome-api-update` | `074f5b90326b878e4881e041e6aba8e86f44c03f` |
| #239 | `snap-stanford/Biomni` / `main` | `3034b8b79f1d0f215a764af1498b22bbd9d70b83` | `snap-stanford/Biomni` / `snap-stanford:biomni_eval_1` | `fcb8d08e4145d146ae6eb43ec2d8198c4c4e20d5` |
| #197 | `snap-stanford/Biomni` / `main` | `b5ad0c7bf4c6c3386b9d73da9656f4d6f257d36a` | `collate/Biomni` / `collate:skadaba/refactor-utils` | `90151ba1b76b9ece2eb3067db85f7d8c6d4a9957` |
| #196 | `snap-stanford/Biomni` / `main` | `b5ad0c7bf4c6c3386b9d73da9656f4d6f257d36a` | `collate/Biomni` / `collate:skadaba/add-helm` | `e6af464332767da468f2f67961211847506ca4e5` |
| #158 | `snap-stanford/Biomni` / `main` | `3147bfaec79bca5f6aa9cff8424f2283ee209e76` | `MintaYLu/Biomni` / `MintaYLu:main` | `0be92e19c6022784dcdb821a399fbd3e8a55d9b7` |
| #155 | `snap-stanford/Biomni` / `main` | `547e7a8478ea917907ae586dc66ca19f02af451f` | `MinxZ/dleader_agent` / `MinxZ:preprocessing` | `0238f0c5d7ccb461132ba9fe4f5ff835f1fa9f34` |
| #151 | `snap-stanford/Biomni` / `main` | `843e83f2bbb226269dded940afd3c2f68687fe2f` | `lwsinclair/Biomni` / `lwsinclair:add-mseep-badge` | `79680db2a7b298d0b81fa22facee79809680c98c` |
| #121 | `snap-stanford/Biomni` / `main` | `f4c3ccae6aa05b754cf342c95366e094575046bd` | `MinxZ/dleader_agent` / `MinxZ:aws_bedrock` | `6136606eda49c4c197da973095a263a36ac73f70` |
| #111 | `snap-stanford/Biomni` / `main` | `843e83f2bbb226269dded940afd3c2f68687fe2f` | `MinxZ/dleader_agent` / `MinxZ:main` | `843e83f2bbb226269dded940afd3c2f68687fe2f` |
| #107 | `snap-stanford/Biomni` / `main` | `6afa5c1a2be1aeadbfa48b8cf935b087b70af00c` | `PabloCabaleiro/Biomni` / `PabloCabaleiro:refactoring_get_llm` | `897211f45618035326d1bdeda0173f02f6ebd1a4` |
| #95 | `snap-stanford/Biomni` / `main` | `2d9784be989daaaa092fba3ca4964cb503714094` | `PabloCabaleiro/Biomni` / `PabloCabaleiro:generalize_get_llm` | `cd595a1da7659b3e40d972f521c993ec6b4a08aa` |
| #80 | `snap-stanford/Biomni` / `main` | `d7d57f7a2af18e7f5256c76f8556123646836610` | `lxasqjc/Biomni` / `lxasqjc:feat/openfda-integration` | `044d12bc97079ab5a2e76e2762a4d1c67788caa3` |
| #71 | `snap-stanford/Biomni` / `main` | `7a05446d80ad6cb8bfa1c9a20051f59607a072d5` | `JinL0/Biomni` / `JinL0:jin/adding_missing_dep` | `fbccf553dcfc9453711284298e07bc4a85226722` |
| #51 | `snap-stanford/Biomni` / `main` | `51b74358e56226bf94b9e191b615d57aded6267c` | `Shindevrp/Biomni` / `Shindevrp:Bidirectional_MCP` | `266d5b29e150e547fb5359eeab0dbae137d5927e` |
| #36 | `snap-stanford/Biomni` / `main` | `31d466d0586d8ce16ec3dc130ca7fde4d8608a05` | `Shindevrp/Biomni` / `Shindevrp:mcp-get_rna_seq_archs4` | `5e457256a25694ebb18194af29930ff5b0204bb5` |
| #35 | `snap-stanford/Biomni` / `main` | `31d466d0586d8ce16ec3dc130ca7fde4d8608a05` | `lxasqjc/Biomni` / `lxasqjc:tool-universe` | `75c56ba67f5f07990d59226d670d0f93b662042b` |
| #2 | `snap-stanford/Biomni` / `main` | `d043e977534b5f8f24fef39f4caabed8976500db` | `erhuve/Biomni` / `erhuve:docs/erhuve/readme-typo` | `5cddda2a5ef5b738abd1c0c6b66296884714c25c` |

## Substantive candidates

- high_relevance_count: `23`
- possible_relevance_count: `8`
- low_relevance_count: `2`
- substantive_status: `PRELIMINARY`; closed/unmerged status was not used as a
  negative quality signal.
- high-priority PRs: `#327, #326, #297, #296, #294, #279, #270, #269, #265,
  #263, #243, #239, #158, #155, #121, #111, #107, #95, #80, #71, #51, #36,
  #35`.
- retained possible leads: `#300, #290, #289, #287, #274, #262, #197, #196`.
- apparent documentation-only entries: `#151, #2`.

## Feature leads

| Feature lead | PRs | Preliminary value |
|---|---|---|
| Tool-schema optional-parameter preservation | #327 | Correct LangChain tool-call interfaces |
| Custom LLM environment configuration | #326 | Fix custom-provider setup mismatch |
| LibInvent/tool templates | #297 | New molecular-design/tool templating capability |
| ClinVar validation | #294 | Variant-validation workflow |
| Token-count logging | #279 | Usage observability |
| Resource filtering | #270 | Agent resource-selection control |
| Sandbox | #269 | Isolation/security-relevant execution surface |
| Memory | #265 | Persistent or conversational agent memory |
| SOP recommendation | #263 | Procedure recommendation/retrieval |
| Reactome API update | #243 | Restores pathway database access |
| Biomni evaluation | #239 | Evaluation/benchmark assets |
| nnU-Net segmentation | #158 | Biomedical image segmentation |
| Biomedical preprocessing | #155 | New preprocessing tool family |
| Configuration/get_llm refactor | #107, #95 | Centralized provider/model configuration |
| openFDA | #80 | FDA data access |
| AWS Bedrock | #71, #121, #296 | Provider support and regional/client handling |
| MCP integration | #36, #51 | Dynamic/remote tool loading and bidirectional MCP |
| ToolUniverse backend | #35 | Optional external tool backend |
| Helm deployment | #196 | Deployment packaging lead inferred from head branch name |
| Utility refactor | #197 | Internal architecture lead inferred from head branch name |
| MathMind | #274 | Alternative mathematical-modeling agent direction |

## Duplicate and lineage flags

- `EXACT_PR_SURFACE_DUPLICATE_CANDIDATE`: #289 and #290 have the same base SHA,
  head repository, head ref, and head SHA. They likely expose one change set, but
  patch identity remains unverified.
- `POSSIBLE_SUCCESSION`: #36 and #51 are by the same author and both concern MCP;
  distinct head SHAs mean they must not be deduplicated without ancestry/diff
  analysis.
- `POSSIBLE_SUCCESSION`: #95 and #107 are by the same author and concern
  `get_llm`/configuration; distinct head SHAs require lineage analysis.
- `FEATURE_FAMILY_NOT_DUPLICATE`: #71, #121, and #296 all concern Bedrock, but
  their titles, authors, bases, and heads indicate potentially distinct changes.
- `POSSIBLE_RELATED_PAIR`: #196 and #197 share author/repository/base and close
  timing, but distinct branches and SHAs suggest separate Helm and utility work.
- #111 has identical reported base and head SHA. This is a `NO_UNIQUE_DIFF`
  candidate at the preserved PR endpoints, not proof that the PR never contained
  a change; event history or commit inspection is needed.

## Evidence

- Search API query (Tier 1):
  `https://api.github.com/search/issues?q=repo%3Asnap-stanford%2FBiomni%20is%3Apr%20is%3Aclosed%20is%3Aunmerged&per_page=100&page=1`
- Explicit terminal search page:
  `https://api.github.com/search/issues?q=repo%3Asnap-stanford%2FBiomni%20is%3Apr%20is%3Aclosed%20is%3Aunmerged&per_page=100&page=2`
- Pull metadata listing (Tier 1):
  `https://api.github.com/repos/snap-stanford/Biomni/pulls?state=closed&sort=created&direction=desc&per_page=100&page=1`
  and subsequent pages through the empty page 3.
- Each PR number in the inventory links to its official GitHub PR page; the
  corresponding API resource is
  `https://api.github.com/repos/snap-stanford/Biomni/pulls/{number}`.

## Uncertainty and unresolved items

- uncertainty: preliminary class/relevance comes from titles and branch metadata;
  no changed-file, commit, discussion, review, or patch content was audited.
- uncertainty: current API head metadata may not reconstruct every historical
  state of a deleted or later-updated fork branch.
- unresolved_head_repositories: `9` PRs report `head.repo=null`: #300, #297,
  #294, #287, #274, #270, #269, #265, #263. Their full head SHAs and labels remain
  available from the official PR resource.
- unresolved_author_head_owner_mappings: #297 (`lulaiao` vs `zhuwangjulia`), #296
  (`xhaaix` vs `vladsavelyev`), #287 (`Chahat08` vs
  `nyu-vis-krueger-group`), #279 (`Ayushmaniar` vs `siavashre`), #265
  (`hklee-hits` vs `jaechang-hits`), #262 (`kuanlinhuang` vs `Kaimen-Inc`), and
  #243 (`divyesh-htree` vs `hplustree`). No identity equivalence is asserted.
- unresolved_lineages: `#289/#290`, `#36/#51`, `#95/#107`, Bedrock family
  `#71/#121/#296`, and `#196/#197`.
- unresolved_main_overlap: no claim is made about whether any closed-unmerged
  change was later independently merged, rewritten, cherry-picked, or superseded
  on `main` or another branch.

## Next action

Perform a static deep-audit queue in this order: (1) preserve/fetch PR commit and
diff metadata for the 23 `HIGH` leads, (2) compute ancestry and patch IDs for the
duplicate/lineage groups, (3) compare candidate behavior against frozen main
`400c1f366b96a35ca253e13c9b06c5076af41d65`, and (4) separately inspect the eight
`POSSIBLE` leads before assigning unique change sets or canonical feature IDs.
Do not collapse any PRs into one feature implementation until those checks pass.
