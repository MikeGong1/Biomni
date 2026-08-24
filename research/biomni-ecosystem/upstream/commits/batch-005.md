# Worker Result: commit-index-005

Parent verification: `VERIFIED`. Official API page 5 contains the final 87
unique SHAs, exactly matching frozen local Git positions 401–487 and order.
Metadata fields are `FACT`; subject-only classifications are `INFERENCE`.

## Task record

- Task ID: `commit-index-005`
- Scope: frozen main commit list, page 5, per_page=100, newest first.
- API response Date header: `Sat, 22 Aug 2026 21:17:00 GMT`
- Processed: 87 records, cumulative positions 401–487 of 487.
- Boundary: first `4da6a12c06527a0f13247afc9a16781e454e8d99`; root/last `54cfd4712e7596cb02aa93c87e22897a2948d5aa`.
- Pagination: `COMPLETE`; response has previous/first links and no next link.
- Safety: static metadata only; no repository code executed.

## Preliminary inventory

| # | Full SHA | Author | Author date | Committer | Committer date | First-line subject | Parents | Preliminary class | PR |
|---:|---|---|---|---|---|---|---:|---|---:|
| 401 | `4da6a12c06527a0f13247afc9a16781e454e8d99` | kexinhuang12345 / kexinhuang12345 | 2025-07-17T05:21:09Z | kexinhuang12345 / kexinhuang12345 | 2025-07-17T05:21:09Z | fix parsing error | 1 | BUG_FIX | — |
| 402 | `8b997fc9b7ff44f09f65fa9e44b658649fda784e` | kexinhuang12345 / Kexin Huang | 2025-07-16T22:04:26Z | web-flow / GitHub | 2025-07-16T22:04:26Z | Merge pull request #56 from snap-stanford/0.0.4_release | 2 | MERGE_ONLY | 56 |
| 403 | `affcaf841f86106bf401bb0059a34a2a4c610942` | kexinhuang12345 / kexinhuang12345 | 2025-07-16T21:31:36Z | kexinhuang12345 / kexinhuang12345 | 2025-07-16T21:31:36Z | fix env install | 1 | BUG_FIX | — |
| 404 | `e1b0c0d33ebce0eec8a34031c4b26590e771bb16` | zskylarli / Zhuoyan Li | 2025-07-16T18:29:05Z | zskylarli / Zhuoyan Li | 2025-07-16T18:29:05Z | fix formatting | 1 | FORMAT_ONLY | — |
| 405 | `fb366d9cfb5c2dba60736249ec2926e85f552bf8` | SnowLightPath / SnowLightPath | 2025-07-16T15:16:59Z | SnowLightPath / SnowLightPath | 2025-07-16T15:35:54Z | Fix ruff linting errors in MCP implementation | 1 | FORMAT_ONLY | — |
| 406 | `875e590dbb5326b4da839d588fc4ccdd2c4df84a` | shibahara-1113 / SnowLightPath | 2025-07-16T10:56:44Z | SnowLightPath / SnowLightPath | 2025-07-16T14:46:52Z | Add MCP (Model Context Protocol) support to biomni agent | 1 | FEATURE | — |
| 407 | `d094b481f27e9a990e022309181623486b8a13e1` | kexinhuang12345 / Kexin Huang | 2025-07-16T06:25:47Z | web-flow / GitHub | 2025-07-16T06:25:47Z | Add files via upload | 1 | FEATURE | — |
| 408 | `6ea469892992ae34fd8faac0ce47cc920eca6cd2` | kexinhuang12345 / Kexin Huang | 2025-07-16T05:24:58Z | web-flow / GitHub | 2025-07-16T05:24:58Z | Merge pull request #49 from Pidem/Bedrock-Support | 2 | MERGE_ONLY | 49 |
| 409 | `2fcaa9cfd5b911821328a5f8b496919a8814e8b8` | zskylarli / Zhuoyan Li | 2025-07-15T15:21:18Z | zskylarli / Zhuoyan Li | 2025-07-15T15:26:37Z | minor stylistic fix | 1 | BUG_FIX | — |
| 410 | `85297f43f141a7aa3ea3751efba46afb312c6fdc` | zskylarli / Zhuoyan Li | 2025-07-14T21:35:09Z | zskylarli / Zhuoyan Li | 2025-07-15T15:26:37Z | adjust log and default output dir | 1 | UNKNOWN | — |
| 411 | `c41361583bc83e7ecf9a2035b3956debe54d3ca2` | zskylarli / Zhuoyan Li | 2025-07-14T20:21:32Z | zskylarli / Zhuoyan Li | 2025-07-15T15:26:37Z | add cell type annotation tool using panhuman azimuth | 1 | FEATURE | — |
| 412 | `ac7c9991af4db5dc48b65c3a70a347b5edbbd5c7` | zskylarli / Zhuoyan Li | 2025-07-14T20:20:21Z | zskylarli / Zhuoyan Li | 2025-07-15T15:26:37Z | add panhumanpy installation | 1 | ENVIRONMENT | — |
| 413 | `51b74358e56226bf94b9e191b615d57aded6267c` | serena2z / Serena Zhang | 2025-07-14T22:42:10Z | web-flow / GitHub | 2025-07-14T22:42:10Z | Merge pull request #45 from HelloWorldLTY/main | 2 | MERGE_ONLY | 45 |
| 414 | `6b03a3f6760668ae852eb645296ed115a07f9fdb` | serena2z / serena2z | 2025-07-14T22:39:26Z | serena2z / serena2z | 2025-07-14T22:39:26Z | removed test code for main | 1 | REMOVAL | — |
| 415 | `914e20fc8f0fe2fac9b59aaf729b4c66094a192e` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T19:38:44Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T19:38:44Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 416 | `54ff0d84f7bc0c5974e5ef0d03fda881244710f1` | Pidem / Pierre de Malliard | 2025-07-14T19:37:55Z | web-flow / GitHub | 2025-07-14T19:37:55Z | AWS Bedrock Support | 1 | FEATURE | — |
| 417 | `b6f8863cb6215dc81d9cb266a767104298743433` | Pidem / Pierre de Malliard | 2025-07-14T19:36:16Z | web-flow / GitHub | 2025-07-14T19:36:16Z | Support AWS Bedrock with API Keys | 1 | FEATURE | — |
| 418 | `309f10f67bf48cabb439b5ca94aadde3a504e7ef` | serena2z / Serena Zhang | 2025-07-14T18:27:44Z | web-flow / GitHub | 2025-07-14T18:27:44Z | Merge pull request #48 from snap-stanford/feature/add-datasets | 2 | MERGE_ONLY | 48 |
| 419 | `732f7a93d316bf98ecfb9427100fda81242d3da0` | serena2z / serena2z | 2025-07-14T18:25:51Z | serena2z / serena2z | 2025-07-14T18:25:51Z | Merge remote-tracking branch 'origin/main' into feature/add-datasets | 2 | MERGE_ONLY | — |
| 420 | `df5c64623063de91855673eb66dad40f3a3a6ef4` | serena2z / serena2z | 2025-07-14T18:17:54Z | serena2z / serena2z | 2025-07-14T18:17:54Z | added dataset descriptions to env_desc | 1 | FEATURE | — |
| 421 | `dbbb65a9123c5f9ad5c2347996c9028fe3d74231` | kexinhuang12345 / Kexin Huang | 2025-07-14T18:17:34Z | web-flow / GitHub | 2025-07-14T18:17:34Z | Merge pull request #47 from snap-stanford/pre-commit-ci-update-config | 2 | MERGE_ONLY | 47 |
| 422 | `56b6ea3f5e0b3ee91e39155418d6395c45abc916` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T18:11:31Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T18:11:31Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 423 | `252b688afd069876a11bcee7eac982265e156ea3` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T18:11:24Z | web-flow / GitHub | 2025-07-14T18:11:24Z | [pre-commit.ci] pre-commit autoupdate | 1 | FORMAT_ONLY | — |
| 424 | `d545d49a57af2acea41bd9831069ca84721c4746` | kexinhuang12345 / Kexin Huang | 2025-07-14T15:59:30Z | web-flow / GitHub | 2025-07-14T15:59:30Z | Update README.md | 1 | DOC_ONLY | — |
| 425 | `a848b494564790562f2871bb78cb6ee01cf110bd` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T01:41:12Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T01:41:12Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 426 | `89395b6d44a68a28c5381554cd4e8696db3e5775` | — / Helloworldlty | 2025-07-14T01:40:59Z | — / Helloworldlty | 2025-07-14T01:40:59Z | Merge branch 'main' of https://github.com/HelloWorldLTY/Biomni | 2 | MERGE_ONLY | — |
| 427 | `98d06458a0b5a3ca84c89cd8275204f21623f6ea` | — / Helloworldlty | 2025-07-14T01:38:25Z | — / Helloworldlty | 2025-07-14T01:38:25Z | fix a loop bug | 1 | BUG_FIX | — |
| 428 | `3edd56cacbbc2bebd2c5f6b4d0e68e3824470465` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T01:35:41Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-14T01:35:42Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 429 | `8a0e79b385e5b145c318ecb51cbfff18f0ddf3b7` | HelloWorldLTY / HelloWorldLTY | 2025-07-14T01:35:33Z | web-flow / GitHub | 2025-07-14T01:35:33Z | Merge branch 'snap-stanford:main' into main | 2 | MERGE_ONLY | — |
| 430 | `69e10e78d68139d5d641b55848035b6a3e2c2979` | — / Helloworldlty | 2025-07-14T01:30:34Z | — / Helloworldlty | 2025-07-14T01:30:34Z | update chatnt include | 1 | UNKNOWN | — |
| 431 | `c4b05e45044bad7e6fcfcf61dcb2bb82398db5b5` | serena2z / Serena Zhang | 2025-07-13T04:29:27Z | web-flow / GitHub | 2025-07-13T04:29:27Z | Merge pull request #18 from PLippmann/ddinter-integration | 2 | MERGE_ONLY | 18 |
| 432 | `ad134339042de2c32d1d58d2e4dad6091c507963` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-13T02:03:33Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-13T02:03:34Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 433 | `9891fe923e8ca4e6551e9074da05c119b058f78e` | MintaYLu / MintaYLu | 2025-07-13T02:03:26Z | web-flow / GitHub | 2025-07-13T02:03:26Z | Update genetics.py | 1 | UNKNOWN | — |
| 434 | `9c21ef98cc645586929eb0cb3727c7f7a4f60b35` | MintaYLu / MintaYLu | 2025-07-13T01:38:43Z | web-flow / GitHub | 2025-07-13T01:38:43Z | Update environment.yml | 1 | ENVIRONMENT | — |
| 435 | `5b2e25937421a465d227249e7e92e97415beb5da` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-13T01:28:58Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-13T01:28:58Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 436 | `e867ae82bdb2da63a8c584c074ad204a28efd7a5` | serena2z / serena2z | 2025-07-13T01:17:08Z | serena2z / serena2z | 2025-07-13T01:17:08Z | Resolve merge | 2 | MERGE_ONLY | — |
| 437 | `31a3bc89f5157554ec57e1b20f03e6a7d1375875` | MintaYLu / MintaYLu | 2025-07-13T01:15:59Z | web-flow / GitHub | 2025-07-13T01:15:59Z | Add tool description for missing data imputation in genetics.py | 1 | FEATURE | — |
| 438 | `e7be7351a24e7989c8c5ff5980df1d249bbad161` | serena2z / serena2z | 2025-07-13T01:13:53Z | serena2z / serena2z | 2025-07-13T01:13:53Z | fix download | 1 | BUG_FIX | — |
| 439 | `a76cf7b0ea9aaf740e44414a6e55d591734a5f11` | MintaYLu / MintaYLu | 2025-07-13T01:11:00Z | web-flow / GitHub | 2025-07-13T01:11:00Z | Add missing data imputation tool (GAIN, MissForest, Iterative) to genetics.py | 1 | FEATURE | — |
| 440 | `4be01489e84a81cb4527b7ca0f71c02b9246f660` | MintaYLu / MintaYLu | 2025-07-13T00:59:46Z | web-flow / GitHub | 2025-07-13T00:59:46Z | add impute hyperimpute for missing data imputation | 1 | FEATURE | — |
| 441 | `1465cb2653a53ddab9c05280bf2677a14841dfd9` | RyanLi1028 / Ryan Li | 2025-07-13T00:34:31Z | web-flow / GitHub | 2025-07-13T00:34:31Z | Merge pull request #41 from snap-stanford/custom_support | 2 | MERGE_ONLY | 41 |
| 442 | `3a595cf17fc904277a55dfc8083adae5cf2ae322` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-13T00:32:54Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-13T00:32:54Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 443 | `cdb4e77b7a6660222ffb630adbbef3abff144827` | RyanLi1028 / Ryan Li | 2025-07-13T00:28:09Z | RyanLi1028 / Ryan Li | 2025-07-13T00:28:09Z | Custom model support | 1 | FEATURE | — |
| 444 | `e5edffc929bfec99f80ed3ce7904b5ab58e3199f` | RyanLi1028 / Ryan Li | 2025-07-12T23:53:34Z | web-flow / GitHub | 2025-07-12T23:53:34Z | Merge pull request #32 from Thiraput01/gemini_support | 2 | MERGE_ONLY | 32 |
| 445 | `6d95064598553a8266c30dc6436a3da784e9c65a` | serena2z / serena2z | 2025-07-12T23:41:42Z | serena2z / serena2z | 2025-07-12T23:41:42Z | added txgnn files | 1 | FEATURE | — |
| 446 | `0a3534ef496556c7d1a2352a6c716e898297f1c7` | kexinhuang12345 / Kexin Huang | 2025-07-12T23:38:16Z | web-flow / GitHub | 2025-07-12T23:38:16Z | Merge pull request #39 from snap-stanford/edit_contrib | 2 | MERGE_ONLY | 39 |
| 447 | `e6e3edf7235752f7f23f550304cb51cee8fa4d00` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-11T17:41:06Z | RyanLi1028 / Ryan Li | 2025-07-12T23:35:57Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 448 | `0d90735149e1c7ad749ffb2ba43fdaef66932bd0` | — / root | 2025-07-11T17:40:51Z | RyanLi1028 / Ryan Li | 2025-07-12T23:35:56Z | chore: revert back notebook's metadata | 1 | REMOVAL | — |
| 449 | `a7ec89c8462d5856e1445db503ce1091f8fe4118` | — / root | 2025-07-11T17:03:00Z | RyanLi1028 / Ryan Li | 2025-07-12T23:35:55Z | chore: del test.ipynb | 1 | UNKNOWN | — |
| 450 | `2137ca005bf2c46939bdc76c47d099ef4c10f65e` | — / root | 2025-07-11T15:32:50Z | RyanLi1028 / Ryan Li | 2025-07-12T23:35:50Z | feat: gemini support | 1 | FEATURE | — |
| 451 | `dadecbe0b83a8fe7593b3b4560dfbbcf3b99310a` | kexinhuang12345 / kexinhuang12345 | 2025-07-12T23:30:50Z | kexinhuang12345 / kexinhuang12345 | 2025-07-12T23:30:50Z | update contrib | 1 | UNKNOWN | — |
| 452 | `8bd745663523ab42e3df7149f1003a113f706145` | RyanLi1028 / Ryan Li | 2025-07-12T23:14:52Z | web-flow / GitHub | 2025-07-12T23:14:52Z | Merge pull request #19 from sbonner0/ollama_support | 2 | MERGE_ONLY | 19 |
| 453 | `1c17f456cdee63554b3bb3b6b5251822d6ebf85b` | kexinhuang12345 / Kexin Huang | 2025-07-12T23:09:19Z | web-flow / GitHub | 2025-07-12T23:09:19Z | Merge pull request #38 from snap-stanford/edit_contrib | 2 | MERGE_ONLY | 38 |
| 454 | `eee0e82d514236925066cec446e45e5df1601627` | kexinhuang12345 / kexinhuang12345 | 2025-07-12T23:08:51Z | kexinhuang12345 / kexinhuang12345 | 2025-07-12T23:08:51Z | add more contribution guideline | 1 | DOC_ONLY | — |
| 455 | `63443affda1a09e758785b55be4c16f06d077b56` | ginylil-tech / Ginylil-Tech | 2025-07-12T10:52:02Z | ginylil-tech / Ginylil-Tech | 2025-07-12T10:52:02Z | Add DETAILS.md for improved documentation | 1 | DOC_ONLY | — |
| 456 | `c7d8bd079e90d8d8ff07a827b6806cb751c933ab` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-12T03:51:48Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-12T03:51:48Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 457 | `d8db0d934dc2bf3c43d3d9b57916d2cea01dc0a0` | shengyongniu / shengyongniu | 2025-07-12T03:43:31Z | shengyongniu / shengyongniu | 2025-07-12T03:43:31Z | add TrialBench data | 1 | BENCHMARK | — |
| 458 | `31d466d0586d8ce16ec3dc130ca7fde4d8608a05` | kexinhuang12345 / Kexin Huang | 2025-07-10T16:01:12Z | web-flow / GitHub | 2025-07-10T16:01:12Z | Merge pull request #20 from snap-stanford/pip_bug_fix | 2 | MERGE_ONLY | 20 |
| 459 | `24c8a97b9c6d8b54296338c3ba7c897e35358cc6` | kexinhuang12345 / kexinhuang12345 | 2025-07-10T15:51:19Z | kexinhuang12345 / kexinhuang12345 | 2025-07-10T15:51:19Z | fix version file | 1 | BUG_FIX | — |
| 460 | `4e3d3304ef4b8b4aab774c280a16346fad9959e9` | kexinhuang12345 / Kexin Huang | 2025-07-10T15:10:23Z | web-flow / GitHub | 2025-07-10T15:10:23Z | 0.0.3 | 1 | UNKNOWN | — |
| 461 | `0d2383e72f52cab86ea6005fd5bb6e316c32ea5e` | kexinhuang12345 / Kexin Huang | 2025-07-10T15:00:36Z | web-flow / GitHub | 2025-07-10T15:00:36Z | fix slack link | 1 | BUG_FIX | — |
| 462 | `3451d022c6e76cd3912ae8a1fc4e3399ba11cedf` | kexinhuang12345 / Kexin Huang | 2025-07-10T14:37:37Z | web-flow / GitHub | 2025-07-10T14:37:37Z | Merge pull request #15 from jucor/patch-1 | 2 | MERGE_ONLY | 15 |
| 463 | `ae0c6afed1758db9c9bead584126de39e00c6535` | sbonner0 / sbonner0 | 2025-07-10T14:30:09Z | sbonner0 / sbonner0 | 2025-07-10T14:30:09Z | Merge branch 'ollama_support' of github.com-sbonner0:sbonner0/Biomni into ollama_support | 2 | MERGE_ONLY | — |
| 464 | `0b336c4444667a92c8471250d0cbc994b938744c` | sbonner0 / sbonner0 | 2025-07-10T14:29:32Z | sbonner0 / sbonner0 | 2025-07-10T14:29:32Z | remove accidental data commit | 1 | REMOVAL | — |
| 465 | `d874bd5661088d2fe3d9e9cf6abe5c5f27c4c937` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-10T14:26:00Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-10T14:26:01Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 466 | `0bad3ab9c0761fd51bf01cc7665f07994cea9eae` | sbonner0 / sbonner0 | 2025-07-10T14:25:17Z | sbonner0 / sbonner0 | 2025-07-10T14:25:17Z | Merge branch 'ollama_support' of github.com-sbonner0:sbonner0/Biomni into ollama_support | 2 | MERGE_ONLY | — |
| 467 | `f3af80bf8190faf6519a7cc6fd9cf6c9ecd5cc1f` | sbonner0 / sbonner0 | 2025-07-10T14:22:47Z | sbonner0 / sbonner0 | 2025-07-10T14:22:47Z | change typing for list | 1 | UNKNOWN | — |
| 468 | `dec95a257b0b574e7d2e856bd156c113f6fed3bc` | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-10T14:20:03Z | pre-commit-ci[bot] / pre-commit-ci[bot] | 2025-07-10T14:20:04Z | [pre-commit.ci] auto fixes from pre-commit.com hooks | 1 | FORMAT_ONLY | — |
| 469 | `3087a3619c6914b1779cf5da8533dc170bc22e56` | kexinhuang12345 / Kexin Huang | 2025-07-10T14:08:53Z | web-flow / GitHub | 2025-07-10T14:08:53Z | Update README.md | 1 | DOC_ONLY | — |
| 470 | `3321172412dc76d0677d631a6d4c08e6323b3005` | sbonner0 / sbonner0 | 2025-07-10T14:01:16Z | sbonner0 / sbonner0 | 2025-07-10T14:01:16Z | Added support for local LLMs using Ollama | 1 | FEATURE | — |
| 471 | `1d1a2c32999ff8ab4d66e750ec3c284cefcb23c4` | PLippmann / PLippmann | 2025-07-10T13:15:05Z | PLippmann / PLippmann | 2025-07-10T13:15:05Z | gitignore update for ddinter | 1 | UNKNOWN | — |
| 472 | `59169f69b777fe1a864a70404c75f269ae26e9d7` | PLippmann / PLippmann | 2025-07-10T13:14:43Z | PLippmann / PLippmann | 2025-07-10T13:14:43Z | ddinter integration into pharacology.py | 1 | FEATURE | — |
| 473 | `96e2f74cc4b4389ecabd455b581298f92cf02fc9` | jucor / Julien Cornebise | 2025-07-10T10:37:04Z | web-flow / GitHub | 2025-07-10T10:37:04Z | Fix logo link in README.md | 1 | DOC_ONLY | — |
| 474 | `7b0d1e30067569f2b9e97d9c141e726a186df905` | kexinhuang12345 / Kexin Huang | 2025-07-10T07:00:33Z | web-flow / GitHub | 2025-07-10T07:00:33Z | Merge pull request #9 from Zethson/main | 2 | MERGE_ONLY | 9 |
| 475 | `5cc0c545f43617e264327ca97e67554cadcab2cc` | Zethson / Lukas Heumos | 2025-07-09T20:36:55Z | Zethson / Lukas Heumos | 2025-07-09T20:36:55Z | A round of pre-commit | 1 | UNKNOWN | — |
| 476 | `ecee5fac812fcb0b46f023fa749957be2fe7466f` | Zethson / Lukas Heumos | 2025-07-09T20:08:02Z | Zethson / Lukas Heumos | 2025-07-09T20:08:02Z | Use pyproject.toml | 1 | UNKNOWN | — |
| 477 | `675a128acf4662e07a9be2dba29a8f1f2455db63` | kexinhuang12345 / Kexin Huang | 2025-07-09T18:31:56Z | web-flow / GitHub | 2025-07-09T18:31:56Z | Update README.md | 1 | DOC_ONLY | — |
| 478 | `fcb1bf99c4e25bd857c382c00b09c9473e4a0fbe` | kexinhuang12345 / Kexin Huang | 2025-07-09T18:31:33Z | web-flow / GitHub | 2025-07-09T18:31:33Z | Create LICENSE | 1 | UNKNOWN | — |
| 479 | `1b2f6cd5c3dd64d43167667e1055b169a3d3bc6a` | kexinhuang12345 / kexinhuang12345 | 2025-07-09T16:11:08Z | kexinhuang12345 / kexinhuang12345 | 2025-07-09T16:11:08Z | cleanup | 1 | UNKNOWN | — |
| 480 | `9b5d96cb986f5346cb63d6495b0bcd3a0a6374c3` | kexinhuang12345 / kexinhuang12345 | 2025-07-09T16:01:08Z | kexinhuang12345 / kexinhuang12345 | 2025-07-09T16:01:08Z | pre-commit | 1 | UNKNOWN | — |
| 481 | `ea4d6e8834258033b1a32f8680fa3b304c1338eb` | kexinhuang12345 / kexinhuang12345 | 2025-07-09T05:16:24Z | kexinhuang12345 / kexinhuang12345 | 2025-07-09T05:16:24Z | 0.0.2 | 1 | UNKNOWN | — |
| 482 | `32bc8ebd8470647ef05b1e6a32afd6b7febf0e35` | kexinhuang12345 / kexinhuang12345 | 2025-07-09T05:11:54Z | kexinhuang12345 / kexinhuang12345 | 2025-07-09T05:11:54Z | oss release 0.0.1 | 1 | ENVIRONMENT | — |
| 483 | `d043e977534b5f8f24fef39f4caabed8976500db` | kexinhuang12345 / Kexin Huang | 2025-06-01T19:22:10Z | web-flow / GitHub | 2025-06-01T19:22:10Z | Update README.md | 1 | DOC_ONLY | — |
| 484 | `67e542a695829f2fa7bb86ca1fdeea87d675b301` | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:57:12Z | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:57:12Z | add all | 1 | FEATURE | — |
| 485 | `f45e4357af77475bea650a50a3b6237fb90d52a2` | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:53:37Z | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:53:37Z | add all | 1 | FEATURE | — |
| 486 | `e73dd93a854ec36b09e90f21b8c6cff1282d5209` | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:44:04Z | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:44:04Z | logo update | 1 | UNKNOWN | — |
| 487 | `54cfd4712e7596cb02aa93c87e22897a2948d5aa` | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:40:35Z | kexinhuang12345 / kexinhuang12345 | 2025-05-12T19:40:35Z | init | 0 | UNKNOWN | — |

## Batch summary

- Unique SHAs: `87`.
- Multi-parent surfaces: `20`.
- Explicit subject-to-PR mappings: `14`.
- PR numbers: `#56, #49, #45, #48, #47, #18, #41, #32, #39, #19, #38, #20, #15, #9`.
- Classification counts: `{"BENCHMARK":1,"BUG_FIX":7,"DOC_ONLY":7,"ENVIRONMENT":3,"FEATURE":16,"FORMAT_ONLY":14,"MERGE_ONLY":20,"REMOVAL":3,"UNKNOWN":16}`.

All 487 reachable commits are now indexed, but subject-level classes are not
feature identities. PR mapping, diff analysis, patch IDs, and DAG normalization
remain required before changes/features are counted.

## Evidence

- https://api.github.com/repos/snap-stanford/Biomni/commits?sha=400c1f366b96a35ca253e13c9b06c5076af41d65&per_page=100&page=5
- First commit: https://github.com/snap-stanford/Biomni/commit/4da6a12c06527a0f13247afc9a16781e454e8d99
- Root commit: https://github.com/snap-stanford/Biomni/commit/54cfd4712e7596cb02aa93c87e22897a2948d5aa
