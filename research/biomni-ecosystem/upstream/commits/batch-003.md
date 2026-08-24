# Worker Result: commit-index-003

Parent verification: `VERIFIED` at `2026-08-22T21:01:14Z`. Frozen local Git
positions 201–300 match all 100 worker SHAs and boundaries. The page contains 34
multi-parent commits and 26 explicit merge-PR subjects. Classes remain subject-only
`INFERENCE` pending normalization.

## Task record

- Task ID: `commit-index-003`
- Scope: official `snap-stanford/Biomni` commit-list API, frozen `main` baseline `400c1f366b96a35ca253e13c9b06c5076af41d65`, page `3`, `per_page=100`, deterministic API order (newest first).
- Status: `PARTIAL`
- Observed at UTC: `2026-08-22T20:57:46Z` (GitHub response `Date` header).
- Processed this batch: `100` commit records, cumulative positions 201–300 inclusive.
- Global frozen-DAG denominator: `487` commits (parent-verified canonical batch 001).
- Boundary: prior batch last `9c5eca618b7171092420ad07c9d6e6cd6c22dcc4`; this batch first `48febfee6fc6433e4fea9c8ca1247981c830195e`; this batch last `d58c9467ab4af42e25f5d2bbb00d6793bbd5e892`.
- Safety: metadata-only inventory; no repository code, workflow, script, package, or external instruction was executed.

## Pagination and boundary evidence

- GitHub returned HTTP 200 and exactly 100 objects.
- The response `Link` header gave `rel="prev"` at page 2, `rel="first"` at page 1, `rel="next"` at page 4, and `rel="last"` at page 5 for the same frozen SHA and `per_page=100` query.
- Worker 002 ended at API position 200 with `9c5eca618b7171092420ad07c9d6e6cd6c22dcc4`; page 3 begins at API position 201 with `48febfee6fc6433e4fea9c8ca1247981c830195e`. The page-3 `prev=2` link and exact page arrays establish the pagination boundary; this does not assert a direct parent-child edge between those two commits.
- Processed cumulatively: `300 / 487`.
- Pagination: `PARTIAL`; next page: `4`.

## Preliminary inventory

`Author` and `Committer` are shown as `GitHub login / commit-signature name`. `—` means GitHub did not expose a linked public account in this response. Classification is preliminary and derives only from parent count plus the first-line subject; it uses the permitted taxonomy and is not a diff audit. Every multi-parent record is provisionally `MERGE_ONLY`. `PR` is populated only where the first-line subject explicitly names one.

