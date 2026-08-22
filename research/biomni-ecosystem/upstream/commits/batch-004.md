# Worker Result: commit-index-004

Parent verification: `VERIFIED`. Official API page 4 contains 100 unique SHAs
that exactly match frozen local Git positions 301–400 and order. Metadata fields
are `FACT`; subject-only classifications are `INFERENCE`.

## Task record

- Task ID: `commit-index-004`
- Scope: frozen main commit list, page 4, per_page=100, newest first.
- API response Date header: `Sat, 22 Aug 2026 21:16:55 GMT`
- Processed: 100 records, cumulative positions 301–400 of 487.
- Boundary: first `2cfa88639b623229a907b0339b7d3e7dd8e838f3`; last `9087e42c36998365422e6d5b496e52d75d0e7a8f`.
- Pagination: `PARTIAL`; previous page 3, next/last page 5.
- Safety: static metadata only; no repository code executed.

## Preliminary inventory

| # | Full SHA | Author | Author date | Committer | Committer date | First-line subject | Parents | Preliminary class | PR |
|---:|---|---|---|---|---|---|---:|---|---:|
| 301 | `2cfa88639b623229a907b0339b7d3e7dd8e838f3` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-29T19:39:21Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-29T19:39:22Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 302 | `a252ebc62caaa908de6e2a7dd4c49773d56df30c` | th86 / Tai-Hsien OuYang | 2025-07-29T19:38:22Z | web-flow / GitHub | 2025-07-29T19:38:22Z | Update llm.py to support deepseek | 1 | FEATURE | — |
| 303 | `1e737be102ac231c2af2b55d613c46c7a6fc465d` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-28T18:15:36Z | web-flow / GitHub | 2025-07-28T18:15:36Z | [pre-commit.ci] pre-commit autoupdate | 1 | FORMAT_ONLY | — |
| 304 | `412741a174782b9d84c92b307c149c9f8667973e` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-28T08:05:06Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-28T08:05:07Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 305 | `c652035bcc81951b917d59c628d89a381736d6ed` | serena2z / Serena Z | 2025-07-28T08:04:44Z | serena2z / Serena Z | 2025-07-28T08:04:44Z | added back support for custom tools -- see biomni/tool/example_mcp_tools as before | 2 | MERGE_ONLY | — |
| 306 | `a5541974c5ef4943c949ff15a1bc5ff78ea9a7ef` | serena2z / Serena Z | 2025-07-28T08:01:42Z | serena2z / Serena Z | 2025-07-28T08:01:42Z | added back support for custom tools -- see biomni/tool/example_mcp_tools as before | 1 | FEATURE | — |
| 307 | `9d0533fa13efdae41d19e373a8b3545df1f08f65` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-28T07:51:42Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-28T07:51:42Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 308 | `1285fee1b46992eb74596877590b6403c530f196` | serena2z / Serena Z | 2025-07-28T07:47:33Z | serena2z / Serena Z | 2025-07-28T07:47:33Z | added readme | 1 | DOC_ONLY | — |
| 309 | `a94f841aaf003a66aa3c8c2e16214e8947217792` | serena2z / Serena Z | 2025-07-28T07:26:58Z | serena2z / Serena Z | 2025-07-28T07:26:58Z | Merge remote-tracking branch 'origin/main' into pr-55 | 2 | MERGE_ONLY | — |
| 310 | `36e3f7b73cb975ea05f1d4e3d61e1dd401679dd3` | serena2z / Serena Z | 2025-07-28T07:26:46Z | serena2z / Serena Z | 2025-07-28T07:26:46Z | changed mcp to external servers w/o defining tools | 1 | FEATURE | — |
| 311 | `6afa5c1a2be1aeadbfa48b8cf935b087b70af00c` | kexinhuang12345 / Kexin Huang | 2025-07-27T16:41:25Z | web-flow / GitHub | 2025-07-27T16:41:25Z | Merge pull request #103 from snap-stanford/kexinhuang12345-patch-1 | 2 | MERGE_ONLY | 103 |
| 312 | `2e5077d7bcf7d64564d0bc23cc76ce02b19d58d1` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-27T16:38:59Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-27T16:39:00Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 313 | `a04f34ef037e03385c496a40aded91c56412d8a2` | kexinhuang12345 / Kexin Huang | 2025-07-27T16:38:50Z | web-flow / GitHub | 2025-07-27T16:38:50Z | update database query function contribution | 1 | FEATURE | — |
| 314 | `b677959799db7482ec78b36164d974641bc1af8f` | evolu8 / evolu8 | 2025-07-27T15:23:22Z | web-flow / GitHub | 2025-07-27T15:23:22Z | Update a1.py | 1 | UNKNOWN | — |
| 315 | `fecc156da47a7ad66b7f8e875d20d1f73bb7427f` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-26T20:35:11Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-26T20:35:12Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 316 | `30cb04a4ac3b0df04106ea36231060cfd664eeaf` | PabloPauling / PabloPauling | 2025-07-26T20:23:46Z | PabloPauling / PabloPauling | 2025-07-26T20:23:46Z | Update README.md | 1 | DOC_ONLY | — |
| 317 | `53cf174a6947534eb876512a39bcd9ec5aa63bc2` | PabloPauling / PabloPauling | 2025-07-26T20:23:39Z | PabloPauling / PabloPauling | 2025-07-26T20:23:39Z | Update llm.py | 1 | UNKNOWN | — |
| 318 | `2d4326ee00fd8fa336f8812a2cbf6a0e7bf1a863` | PabloPauling / PabloPauling | 2025-07-26T20:22:40Z | PabloPauling / PabloPauling | 2025-07-26T20:22:40Z | Update a1.py | 1 | UNKNOWN | — |
| 319 | `36a7407c635ecd9e04710a64a7748c9d383bb1a2` | PabloPauling / PabloPauling | 2025-07-26T20:07:47Z | PabloPauling / PabloPauling | 2025-07-26T20:07:47Z | Update llm.py | 1 | UNKNOWN | — |
| 320 | `2984f7d564688bc208207b9fd158be35bf71d266` | PabloPauling / PabloPauling | 2025-07-26T19:42:00Z | PabloPauling / PabloPauling | 2025-07-26T19:42:00Z | Update a1.py | 1 | UNKNOWN | — |
| 321 | `da73e7c408a9cd349dfe155e7fbbe746485c2cc0` | PabloPauling / PabloPauling | 2025-07-26T19:36:06Z | PabloPauling / PabloPauling | 2025-07-26T19:36:06Z | Update llm.py | 1 | UNKNOWN | — |
| 322 | `693c0364c4a5eb4c40e5b8327ad34bba5ebe7c19` | PabloPauling / PabloPauling | 2025-07-26T19:31:22Z | PabloPauling / PabloPauling | 2025-07-26T19:31:22Z | Update llm.py | 1 | UNKNOWN | — |
| 323 | `92ad3ef1233bc4284350cf6564a38655e2489118` | PabloPauling / PabloPauling | 2025-07-26T19:25:30Z | PabloPauling / PabloPauling | 2025-07-26T19:25:30Z | Update llm.py | 1 | UNKNOWN | — |
| 324 | `8df459e479c6493add991c0e5a2a2a1c7695825e` | PabloPauling / PabloPauling | 2025-07-26T19:21:10Z | PabloPauling / PabloPauling | 2025-07-26T19:21:10Z | Update llm.py | 1 | UNKNOWN | — |
| 325 | `64cf9f48da0f2990dfcf576de0675cc0f97e5852` | PabloPauling / PabloPauling | 2025-07-26T19:10:14Z | PabloPauling / PabloPauling | 2025-07-26T19:10:14Z | Update llm.py | 1 | UNKNOWN | — |
| 326 | `a7d88fc9da597f2c9839aec4d4338668fd1eb567` | kexinhuang12345 / Kexin Huang | 2025-07-26T17:34:06Z | web-flow / GitHub | 2025-07-26T17:34:06Z | Merge pull request #86 from HasanAldhahi/fix_react_agent | 2 | MERGE_ONLY | 86 |
| 327 | `50b64f5ff6a0413ac9b44bbc09d403359d2cd7d3` | kexinhuang12345 / Kexin Huang | 2025-07-26T17:33:42Z | web-flow / GitHub | 2025-07-26T17:33:42Z | Merge pull request #97 from PabloPauling/main | 2 | MERGE_ONLY | 97 |
| 328 | `225c635f6bc3445fe7733e39eb7aafd46ec266e8` | kexinhuang12345 / Kexin Huang | 2025-07-26T17:32:02Z | web-flow / GitHub | 2025-07-26T17:32:02Z | Merge pull request #94 from Edison-A-N/fix/self-critic-variable-conflict | 2 | MERGE_ONLY | 94 |
| 329 | `e4be55c2fc0dcb3ae1d99e23d49a3021217cf9d6` | serena2z / Serena Zhang | 2025-07-26T07:48:42Z | web-flow / GitHub | 2025-07-26T07:48:42Z | Merge pull request #98 from snap-stanford/feature/add-datasets | 2 | MERGE_ONLY | 98 |
| 330 | `55ed5c0881986477a5a6afaf939955e1131361dd` | serena2z / serena2z | 2025-07-26T07:47:58Z | serena2z / serena2z | 2025-07-26T07:47:58Z | added sgRNA datasets | 1 | FEATURE | — |
| 331 | `203f9ed61a5c3909001de1c8b944d742d3934993` | PabloPauling / Pablo Villanueva | 2025-07-26T07:12:13Z | web-flow / GitHub | 2025-07-26T07:12:13Z | Update README.md | 1 | DOC_ONLY | — |
| 332 | `8f83e84d5608504ac21a555b62b691038c5a1d27` | serena2z / Serena Zhang | 2025-07-25T23:19:06Z | web-flow / GitHub | 2025-07-25T23:19:06Z | Merge pull request #82 from marcosbolanos/feature/add-depmap-data | 2 | MERGE_ONLY | 82 |
| 333 | `25543550d941d49224d0a0dddf7ee35a41d41ce6` | serena2z / Serena Zhang | 2025-07-25T23:05:31Z | web-flow / GitHub | 2025-07-25T23:05:31Z | Merge pull request #74 from PabloPauling/main | 2 | MERGE_ONLY | 74 |
| 334 | `a6636b7de0f38ef066034b62ec3ea42e61d56773` | serena2z / serena2z | 2025-07-25T23:03:16Z | serena2z / serena2z | 2025-07-25T23:03:16Z | added comment | 1 | FEATURE | — |
| 335 | `c60be60ed11437253f2acc5e801e24fd6cdef96d` | serena2z / serena2z | 2025-07-25T22:54:43Z | serena2z / serena2z | 2025-07-25T22:54:43Z | Merge remote-tracking branch 'origin/main' into pr-74 | 2 | MERGE_ONLY | — |
| 336 | `ba9aa3b76d2b72f24714c3afb43a9493ea83e881` | serena2z / Serena Zhang | 2025-07-25T22:50:02Z | web-flow / GitHub | 2025-07-25T22:50:02Z | Merge pull request #96 from snap-stanford/pr-79 | 2 | MERGE_ONLY | 96 |
| 337 | `51d8a6ba0f08d3a3e339c861365e96f6ee0a7cae` | serena2z / Serena Zhang | 2025-07-25T22:49:24Z | web-flow / GitHub | 2025-07-25T22:49:24Z | Merge pull request #79 from lxasqjc/feat/monarch-integration | 2 | MERGE_ONLY | 79 |
| 338 | `5c9445d83b7edc1089ef14605721f1990c030378` | serena2z / serena2z | 2025-07-25T22:43:53Z | serena2z / serena2z | 2025-07-25T22:43:53Z | add database description | 1 | FEATURE | — |
| 339 | `eaf2d7603fe0db5d9a6e41859f9db6bb44216924` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-25T22:37:16Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-25T22:37:16Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 340 | `733c610c2df89285d328146e8fb893bcdd323fa8` | serena2z / serena2z | 2025-07-25T22:35:41Z | serena2z / serena2z | 2025-07-25T22:35:41Z | Merge remote-tracking branch 'origin/main' into pr-79 | 2 | MERGE_ONLY | — |
| 341 | `019f99ac68f64a3712408e7e0afaa45ea5349341` | serena2z / serena2z | 2025-07-25T22:35:32Z | serena2z / serena2z | 2025-07-25T22:35:32Z | fixed monarch api | 1 | BUG_FIX | — |
| 342 | `e3ee8cb1c21ff8dc11495a49e3383c25e057540a` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-25T08:57:18Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-25T08:57:19Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 343 | `3c6c08267b5004ab39d20e5800c04bc680681bd3` | Edison-A-N / Edison-A-N | 2025-07-25T08:49:56Z | Edison-A-N / Edison-A-N | 2025-07-25T08:49:56Z | fix: resolve variable name conflict in self_critic implementation | 1 | BUG_FIX | — |
| 344 | `f9a5b9542702d42e48aa2c77c1d66fd1be4ff597` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-23T11:02:57Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-23T11:02:57Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 345 | `e63d7a7b85cb0bc0d220f97fd6f183eb92ab37c1` | HasanAldhahi / Hasan Aldhahi | 2025-07-23T11:00:23Z | HasanAldhahi / Hasan Aldhahi | 2025-07-23T11:00:23Z | solved self.prompt and self.system_prompt not defined | 1 | UNKNOWN | — |
| 346 | `2d9784be989daaaa092fba3ca4964cb503714094` | kexinhuang12345 / Kexin Huang | 2025-07-23T05:44:57Z | web-flow / GitHub | 2025-07-23T05:44:57Z | Update README.md | 1 | DOC_ONLY | — |
| 347 | `33cee4e38e8c18e435d82a7b233af2c3ea6f2a83` | kexinhuang12345 / Kexin Huang | 2025-07-23T05:44:38Z | web-flow / GitHub | 2025-07-23T05:44:38Z | Update README.md | 1 | DOC_ONLY | — |
| 348 | `e2994af0014a7f9453af606968214315c29f44e6` | serena2z / Serena Zhang | 2025-07-22T20:32:24Z | web-flow / GitHub | 2025-07-22T20:32:24Z | Merge pull request #84 from snap-stanford/fix_environment | 2 | MERGE_ONLY | 84 |
| 349 | `593b680cd16a69254129d6f9502ce360d8678b82` | serena2z / serena2z | 2025-07-22T20:27:30Z | serena2z / serena2z | 2025-07-22T20:27:30Z | added readme for package conflicts | 1 | DOC_ONLY | — |
| 350 | `c22e0413bbd10acad043229c769a348ea144e5fc` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-22T17:57:06Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-22T17:57:06Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 351 | `62940c152b5be455f3336fdf6efe2c9dd0b21173` | marcosbolanos / marcosbolanos | 2025-07-22T17:19:13Z | marcosbolanos / marcosbolanos | 2025-07-22T17:19:13Z | added depmap data for whole genome crispr screens, gene dependency and gene expression in cancer cell lines, as well as the data model | 1 | DEPENDENCY_ONLY | — |
| 352 | `34be78ba40abb0b56d7586b715c1472b5f58a785` | PabloPauling / Pablo Villanueva | 2025-07-22T12:47:14Z | web-flow / GitHub | 2025-07-22T12:47:14Z | Merge branch 'main' into main | 2 | MERGE_ONLY | — |
| 353 | `b2f9835bd28abcfd0936af637acf7f1a053751bb` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-22T08:59:44Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-22T08:59:44Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 354 | `7c0cae2c19a41092f8957fdf163ffc21e564b7ce` | lxasqjc / lxasqjc | 2025-07-22T08:47:52Z | lxasqjc / lxasqjc | 2025-07-22T08:47:52Z | Add Monarch Initiative integration as a first-class data source | 1 | FEATURE | — |
| 355 | `85e6dc9ed568b976da99ce7b84414f2324ba0baa` | serena2z / Serena Zhang | 2025-07-22T06:21:10Z | web-flow / GitHub | 2025-07-22T06:21:10Z | Merge pull request #77 from snap-stanford/fix_environment | 2 | MERGE_ONLY | 77 |
| 356 | `b0576d17510dd265621d2c977b78ce973d5c0db9` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-22T05:13:48Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-22T05:13:48Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 357 | `d05f5fda5dd2ba5bf338cf216448e8d7122184dd` | SnowLightPath / SnowLightPath | 2025-07-22T05:12:37Z | web-flow / GitHub | 2025-07-22T05:12:37Z | Merge branch 'main' into add_mcp | 2 | MERGE_ONLY | — |
| 358 | `0506666ad3b32b73556aad58a89201430503b5e9` | SnowLightPath / SnowLightPath | 2025-07-22T05:10:35Z | SnowLightPath / SnowLightPath | 2025-07-22T05:10:35Z | move mcp_tools to example_mcp_tools for clarity and organization | 1 | FEATURE | — |
| 359 | `a781f2bc9a0daa881427cc7532d555e64b4d14e5` | serena2z / Serena Zhang | 2025-07-22T04:18:38Z | web-flow / GitHub | 2025-07-22T04:18:38Z | Merge pull request #70 from SnowLightPath/dotenv | 2 | MERGE_ONLY | 70 |
| 360 | `23ecd338479e81235bdbe6cafe4a33d0b2dcf29d` | serena2z / Serena Zhang | 2025-07-22T04:07:31Z | web-flow / GitHub | 2025-07-22T04:07:31Z | Merge pull request #68 from PLippmann/grounding-integration | 2 | MERGE_ONLY | 68 |
| 361 | `0274ebcb3b5d97fdb81ca9dffbeb6c6f6d60107e` | serena2z / serena2z | 2025-07-21T23:38:10Z | serena2z / serena2z | 2025-07-21T23:38:10Z | remove unused functions | 1 | REMOVAL | — |
| 362 | `421eba3cc79739783a3ecd1404526f155ea28f46` | serena2z / serena2z | 2025-07-21T23:28:55Z | serena2z / serena2z | 2025-07-21T23:28:55Z | Merge remote-tracking branch 'origin/main' into pr-68 | 2 | MERGE_ONLY | — |
| 363 | `c25279f1789bf64b917b3b9447727b55cbe11777` | serena2z / serena2z | 2025-07-21T23:14:46Z | serena2z / serena2z | 2025-07-21T23:14:46Z | fix aws bedrock dependency | 1 | DEPENDENCY_ONLY | — |
| 364 | `7a5c7cb5e87f36f280923d633cb6b3a52bee1c1c` | PabloPauling / PabloPauling | 2025-07-21T12:52:25Z | PabloPauling / PabloPauling | 2025-07-21T12:52:25Z | Update README.md | 1 | DOC_ONLY | — |
| 365 | `b1cd492a39e225c69b6aa6eeda54c3fe5d54ee0b` | PabloPauling / PabloPauling | 2025-07-21T12:49:25Z | PabloPauling / PabloPauling | 2025-07-21T12:49:25Z | Update llm.py | 1 | UNKNOWN | — |
| 366 | `aa7efd4ea7d819f4978aafbd54f20ccf25c4275b` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-19T12:29:10Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-19T12:29:11Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 367 | `e4641c6b86bdde21d67395719a2226eaefc44458` | SnowLightPath / SnowLightPath | 2025-07-19T12:19:19Z | SnowLightPath / SnowLightPath | 2025-07-19T12:19:19Z | feat: add dotenv support for environment configuration with .env file | 1 | ENVIRONMENT | — |
| 368 | `b41c541a94e4f02156c6b4fd88a4739b5bda6571` | SnowLightPath / SnowLightPath | 2025-07-19T12:06:37Z | SnowLightPath / SnowLightPath | 2025-07-19T12:06:37Z | typo | 1 | DOC_ONLY | — |
| 369 | `b9cb4a84553d85b9aef6ef06ba370afd20f621e1` | SnowLightPath / SnowLightPath | 2025-07-19T01:39:05Z | SnowLightPath / SnowLightPath | 2025-07-19T01:39:05Z | Fixed type annotations in tooluniverse_mcp.py | 1 | BUG_FIX | — |
| 370 | `d4c1efc81594463672590c3c3b7bfb14779b4df6` | SnowLightPath / SnowLightPath | 2025-07-19T01:35:33Z | SnowLightPath / SnowLightPath | 2025-07-19T01:35:33Z | Updated Jupyter notebook with ToolUniverse MCP usage and config file overview | 1 | FEATURE | — |
| 371 | `916eb96b68033bdfac906cf457f78138080302e4` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-19T01:24:39Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-19T01:24:39Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 372 | `48315f15fb1ff32c0d3e71166ff7a4ab95fa25ec` | SnowLightPath / SnowLightPath | 2025-07-19T01:24:29Z | web-flow / GitHub | 2025-07-19T01:24:29Z | Merge branch 'main' into add_mcp | 2 | MERGE_ONLY | — |
| 373 | `f1451aa2b47cca079743e5926e7a90d9754ce712` | SnowLightPath / SnowLightPath | 2025-07-19T01:18:43Z | SnowLightPath / SnowLightPath | 2025-07-19T01:18:43Z | Activated all 214 functions provided by ToolUniverse | 1 | FEATURE | — |
| 374 | `7a05446d80ad6cb8bfa1c9a20051f59607a072d5` | serena2z / Serena Zhang | 2025-07-18T17:19:15Z | web-flow / GitHub | 2025-07-18T17:19:15Z | Merge pull request #69 from snap-stanford/fix_environment | 2 | MERGE_ONLY | 69 |
| 375 | `174ac3ebdfe86c1b2ba4b62422dc44b710eaa30c` | serena2z / serena2z | 2025-07-18T17:14:57Z | serena2z / serena2z | 2025-07-18T17:14:57Z | fix environment dependency issues | 1 | DEPENDENCY_ONLY | — |
| 376 | `788d02f624b45f0d1450a975d14d701e55ee1274` | PLippmann / PLippmann | 2025-07-18T16:57:22Z | PLippmann / PLippmann | 2025-07-18T16:57:22Z | Fixed the import stuff | 1 | BUG_FIX | — |
| 377 | `081ec1962a093080f916dba79cce423386dc7a36` | PLippmann / PLippmann | 2025-07-18T16:21:05Z | PLippmann / PLippmann | 2025-07-18T16:21:05Z | OpenFDA integration | 1 | FEATURE | — |
| 378 | `7147aba40bd6215ac6a9fae50f8b19f8e270fd79` | serena2z / serena2z | 2025-07-18T05:17:55Z | serena2z / serena2z | 2025-07-18T05:17:55Z | fix environment | 1 | BUG_FIX | — |
| 379 | `a3ffd368d2d8691874c06ba2677bcb773e4f1403` | serena2z / serena2z | 2025-07-18T04:52:52Z | serena2z / serena2z | 2025-07-18T04:54:50Z | Add MCP server support for Biomni tool functions | 1 | FEATURE | — |
| 380 | `b6a994763ab00d4f6138afffe5f3478499ae653c` | SnowLightPath / SnowLightPath | 2025-07-18T03:25:48Z | SnowLightPath / SnowLightPath | 2025-07-18T03:25:48Z | Fix MCP server development guide for Jupyter notebooks | 1 | DOC_ONLY | — |
| 381 | `bc44473d2eb4b721e76e61d21c4508d77f4d4520` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-18T03:15:48Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-18T03:15:48Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 382 | `6970107ab4e9bcdbdba1f1d4718f53f3bffdd196` | SnowLightPath / SnowLightPath | 2025-07-18T03:15:18Z | SnowLightPath / SnowLightPath | 2025-07-18T03:15:18Z | Add MCP server development guide for Jupyter notebooks | 1 | DOC_ONLY | — |
| 383 | `50309d2777fb84e75fe663212e26464665485c59` | SnowLightPath / SnowLightPath | 2025-07-18T03:15:08Z | SnowLightPath / SnowLightPath | 2025-07-18T03:15:08Z | Add tooluniverse dependencies to environment | 1 | DEPENDENCY_ONLY | — |
| 384 | `8bd8c03f9df5d24c15da99968a1380871e0231f0` | serena2z / serena2z | 2025-07-18T02:20:12Z | serena2z / serena2z | 2025-07-18T02:20:12Z | added mcp package to environment | 1 | ENVIRONMENT | — |
| 385 | `8852bf26cb648b879176aabff4a1cca6b34646d1` | serena2z / serena2z | 2025-07-18T01:02:33Z | serena2z / serena2z | 2025-07-18T01:02:33Z | Merge remote-tracking branch 'origin/main' into pr-54 | 2 | MERGE_ONLY | — |
| 386 | `2198f9d805446f0b12a6329a668c88b6560bcb4e` | serena2z / serena2z | 2025-07-18T01:01:08Z | serena2z / serena2z | 2025-07-18T01:01:08Z | moving mcp tools to own folder | 1 | FEATURE | — |
| 387 | `a739d417c5ab7917b6a0a55cc95772327f561753` | serena2z / Serena Zhang | 2025-07-17T22:54:25Z | web-flow / GitHub | 2025-07-17T22:54:25Z | Merge pull request #42 from MintaYLu/main | 2 | MERGE_ONLY | 42 |
| 388 | `5fe31c81b1f9079e851336039dd0699a2b80cc04` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-17T22:54:11Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-17T22:54:11Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 389 | `3221be102fe40c5e4aeecf1355f89f2efa18ede8` | serena2z / serena2z | 2025-07-17T22:53:22Z | serena2z / serena2z | 2025-07-17T22:53:22Z | added hyperimpute package, removed tool for now | 2 | MERGE_ONLY | — |
| 390 | `4f0b47a157c23bfcca28ab1cafc9b9438a403534` | serena2z / Serena Zhang | 2025-07-17T22:38:57Z | web-flow / GitHub | 2025-07-17T22:38:57Z | Merge pull request #34 from Ginylil/feature/add-details-md | 2 | MERGE_ONLY | 34 |
| 391 | `6ef021d9d0184fb08d79288cd04c5a0650567d53` | serena2z / Serena Zhang | 2025-07-17T22:24:27Z | web-flow / GitHub | 2025-07-17T22:24:27Z | Merge pull request #55 from zskylarli/panhuman-azimuth | 2 | MERGE_ONLY | 55 |
| 392 | `6b6c43f0e20275f46184cda02dcf157681cd99c3` | serena2z / Serena Zhang | 2025-07-17T22:23:34Z | web-flow / GitHub | 2025-07-17T22:23:34Z | Merge branch 'main' into panhuman-azimuth | 2 | MERGE_ONLY | — |
| 393 | `d7f041b16e6bb024f2b3b8c6979d1fb4d1ec8ca3` | serena2z / serena2z | 2025-07-17T22:20:28Z | serena2z / serena2z | 2025-07-17T22:20:28Z | created separate env for panhumanpy due to dependency conflicts with biomni_e1 | 1 | DEPENDENCY_ONLY | — |
| 394 | `04ffc79369cf57882caacda8a60d5e7e5cc3dee8` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-17T15:36:09Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-17T15:36:10Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 395 | `9f42c4e54bd8928a462c19c5d30b4bdc732d70a0` | SnowLightPath / SnowLightPath | 2025-07-17T15:35:50Z | SnowLightPath / SnowLightPath | 2025-07-17T15:35:50Z | Add MCP support documentation to README | 1 | DOC_ONLY | — |
| 396 | `89e30337fc4d895d50bec1f04971c5ca47017955` | SnowLightPath / SnowLightPath | 2025-07-17T15:29:40Z | SnowLightPath / SnowLightPath | 2025-07-17T15:29:40Z | Add comprehensive FDA tools to ToolUniverse MCP server | 1 | FEATURE | — |
| 397 | `4199f7870ad2ad543571ae1e6b6cd86f859c32eb` | kexinhuang12345 / Kexin Huang | 2025-07-17T05:32:13Z | web-flow / GitHub | 2025-07-17T05:32:13Z | Merge pull request #60 from snap-stanford/readme_security | 2 | MERGE_ONLY | 60 |
| 398 | `df75368aa2da7f50689f7ec3f65a0000229bc643` | kexinhuang12345 / kexinhuang12345 | 2025-07-17T05:31:47Z | kexinhuang12345 / kexinhuang12345 | 2025-07-17T05:31:47Z | update security | 1 | SECURITY | — |
| 399 | `1f62105bee02cafbcc454fe6a7fafb2654ef0b95` | kexinhuang12345 / Kexin Huang | 2025-07-17T05:21:58Z | web-flow / GitHub | 2025-07-17T05:21:58Z | Merge pull request #59 from snap-stanford/fix_parsing_error | 2 | MERGE_ONLY | 59 |
| 400 | `9087e42c36998365422e6d5b496e52d75d0e7a8f` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-17T05:21:49Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-17T05:21:49Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |

## Batch summary

- Unique SHAs: `100`.
- Multi-parent surfaces: `30`.
- Explicit subject-to-PR mappings: `19`.
- PR numbers: `#103, #86, #97, #94, #98, #82, #74, #96, #79, #84, #77, #70, #68, #69, #42, #34, #55, #60, #59`.
- Classification counts: `{"BUG_FIX":5,"DEPENDENCY_ONLY":5,"DOC_ONLY":11,"ENVIRONMENT":2,"FEATURE":15,"FORMAT_ONLY":18,"MERGE_ONLY":30,"REMOVAL":1,"SECURITY":1,"UNKNOWN":12}`.

Merge and PR surfaces are not independent features. Exact change identity, patch
equivalence, security, license, and feature decomposition remain pending.

## Evidence

- https://api.github.com/repos/snap-stanford/Biomni/commits?sha=400c1f366b96a35ca253e13c9b06c5076af41d65&per_page=100&page=4
- First commit: https://github.com/snap-stanford/Biomni/commit/2cfa88639b623229a907b0339b7d3e7dd8e838f3
- Last commit: https://github.com/snap-stanford/Biomni/commit/9087e42c36998365422e6d5b496e52d75d0e7a8f

## Next action

Index page 5 and mark the collection complete only if its 87 records match the
remaining frozen DAG positions and the API exposes no next page.
