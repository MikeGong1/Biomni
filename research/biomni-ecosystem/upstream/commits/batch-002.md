# Worker Result: commit-index-002

Parent verification: `VERIFIED` at `2026-08-22T20:57:48Z`. Frozen local Git
positions 101–200 match all 100 worker SHAs and boundaries. The page contains 29
multi-parent commits, 20 explicit merge-PR subjects, and three single-parent PR
subjects. Classes remain subject-only `INFERENCE` pending normalization.

## Task record

- Task ID: `commit-index-002`
- Scope: official `snap-stanford/Biomni` commit-list API, frozen `main` baseline `400c1f366b96a35ca253e13c9b06c5076af41d65`, page `2`, `per_page=100`, deterministic API order (newest first).
- Status: `PARTIAL`
- Observed at UTC: `2026-08-22T20:45:43Z` (GitHub response `Date` header).
- Processed this batch: `100` commit records, cumulative positions 101–200 inclusive.
- Global frozen-DAG denominator: `487` commits (parent-verified local frozen DAG; supplied by coordinator).
- Boundary: prior batch last `899eefb22a5a102fd81f1d845490b4b83fee3402`; this batch first `3371e3207dc8e63887d3cd3904243678c737334e`; this batch last `9c5eca618b7171092420ad07c9d6e6cd6c22dcc4`.
- Safety: metadata-only inventory; no repository code, workflow, script, package, or external instruction was executed.

## Pagination and boundary evidence

- GitHub returned HTTP 200 and exactly 100 objects.
- The response `Link` header gave `rel="prev"` and `rel="first"` at page 1, `rel="next"` at page 3, and `rel="last"` at page 5 for the same frozen SHA and `per_page=100` query.
- Batch 001 ended at API position 100 with `899eefb22a5a102fd81f1d845490b4b83fee3402`; page 2 begins at API position 101 with `3371e3207dc8e63887d3cd3904243678c737334e`. The page-2 `prev=1` link and exact page arrays establish the pagination boundary; this does not assert a direct parent-child edge between those two commits.
- Processed cumulatively: `200 / 487`.
- Pagination: `PARTIAL`; next page: `3`.

## Preliminary inventory

`Author` and `Committer` are shown as `GitHub login / commit-signature name`. `—` means GitHub did not expose a linked public account in this response. Classification is preliminary and derives only from parent count plus the first-line subject; it uses the permitted taxonomy and is not a diff audit. Every multi-parent record is provisionally `MERGE_ONLY`. `PR` is populated only where the first-line subject explicitly names one.

