# Worker Result: commit-index-001

Parent verification: `VERIFIED` at `2026-08-22T20:45:24Z`. The frozen local Git
DAG contains exactly 487 commits reachable from main. Its first 100 SHAs match the
worker boundaries and order; all are unique, 42 are multi-parent, and 29 subjects
map explicitly to PR numbers. The official API Link header reports next page 2 and
last page 5. Subject-based classes remain `INFERENCE` pending diff/PR analysis.

## Task record

- Task ID: `commit-index-001`
- Scope: official `snap-stanford/Biomni` commit-list API, frozen `main` baseline `400c1f366b96a35ca253e13c9b06c5076af41d65`, page `1`, `per_page=100`, deterministic API order (newest first).
- Status: `PARTIAL`
- Observed at UTC: `2026-08-22T20:35:35Z` (GitHub response `Date` header).
- Processed: `100` commit records, positions 1–100 inclusive.
- Boundary: first `400c1f366b96a35ca253e13c9b06c5076af41d65`; last `899eefb22a5a102fd81f1d845490b4b83fee3402`.
- Safety: metadata-only inventory; no repository code, workflow, script, package, or external instruction was executed.

## Global discovery and pagination

- GitHub returned HTTP 200 and exactly 100 objects.
- The response `Link` header gave `rel="next"` at `page=2` and `rel="last"` at `page=5` for the same frozen SHA and `per_page=100` query.
- Global discovered count: `487` commits, independently established from the
  fetched frozen Git DAG. API pagination still requires pages 2–5 to be indexed.
- Pagination: `PARTIAL`; next page: `2`.

## Preliminary inventory

`Author` and `Committer` are shown as `GitHub login / commit-signature name`. `—` means GitHub did not expose a linked public account in this response. Classification is preliminary and derives only from parent count plus the first-line subject; it uses the permitted taxonomy and is not a diff audit. `PR` is populated only where the first-line subject explicitly names one.