| # | Full SHA | Author | Author date | Committer | Committer date | First-line subject | Parents | Preliminary class | PR |
|---:|---|---|---|---|---|---|---:|---|---:|
| 201 | `48febfee6fc6433e4fea9c8ca1247981c830195e` | shengyongniu / shengyongniu | 2025-08-16T01:15:48Z | shengyongniu / shengyongniu | 2025-08-16T01:15:48Z | Merge branch 'shengyong/trialbench' of github.com:shengyongniu/Biomni into shengyong/trialbench | 2 | MERGE_ONLY | — |
| 202 | `4f589b768be990a153c77b7ac3d3a7aaa4ed245a` | shengyongniu / shengyongniu | 2025-08-16T01:15:12Z | shengyongniu / shengyongniu | 2025-08-16T01:15:12Z | remove test comment | 1 | REMOVAL | — |
| 203 | `1140513b2d97f01faf4b734c3669372f32ea74d1` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T01:06:26Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T01:06:27Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 204 | `bddc222d69b1369eabbc3c6bb230e09f8d2326af` | shengyongniu / shengyongniu | 2025-08-16T01:02:31Z | shengyongniu / shengyongniu | 2025-08-16T01:02:31Z | Merge branch 'shengyong/trialbench' of github.com:shengyongniu/Biomni into shengyong/trialbench | 2 | MERGE_ONLY | — |
| 205 | `803a4dc46ec999814eeef8b67015b73f2fb0b4a9` | shengyongniu / shengyongniu | 2025-08-16T01:02:20Z | shengyongniu / shengyongniu | 2025-08-16T01:02:20Z | API | 1 | FEATURE | — |
| 206 | `127b4193a8c450747d21e232ae82f3a7464d557b` | shengyongniu / NIU, SHENG-YONG | 2025-08-16T00:43:02Z | web-flow / GitHub | 2025-08-16T00:43:02Z | Delete tutorials/examples/clinicaltrials_example.md | 1 | REMOVAL | — |
| 207 | `c7a6526a5171bb8652f57bacfacd0daa072bfefd` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T00:37:46Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T00:37:47Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 208 | `2bd9f682a4e4f9b608e93c90fa3cfd42b7d1aa4b` | shengyongniu / shengyongniu | 2025-08-16T00:37:25Z | shengyongniu / shengyongniu | 2025-08-16T00:37:25Z | feat(database): add ClinicalTrials.gov integration as query_clinicaltrials per contribution guide; add tool description and example | 1 | FEATURE | — |
| 209 | `e996234b8ed7077685115bfd7fa4b02c1348a251` | shengyongniu / shengyongniu | 2025-08-16T00:24:54Z | shengyongniu / shengyongniu | 2025-08-16T00:24:54Z | Merge branch 'main' into shengyong/trialbench | 2 | MERGE_ONLY | — |
| 210 | `644ec8aa60838813d14db15d7f672dcea6a30f75` | shengyongniu / shengyongniu | 2025-08-16T00:24:33Z | shengyongniu / shengyongniu | 2025-08-16T00:24:33Z | remove trialbench | 1 | REMOVAL | — |
| 211 | `a00c452fe5940ac0fdb29f82add681263f0717c1` | serena2z / Serena Zhang | 2025-08-15T20:25:34Z | web-flow / GitHub | 2025-08-15T20:25:34Z | Merge pull request #149 from vlln/add-sphinx-docs | 2 | MERGE_ONLY | 149 |
| 212 | `c7222819750dda1f056c57a1b7376bf65285b95a` | serena2z / Serena Z | 2025-08-15T20:07:33Z | serena2z / Serena Z | 2025-08-15T20:07:33Z | changed known_conflicts readme | 1 | DOC_ONLY | — |
| 213 | `2089a88ee2cbb675a9289225014d2a3390c5d9b6` | serena2z / Serena Z | 2025-08-15T20:06:55Z | serena2z / Serena Z | 2025-08-15T20:06:55Z | changed environment installation and documentation | 1 | ENVIRONMENT | — |
| 214 | `53767cf454d67b6839138ccb0a969690497c5deb` | serena2z / Serena Z | 2025-08-15T18:54:44Z | serena2z / Serena Z | 2025-08-15T18:54:44Z | Merge remote-tracking branch 'origin/main' into feature/cnv-purity-ploidy | 2 | MERGE_ONLY | — |
| 215 | `547e7a8478ea917907ae586dc66ca19f02af451f` | serena2z / Serena Zhang | 2025-08-15T02:54:55Z | web-flow / GitHub | 2025-08-15T02:54:55Z | Merge pull request #143 from Edison-A-N/feature/lazy-import-llm | 2 | MERGE_ONLY | 143 |
| 216 | `67fc7ecbcc7194ee5474d2a88e0494ce6ece87a8` | serena2z / Serena Z | 2025-08-15T02:52:14Z | serena2z / Serena Z | 2025-08-15T02:52:14Z | added bedrock | 1 | FEATURE | — |
| 217 | `1158ac5d6a77cc957b705311e0f10478da108668` | serena2z / Serena Z | 2025-08-15T02:24:10Z | serena2z / Serena Z | 2025-08-15T02:24:10Z | Merge remote-tracking branch 'origin/main' into feature/lazy-import-llm | 2 | MERGE_ONLY | — |
| 218 | `212700b3c69717967e984fe8138e698a0e1fc159` | serena2z / Serena Zhang | 2025-08-15T02:17:48Z | web-flow / GitHub | 2025-08-15T02:17:48Z | Merge pull request #126 from tuln128/autonomous_function_generation | 2 | MERGE_ONLY | 126 |
| 219 | `bf8095d8aaba8eb696ba241326cc99d3e282615e` | serena2z / Serena Zhang | 2025-08-15T01:54:10Z | web-flow / GitHub | 2025-08-15T01:54:10Z | Merge pull request #122 from Edison-A-N/feature/stream-go-function | 2 | MERGE_ONLY | 122 |
| 220 | `a6d08d0208031d2c9af22c51189a55f6e42c41a2` | serena2z / Serena Zhang | 2025-08-15T01:26:13Z | web-flow / GitHub | 2025-08-15T01:26:13Z | Merge pull request #153 from snap-stanford/datasets | 2 | MERGE_ONLY | 153 |
| 221 | `b3c61a9200210b5fe1d9f2c8af8ddd7af99d22b1` | serena2z / Serena Z | 2025-08-15T01:23:38Z | serena2z / Serena Z | 2025-08-15T01:23:38Z | deprecated opentargetgenetics query | 1 | REMOVAL | — |
| 222 | `91c4f7e7227659aa18ad52431068b39c3479aa56` | serena2z / Serena Zhang | 2025-08-14T21:51:37Z | web-flow / GitHub | 2025-08-14T21:51:37Z | Merge pull request #139 from amehrjou/fix/wget-fallback | 2 | MERGE_ONLY | 139 |
| 223 | `67e5f387bcb4a893c216f4ec84bf8d6f417a75cc` | kuanlinhuang / huangkuanlin | 2025-08-13T22:24:52Z | kuanlinhuang / huangkuanlin | 2025-08-13T22:24:52Z | added chembl beaker Class w/ many common biochemical functionalities, updated tool description, also refined chembl database query and schema | 1 | FEATURE | — |
| 224 | `4a4f4ff733900d064ec29e72a1b6add1675d36b9` | kuanlinhuang / huangkuanlin | 2025-08-13T21:27:42Z | kuanlinhuang / huangkuanlin | 2025-08-13T21:27:42Z | update cellxgene census for accuracy | 1 | BUG_FIX | — |
| 225 | `a21bbb74051921f996aed6dec38e6dff37e55f24` | kuanlinhuang / huangkuanlin | 2025-08-13T21:20:45Z | kuanlinhuang / huangkuanlin | 2025-08-13T21:20:45Z | updated quickgo for API accuracy, deleted OLS as it's hard to use | 1 | REMOVAL | — |
| 226 | `a8a6238f45f2b2db7f8befbc851ce9044a42b86c` | kuanlinhuang / huangkuanlin | 2025-08-13T21:07:02Z | kuanlinhuang / huangkuanlin | 2025-08-13T21:07:02Z | updated clinicaltrails dailymed and openfda queries for accuracies regarding current APIs, clinicaltrials "experimental" API seem to be not working yet | 1 | BUG_FIX | — |
| 227 | `00e286f894fda8d68893646382008afc604c205b` | kuanlinhuang / huangkuanlin | 2025-08-13T20:12:28Z | kuanlinhuang / huangkuanlin | 2025-08-13T20:12:28Z | updated chembl and unichem query to be more precise and schema, deleted drugcentral as the API seems down most of the time | 1 | REMOVAL | — |
| 228 | `0e003b9d0ae016bd8d68a11c71df96e1428a8489` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-13T09:45:55Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-13T09:45:56Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 229 | `c66f22a4b81f2f2cf79b9938cd1c034eb7f459eb` | vlln / vlln | 2025-08-13T09:09:57Z | vlln / vlln | 2025-08-13T09:09:57Z | feat: Add Sphinx documentation build system | 1 | DOC_ONLY | — |
| 230 | `843e83f2bbb226269dded940afd3c2f68687fe2f` | serena2z / Serena Zhang | 2025-08-13T00:15:02Z | web-flow / GitHub | 2025-08-13T00:15:02Z | Merge pull request #144 from snap-stanford/datasets | 2 | MERGE_ONLY | 144 |
| 231 | `7c435043d47159e0e9ce5bad939e4f32de754661` | serena2z / Serena Z | 2025-08-13T00:11:32Z | serena2z / Serena Z | 2025-08-13T00:11:32Z | fixed env versions | 1 | ENVIRONMENT | — |
| 232 | `aec5bb99c3ce9e467ae5c17c0215a13a26e33d54` | Edison-A-N / Edison-A-N | 2025-08-12T08:12:18Z | Edison-A-N / Edison-A-N | 2025-08-12T08:12:18Z | feat: implement lazy import for LLM dependencies | 1 | FEATURE | — |
| 233 | `43de1d29912698072362bd12e730835e7b2b181d` | serena2z / Serena Zhang | 2025-08-12T03:34:43Z | web-flow / GitHub | 2025-08-12T03:34:43Z | Merge pull request #141 from snap-stanford/datasets | 2 | MERGE_ONLY | 141 |
| 234 | `7b08d7972c44ba81938b5bbee53ef16f6d61ee14` | serena2z / Serena Z | 2025-08-12T03:33:02Z | serena2z / Serena Z | 2025-08-12T03:33:02Z | added github mcp back | 1 | FEATURE | — |
| 235 | `f474aeaf9decba38eb47b9e9e96e62de855800c2` | serena2z / Serena Z | 2025-08-12T03:31:05Z | serena2z / Serena Z | 2025-08-12T03:31:05Z | remove datasets for license purposes, fix mcp config file | 1 | UNKNOWN | — |
| 236 | `d43535762a4ff829f33160a62173ea9aab82118c` | kexinhuang12345 / Kexin Huang | 2025-08-11T21:01:01Z | web-flow / GitHub | 2025-08-11T21:01:01Z | Merge pull request #120 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 120 |
| 237 | `a217b2bd072c723b302eca36af5f8a376bdb3826` | kexinhuang12345 / Kexin Huang | 2025-08-11T20:25:48Z | web-flow / GitHub | 2025-08-11T20:25:48Z | Merge pull request #129 from PabloPauling/main | 2 | MERGE_ONLY | 129 |
| 238 | `2b7111e9c2261dad2e8a5d9c62eab020fc27dc36` | amehrjou / amehrjou | 2025-08-11T20:21:07Z | amehrjou / amehrjou | 2025-08-11T20:21:07Z | Add wget/curl fallback in install_cli_tools.sh | 1 | BUG_FIX | — |
| 239 | `6fe2550d92ceeba37866abd76a9a3eac270e4e8f` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-11T18:41:23Z | web-flow / GitHub | 2025-08-11T18:41:23Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 240 | `0301c22142b33b9cd08997a3c12bdcc08326f4ef` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-10T11:02:00Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-10T11:02:00Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 241 | `b82d340786828b468af0b37fe6cc4eaf82f5a521` | marcosbolanos / marcos | 2025-08-10T10:42:17Z | marcosbolanos / marcos | 2025-08-10T10:42:17Z | feat: simplified implementation and re-tested successfully | 1 | REFACTOR | — |
| 242 | `94482ef81c15ed56f04dec851f9475ea64b4e2d2` | marcosbolanos / marcos | 2025-08-10T10:32:41Z | marcosbolanos / marcos | 2025-08-10T10:32:41Z | fully tested and finalized workflow, added isolated environment for CNVkit | 1 | ENVIRONMENT | — |
| 243 | `9ffa83f12334861c4c39c813ffa082f9199b64dc` | kuanlinhuang / huangkuanlin | 2025-08-09T22:19:49Z | kuanlinhuang / huangkuanlin | 2025-08-09T22:19:49Z | Make DataLake Loading optional to save time/memory, and handling of using OPENAI models | 1 | FEATURE | — |
| 244 | `3456f4a5648241e2ce0b4a8f86f6da8da51a6613` | marcosbolanos / marcos | 2025-08-09T08:26:26Z | marcosbolanos / marcos | 2025-08-09T08:26:26Z | chore: added a little space after my latest tool so I can avoid conflicts with later pull requests | 1 | FORMAT_ONLY | — |
| 245 | `4b20cdb36527ade0acb2a43efb93542231fccacd` | marcosbolanos / marcos | 2025-08-09T08:25:13Z | marcosbolanos / marcos | 2025-08-09T08:25:13Z | chore: add cnvkit to bio_env.yml dependencies | 1 | DEPENDENCY_ONLY | — |
| 246 | `f70a00f25b309174962fb39ff450c64b81a75cab` | marcosbolanos / marcos | 2025-08-09T08:11:29Z | marcosbolanos / marcos | 2025-08-09T08:11:29Z | chore: add cnvkit python package to dependencies | 1 | DEPENDENCY_ONLY | — |
| 247 | `df7e3da59c7d145421f0343b677ee26e3034248b` | marcosbolanos / marcos | 2025-08-09T08:09:54Z | marcosbolanos / marcos | 2025-08-09T08:09:54Z | feat: add comprehensive copy number workflow | 1 | FEATURE | — |
| 248 | `0f9dbf925a0512292a2486c87f87152484a9d18a` | serena2z / Serena Zhang | 2025-08-07T07:05:25Z | web-flow / GitHub | 2025-08-07T07:05:25Z | Merge pull request #131 from snap-stanford/release_0.0.5 | 2 | MERGE_ONLY | 131 |
| 249 | `3e704830ed2f8f36a6b156244a2a087cc928c175` | serena2z / serena2z | 2025-08-07T06:58:10Z | serena2z / serena2z | 2025-08-07T06:58:10Z | fixed v005.sh | 2 | MERGE_ONLY | — |
| 250 | `cba3d53aaac7978d78bf97d688c6391f6e418046` | kuanlinhuang / huangkuanlin | 2025-08-07T01:39:09Z | kuanlinhuang / huangkuanlin | 2025-08-07T01:39:09Z | first commit for new databases & initial tests (not all working yet) | 1 | UNKNOWN | — |
| 251 | `cec6fd6a3c38e8bb949e402d34caa2aa47f9a9a0` | kuanlinhuang / huangkuanlin | 2025-08-06T22:31:37Z | kuanlinhuang / huangkuanlin | 2025-08-06T22:31:37Z | gitignore update | 1 | FORMAT_ONLY | — |
| 252 | `d4a72633fdb628fe3ed74e42dc0d4e7ed469072e` | serena2z / serena2z | 2025-08-06T19:39:02Z | serena2z / serena2z | 2025-08-06T19:39:02Z | changed software v005.sh | 1 | ENVIRONMENT | — |
| 253 | `eef94cc653a9c6373d968b1e2fee58fb08c41945` | serena2z / serena2z | 2025-08-06T19:38:27Z | serena2z / serena2z | 2025-08-06T19:38:27Z | reverted env | 1 | REMOVAL | — |
| 254 | `2a2b1fe82706cbc8b0fd134af3b824cc32152da4` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-06T10:49:20Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-06T10:49:20Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 255 | `e4e1aedf9860cccbbd7722f2817d51d2c667e71a` | PabloPauling / Pablo Villanueva | 2025-08-06T10:47:31Z | web-flow / GitHub | 2025-08-06T10:47:31Z | Update llm.py | 1 | UNKNOWN | — |
| 256 | `a5eae7428ddd4cc87caae94b997abbd05129b593` | serena2z / Serena Zhang | 2025-08-06T05:35:50Z | web-flow / GitHub | 2025-08-06T05:35:50Z | Merge pull request #128 from snap-stanford/serena2z-patch-1-1 | 2 | MERGE_ONLY | 128 |
| 257 | `2274b480fb9d9cef2299c14d8bad108afd620b8c` | serena2z / Serena Zhang | 2025-08-06T05:35:23Z | web-flow / GitHub | 2025-08-06T05:35:23Z | Merge pull request #127 from snap-stanford/serena2z-patch-1 | 2 | MERGE_ONLY | 127 |
| 258 | `666b67e9a849dc3b69347ef946d5947040e90a93` | serena2z / Serena Zhang | 2025-08-06T05:34:45Z | web-flow / GitHub | 2025-08-06T05:34:45Z | Update new_software_v004.sh | 1 | ENVIRONMENT | — |
| 259 | `a05b1e2f6709d53c0a94fa52fbea501c0c69a161` | serena2z / Serena Zhang | 2025-08-06T05:33:50Z | web-flow / GitHub | 2025-08-06T05:33:50Z | Update environment.yml | 1 | ENVIRONMENT | — |
| 260 | `b0a0412560d98f2a134e0c78944550b4e734dddc` | serena2z / serena2z | 2025-08-06T04:47:37Z | serena2z / serena2z | 2025-08-06T04:47:37Z | set up version 0.0.5 | 1 | ENVIRONMENT | — |
| 261 | `69473fe5956743c87f5110b06a3c85aeace93168` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-06T02:58:13Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-06T02:58:14Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 262 | `2c30bd1069e51ba39032f9448719efe2d3e1d364` | tuln128 / tuln128 | 2025-08-06T02:19:01Z | tuln128 / tuln128 | 2025-08-06T02:19:01Z | Add scripts to autonomously generate Python functions for tasks given task descriptions, using code agent of the backend LLM. | 1 | FEATURE | — |
| 263 | `7b822cd79550b452cdce3742f728e6fcc4e4bc21` | Edison-A-N / Edison-A-N | 2025-08-05T08:53:43Z | Edison-A-N / Edison-A-N | 2025-08-06T00:25:18Z | feat: add streaming output and refactor resource retrieval logic | 1 | FEATURE | — |
| 264 | `2e07080046b4e2fbc4d6ee3d57ace43d21e05bfb` | kexinhuang12345 / Kexin Huang | 2025-08-05T19:15:48Z | web-flow / GitHub | 2025-08-05T19:15:48Z | Merge pull request #123 from zancmeresek/license-tracking | 2 | MERGE_ONLY | 123 |
| 265 | `335fb962f2a620214ea6911096a36023c712b421` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-05T09:15:10Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-05T09:15:10Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 266 | `5be01d8569841ad8db6f47a5f1fc62ad44a2dc4b` | zancmeresek / Žan Cmerešek | 2025-08-05T09:12:10Z | zancmeresek / Žan Cmerešek | 2025-08-05T09:12:10Z | Add initial license tracking table | 1 | FEATURE | — |
| 267 | `f4c3ccae6aa05b754cf342c95366e094575046bd` | serena2z / Serena Zhang | 2025-08-04T06:59:37Z | web-flow / GitHub | 2025-08-04T06:59:37Z | Merge pull request #119 from snap-stanford/dataset/openfda | 2 | MERGE_ONLY | 119 |
| 268 | `ab51d6dfc58958fac785f9dbbce4747b71a21b31` | serena2z / Serena Z | 2025-08-04T06:59:06Z | serena2z / Serena Z | 2025-08-04T06:59:06Z | fixed readme again | 1 | DOC_ONLY | — |
| 269 | `e1c395dfa16cc777a52da2c50968a7f1039efacd` | serena2z / Serena Zhang | 2025-08-04T06:55:58Z | web-flow / GitHub | 2025-08-04T06:55:58Z | Merge pull request #118 from snap-stanford/dataset/openfda | 2 | MERGE_ONLY | 118 |
| 270 | `938226510708552d7f816857a4de64d33f18dec1` | serena2z / Serena Z | 2025-08-04T06:55:38Z | serena2z / Serena Z | 2025-08-04T06:55:38Z | fix readme | 1 | DOC_ONLY | — |
| 271 | `6e86fb04a5afea01cad2e008f51f7d9f4da93438` | serena2z / Serena Zhang | 2025-08-04T06:52:28Z | web-flow / GitHub | 2025-08-04T06:52:28Z | Merge pull request #112 from MinxZ/azure-test | 2 | MERGE_ONLY | 112 |
| 272 | `8b41a1425020dd1f53bb8519205cc11b389fae1d` | serena2z / Serena Z | 2025-08-04T06:51:50Z | serena2z / Serena Z | 2025-08-04T06:51:50Z | Merge remote-tracking branch 'origin/main' into azure-test | 2 | MERGE_ONLY | — |
| 273 | `9e088c684ac54a665ce9e2d3d50a4856fc6e389d` | serena2z / Serena Z | 2025-08-04T06:45:16Z | serena2z / Serena Z | 2025-08-04T06:45:16Z | fixed readme | 1 | DOC_ONLY | — |
| 274 | `7fe59624ba9768c60add405a5870d992dae8e43f` | serena2z / Serena Zhang | 2025-08-04T06:31:06Z | web-flow / GitHub | 2025-08-04T06:31:06Z | Merge pull request #100 from PabloPauling/main | 2 | MERGE_ONLY | 100 |
| 275 | `5102c3458874900be1ca16a8193f2f5ca26bbe77` | serena2z / Serena Zhang | 2025-08-04T06:28:11Z | web-flow / GitHub | 2025-08-04T06:28:11Z | Merge branch 'main' into main | 2 | MERGE_ONLY | — |
| 276 | `f203e2c0e0c7b992991dd1e197df98f308cd17ba` | serena2z / Serena Z | 2025-08-04T06:25:14Z | serena2z / Serena Z | 2025-08-04T06:25:14Z | added deepseek | 1 | FEATURE | — |
| 277 | `d16d2a833688bee324318efd69c5134015243128` | serena2z / Serena Zhang | 2025-08-04T06:04:19Z | web-flow / GitHub | 2025-08-04T06:04:19Z | Update README.md | 1 | DOC_ONLY | — |
| 278 | `e235ba8ed62e4ecef2d2e721d05f7a3e0f861ba2` | serena2z / Serena Zhang | 2025-08-04T05:52:30Z | web-flow / GitHub | 2025-08-04T05:52:30Z | Merge pull request #117 from snap-stanford/dataset/openfda | 2 | MERGE_ONLY | 117 |
| 279 | `a77e12c14d04c7597d04749d166cca370dcf55a0` | serena2z / Serena Z | 2025-08-03T19:35:55Z | serena2z / Serena Z | 2025-08-03T19:35:55Z | precommit check | 1 | UNKNOWN | — |
| 280 | `c96724c6b98d919c80fefc7d6d41ad13981bb4e3` | kexinhuang12345 / Kexin Huang | 2025-08-03T17:03:01Z | web-flow / GitHub | 2025-08-03T17:03:01Z | Delete tutorials/101_biomni.ipynb | 1 | REMOVAL | — |
| 281 | `d81a3e52883384f8c3cc631bd2ac97037e48c494` | kexinhuang12345 / Kexin Huang | 2025-08-03T17:02:17Z | web-flow / GitHub | 2025-08-03T17:02:17Z | Merge pull request #116 from snap-stanford/add_mcp | 2 | MERGE_ONLY | 116 |
| 282 | `d7d57f7a2af18e7f5256c76f8556123646836610` | kexinhuang12345 / Kexin Huang | 2025-08-03T05:19:59Z | web-flow / GitHub | 2025-08-03T05:19:59Z | Merge pull request #76 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 76 |
| 283 | `172235b97adc8475eb55f8186aef7ea0f9f20d4d` | kexinhuang12345 / Kexin Huang | 2025-08-03T05:17:45Z | web-flow / GitHub | 2025-08-03T05:17:45Z | Merge pull request #54 from SnowLightPath/add_mcp | 2 | MERGE_ONLY | 54 |
| 284 | `9c469f21d6739d2bba67883bd04f54cd109cd47d` | kexinhuang12345 / kexinhuang12345 | 2025-08-03T05:16:46Z | kexinhuang12345 / kexinhuang12345 | 2025-08-03T05:16:46Z | add mcp | 1 | FEATURE | — |
| 285 | `87c4ab8881966f629958021ee9f6ceb3fba6ba3f` | kexinhuang12345 / Kexin Huang | 2025-08-03T05:07:52Z | web-flow / GitHub | 2025-08-03T05:07:52Z | Merge pull request #114 from snap-stanford/revert-102-yield_each_message | 2 | MERGE_ONLY | 114 |
| 286 | `142c4dec4f9ad55972a54366b69e81b64e172711` | kexinhuang12345 / Kexin Huang | 2025-08-03T05:07:40Z | web-flow / GitHub | 2025-08-03T05:07:40Z | Revert "yield each message " | 1 | REMOVAL | — |
| 287 | `cb56c2072ef2024599d4022b369a1f1e1c861850` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-03T04:12:43Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-03T04:12:43Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 288 | `d6b9b0a1cbff3ebed758ff435e2384560287c170` | serena2z / Serena Z | 2025-08-03T04:12:21Z | serena2z / Serena Z | 2025-08-03T04:12:21Z | dixed env variable with mcp server creation | 1 | UNKNOWN | — |
| 289 | `8c188c2e3f9b1558729c8d2f9402e7fdb804a0c5` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-02T06:24:12Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-02T06:24:13Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 290 | `2b4adf222f42b6f60187aefd2022ff6d8871e1f3` | MinxZ / MinxZ | 2025-08-02T06:24:01Z | MinxZ / MinxZ | 2025-08-02T06:24:01Z | merge the redme to one | 1 | UNKNOWN | — |
| 291 | `2cdf6186b8ae6282311be22aa9a093fa19644d5b` | kexinhuang12345 / Kexin Huang | 2025-08-02T05:41:29Z | web-flow / GitHub | 2025-08-02T05:41:29Z | Merge pull request #102 from evolu8/yield_each_message | 2 | MERGE_ONLY | 102 |
| 292 | `7f5995f4886d0bf6ed91028b92f65053db368016` | kexinhuang12345 / Kexin Huang | 2025-08-02T05:41:01Z | web-flow / GitHub | 2025-08-02T05:41:01Z | Merge pull request #106 from th86/patch-1 | 2 | MERGE_ONLY | 106 |
| 293 | `54929e400a6ccf6e062cb0e5ee22a9800bbed06f` | kexinhuang12345 / Kexin Huang | 2025-08-02T05:36:32Z | web-flow / GitHub | 2025-08-02T05:36:32Z | Merge pull request #108 from HelloWorldLTY/main | 2 | MERGE_ONLY | 108 |
| 294 | `e61d659ae7e30398ea0a8350ade063c0f09930e8` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-01T06:54:24Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-01T06:54:24Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 295 | `3200852e04251b0718256977c1dd62ccf67d432c` | MinxZ / MinxZ | 2025-08-01T06:47:57Z | MinxZ / MinxZ | 2025-08-01T06:47:57Z | add readme for azure setup | 1 | DOC_ONLY | — |
| 296 | `ea8091b287ae28693d620d42576585d9757b5f2c` | MinxZ / MinxZ | 2025-08-01T06:33:40Z | MinxZ / MinxZ | 2025-08-01T06:33:40Z | add azure support for model_id | 1 | FEATURE | — |
| 297 | `997bba8de716ca792305a56f54d809cc28f54b53` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-01T06:28:14Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-01T06:28:14Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 298 | `9280ce26b4be2c4bd5099084cf6ca8c32c0b951e` | MinxZ / MinxZ | 2025-08-01T06:26:05Z | MinxZ / MinxZ | 2025-08-01T06:26:05Z | install gcc and unzip since some instance like aws ec2 do not originally come with them | 1 | ENVIRONMENT | — |
| 299 | `6122a8320fbddbfb45dc6d4a7754671f7619914e` | HelloWorldLTY / HelloWorldLTY | 2025-07-30T21:14:16Z | web-flow / GitHub | 2025-07-30T21:14:16Z | Update environment.yml | 1 | ENVIRONMENT | — |
| 300 | `d58c9467ab4af42e25f5d2bbb00d6793bbd5e892` | HelloWorldLTY / HelloWorldLTY | 2025-07-30T21:09:17Z | web-flow / GitHub | 2025-07-30T21:09:17Z | fix the error in biomni initialize | 1 | BUG_FIX | — |