| # | Full SHA | Author | Author date | Committer | Committer date | First-line subject | Parents | Preliminary class | PR |
|---:|---|---|---|---|---|---|---:|---|---:|
| 101 | `3371e3207dc8e63887d3cd3904243678c737334e` | serena2z / Serena Zhang | 2025-09-25T22:18:20Z | web-flow / GitHub | 2025-09-25T22:18:20Z | Merge pull request #205 from igor-sadalski/protein_ESM_embeddings | 2 | MERGE_ONLY | 205 |
| 102 | `b8c6d0d8a35ce1918c0574fe30d00d6dbe8dad40` | serena2z / Serena Z | 2025-09-25T22:17:51Z | serena2z / Serena Z | 2025-09-25T22:17:51Z | changed package import and saving mechanism | 2 | MERGE_ONLY | — |
| 103 | `426072361f0ed991811a270f8998ed8451f3bc31` | serena2z / Serena Zhang | 2025-09-25T21:42:09Z | web-flow / GitHub | 2025-09-25T21:42:09Z | Merge pull request #204 from igor-sadalski/interspecies_gene_name_conversions | 2 | MERGE_ONLY | 204 |
| 104 | `2a14feea919218ade6e727f915d79d69a2888fe1` | serena2z / Serena Z | 2025-09-24T22:38:02Z | serena2z / Serena Z | 2025-09-24T22:38:02Z | removed test/log and generator files | 2 | MERGE_ONLY | — |
| 105 | `a54809070b6e4695d82bc96913f5b38579270176` | serena2z / Serena Z | 2025-09-24T22:36:48Z | serena2z / Serena Z | 2025-09-24T22:36:48Z | removed test/log and generator files | 1 | REMOVAL | — |
| 106 | `ee05130dc1634636d6e4a341980b42f5134b162e` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-24T22:33:18Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-24T22:33:18Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 107 | `3e0c7ed0430f85b5f9934a20a25c63d562029895` | serena2z / Serena Z | 2025-09-24T22:32:59Z | serena2z / Serena Z | 2025-09-24T22:32:59Z | removed cellxgene and merged with main | 2 | MERGE_ONLY | — |
| 108 | `9bcb417990d28ec822e6b6646263acab66a0a84a` | — / Igor Sadalski | 2025-09-24T12:28:58Z | — / Igor Sadalski | 2025-09-24T12:28:58Z | frix merge issue | 2 | MERGE_ONLY | — |
| 109 | `15d19be4f9108695ce2ccc19ef95c36a20add8f7` | — / Igor Sadalski | 2025-09-24T12:26:32Z | — / Igor Sadalski | 2025-09-24T12:26:32Z | Update pre-commit hooks to latest versions: biome-format to v2.2.3 and ruff-check to v0.12.12 | 1 | FORMAT_ONLY | — |
| 110 | `356fe0f8232f8e2433254e4a313c9d275fddae0b` | — / Igor Sadalski | 2025-09-24T12:20:09Z | — / Igor Sadalski | 2025-09-24T12:20:09Z | Test commit without pre-commit hooks | 2 | MERGE_ONLY | — |
| 111 | `18ca5618d2b55381394bb66d4fac850b26e4ee58` | serena2z / Serena Z | 2025-09-24T07:22:16Z | serena2z / Serena Z | 2025-09-24T07:22:16Z | dynamically pulling from commit hash 106aef9c8699ceb826d8c9c894eba304a082f24d | 1 | ENVIRONMENT | — |
| 112 | `9fd21137a5855f0c7bd2fac33941d38f9cb14c09` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-23T19:21:41Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-23T19:21:42Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 113 | `d811aba230369ba4e24b32ad799ce8c13785c618` | — / Minta | 2025-09-23T18:59:42Z | — / Minta | 2025-09-23T19:21:18Z | Add bio-imaging registration | 1 | FEATURE | — |
| 114 | `27ae81ad4e3b95c14d11290ecd907ac3b954c33d` | — / Minta | 2025-08-03T18:39:30Z | — / Minta | 2025-09-23T19:21:16Z | bioimaging support with nnunet | 1 | FEATURE | — |
| 115 | `9b43c3420715b5c973f1c5c78c52738e4f567911` | — / Igor Sadalski | 2025-09-23T01:30:27Z | — / Igor Sadalski | 2025-09-23T01:30:27Z | Merge branch 'download_pdf_of_research' of https://github.com/igor-sadalski/Biomni into download_pdf_of_research | 2 | MERGE_ONLY | — |
| 116 | `133be3fbcb9ad757c5d2e77ab49dd72a4320e0d4` | — / Igor Sadalski | 2025-09-23T00:31:18Z | — / Igor Sadalski | 2025-09-23T00:31:18Z | change print in how we save the figures | 1 | UNKNOWN | — |
| 117 | `661b71e9095ac919f05d78f3e5c89c7547c5437f` | — / Igor Sadalski | 2025-09-23T00:28:46Z | — / Igor Sadalski | 2025-09-23T00:28:46Z | add fix to pass the precomitt hooks | 1 | BUG_FIX | — |
| 118 | `f2b28297e742cb403863126602167620870e829f` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-23T00:11:04Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-23T00:11:05Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 119 | `ed13e6e4fc06eaa5844b49a119b1776d8d65ca20` | — / Igor Sadalski | 2025-09-23T00:04:20Z | — / Igor Sadalski | 2025-09-23T00:04:20Z | save just the pdf | 1 | UNKNOWN | — |
| 120 | `4937c74da611daa1263815db3184729a0b92cdca` | — / Igor Sadalski | 2025-09-22T20:06:59Z | — / Igor Sadalski | 2025-09-22T20:06:59Z | add better function descriptions | 1 | DOC_ONLY | — |
| 121 | `ddbf8e76e76e3448116060e0970d028aa6a56b62` | — / Igor Sadalski | 2025-09-22T19:50:45Z | — / Igor Sadalski | 2025-09-22T19:50:45Z | add back removed emojis but don't include them in final PDF conversion pipline | 1 | FEATURE | — |
| 122 | `17df36c8c1541b01e61717536682a28902268f8a` | — / Igor Sadalski | 2025-09-22T19:33:30Z | — / Igor Sadalski | 2025-09-22T19:33:30Z | remove the plan text | 1 | REMOVAL | — |
| 123 | `638cdc934a8868bb19427b85a924b739025902fa` | — / Igor Sadalski | 2025-09-22T19:29:24Z | — / Igor Sadalski | 2025-09-22T19:29:24Z | fix bug where the observation tags were not parsed properly | 1 | BUG_FIX | — |
| 124 | `c54ecaafb13506734c5067ac281df8506fd4767e` | — / Igor Sadalski | 2025-09-22T19:18:45Z | — / Igor Sadalski | 2025-09-22T19:18:45Z | refactor code moving more content to the utils.py | 1 | REFACTOR | — |
| 125 | `c61c112d51a6997c79f912467453211c4e6537fd` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-22T18:39:59Z | web-flow / GitHub | 2025-09-22T18:39:59Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 126 | `629f514e44b759adedc58198f35c3c662da5951d` | — / Igor Sadalski | 2025-09-22T02:07:31Z | — / Igor Sadalski | 2025-09-22T02:07:31Z | add LLM parsin error | 1 | FEATURE | — |
| 127 | `51aef50f6030c6c11e169e486f97073265118685` | — / Igor Sadalski | 2025-09-22T01:56:19Z | — / Igor Sadalski | 2025-09-22T01:56:19Z | correct how plotting of the list is done | 1 | BUG_FIX | — |
| 128 | `b215cb485b01db5aa24958f4db17d4f5a4d6eda1` | — / Igor Sadalski | 2025-09-21T17:56:44Z | — / Igor Sadalski | 2025-09-21T17:56:44Z | add formating for the plan | 1 | FEATURE | — |
| 129 | `f172aaf953b8ba955ae0fec75e325605f2a827af` | — / Igor Sadalski | 2025-09-21T17:38:09Z | — / Igor Sadalski | 2025-09-21T17:38:09Z | add better formating | 1 | FEATURE | — |
| 130 | `a0032a45a24a0eba94b74a68dd1c069a09850c33` | HelloWorldLTY / HelloWorldLTY | 2025-09-20T18:47:53Z | web-flow / GitHub | 2025-09-20T18:47:53Z | Update fixed_env.yml | 1 | ENVIRONMENT | — |
| 131 | `53a1f0f313b45cb39d4e82ce4bdbc41e6e52785c` | serena2z / Serena Z | 2025-09-19T05:46:28Z | serena2z / Serena Z | 2025-09-19T05:46:28Z | added tutorial functions for generating scripts and test for validating scripts | 1 | FEATURE | — |
| 132 | `709dfcab6d023f4e4100d90945c4ba3d4d7af6d7` | shantanusharma / Shantanu Sharma | 2025-09-17T21:56:48Z | shantanusharma / Shantanu Sharma | 2025-09-17T21:56:48Z | Fixes ruff checks | 1 | FORMAT_ONLY | — |
| 133 | `b697d22ff37dc13324987da614333b9bef0a804b` | shantanusharma / Shantanu Sharma | 2025-09-17T21:52:12Z | shantanusharma / Shantanu Sharma | 2025-09-17T21:52:12Z | Fixes ruff checks | 1 | FORMAT_ONLY | — |
| 134 | `f1b631180ebadd49b9134057003389ef10dc1a73` | serena2z / Serena Zhang | 2025-09-17T07:06:46Z | web-flow / GitHub | 2025-09-17T07:06:46Z | Update biomni_env/new_software_v006.sh | 1 | ENVIRONMENT | — |
| 135 | `b1959cab48e3fa931f71eb19b336138ba5169523` | shantanusharma / Shantanu Sharma | 2025-09-16T17:26:57Z | shantanusharma / Shantanu Sharma | 2025-09-16T17:26:57Z | Adds glycoengineering tools | 1 | FEATURE | — |
| 136 | `26f1f977eb98272c04dc4abc43ebc29d0b442d35` | serena2z / Serena Z | 2025-09-16T05:07:44Z | serena2z / Serena Z | 2025-09-16T05:07:44Z | added example script | 1 | DOC_ONLY | — |
| 137 | `123a7b96be29ae932094338f0c7692c96f2f0f7f` | serena2z / Serena Zhang | 2025-09-16T04:53:04Z | web-flow / GitHub | 2025-09-16T04:53:04Z | Merge pull request #211 from snap-stanford/advanced_web_search | 2 | MERGE_ONLY | 211 |
| 138 | `64ab648b18b3c9737bdaa21fca80cbb8e04358c8` | serena2z / Serena Z | 2025-09-16T04:51:13Z | serena2z / Serena Z | 2025-09-16T04:51:13Z | add new literature search function | 1 | FEATURE | — |
| 139 | `2af043406d4024ec38e366c0e0e4334f33c85f1e` | serena2z / Serena Z | 2025-09-16T04:10:31Z | serena2z / Serena Z | 2025-09-16T04:10:31Z | added pylabrobot to env | 1 | ENVIRONMENT | — |
| 140 | `ff4ddeda693749f9c5c9228f6ec4f06844566174` | serena2z / Serena Zhang | 2025-09-16T04:02:34Z | web-flow / GitHub | 2025-09-16T04:02:34Z | Merge pull request #209 from snap-stanford/synapse_fix | 2 | MERGE_ONLY | 209 |
| 141 | `2b82a9ae127a704ff46aabe1e314d82ebba65763` | serena2z / Serena Z | 2025-09-16T04:00:13Z | serena2z / Serena Z | 2025-09-16T04:00:13Z | quick prompt fix | 1 | BUG_FIX | — |
| 142 | `ef24d21abf158a5b31efcaad1d6f4da79e7ecc4d` | — / Igor Sadalski | 2025-09-16T02:38:24Z | — / Igor Sadalski | 2025-09-16T02:38:24Z | create mvp of working markdown/PDF conversion engine | 1 | FEATURE | — |
| 143 | `3147bfaec79bca5f6aa9cff8424f2283ee209e76` | serena2z / Serena Zhang | 2025-09-12T23:00:41Z | web-flow / GitHub | 2025-09-12T23:00:41Z | Merge pull request #200 from lxasqjc/feature/commercial-mode-config | 2 | MERGE_ONLY | 200 |
| 144 | `fd9c8aed4026a34d0c51fff2759400622dec370f` | serena2z / Serena Zhang | 2025-09-12T22:51:50Z | web-flow / GitHub | 2025-09-12T22:51:50Z | Merge pull request #181 from Edison-A-N/fix/mcp-required-parameters-parsing | 2 | MERGE_ONLY | 181 |
| 145 | `a66d042a5a5fe5019faf4d84f1d61f52e154aee3` | serena2z / Serena Zhang | 2025-09-12T22:41:42Z | web-flow / GitHub | 2025-09-12T22:41:42Z | Merge pull request #201 from igor-sadalski/unsupervised_celltype_transfer_between_scRNA_datasets | 2 | MERGE_ONLY | 201 |
| 146 | `02c0e360be52bd6744d1345afdc03603daf8d96b` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-12T21:19:35Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-12T21:19:35Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 147 | `68df3370ddd00d4c3611b2b86dc7adfa19f07860` | — / Igor Sadalski | 2025-09-12T21:06:20Z | — / Igor Sadalski | 2025-09-12T21:06:20Z | add better safeguards for CUDA OOM when batching isoforms | 1 | BUG_FIX | — |
| 148 | `45e43293de9af4d5c013ae22d56baf4706deedca` | — / Igor Sadalski | 2025-09-12T20:57:17Z | — / Igor Sadalski | 2025-09-12T20:57:17Z | add memory efficient batching of isoforms | 1 | FEATURE | — |
| 149 | `87325e1c01d0bc66818c40b1d06c47add6772aeb` | kexinhuang12345 / Kexin Huang | 2025-09-12T15:37:40Z | web-flow / GitHub | 2025-09-12T15:37:40Z | Merge pull request #199 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 199 |
| 150 | `906869bc6f2dd10ca794a6cc0d4b0d6f7916bb57` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-10T17:24:27Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-10T17:24:27Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 151 | `b5314a09fb4473433de7dbd5f1811a6bd2f50dde` | — / Igor Sadalski | 2025-09-10T17:08:25Z | — / Igor Sadalski | 2025-09-10T17:08:25Z | add a tooling to convert gene names between species | 1 | FEATURE | — |
| 152 | `4c93e1f0176f0e716793c53e57580c856830e658` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-10T12:27:40Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-10T12:27:41Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 153 | `fb6c587454ab3ea411bf1b0903d9f2f38d275a86` | — / Igor Sadalski | 2025-09-10T12:09:15Z | — / Igor Sadalski | 2025-09-10T12:09:15Z | add genomic tool that does unsupervised celltype transfer | 1 | FEATURE | — |
| 154 | `fc50caea3f41ccbcacc984deea79b98352a4bac4` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-09T12:39:01Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-09T12:39:02Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 155 | `647e9f1fca9ef4565fb8541135a03371de861307` | lxasqjc / lxasqjc | 2025-09-09T12:36:05Z | lxasqjc / lxasqjc | 2025-09-09T12:36:05Z | feat: Add commercial mode configuration for license compliance | 1 | FEATURE | — |
| 156 | `df821c88cd396c6c43333b79bf8999e96c459899` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-08T18:29:16Z | web-flow / GitHub | 2025-09-08T18:29:16Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 157 | `d4b410d64eedc7b8a9d3a1b22eace52bb1d0cf58` | Edison-A-N / Edison-A-N | 2025-09-03T00:30:05Z | Edison-A-N / Edison-A-N | 2025-09-03T00:30:05Z | fix: correct required parameter parsing for auto-discovered MCP tools | 1 | BUG_FIX | — |
| 158 | `b5ad0c7bf4c6c3386b9d73da9656f4d6f257d36a` | serena2z / Serena Zhang | 2025-09-01T22:34:13Z | web-flow / GitHub | 2025-09-01T22:34:13Z | Merge pull request #159 from Edison-A-N/fix-unused-imports | 2 | MERGE_ONLY | 159 |
| 159 | `d146ad7fbfbe81735eb1abe658f4b139ae1a43a3` | serena2z / Serena Zhang | 2025-09-01T22:30:45Z | web-flow / GitHub | 2025-09-01T22:30:45Z | Merge pull request #156 from ryanDing26/lazyslide-support | 2 | MERGE_ONLY | 156 |
| 160 | `a94758537f84d1566a992467c286300f7cb2130b` | kexinhuang12345 / Kexin Huang | 2025-09-01T22:16:00Z | web-flow / GitHub | 2025-09-01T22:16:00Z | Merge pull request #176 from HelloWorldLTY/main | 2 | MERGE_ONLY | 176 |
| 161 | `b97ca7696cdaa63223b9df58c2c190424fa8713c` | kexinhuang12345 / Kexin Huang | 2025-09-01T22:13:04Z | web-flow / GitHub | 2025-09-01T22:13:04Z | Merge pull request #179 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 179 |
| 162 | `bb4d9011e1ec5220dbb19801b93c867725028ff3` | kexinhuang12345 / Kexin Huang | 2025-09-01T21:52:53Z | web-flow / GitHub | 2025-09-01T21:52:53Z | Merge pull request #173 from anngvu/feat/synapse-integration-full | 2 | MERGE_ONLY | 173 |
| 163 | `640417543aa9496a971cd3c8412515b367baae6a` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-09-01T18:23:29Z | web-flow / GitHub | 2025-09-01T18:23:29Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 164 | `99311865fa18525551ffb7a7b1582baa855effa9` | serena2z / Serena Z | 2025-09-01T02:03:39Z | serena2z / Serena Z | 2025-09-01T02:03:39Z | updated V006.sh to include lazyslide | 2 | MERGE_ONLY | — |
| 165 | `ace136d987f02ef195a2ace385b132e4a419f840` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-29T15:20:03Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-29T15:20:03Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 166 | `ae459406706add6c5aa3baab0c4c0c0485c754a7` | HelloWorldLTY / HelloWorldLTY | 2025-08-29T15:17:51Z | web-flow / GitHub | 2025-08-29T15:17:51Z | Update a1.py | 1 | UNKNOWN | — |
| 167 | `9f51eeb1010cb536623bebcfa44bcaf2cdccabfd` | Edison-A-N / Edison | 2025-08-27T07:06:52Z | web-flow / GitHub | 2025-08-27T07:06:52Z | Merge branch 'snap-stanford:main' into fix-unused-imports | 2 | MERGE_ONLY | — |
| 168 | `5f540c25587474444ea7c14953001d98f088b19d` | anngvu / Anh Nguyet Vu | 2025-08-27T00:03:57Z | anngvu / Anh Nguyet Vu | 2025-08-27T00:03:57Z | Optimize tools | 1 | REFACTOR | — |
| 169 | `415d21521913fc856c6adb8295a4e880c8457175` | kexinhuang12345 / Kexin Huang | 2025-08-26T02:57:50Z | web-flow / GitHub | 2025-08-26T02:57:50Z | Merge pull request #169 from SALhik/main | 2 | MERGE_ONLY | 169 |
| 170 | `321c2931d3ce1e3a7186a1265247746074dace96` | kexinhuang12345 / Kexin Huang | 2025-08-26T02:57:34Z | web-flow / GitHub | 2025-08-26T02:57:34Z | Merge pull request #171 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 171 |
| 171 | `650ecf4ba2470ef6465bb6b8c1942e294530cd57` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-25T18:21:00Z | web-flow / GitHub | 2025-08-25T18:21:00Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 172 | `12e2833974727b3b3330dd81110d19f77163f5be` | SALhik / SALhik | 2025-08-25T05:17:53Z | web-flow / GitHub | 2025-08-25T05:17:53Z | Update llm.py | 1 | UNKNOWN | — |
| 173 | `a4e74883a6f586b60737cdf4aac914b96eb40d49` | kexinhuang12345 / Kexin Huang | 2025-08-24T17:01:32Z | web-flow / GitHub | 2025-08-24T17:01:32Z | Merge pull request #168 from amehrjou/fix/lab-bench-import | 2 | MERGE_ONLY | 168 |
| 174 | `f8a62f51f750002108b12313e812ef68b3061548` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-23T19:44:13Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-23T19:44:13Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 175 | `97b4da64aad811baa0a7f6def878b4542d8fbae3` | amehrjou / amehrjou | 2025-08-23T19:41:15Z | amehrjou / amehrjou | 2025-08-23T19:41:15Z | Fix wrong import in lab_bench.py (bioagentos → biomni) | 1 | BUG_FIX | — |
| 176 | `4628f214ad6bb7ca4597ceefc89ddebe26d03e08` | kexinhuang12345 / Kexin Huang | 2025-08-23T17:39:12Z | web-flow / GitHub | 2025-08-23T17:39:12Z | Merge pull request #162 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 162 |
| 177 | `6e4a5399cb47c7630ebc91854ab26e4ad31110ba` | anngvu / Anh Nguyet Vu | 2025-08-21T17:06:48Z | anngvu / Anh Nguyet Vu | 2025-08-21T17:06:48Z | Add Synapse download tool | 1 | FEATURE | — |
| 178 | `4fb14875fc36a234e731d1de0ffcc10719327c05` | kexinhuang12345 / Kexin Huang | 2025-08-21T16:33:07Z | web-flow / GitHub | 2025-08-21T16:33:07Z | Merge pull request #166 from snap-stanford/kexinhuang12345-patch-2 | 2 | MERGE_ONLY | 166 |
| 179 | `4aa8f63628c24366ea98da49876078f7e7a45292` | kexinhuang12345 / Kexin Huang | 2025-08-21T16:32:56Z | web-flow / GitHub | 2025-08-21T16:32:56Z | update slack link | 1 | DOC_ONLY | — |
| 180 | `88b1c843d81a1a8810d1f412b7b8150f55351880` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-21T07:51:04Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-21T07:51:05Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 181 | `1081fdaf0f12dcfe915c75acbf8a7abba2e48e5e` | Edison-A-N / Edison-A-N | 2025-08-17T07:35:18Z | Edison-A-N / Edison-A-N | 2025-08-21T07:49:19Z | fix: enable F401 unused import checks and clean up imports | 1 | FORMAT_ONLY | — |
| 182 | `4a98fb41229f98d8499dd1e0483470c73ed7b1b5` | anngvu / Anh Nguyet Vu | 2025-08-21T05:15:39Z | anngvu / Anh Nguyet Vu | 2025-08-21T05:15:39Z | Augment query results with important AR info | 1 | FEATURE | — |
| 183 | `1dcc3063d99db750c93034f759f665431854ef3b` | anngvu / Anh Nguyet Vu | 2025-08-21T04:29:14Z | anngvu / Anh Nguyet Vu | 2025-08-21T04:29:14Z | Add query_synapse | 1 | FEATURE | — |
| 184 | `8b39c607014dffaed6bcb98137162b6cf1ed9411` | serena2z / Serena Zhang | 2025-08-20T23:12:35Z | web-flow / GitHub | 2025-08-20T23:12:35Z | Hotfix/v0.0.6 param naming (#165) | 1 | BUG_FIX | 165 |
| 185 | `362368d0c5bbc2ab76524d5044036bfa53d05270` | serena2z / Serena Zhang | 2025-08-20T22:50:05Z | web-flow / GitHub | 2025-08-20T22:50:05Z | Release/v0.0.6 (#164) | 1 | ENVIRONMENT | 164 |
| 186 | `3781116a4555bd3fc586d58cfcfa9d31c81e580e` | serena2z / Serena Zhang | 2025-08-20T21:22:05Z | web-flow / GitHub | 2025-08-20T21:22:05Z | Config management (#161) | 1 | FEATURE | 161 |
| 187 | `dc3fd8c340b63d3cb3b6270b6fb016da2ea91b71` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-18T18:24:34Z | web-flow / GitHub | 2025-08-18T18:24:34Z | [pre-commit.ci] pre-commit autoupdate | 1 | DEPENDENCY_ONLY | — |
| 188 | `2927ef128c195fc1920a693b2ef16b1cfe9e779c` | kuanlinhuang / huangkuanlin | 2025-08-17T20:47:46Z | kuanlinhuang / huangkuanlin | 2025-08-17T20:47:46Z | delete unncessary files | 1 | REMOVAL | — |
| 189 | `3bef2a051685d99a58191a150f68da4bf24044d6` | kuanlinhuang / huangkuanlin | 2025-08-17T20:06:27Z | kuanlinhuang / huangkuanlin | 2025-08-17T20:06:27Z | final, delete chembl beaker class as it's similar to RDKit, also finalizing the test scripts and logs, continued to improve cellxgene and encode though those still dicey | 1 | UNKNOWN | — |
| 190 | `594278c98202bf275dc9c32be67e8ef173e8e1ff` | serena2z / Serena Zhang | 2025-08-17T00:22:21Z | web-flow / GitHub | 2025-08-17T00:22:21Z | Merge pull request #138 from marcosbolanos/feature/cnv-purity-ploidy | 2 | MERGE_ONLY | 138 |
| 191 | `52dca675739c5f64365699a31d660569850f1aa3` | serena2z / Serena Zhang | 2025-08-16T23:57:48Z | web-flow / GitHub | 2025-08-16T23:57:48Z | Merge pull request #33 from shengyongniu/shengyong/trialbench | 2 | MERGE_ONLY | 33 |
| 192 | `7c70367622de88755931806679341924166629f9` | serena2z / Serena Z | 2025-08-16T23:56:18Z | serena2z / Serena Z | 2025-08-16T23:56:18Z | fixed dbsnp | 1 | BUG_FIX | — |
| 193 | `97d9bf91f04c8c90c1810223bafc2e7a5c477a9d` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T03:35:26Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T03:35:27Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 194 | `c1a6552da6047fcae6c47868ec27286f973d900f` | ryanDing26 / Ryan Ding | 2025-08-16T03:29:14Z | web-flow / GitHub | 2025-08-16T03:29:14Z | Merge branch 'snap-stanford:main' into lazyslide-support | 2 | MERGE_ONLY | — |
| 195 | `0c66fc9daaf65b1244f4389bc2a94c45b6844038` | ryanDing26 / ryanDing26 | 2025-08-16T03:27:42Z | ryanDing26 / ryanDing26 | 2025-08-16T03:27:42Z | Add lazyslide support | 1 | FEATURE | — |
| 196 | `2c440d68597f104894473c6bd84452d63a2b799c` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T01:27:04Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T01:27:05Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 197 | `30e085557fa4c4c536ff8c1e473ca60676c932b8` | shengyongniu / NIU, SHENG-YONG | 2025-08-16T01:26:57Z | web-flow / GitHub | 2025-08-16T01:26:57Z | add back description | 1 | DOC_ONLY | — |
| 198 | `0b57547d943692565192023ac92c5edefcdf8793` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T01:23:37Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-08-16T01:23:37Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 199 | `948a5c1576afc0d736cbccee03f7091a4d44312a` | shengyongniu / shengyongniu | 2025-08-16T01:23:28Z | shengyongniu / shengyongniu | 2025-08-16T01:23:28Z | add back description | 1 | DOC_ONLY | — |
| 200 | `9c5eca618b7171092420ad07c9d6e6cd6c22dcc4` | shengyongniu / shengyongniu | 2025-08-16T01:16:51Z | shengyongniu / shengyongniu | 2025-08-16T01:16:51Z | remove test.py | 1 | REMOVAL | — |

## PR mapping and duplicate/lineage notes

- `mapped_to_pr`: 23 records from explicit first-line subjects.
- Explicit PRs: `#33`, `#138`, `#156`, `#159`, `#161`, `#162`, `#164`, `#165`, `#166`, `#168`, `#169`, `#171`, `#173`, `#176`, `#179`, `#181`, `#199`, `#200`, `#201`, `#204`, `#205`, `#209`, `#211`.
- Of these, 20 are two-parent `Merge pull request` commits. `#161`, `#164`, and `#165` are single-parent subject references and may be squash/rebase lineages; exact merge methods are unresolved.
- There are 29 multi-parent commits total: the 20 explicit PR merges plus 9 branch/remote/content merges without a PR number in the first line. Treat all 29 as duplicate/sync/lineage surfaces until PR and DAG normalization; do not count them as 29 independent features.
- No duplicate substantive change set was proven in this metadata-only pass. Exact ancestry/patch identity remains for normalization.

## Substantive and feature leads

These are discovery leads, not validated independent features:

- Protein and cross-species representation: PR `#205` protein ESM embeddings; PR `#204` and `b5314a09fb4473433de7dbd5f1811a6bd2f50dde` interspecies gene-name conversion.
- Bioimaging: `d811aba230369ba4e24b32ad799ce8c13785c618` registration and `27ae81ad4e3b95c14d11290ecd907ac3b954c33d` nnU-Net support.
- PDF/report generation: `ef24d21abf158a5b31efcaad1d6f4da79e7ecc4d` Markdown/PDF conversion engine and adjacent save/format/parser changes.
- Glycoengineering: `b1959cab48e3fa931f71eb19b336138ba5169523`.
- Literature search: PR `#211` and `64ab648b18b3c9737bdaa21fca80cbb8e04358c8` advanced literature search.
- Commercial-mode license configuration: PR `#200` / `647e9f1fca9ef4565fb8541135a03371de861307`.
- MCP parsing: PR `#181` / `d4b410d64eedc7b8a9d3a1b22eace52bb1d0cf58` required-parameter parsing fix.
- Single-cell genomics: PR `#201` / `fb6c587454ab3ea411bf1b0903d9f2f38d275a86` unsupervised cell-type transfer; PR `#156` / `0c66fc9daaf65b1244f4389bc2a94c45b6844038` LazySlide support.
- Synapse: PRs `#209` and `#173`, plus `6e4a5399cb47c7630ebc91854ab26e4ad31110ba`, `1dcc3063d99db750c93034f759f665431854ef3b`, and `4a98fb41229f98d8499dd1e0483470c73ed7b1b5`.
- Config management and releases: PRs `#161`, `#164`, `#165`.
- Cancer genomics and evaluation: PR `#138` CNV purity/ploidy and PR `#33` TrialBench.

## Evidence URLs

- Frozen page-2 API query: https://api.github.com/repos/snap-stanford/Biomni/commits?sha=400c1f366b96a35ca253e13c9b06c5076af41d65&per_page=100&page=2
- Frozen page-1 boundary query: https://api.github.com/repos/snap-stanford/Biomni/commits?sha=400c1f366b96a35ca253e13c9b06c5076af41d65&per_page=100&page=1
- Prior boundary commit: https://github.com/snap-stanford/Biomni/commit/899eefb22a5a102fd81f1d845490b4b83fee3402
- This page first commit: https://github.com/snap-stanford/Biomni/commit/3371e3207dc8e63887d3cd3904243678c737334e
- PR pattern (replace number with the explicit IDs above): https://github.com/snap-stanford/Biomni/pull/205

## Uncertainty and unresolved work

- The denominator `487` is parent-verified from the local frozen DAG and was supplied by the coordinator; this worker did not independently recalculate it.
- GitHub login absence reflects a null linked account in this API response; signature names are not independently identity-verified here.
- Commit dates are Git author/committer metadata and are not guaranteed to equal public-push time.
- Subject-based classes can be wrong, especially for terse or mixed subjects such as positions 102, 104, 107–111, 116, 119–122, 126, 131, 136, 141, 147, 166, 168, 172, 182, 186, 189, 197, and 199. Diff/PR evidence is required before canonical classification.
- Merge commits and adjacent child commits likely repeat PR lineages; no independent-feature counts should be derived from this page without DAG/PR normalization.
- This task did not audit diffs, licenses, security, runtime correctness, PR state, or feature completeness.

## Next action

Fetch the same frozen commit-list query with `per_page=100&page=3`, preserve newest-first order, verify its boundary after `9c5eca618b7171092420ad07c9d6e6cd6c22dcc4`, and continue the inventory. Keep collection `PARTIAL` until all 487 frozen-DAG commits are processed and API pagination is exhausted.