| # | Full SHA | Author | Author date | Committer | Committer date | First-line subject | Parents | Preliminary class | PR |
|---:|---|---|---|---|---|---|---:|---|---:|
| 1 | `400c1f366b96a35ca253e13c9b06c5076af41d65` | kexinhuang12345 / Kexin Huang | 2026-01-15T04:23:42Z | web-flow / GitHub | 2026-01-15T04:23:42Z | Merge pull request #259 from snap-stanford/protocols_database | 2 | MERGE_ONLY | 259 |
| 2 | `5394e9980f18e1f33c5291bc6c95044a2e8ad541` | kexinhuang12345 / Kexin Huang | 2026-01-15T04:23:09Z | web-flow / GitHub | 2026-01-15T04:23:09Z | Merge pull request #253 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 253 |
| 3 | `615dab53cadf9855414907eb02122a933cefa5ad` | kexinhuang12345 / Kexin Huang | 2026-01-15T04:22:59Z | web-flow / GitHub | 2026-01-15T04:22:59Z | Merge pull request #266 from nevergreendd/band_roi_detection | 2 | MERGE_ONLY | 266 |
| 4 | `c41cae53ff8f367034008262faafa903717fb589` | kexinhuang12345 / Kexin Huang | 2026-01-15T04:22:20Z | web-flow / GitHub | 2026-01-15T04:22:20Z | Merge pull request #268 from andrewsu/fix/gradio-version-compatibility | 2 | MERGE_ONLY | 268 |
| 5 | `72600f0ddd9204bda3df9a1e64042ad473c81f03` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2026-01-12T18:34:53Z | web-flow / GitHub | 2026-01-12T18:34:53Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 6 | `c73eb050597f566c14f6313b1920c65d668db3aa` | andrewsu / Andrew Su | 2025-12-11T17:54:00Z | andrewsu / Andrew Su | 2025-12-11T17:54:00Z | Fix Gradio version compatibility issue | 1 | BUG_FIX | — |
| 7 | `7cefe0ea43aab28bc232a57d924145bf637b3f2e` | nevergreendd / nevergreendd | 2025-12-08T05:36:32Z | nevergreendd / nevergreendd | 2025-12-08T05:36:32Z | Bug fixed | 1 | BUG_FIX | — |
| 8 | `06760387470ba132ff7e2fd1d2cc17e57edf73fa` | nevergreendd / nevergreendd | 2025-12-08T05:26:44Z | nevergreendd / nevergreendd | 2025-12-08T05:26:44Z | Add analyze_pixel_distribution and find_roi_from_image tools | 1 | FEATURE | — |
| 9 | `6603b4aa43694d2a2eb8565c484c16264dc68daf` | serena2z / Serena Z | 2025-11-13T03:08:02Z | serena2z / Serena Z | 2025-11-13T03:08:02Z | added addgene/thermo protocols | 1 | FEATURE | — |
| 10 | `c36e39f9202863bc7b0665563e74e97723862fa5` | kexinhuang12345 / Kexin Huang | 2025-11-06T22:21:23Z | web-flow / GitHub | 2025-11-06T22:21:23Z | Merge pull request #256 from snap-stanford/know_how | 2 | MERGE_ONLY | 256 |
| 11 | `8490900aa6b050f992a3384321d70d93e8cdd85e` | kexinhuang12345 / Kexin Huang | 2025-11-06T22:21:10Z | kexinhuang12345 / Kexin Huang | 2025-11-06T22:21:10Z | add resource | 1 | FEATURE | — |
| 12 | `1889c75d628d9f00961c8f6353f96390da0afc2a` | kexinhuang12345 / Kexin Huang | 2025-11-06T22:19:50Z | kexinhuang12345 / Kexin Huang | 2025-11-06T22:19:50Z | minor fix | 1 | BUG_FIX | — |
| 13 | `d30453fcb86841316b58bb90e706ef76324f01d4` | kexinhuang12345 / Kexin Huang | 2025-11-06T01:39:20Z | web-flow / GitHub | 2025-11-06T01:39:20Z | Merge pull request #252 from snap-stanford/know_how | 2 | MERGE_ONLY | 252 |
| 14 | `0260c876e88868002a0a59f0eef03ce340aa2841` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-11-05T19:25:43Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-11-05T19:25:43Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 15 | `e875ed42f89892f67d0ba8bd03a1f37729851725` | yhqu / Yuanhao Qu | 2025-11-05T19:25:19Z | yhqu / Yuanhao Qu | 2025-11-05T19:25:19Z | added sgRNA_design knowhow | 1 | FEATURE | — |
| 16 | `0d689541159e42e5aeb75fc289f3bece93c09940` | kexinhuang12345 / Kexin Huang | 2025-11-03T06:12:34Z | web-flow / GitHub | 2025-11-03T06:12:34Z | Merge branch 'main' into know_how | 2 | MERGE_ONLY | — |
| 17 | `ec78dd855dce1e53d0f67070d50a2cd73f2e185f` | kexinhuang12345 / Kexin Huang | 2025-11-03T06:09:47Z | kexinhuang12345 / Kexin Huang | 2025-11-03T06:09:47Z | know-how | 1 | FEATURE | — |
| 18 | `429e5be970f149877515198aa138d204b308e32a` | serena2z / Serena Zhang | 2025-10-31T03:21:57Z | web-flow / GitHub | 2025-10-31T03:21:57Z | Merge pull request #251 from snap-stanford/protocolio_integration | 2 | MERGE_ONLY | 251 |
| 19 | `9dfc9bc5249202474962a0a02084265952197cb9` | serena2z / Serena Z | 2025-10-30T22:27:51Z | serena2z / Serena Z | 2025-10-30T22:27:51Z | protocol io integration | 1 | FEATURE | — |
| 20 | `f9f8fb7c3f744567423b809fa9fe16c91393b95f` | serena2z / Serena Zhang | 2025-10-27T21:31:47Z | web-flow / GitHub | 2025-10-27T21:31:47Z | Merge pull request #249 from snap-stanford/release/v0.0.8 | 2 | MERGE_ONLY | 249 |
| 21 | `d15b3c9277b8945f3bfa6af8faf20bae92c09628` | serena2z / Serena Z | 2025-10-27T21:07:56Z | serena2z / Serena Z | 2025-10-27T21:07:56Z | Bump version to 0.0.8 | 1 | ENVIRONMENT | — |
| 22 | `be5e61305804a09576decf5d88d86d5daa31b441` | serena2z / Serena Z | 2025-10-27T20:13:59Z | serena2z / Serena Z | 2025-10-27T20:13:59Z | version 0.0.8 | 1 | ENVIRONMENT | — |
| 23 | `bdbee1e054e868589ef6345387dd0071f42c7fb8` | serena2z / Serena Zhang | 2025-10-27T19:55:11Z | web-flow / GitHub | 2025-10-27T19:55:11Z | Merge pull request #227 from igor-sadalski/transcripformer_embeddings | 2 | MERGE_ONLY | 227 |
| 24 | `87230d966903209ccc0a45bbffd284b89e42e0e4` | serena2z / Serena Zhang | 2025-10-27T19:54:50Z | web-flow / GitHub | 2025-10-27T19:54:50Z | Merge pull request #248 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 248 |
| 25 | `55a485e9ff81708cde1a249635629959b33c80d6` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-27T18:24:16Z | web-flow / GitHub | 2025-10-27T18:24:16Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 26 | `fd770330e38cc33d82ff7d192d52525be51fb532` | serena2z / Serena Z | 2025-10-27T05:51:24Z | serena2z / Serena Z | 2025-10-27T05:51:24Z | merge with main | 2 | MERGE_ONLY | — |
| 27 | `6b0c273b8fe59884e053ea7d05703deb14b0d9dd` | serena2z / Serena Zhang | 2025-10-27T05:43:36Z | web-flow / GitHub | 2025-10-27T05:43:36Z | Merge pull request #247 from snap-stanford/ui | 2 | MERGE_ONLY | 247 |
| 28 | `82c3de4695a5c3d15da774b3f0c245008b5acf89` | serena2z / Serena Z | 2025-10-27T05:43:01Z | serena2z / Serena Z | 2025-10-27T05:43:01Z | fix precommit hook | 1 | BUG_FIX | — |
| 29 | `a9c9e08224c76717e32b386dfb616da88b7dbd95` | serena2z / Serena Z | 2025-10-27T05:37:20Z | serena2z / Serena Z | 2025-10-27T05:37:20Z | added to readme | 1 | DOC_ONLY | — |
| 30 | `aac96d1dc6e8f61ee3e90b6600d1fe3c642ce89a` | serena2z / Serena Zhang | 2025-10-27T05:17:42Z | web-flow / GitHub | 2025-10-27T05:17:42Z | Merge pull request #229 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 229 |
| 31 | `e79fafc369aeaf57ee858ad566f0bca1b083c6d3` | serena2z / Serena Zhang | 2025-10-27T05:16:50Z | web-flow / GitHub | 2025-10-27T05:16:50Z | Merge pull request #246 from mickaelleclercq/feat/gpt5-mini-support | 2 | MERGE_ONLY | 246 |
| 32 | `eced3971f27433da9ace363b6b84b57cd28919d8` | serena2z / Serena Zhang | 2025-10-27T05:16:29Z | web-flow / GitHub | 2025-10-27T05:16:29Z | Merge branch 'main' into feat/gpt5-mini-support | 2 | MERGE_ONLY | — |
| 33 | `aa3608ead309aaa08dc1622ef47eab86f5011c10` | serena2z / Serena Z | 2025-10-27T05:12:17Z | serena2z / Serena Z | 2025-10-27T05:12:17Z | change temperature for gpt-5 | 1 | UNKNOWN | — |
| 34 | `3e176e76746c8ce060d789d37408861223373627` | serena2z / Serena Zhang | 2025-10-27T00:10:22Z | web-flow / GitHub | 2025-10-27T00:10:22Z | Merge pull request #232 from zhanxw/patch-1 | 2 | MERGE_ONLY | 232 |
| 35 | `2c35ff21fc5fd1c7c0b47c0f2e0183366e0dfe62` | serena2z / Serena Zhang | 2025-10-27T00:07:00Z | web-flow / GitHub | 2025-10-27T00:07:00Z | Merge pull request #224 from igor-sadalski/state_embeddings | 2 | MERGE_ONLY | 224 |
| 36 | `5480b7e0a279135a19320f96f46c62a15181441f` | serena2z / Serena Z | 2025-10-27T00:00:18Z | serena2z / Serena Z | 2025-10-27T00:00:18Z | slight fix in checking if model is downloaded | 1 | BUG_FIX | — |
| 37 | `d39905e0aa65ff28ea7a5edb443fba19ca0b7821` | serena2z / Serena Zhang | 2025-10-26T23:21:40Z | web-flow / GitHub | 2025-10-26T23:21:40Z | Merge pull request #244 from hplustree/fix/reactome-api-update | 2 | MERGE_ONLY | 244 |
| 38 | `f4611f58d16b0c88ac384845203054e6f4df90a7` | serena2z / Serena Zhang | 2025-10-26T23:12:10Z | web-flow / GitHub | 2025-10-26T23:12:10Z | Merge pull request #226 from HelloWorldLTY/main | 2 | MERGE_ONLY | 226 |
| 39 | `52c6dd3a8df99b7a0eca3a3f73c41a103bebe41a` | serena2z / Serena Zhang | 2025-10-26T23:08:18Z | web-flow / GitHub | 2025-10-26T23:08:18Z | Merge pull request #160 from kuanlinhuang/feature/clinical_databases_and_others | 2 | MERGE_ONLY | 160 |
| 40 | `46847a1136baca5d4b2afa27ccfae1190950fc9b` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-25T22:18:08Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-25T22:18:08Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 41 | `3ab60e05fa43212bb638a0b55bbb77a6711e9daf` | kexinhuang12345 / Kexin Huang | 2025-10-25T22:18:01Z | web-flow / GitHub | 2025-10-25T22:18:01Z | Merge branch 'main' into ui | 2 | MERGE_ONLY | — |
| 42 | `c187ac7640ea10cc82a1d0b06b6bd82cfd79d055` | kexinhuang12345 / Kexin Huang | 2025-10-25T22:16:45Z | kexinhuang12345 / Kexin Huang | 2025-10-25T22:16:45Z | ui | 1 | FEATURE | — |
| 43 | `b3d4deb81e79903ce84ae1477da80c4c0b415820` | mickaelleclercq / Mickael Leclercq | 2025-10-23T14:24:13Z | mickaelleclercq / Mickael Leclercq | 2025-10-23T14:24:24Z | docs: remove FORK_WORKFLOW.md from PR to keep changes code-only | 1 | DOC_ONLY | — |
| 44 | `e7dfd681791fd58d37ef561a21f0e6a2f6b33fa1` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-23T14:14:26Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-23T14:14:27Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 45 | `4aaa134f304a9ef898070d7518bfb6f06080da37` | mickaelleclercq / Mickael Leclercq | 2025-10-23T14:03:10Z | mickaelleclercq / Mickael Leclercq | 2025-10-23T14:11:34Z | fix: chain original exception in BiomniEval1.evaluate() (ruff B904) | 1 | FORMAT_ONLY | — |
| 46 | `0aa0eb86b41d458a16157261e54d8a71168c53c1` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-22T01:59:17Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-22T01:59:18Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 47 | `2df045a9710270efd579740cefad2c3e43627a9b` | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:17:40Z | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:17:40Z | docs: add fork workflow documentation and helper scripts | 1 | UNKNOWN | — |
| 48 | `50c0c2e7aa1c089800f9804c3b9551a852b8db79` | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:13:48Z | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:13:48Z | fix(agent): flatten Responses API content blocks before parsing tags | 1 | BUG_FIX | — |
| 49 | `6f6170fe570f658d0db258855dc3c96358be5b0f` | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:13:19Z | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:13:19Z | fix(retriever): normalize Responses API content blocks to string | 1 | BUG_FIX | — |
| 50 | `eeff62cc4a82f3c67f7d7dfd942891676e341417` | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:11:56Z | mickaelleclercq / Mickael Leclercq | 2025-10-22T01:11:56Z | feat(llm): add OpenAI Responses API support for gpt-5 models | 1 | FEATURE | — |
| 51 | `d92c7b9aae05b1f7f1658060dcdfa544fa7c6cac` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-20T20:37:24Z | web-flow / GitHub | 2025-10-20T20:37:24Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 52 | `074f5b90326b878e4881e041e6aba8e86f44c03f` | divyesh-htree / divyesh-htree | 2025-10-16T06:27:53Z | divyesh-htree / divyesh-htree | 2025-10-16T06:27:53Z | add lint in biomni eval 1 | 1 | FORMAT_ONLY | — |
| 53 | `37db580b91bc55fef2f4e42409f808fa3b769067` | divyesh-htree / divyesh-htree | 2025-10-16T05:24:57Z | divyesh-htree / divyesh-htree | 2025-10-16T05:24:57Z | fix: update query_reactome() to use 2025 Reactome /search/query endpoint | 1 | BUG_FIX | — |
| 54 | `8fd7b218c43b78538f79cd93d05db43d8a8073c6` | kexinhuang12345 / Kexin Huang | 2025-10-13T06:21:09Z | web-flow / GitHub | 2025-10-13T06:21:09Z | Merge pull request #240 from snap-stanford/r0-tutorial | 2 | MERGE_ONLY | 240 |
| 55 | `8089bed75c32f6f7bdcace72c837ad3784984c04` | RyanLi1028 / Ryan Li | 2025-10-13T06:20:16Z | RyanLi1028 / Ryan Li | 2025-10-13T06:20:16Z | cleanup | 1 | REFACTOR | — |
| 56 | `12d262d3edff19c21cfa07ab7511e5230d449446` | RyanLi1028 / Ryan Li | 2025-10-13T06:18:46Z | RyanLi1028 / Ryan Li | 2025-10-13T06:18:46Z | update readme for biomni-r0 | 1 | DOC_ONLY | — |
| 57 | `8b1724ee3deba1a04c7cb096f09cc5036623c645` | kexinhuang12345 / Kexin Huang | 2025-10-13T06:11:11Z | web-flow / GitHub | 2025-10-13T06:11:11Z | Update Biomni-Eval1 instance count in README | 1 | DOC_ONLY | — |
| 58 | `fcb8d08e4145d146ae6eb43ec2d8198c4c4e20d5` | kexinhuang12345 / Kexin Huang | 2025-10-13T06:09:52Z | kexinhuang12345 / Kexin Huang | 2025-10-13T06:09:52Z | Merge branch 'biomni_eval_1' of https://github.com/snap-stanford/Biomni into biomni_eval_1 | 2 | MERGE_ONLY | — |
| 59 | `bcbcb9b10bb5492933d837f4e42248c71409e804` | kexinhuang12345 / Kexin Huang | 2025-10-13T06:09:39Z | kexinhuang12345 / Kexin Huang | 2025-10-13T06:09:39Z | update eval | 1 | BENCHMARK | — |
| 60 | `3034b8b79f1d0f215a764af1498b22bbd9d70b83` | kexinhuang12345 / Kexin Huang | 2025-10-13T01:24:30Z | web-flow / GitHub | 2025-10-13T01:24:30Z | eval (#238) | 1 | BENCHMARK | 238 |
| 61 | `d146f9a4546af192ba1c2f763a3fbe769310462c` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-12T21:30:09Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-10-12T21:30:09Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 62 | `f2d9f3cd013d9d52536818d397437f2259436eaa` | kexinhuang12345 / Kexin Huang | 2025-10-12T21:29:42Z | kexinhuang12345 / Kexin Huang | 2025-10-12T21:29:42Z | eval | 1 | BENCHMARK | — |
| 63 | `d8f9a9222e8696887e48328b78317ea88f4fc536` | serena2z / Serena Zhang | 2025-10-09T04:58:27Z | web-flow / GitHub | 2025-10-09T04:58:27Z | Merge pull request #210 from snap-stanford/pylabrobot | 2 | MERGE_ONLY | 210 |
| 64 | `98c2c8aef4534a107cdc63e7dcd1a9dc2c9b593b` | serena2z / Serena Z | 2025-10-09T04:45:20Z | serena2z / Serena Z | 2025-10-09T04:45:20Z | resolve merge | 2 | MERGE_ONLY | — |
| 65 | `bf667b6fdf29b275c55f5ca32bd27ef96a297f4e` | serena2z / Serena Z | 2025-10-08T22:41:58Z | serena2z / Serena Z | 2025-10-08T22:41:58Z | reformatted pylabrobot tools to rely more heavily on validation loop in generating accurate scripts | 1 | FEATURE | — |
| 66 | `6b378531bfcd15b389dd428efa52d441648931e2` | zhanxw / zhanxw | 2025-10-02T00:37:49Z | web-flow / GitHub | 2025-10-02T00:37:49Z | Fix package names to match correct casing | 1 | BUG_FIX | — |
| 67 | `0de0af2030d8019696ed5ec6321f0a787f000851` | igor-sadalski / Igor Sadalski | 2025-09-30T12:28:23Z | igor-sadalski / Igor Sadalski | 2025-09-30T12:28:23Z | Merge remote-tracking branch 'origin/main' into state_embeddings | 2 | MERGE_ONLY | — |
| 68 | `41aeb57bd13ad6ebbdecd1f1d10554c58cb341db` | igor-sadalski / Igor Sadalski | 2025-09-30T12:26:32Z | igor-sadalski / Igor Sadalski | 2025-09-30T12:26:32Z | resolve merge conflict | 2 | MERGE_ONLY | — |
| 69 | `958da0c76de7e42d5a08038e5f2425305fcbbcb4` | igor-sadalski / Igor Sadalski | 2025-09-30T12:22:49Z | igor-sadalski / Igor Sadalski | 2025-09-30T12:22:49Z | Refactor generate_embeddings_with_state function to improve logging by printing output to console before appending to steps list. Update installation command for arc-state in the setup script for consistency. | 1 | REFACTOR | — |
| 70 | `c5bc7d9f46a6cd1754cf008b4e21db5c47205c6f` | igor-sadalski / Igor Sadalski | 2025-09-29T21:30:02Z | igor-sadalski / Igor Sadalski | 2025-09-29T21:30:02Z | Enhance logging in generate_embeddings_with_state function to track steps and errors, and update output format description. | 1 | REFACTOR | — |
| 71 | `eb22cef6f35ddaf10cefd7f25c4b9f816eaf3fce` | serena2z / Serena Zhang | 2025-09-29T21:18:46Z | web-flow / GitHub | 2025-09-29T21:18:46Z | Merge pull request #230 from snap-stanford/release/v0.0.7 | 2 | MERGE_ONLY | 230 |
| 72 | `e8b76ec2fb45efe9e9605b69d4f3d93864a13fcd` | serena2z / Serena Z | 2025-09-29T21:12:10Z | serena2z / Serena Z | 2025-09-29T21:12:10Z | release 0.0.7 | 1 | ENVIRONMENT | — |
| 73 | `07c9dc194fd589030a1f8bf6041ba17004b0deca` | — / Igor Sadalski | 2025-09-28T15:43:26Z | — / Igor Sadalski | 2025-09-28T15:43:26Z | Merge remote-tracking branch 'origin' into transcripformer_embeddings | 2 | MERGE_ONLY | — |
| 74 | `2e8169abe88f880612bcb04808bc940f96b08421` | — / Igor Sadalski | 2025-09-28T15:39:48Z | — / Igor Sadalski | 2025-09-28T15:39:48Z | fix precommit hooks | 1 | BUG_FIX | — |
| 75 | `a501828ab71022e615502da72898409b5345f8c8` | — / Igor Sadalski | 2025-09-28T15:27:05Z | — / Igor Sadalski | 2025-09-28T15:27:05Z | add more params to transcriptofmer and better data perprocessing | 1 | FEATURE | — |
| 76 | `5c6161990a52da7a7687a1971e1bcde2cf439da5` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-28T15:14:26Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-28T15:14:27Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 77 | `f5f2711f804e6bd7b23521ef0aab47f7b8c80959` | HelloWorldLTY / HelloWorldLTY | 2025-09-28T15:13:12Z | web-flow / GitHub | 2025-09-28T15:13:12Z | Update literature.py | 1 | UNKNOWN | — |
| 78 | `c89ead2500999bde54fb706d5d36bd9dba7e6d1b` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-27T15:33:46Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-27T15:33:47Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 79 | `c6b13e9b63d8fd261603c32d83404a104567ff59` | — / Igor Sadalski | 2025-09-27T15:33:31Z | — / Igor Sadalski | 2025-09-27T15:33:31Z | Merge branch 'main' into state_embeddings | 2 | MERGE_ONLY | — |
| 80 | `089c7927b83121472001fce825dfc0d19e9491b2` | — / Igor Sadalski | 2025-09-27T15:24:21Z | — / Igor Sadalski | 2025-09-27T15:24:21Z | add updated installs required for STATE | 1 | ENVIRONMENT | — |
| 81 | `f9d1527e7aa84da88c9ac0804115fb657f6d12b9` | — / Igor Sadalski | 2025-09-27T15:23:51Z | — / Igor Sadalski | 2025-09-27T15:23:51Z | update state embeddings generation function with better error handling and recovery | 1 | BUG_FIX | — |
| 82 | `b769281b14f53ea9670d71028d1f38449a5e4f53` | serena2z / Serena Zhang | 2025-09-27T10:21:45Z | web-flow / GitHub | 2025-09-27T10:21:45Z | Merge pull request #223 from snap-stanford/patch_pdf_font_stack | 2 | MERGE_ONLY | 223 |
| 83 | `cfa41893f6145a2c468d3a07ca0998f5c4572465` | serena2z / Serena Z | 2025-09-27T10:21:04Z | serena2z / Serena Z | 2025-09-27T10:21:04Z | patched font for unavailable characters | 1 | BUG_FIX | — |
| 84 | `ac9e114d59982760446850aba89aadbe29948494` | serena2z / Serena Zhang | 2025-09-27T09:54:37Z | web-flow / GitHub | 2025-09-27T09:54:37Z | Merge pull request #217 from igor-sadalski/download_pdf_of_research | 2 | MERGE_ONLY | 217 |
| 85 | `605cbdfb28b160d37d23d3d6cdcf245e3daaca80` | serena2z / Serena Z | 2025-09-27T09:51:56Z | serena2z / Serena Z | 2025-09-27T09:51:56Z | modified readme | 1 | DOC_ONLY | — |
| 86 | `9b55bf835bca6db87d769219a02fa79ae8f02834` | serena2z / Serena Z | 2025-09-27T09:40:37Z | serena2z / Serena Z | 2025-09-27T09:40:37Z | added weasyprint package installation, merged with main | 2 | MERGE_ONLY | — |
| 87 | `0f1f7b0ec09f9c88a333794523c4e3df70f20794` | serena2z / Serena Z | 2025-09-27T09:37:43Z | serena2z / Serena Z | 2025-09-27T09:37:43Z | added to readme | 1 | DOC_ONLY | — |
| 88 | `b4158b3b22a5c081a1a39b3878b1613b066b22d8` | serena2z / Serena Zhang | 2025-09-27T03:29:35Z | web-flow / GitHub | 2025-09-27T03:29:35Z | Merge pull request #207 from MintaYLu/bioimaging | 2 | MERGE_ONLY | 207 |
| 89 | `d2daee350556a55d2d995f8f44cfd044661cf00e` | serena2z / Serena Zhang | 2025-09-27T03:28:32Z | web-flow / GitHub | 2025-09-27T03:28:32Z | Merge branch 'main' into bioimaging | 2 | MERGE_ONLY | — |
| 90 | `3844727f157dbe95aba71cc8e16efeae135bba7b` | serena2z / Serena Zhang | 2025-09-26T20:13:09Z | web-flow / GitHub | 2025-09-26T20:13:09Z | Merge pull request #222 from snap-stanford/openfda-fix | 2 | MERGE_ONLY | 222 |
| 91 | `14d86f3246240617b8f82e24d10a794f2daf5565` | serena2z / Serena Z | 2025-09-26T20:12:03Z | serena2z / Serena Z | 2025-09-26T20:12:03Z | fix openfda query | 1 | BUG_FIX | — |
| 92 | `0fb99ee5bc7c4d66a1e62884b4c37703b969b1b7` | igor-sadalski / Igor Sadalski | 2025-09-26T02:01:23Z | igor-sadalski / Igor Sadalski | 2025-09-26T02:01:23Z | generate mvp tool to generate embeddings with transcriptformer | 1 | FEATURE | — |
| 93 | `54c080157feb323892699c45dcf7f51bc60879bf` | serena2z / Serena Zhang | 2025-09-26T01:55:35Z | web-flow / GitHub | 2025-09-26T01:55:35Z | Merge pull request #208 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 208 |
| 94 | `0601ffbe70c3d7d15e3fdb1866dd9007bc80670e` | igor-sadalski / Igor Sadalski | 2025-09-26T01:48:45Z | igor-sadalski / Igor Sadalski | 2025-09-26T01:48:45Z | add function to add mvp embeddings with state | 1 | FEATURE | — |
| 95 | `dbab0996cf78f9a2f6d8bde05f7d247cf6e9b2e5` | serena2z / Serena Zhang | 2025-09-26T01:41:45Z | web-flow / GitHub | 2025-09-26T01:41:45Z | Merge pull request #216 from HelloWorldLTY/main | 2 | MERGE_ONLY | 216 |
| 96 | `631b5120b8e7d9eae5d4b5f4ea43c761fe78775f` | serena2z / Serena Z | 2025-09-26T01:41:00Z | serena2z / Serena Z | 2025-09-26T01:41:00Z | added to new_software_v006 | 1 | ENVIRONMENT | — |
| 97 | `7b65121bcf91c0166565f197b7a8924bea409f6b` | serena2z / Serena Z | 2025-09-26T01:31:03Z | serena2z / Serena Z | 2025-09-26T01:31:03Z | Merge remote-tracking branch 'origin/main' into HelloWorldLTY/main | 2 | MERGE_ONLY | — |
| 98 | `0f4e96ab34586d9a16e4d7dfe10269ed9a487191` | serena2z / Serena Zhang | 2025-09-26T01:26:19Z | web-flow / GitHub | 2025-09-26T01:26:19Z | Merge pull request #212 from svamintgit/1-add-glycoengineering-tools | 2 | MERGE_ONLY | 212 |
| 99 | `27b04d95a3c8f579d30eb892116058fa1b19ef9c` | serena2z / Serena Z | 2025-09-26T00:51:30Z | serena2z / Serena Z | 2025-09-26T00:51:30Z | fixed segment_with_nn_unet task download that wasn't working (see error in nnunet github repo) | 1 | BUG_FIX | — |
| 100 | `899eefb22a5a102fd81f1d845490b4b83fee3402` | serena2z / Serena Z | 2025-09-25T22:27:38Z | serena2z / Serena Z | 2025-09-25T22:27:38Z | Merge remote-tracking branch 'origin/main' into bioimaging | 2 | MERGE_ONLY | — |

## PR mapping and duplicate/lineage notes

- `mapped_to_pr`: 29 records from explicit first-line subjects.
- Explicit PRs: `#160`, `#207`, `#208`, `#210`, `#212`, `#216`, `#217`, `#222`, `#223`, `#224`, `#226`, `#227`, `#229`, `#230`, `#232`, `#238`, `#240`, `#244`, `#246`, `#247`, `#248`, `#249`, `#251`, `#252`, `#253`, `#256`, `#259`, `#266`, `#268`.
- Of these, 28 are two-parent `Merge pull request` commits. `#238` is a single-parent subject reference and may be a squash/rebase lineage; exact merge method is unresolved.
- There are 42 multi-parent commits total: the 28 explicit PR merges plus 14 branch/remote/conflict merges without a PR number in the first line. Treat all 42 as duplicate/sync/lineage surfaces until PR and DAG normalization; do not count them as 42 independent features.
- No duplicate substantive change set was proven in this metadata-only pass. Exact ancestry/patch identity remains for normalization.

## Substantive and feature leads

These are discovery leads, not validated independent features:

- Protocol expansion and retrieval: PR `#259` / protocols database; Addgene/Thermo protocols; PR `#251` / Protocol.io integration.
- Bioimaging: PR `#266` plus `06760387470ba132ff7e2fd1d2cc17e57edf73fa` for pixel-distribution and ROI tools; PR `#207`; nnU-Net download repair.
- Know-how: sgRNA design (`e875ed42f89892f67d0ba8bd03a1f37729851725`) and other resource/know-how commits/PRs `#252`, `#256`.
- Model/runtime support: PR `#246` and `eeff62cc4a82f3c67f7d7dfd942891676e341417` for OpenAI Responses API / GPT-5; adjacent parsing fixes.
- Database/API capability: PR `#160` clinical databases; Reactome and openFDA repairs.
- UI: PR `#247` and `c187ac7640ea10cc82a1d0b06b6bd82cfd79d055`.
- Biomni-R0 tutorial/evaluation: PRs `#240`, `#238` and adjacent benchmark commits.
- Lab automation: PR `#210` / PyLabRobot and `bf667b6fdf29b275c55f5ca32bd27ef96a297f4e` validation-loop change.
- Embeddings: PR `#227` / TranscriptFormer and PR `#224` / STATE, with several adjacent generation, preprocessing, logging, install, and recovery commits.
- PDF/reporting: PR `#217` research PDF download and PR `#223` font-stack patch.
- Glycoengineering: PR `#212`.

## Evidence URLs

- Frozen page-1 API query: https://api.github.com/repos/snap-stanford/Biomni/commits?sha=400c1f366b96a35ca253e13c9b06c5076af41d65&per_page=100&page=1
- Human commit history at frozen baseline: https://github.com/snap-stanford/Biomni/commits/400c1f366b96a35ca253e13c9b06c5076af41d65
- Frozen HEAD commit: https://github.com/snap-stanford/Biomni/commit/400c1f366b96a35ca253e13c9b06c5076af41d65
- PR pattern (replace number with the explicit IDs above): https://github.com/snap-stanford/Biomni/pull/259

## Uncertainty and unresolved work

- The exact global commit count is unresolved until page 5 is read; `401–500` must not be promoted to an exact denominator.
- GitHub login absence for positions 73–75, 79–81 reflects a null linked account in this API response; the signature name `Igor Sadalski` is not independently identity-verified here.
- Commit dates are Git author/committer metadata and are not guaranteed to equal public-push time.
- Subject-based classes can be wrong for mixed commits (especially positions 11, 12, 17, 33, 45, 47, 65, 69, 70, 74, 77, 80, and 96). Diff/PR evidence is required before canonical classification.
- Merge commits and adjacent child commits likely repeat PR lineages; no independent-feature counts should be derived from this page without DAG/PR normalization.
- This task did not audit diffs, licenses, security, runtime correctness, PR state, or feature completeness.

## Next action

Fetch the same frozen commit-list query with `per_page=100&page=2`, preserve newest-first order, verify that its first SHA follows `899eefb22a5a102fd81f1d845490b4b83fee3402`, and continue the inventory. Keep collection `PARTIAL` until all five pages are processed and the final-page length establishes the exact denominator.