## PR mapping and duplicate/lineage notes

- `mapped_to_pr`: 26 records from explicit `Merge pull request` first-line subjects.
- Explicit PRs: `#54`, `#76`, `#100`, `#102`, `#106`, `#108`, `#112`, `#114`, `#116`, `#117`, `#118`, `#119`, `#120`, `#122`, `#123`, `#126`, `#127`, `#128`, `#129`, `#131`, `#139`, `#141`, `#143`, `#144`, `#149`, `#153`.
- All 26 explicit PR mappings on this page are multi-parent merge commits.
- There are 34 multi-parent commits total: the 26 explicit PR merges plus 8 branch/remote/content merges without a PR number in the first line. Treat all 34 as duplicate/sync/lineage surfaces until PR and DAG normalization; do not count them as 34 independent features.
- No duplicate substantive change set was proven in this metadata-only pass. Exact ancestry/patch identity remains for normalization.

## Substantive and feature leads

These are discovery leads, not validated independent features:

- Clinical/evaluation databases: `2bd9f682a4e4f9b608e93c90fa3cfd42b7d1aa4b` ClinicalTrials.gov integration; adjacent TrialBench lineage; broad database/API update series covering ChEMBL, CellxGene, QuickGO, ClinicalTrials, DailyMed, openFDA, UniChem, OLS, and DrugCentral.
- Documentation infrastructure: PR `#149` / `c66f22a4b81f2f2cf79b9938cd1c034eb7f459eb` Sphinx documentation build system.
- LLM/runtime providers: PR `#143` lazy LLM dependency imports; `67fc7ecbcc7194ee5474d2a88e0494ce6ece87a8` Bedrock; `f203e2c0e0c7b992991dd1e197df98f308cd17ba` DeepSeek; PR `#112` Azure plus `ea8091b287ae28693d620d42576585d9757b5f2c`.
- Agentic/code generation: PR `#126` / `2c30bd1069e51ba39032f9448719efe2d3e1d364` autonomous Python-function generation from task descriptions.
- Streaming/resource retrieval: PR `#122` / `7b822cd79550b452cdce3742f728e6fcc4e4bc21`.
- Dataset/license controls: PRs `#141`, `#144`, `#153`; dataset removal for license purposes; PR `#123` / `5be01d8569841ad8db6f47a5f1fc62ad44a2dc4b` license tracking.
- Cancer genomics: `df7e3da59c7d145421f0343b677ee26e3034248b` comprehensive copy-number workflow with CNVkit environment changes.
- MCP: PRs `#54` and `#116`, plus `9c469f21d6739d2bba67883bd04f54cd109cd47d` and MCP configuration/environment fixes.
- Installation resilience: PR `#139` wget/curl fallback.
- Message streaming behavior: PR `#102`, later reverted by PR `#114`; this is an explicit feature/reversion lineage lead.

## Evidence URLs

- Frozen page-3 API query: https://api.github.com/repos/snap-stanford/Biomni/commits?sha=400c1f366b96a35ca253e13c9b06c5076af41d65&per_page=100&page=3
- Frozen page-2 boundary query: https://api.github.com/repos/snap-stanford/Biomni/commits?sha=400c1f366b96a35ca253e13c9b06c5076af41d65&per_page=100&page=2
- Prior boundary commit: https://github.com/snap-stanford/Biomni/commit/9c5eca618b7171092420ad07c9d6e6cd6c22dcc4
- This page first commit: https://github.com/snap-stanford/Biomni/commit/48febfee6fc6433e4fea9c8ca1247981c830195e
- PR pattern (replace number with the explicit IDs above): https://github.com/snap-stanford/Biomni/pull/149

## Uncertainty and unresolved work

- The denominator `487` is parent-verified in canonical commit batch 001; this worker did not independently recalculate it.
- GitHub login absence reflects a null linked account in this API response; signature names are not independently identity-verified here.
- Commit dates are Git author/committer metadata and are not guaranteed to equal public-push time.
- Subject-based classes can be wrong, especially for terse or mixed subjects such as positions 202, 205, 213, 221, 223–227, 235, 241–243, 250, 255, 263, 276, 286, 288, and 290. Diff/PR evidence is required before canonical classification.
- Merge commits and adjacent child commits likely repeat PR lineages; no independent-feature counts should be derived from this page without DAG/PR normalization.
- This task did not audit diffs, licenses, security, runtime correctness, PR state, or feature completeness.

## Next action

Fetch the same frozen commit-list query with `per_page=100&page=4`, preserve newest-first order, verify its boundary after `d58c9467ab4af42e25f5d2bbb00d6793bbd5e892`, and continue the inventory. Keep collection `PARTIAL` until all 487 frozen-DAG commits are processed and API pagination is exhausted.
