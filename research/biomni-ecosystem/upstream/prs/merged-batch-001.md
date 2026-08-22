# Merged PR Inventory — Batch 001

Parent verification: `VERIFIED` at `2026-08-22T20:38:07Z`. A fresh official
Search API query returned `total_count=111`, `incomplete_results=false`, 100 page
records, first PR `#9`, and last PR `#244`. All 100 recorded PR numbers are unique,
and the classification totals recalculate to the stated summary. Classifications
remain title-only `INFERENCE`; PR metadata is `FACT`.

- **Task ID:** `merged-pr-inventory-001`
- **Status:** `PARTIAL`
- **Scope/query/sort:** official GitHub Search API query `repo:snap-stanford/Biomni is:pr is:merged`; deterministic `sort=created&order=asc`; `per_page=100&page=1`. This is the oldest-created-first first page.
- **Entities discovered globally:** 111 merged pull requests reported by the live query.
- **Entities processed in batch:** 100 pull requests (all records returned on page 1).
- **Pagination completed?:** No (`PARTIAL`).
- **next page:** `2`.
- **discovered_count:** `111`
- **processed_count:** `100`
- **observed_at UTC:** `2026-08-22T20:35:53Z`
- **Claim/evidence posture:** PR metadata below is `FACT` from a Tier-1 official GitHub API response. Preliminary classifications and feature leads are `INFERENCE` from titles only and require diff-level validation.

## Batch summary

- Unique PR authors observed: 36.
- Authors: `amehrjou`, `anngvu`, `divyesh-htree`, `Edison-A-N`, `evolu8`, `ginylil-tech`, `HasanAldhahi`, `HelloWorldLTY`, `igor-sadalski`, `jucor`, `kexinhuang12345`, `kuanlinhuang`, `lxasqjc`, `marcosbolanos`, `MintaYLu`, `MinxZ`, `PabloPauling`, `Pidem`, `PLippmann`, `pre-commit-ci[bot]`, `ryanDing26`, `RyanLi1028`, `SALhik`, `sbonner0`, `serena2z`, `shantanusharma`, `shengyongniu`, `SnowLightPath`, `th86`, `Thiraput01`, `tuln128`, `vlln`, `zancmeresek`, `Zethson`, `zhanxw`, `zskylarli`.
- Preliminary title-only classification counts: BENCHMARK=2, BUG_FIX=14, DEPENDENCY_ONLY=12, DOC_ONLY=12, ENVIRONMENT=6, FEATURE=41, FORMAT_ONLY=1, MERGE_ONLY=3, REFACTOR=3, REMOVAL=3, SECURITY=1, UNKNOWN=2.
- First record: PR #9, created 2025-07-09T20:39:01Z.
- Last record: PR #244, created 2025-10-16T06:35:23Z.
- The GitHub Search response exposes `pull_request.merged_at`, but does **not** expose merge commit SHA, base ref/SHA, or head ref/SHA. Per-item expansion was intentionally not performed in this bounded inventory.

## Per-PR inventory

| PR | Title | Author | Created | Updated | Closed | Merged | Preliminary class | Merge/base/head details |
|---:|---|---|---|---|---|---|---|---|
| [#9](https://github.com/snap-stanford/Biomni/pull/9) | Replace old setup.py based config with pyproject.toml & add pre-commit config | [Zethson](https://github.com/Zethson) | 2025-07-09T20:39:01Z | 2025-07-10T07:00:33Z | 2025-07-10T07:00:33Z | 2025-07-10T07:00:33Z | ENVIRONMENT | Not returned by Search API |
| [#15](https://github.com/snap-stanford/Biomni/pull/15) | Fix logo link in README.md | [jucor](https://github.com/jucor) | 2025-07-10T10:37:16Z | 2025-07-10T16:06:46Z | 2025-07-10T14:37:38Z | 2025-07-10T14:37:38Z | DOC_ONLY | Not returned by Search API |
| [#18](https://github.com/snap-stanford/Biomni/pull/18) | Drug interaction checking tool (Ddinter 2.0) | [PLippmann](https://github.com/PLippmann) | 2025-07-10T14:13:47Z | 2025-07-13T04:29:27Z | 2025-07-13T04:29:27Z | 2025-07-13T04:29:27Z | FEATURE | Not returned by Search API |
| [#19](https://github.com/snap-stanford/Biomni/pull/19) | Add support for local LLMs using Ollama | [sbonner0](https://github.com/sbonner0) | 2025-07-10T14:19:57Z | 2025-07-19T04:43:39Z | 2025-07-12T23:14:53Z | 2025-07-12T23:14:53Z | FEATURE | Not returned by Search API |
| [#20](https://github.com/snap-stanford/Biomni/pull/20) | fix version file | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-07-10T16:01:06Z | 2025-07-10T16:01:13Z | 2025-07-10T16:01:12Z | 2025-07-10T16:01:12Z | BUG_FIX | Not returned by Search API |
| [#32](https://github.com/snap-stanford/Biomni/pull/32) | Add Gemini support | [Thiraput01](https://github.com/Thiraput01) | 2025-07-11T17:35:12Z | 2025-07-12T23:53:34Z | 2025-07-12T23:53:34Z | 2025-07-12T23:53:34Z | FEATURE | Not returned by Search API |
| [#33](https://github.com/snap-stanford/Biomni/pull/33) | add TrialBench data | [shengyongniu](https://github.com/shengyongniu) | 2025-07-12T03:51:41Z | 2025-08-16T23:57:49Z | 2025-08-16T23:57:48Z | 2025-08-16T23:57:48Z | BENCHMARK | Not returned by Search API |
| [#34](https://github.com/snap-stanford/Biomni/pull/34) | Add DETAILS.md for improved documentation | [ginylil-tech](https://github.com/ginylil-tech) | 2025-07-12T10:52:04Z | 2025-07-17T22:38:57Z | 2025-07-17T22:38:57Z | 2025-07-17T22:38:57Z | DOC_ONLY | Not returned by Search API |
| [#38](https://github.com/snap-stanford/Biomni/pull/38) | add more contribution guideline | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-07-12T23:09:10Z | 2025-07-12T23:09:19Z | 2025-07-12T23:09:19Z | 2025-07-12T23:09:19Z | DOC_ONLY | Not returned by Search API |
| [#39](https://github.com/snap-stanford/Biomni/pull/39) | update contrib | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-07-12T23:38:06Z | 2025-07-12T23:38:16Z | 2025-07-12T23:38:16Z | 2025-07-12T23:38:16Z | DOC_ONLY | Not returned by Search API |
| [#41](https://github.com/snap-stanford/Biomni/pull/41) | Custom Model Support | [RyanLi1028](https://github.com/RyanLi1028) | 2025-07-13T00:30:41Z | 2025-07-13T00:34:32Z | 2025-07-13T00:34:31Z | 2025-07-13T00:34:31Z | FEATURE | Not returned by Search API |
| [#42](https://github.com/snap-stanford/Biomni/pull/42) | Add HyperImpute-based imputation tool (GAIN, MissForest, Iterative) to genetics.py | [MintaYLu](https://github.com/MintaYLu) | 2025-07-13T01:28:52Z | 2025-07-17T22:54:26Z | 2025-07-17T22:54:26Z | 2025-07-17T22:54:25Z | FEATURE | Not returned by Search API |
| [#45](https://github.com/snap-stanford/Biomni/pull/45) | Include ChatNT for DNA sequence analysis | [HelloWorldLTY](https://github.com/HelloWorldLTY) | 2025-07-14T01:31:56Z | 2025-07-14T22:42:10Z | 2025-07-14T22:42:10Z | 2025-07-14T22:42:10Z | FEATURE | Not returned by Search API |
| [#47](https://github.com/snap-stanford/Biomni/pull/47) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-07-14T18:11:25Z | 2025-07-14T18:17:34Z | 2025-07-14T18:17:34Z | 2025-07-14T18:17:34Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#48](https://github.com/snap-stanford/Biomni/pull/48) | Feature/add datasets | [serena2z](https://github.com/serena2z) | 2025-07-14T18:27:23Z | 2025-07-14T18:27:44Z | 2025-07-14T18:27:44Z | 2025-07-14T18:27:44Z | FEATURE | Not returned by Search API |
| [#49](https://github.com/snap-stanford/Biomni/pull/49) | Bedrock support | [Pidem](https://github.com/Pidem) | 2025-07-14T19:38:38Z | 2025-07-16T05:25:05Z | 2025-07-16T05:24:58Z | 2025-07-16T05:24:58Z | FEATURE | Not returned by Search API |
| [#54](https://github.com/snap-stanford/Biomni/pull/54) | Dynamic MCP Integration: Biomedical tool ecosystems (e.g., ToolUniverse) | [SnowLightPath](https://github.com/SnowLightPath) | 2025-07-16T15:13:04Z | 2025-08-03T14:04:16Z | 2025-08-03T05:17:45Z | 2025-08-03T05:17:45Z | FEATURE | Not returned by Search API |
| [#55](https://github.com/snap-stanford/Biomni/pull/55) | Integrate Panhuman Azimuth for scalable cell type annotation | [zskylarli](https://github.com/zskylarli) | 2025-07-16T18:20:54Z | 2025-07-18T15:09:47Z | 2025-07-17T22:24:27Z | 2025-07-17T22:24:27Z | FEATURE | Not returned by Search API |
| [#56](https://github.com/snap-stanford/Biomni/pull/56) | fix env install | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-07-16T22:04:19Z | 2025-07-16T22:04:26Z | 2025-07-16T22:04:26Z | 2025-07-16T22:04:26Z | ENVIRONMENT | Not returned by Search API |
| [#59](https://github.com/snap-stanford/Biomni/pull/59) | fix parsing error | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-07-17T05:21:41Z | 2025-07-17T05:21:58Z | 2025-07-17T05:21:58Z | 2025-07-17T05:21:58Z | BUG_FIX | Not returned by Search API |
| [#60](https://github.com/snap-stanford/Biomni/pull/60) | update security | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-07-17T05:32:07Z | 2025-07-17T05:32:13Z | 2025-07-17T05:32:13Z | 2025-07-17T05:32:13Z | SECURITY | Not returned by Search API |
| [#68](https://github.com/snap-stanford/Biomni/pull/68) | Grounding integration | [PLippmann](https://github.com/PLippmann) | 2025-07-18T17:05:31Z | 2025-07-22T04:07:32Z | 2025-07-22T04:07:32Z | 2025-07-22T04:07:32Z | FEATURE | Not returned by Search API |
| [#69](https://github.com/snap-stanford/Biomni/pull/69) | fix environment dependency issues | [serena2z](https://github.com/serena2z) | 2025-07-18T17:17:19Z | 2025-07-18T17:19:16Z | 2025-07-18T17:19:16Z | 2025-07-18T17:19:16Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#70](https://github.com/snap-stanford/Biomni/pull/70) | Add dotenv support for easier environment configuration | [SnowLightPath](https://github.com/SnowLightPath) | 2025-07-19T12:29:04Z | 2025-07-22T04:18:39Z | 2025-07-22T04:18:38Z | 2025-07-22T04:18:38Z | FEATURE | Not returned by Search API |
| [#74](https://github.com/snap-stanford/Biomni/pull/74) | Add aistudio GEMINI Support | [PabloPauling](https://github.com/PabloPauling) | 2025-07-21T13:04:24Z | 2025-07-25T23:05:31Z | 2025-07-25T23:05:31Z | 2025-07-25T23:05:31Z | FEATURE | Not returned by Search API |
| [#76](https://github.com/snap-stanford/Biomni/pull/76) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-07-21T18:18:36Z | 2025-08-03T05:20:00Z | 2025-08-03T05:20:00Z | 2025-08-03T05:20:00Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#77](https://github.com/snap-stanford/Biomni/pull/77) | fix aws bedrock dependency | [serena2z](https://github.com/serena2z) | 2025-07-21T23:15:31Z | 2025-07-22T06:21:10Z | 2025-07-22T06:21:10Z | 2025-07-22T06:21:10Z | BUG_FIX | Not returned by Search API |
| [#79](https://github.com/snap-stanford/Biomni/pull/79) | Add Monarch Initiative integration as a first-class data source | [lxasqjc](https://github.com/lxasqjc) | 2025-07-22T08:59:37Z | 2025-07-25T22:49:24Z | 2025-07-25T22:49:24Z | 2025-07-25T22:49:24Z | FEATURE | Not returned by Search API |
| [#82](https://github.com/snap-stanford/Biomni/pull/82) | added depmap data for whole genome crispr screens, gene dependency an… | [marcosbolanos](https://github.com/marcosbolanos) | 2025-07-22T17:56:56Z | 2025-09-02T13:30:10Z | 2025-07-25T23:19:06Z | 2025-07-25T23:19:06Z | FEATURE | Not returned by Search API |
| [#84](https://github.com/snap-stanford/Biomni/pull/84) | added readme for package conflicts | [serena2z](https://github.com/serena2z) | 2025-07-22T20:27:57Z | 2025-07-22T20:32:25Z | 2025-07-22T20:32:25Z | 2025-07-22T20:32:25Z | DOC_ONLY | Not returned by Search API |
| [#86](https://github.com/snap-stanford/Biomni/pull/86) | solved self.prompt and self.system_prompt not defined | [HasanAldhahi](https://github.com/HasanAldhahi) | 2025-07-23T11:02:49Z | 2025-07-26T17:34:06Z | 2025-07-26T17:34:06Z | 2025-07-26T17:34:06Z | BUG_FIX | Not returned by Search API |
| [#94](https://github.com/snap-stanford/Biomni/pull/94) | Fix: Resolve variable name conflict in self_critic implementation (#93) | [Edison-A-N](https://github.com/Edison-A-N) | 2025-07-25T08:57:10Z | 2025-07-27T03:31:06Z | 2025-07-26T17:32:02Z | 2025-07-26T17:32:02Z | BUG_FIX | Not returned by Search API |
| [#96](https://github.com/snap-stanford/Biomni/pull/96) | pr-79 add tool description for Monarch API database function | [serena2z](https://github.com/serena2z) | 2025-07-25T22:49:57Z | 2025-07-25T22:50:03Z | 2025-07-25T22:50:03Z | 2025-07-25T22:50:03Z | FEATURE | Not returned by Search API |
| [#97](https://github.com/snap-stanford/Biomni/pull/97) | Update README.md | [PabloPauling](https://github.com/PabloPauling) | 2025-07-26T07:14:08Z | 2025-07-26T17:33:42Z | 2025-07-26T17:33:42Z | 2025-07-26T17:33:42Z | DOC_ONLY | Not returned by Search API |
| [#98](https://github.com/snap-stanford/Biomni/pull/98) | added sgRNA datasets | [serena2z](https://github.com/serena2z) | 2025-07-26T07:48:21Z | 2025-07-26T07:48:43Z | 2025-07-26T07:48:42Z | 2025-07-26T07:48:42Z | FEATURE | Not returned by Search API |
| [#100](https://github.com/snap-stanford/Biomni/pull/100) | Add Groq support and make LLM source configurable via environment | [PabloPauling](https://github.com/PabloPauling) | 2025-07-26T20:35:05Z | 2025-08-04T06:31:06Z | 2025-08-04T06:31:06Z | 2025-08-04T06:31:06Z | FEATURE | Not returned by Search API |
| [#102](https://github.com/snap-stanford/Biomni/pull/102) | yield each message  | [evolu8](https://github.com/evolu8) | 2025-07-27T15:29:50Z | 2025-08-05T09:13:49Z | 2025-08-02T05:41:29Z | 2025-08-02T05:41:29Z | FEATURE | Not returned by Search API |
| [#103](https://github.com/snap-stanford/Biomni/pull/103) | update database query function contribution | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-07-27T16:38:53Z | 2025-07-27T16:41:25Z | 2025-07-27T16:41:25Z | 2025-07-27T16:41:25Z | FEATURE | Not returned by Search API |
| [#106](https://github.com/snap-stanford/Biomni/pull/106) | Update llm.py to support deepseek | [th86](https://github.com/th86) | 2025-07-29T19:39:11Z | 2025-08-02T05:41:01Z | 2025-08-02T05:41:01Z | 2025-08-02T05:41:01Z | FEATURE | Not returned by Search API |
| [#108](https://github.com/snap-stanford/Biomni/pull/108) | Fix installation errors. | [HelloWorldLTY](https://github.com/HelloWorldLTY) | 2025-07-30T21:15:56Z | 2025-08-02T05:36:32Z | 2025-08-02T05:36:32Z | 2025-08-02T05:36:32Z | ENVIRONMENT | Not returned by Search API |
| [#112](https://github.com/snap-stanford/Biomni/pull/112) | Add support for Azure OpenAI with azure- model prefix and .env config | [MinxZ](https://github.com/MinxZ) | 2025-08-01T06:51:12Z | 2025-08-04T06:59:17Z | 2025-08-04T06:52:28Z | 2025-08-04T06:52:28Z | FEATURE | Not returned by Search API |
| [#114](https://github.com/snap-stanford/Biomni/pull/114) | Revert "yield each message " | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-08-03T05:07:43Z | 2025-08-03T05:07:52Z | 2025-08-03T05:07:52Z | 2025-08-03T05:07:52Z | REMOVAL | Not returned by Search API |
| [#116](https://github.com/snap-stanford/Biomni/pull/116) | add mcp example | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-08-03T17:02:09Z | 2025-08-03T17:02:17Z | 2025-08-03T17:02:17Z | 2025-08-03T17:02:17Z | DOC_ONLY | Not returned by Search API |
| [#117](https://github.com/snap-stanford/Biomni/pull/117) | add openfda database queries and change database queries to all llm models | [serena2z](https://github.com/serena2z) | 2025-08-04T05:51:15Z | 2025-08-04T05:52:31Z | 2025-08-04T05:52:30Z | 2025-08-04T05:52:30Z | FEATURE | Not returned by Search API |
| [#118](https://github.com/snap-stanford/Biomni/pull/118) | fix readme | [serena2z](https://github.com/serena2z) | 2025-08-04T06:55:50Z | 2025-08-04T06:55:58Z | 2025-08-04T06:55:58Z | 2025-08-04T06:55:58Z | DOC_ONLY | Not returned by Search API |
| [#119](https://github.com/snap-stanford/Biomni/pull/119) | fixed readme again | [serena2z](https://github.com/serena2z) | 2025-08-04T06:59:31Z | 2025-08-20T21:43:37Z | 2025-08-04T06:59:37Z | 2025-08-04T06:59:37Z | DOC_ONLY | Not returned by Search API |
| [#120](https://github.com/snap-stanford/Biomni/pull/120) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-08-04T18:34:25Z | 2025-08-11T21:01:01Z | 2025-08-11T21:01:01Z | 2025-08-11T21:01:01Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#122](https://github.com/snap-stanford/Biomni/pull/122) | Introduce `go_stream` and Refactor Resource Preparation Logic | [Edison-A-N](https://github.com/Edison-A-N) | 2025-08-05T09:12:05Z | 2025-08-21T07:56:43Z | 2025-08-15T01:54:10Z | 2025-08-15T01:54:10Z | REFACTOR | Not returned by Search API |
| [#123](https://github.com/snap-stanford/Biomni/pull/123) | Add license tracking table | [zancmeresek](https://github.com/zancmeresek) | 2025-08-05T09:15:02Z | 2025-08-05T19:15:48Z | 2025-08-05T19:15:48Z | 2025-08-05T19:15:48Z | FEATURE | Not returned by Search API |
| [#126](https://github.com/snap-stanford/Biomni/pull/126) | Generating functions from task descriptions | [tuln128](https://github.com/tuln128) | 2025-08-06T02:58:06Z | 2025-08-15T03:54:06Z | 2025-08-15T02:17:48Z | 2025-08-15T02:17:48Z | FEATURE | Not returned by Search API |
| [#127](https://github.com/snap-stanford/Biomni/pull/127) | Update environment.yml | [serena2z](https://github.com/serena2z) | 2025-08-06T05:34:07Z | 2025-08-20T21:43:34Z | 2025-08-06T05:35:23Z | 2025-08-06T05:35:23Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#128](https://github.com/snap-stanford/Biomni/pull/128) | Update new_software_v004.sh | [serena2z](https://github.com/serena2z) | 2025-08-06T05:35:34Z | 2025-08-20T21:43:32Z | 2025-08-06T05:35:50Z | 2025-08-06T05:35:50Z | ENVIRONMENT | Not returned by Search API |
| [#129](https://github.com/snap-stanford/Biomni/pull/129) | Update llm.py | [PabloPauling](https://github.com/PabloPauling) | 2025-08-06T10:48:12Z | 2025-08-11T20:25:49Z | 2025-08-11T20:25:48Z | 2025-08-11T20:25:48Z | UNKNOWN | Not returned by Search API |
| [#131](https://github.com/snap-stanford/Biomni/pull/131) | Biomni Release 0.0.5 | [serena2z](https://github.com/serena2z) | 2025-08-07T06:59:22Z | 2025-08-07T07:05:25Z | 2025-08-07T07:05:25Z | 2025-08-07T07:05:25Z | MERGE_ONLY | Not returned by Search API |
| [#138](https://github.com/snap-stanford/Biomni/pull/138) | CNVkit workflow + potential solution to env clutter | [marcosbolanos](https://github.com/marcosbolanos) | 2025-08-10T11:01:40Z | 2025-09-02T13:30:07Z | 2025-08-17T00:22:21Z | 2025-08-17T00:22:21Z | FEATURE | Not returned by Search API |
| [#139](https://github.com/snap-stanford/Biomni/pull/139) | Add wget/curl fallback in install_cli_tools.sh | [amehrjou](https://github.com/amehrjou) | 2025-08-11T20:28:33Z | 2025-08-14T21:51:38Z | 2025-08-14T21:51:38Z | 2025-08-14T21:51:38Z | ENVIRONMENT | Not returned by Search API |
| [#141](https://github.com/snap-stanford/Biomni/pull/141) | Removed Datasets and Fixed MCP | [serena2z](https://github.com/serena2z) | 2025-08-12T03:33:55Z | 2025-08-12T03:34:44Z | 2025-08-12T03:34:43Z | 2025-08-12T03:34:43Z | REMOVAL | Not returned by Search API |
| [#143](https://github.com/snap-stanford/Biomni/pull/143) | feat: implement lazy import for LLM dependencies | [Edison-A-N](https://github.com/Edison-A-N) | 2025-08-12T08:21:37Z | 2025-08-21T07:56:14Z | 2025-08-15T02:54:55Z | 2025-08-15T02:54:55Z | REFACTOR | Not returned by Search API |
| [#144](https://github.com/snap-stanford/Biomni/pull/144) | fixed env versions | [serena2z](https://github.com/serena2z) | 2025-08-13T00:12:12Z | 2025-08-13T00:15:02Z | 2025-08-13T00:15:02Z | 2025-08-13T00:15:02Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#149](https://github.com/snap-stanford/Biomni/pull/149) | feat: Add Sphinx documentation build system | [vlln](https://github.com/vlln) | 2025-08-13T09:45:35Z | 2025-08-15T20:25:34Z | 2025-08-15T20:25:34Z | 2025-08-15T20:25:34Z | DOC_ONLY | Not returned by Search API |
| [#153](https://github.com/snap-stanford/Biomni/pull/153) | deprecated opentargetgenetics query | [serena2z](https://github.com/serena2z) | 2025-08-15T01:24:21Z | 2025-08-15T01:26:13Z | 2025-08-15T01:26:13Z | 2025-08-15T01:26:13Z | REMOVAL | Not returned by Search API |
| [#156](https://github.com/snap-stanford/Biomni/pull/156) | Add Lazyslide Support | [ryanDing26](https://github.com/ryanDing26) | 2025-08-16T03:35:20Z | 2025-09-01T22:30:45Z | 2025-09-01T22:30:45Z | 2025-09-01T22:30:45Z | FEATURE | Not returned by Search API |
| [#159](https://github.com/snap-stanford/Biomni/pull/159) | fix: enable F401 unused import checks and clean up imports | [Edison-A-N](https://github.com/Edison-A-N) | 2025-08-17T07:40:21Z | 2025-09-01T22:34:13Z | 2025-09-01T22:34:13Z | 2025-09-01T22:34:13Z | FORMAT_ONLY | Not returned by Search API |
| [#160](https://github.com/snap-stanford/Biomni/pull/160) | Feature/clinical databases and others | [kuanlinhuang](https://github.com/kuanlinhuang) | 2025-08-17T20:49:14Z | 2026-03-13T23:33:22Z | 2025-10-26T23:08:18Z | 2025-10-26T23:08:18Z | FEATURE | Not returned by Search API |
| [#161](https://github.com/snap-stanford/Biomni/pull/161) | Config management | [serena2z](https://github.com/serena2z) | 2025-08-18T01:12:30Z | 2025-08-20T21:42:42Z | 2025-08-20T21:22:06Z | 2025-08-20T21:22:06Z | REFACTOR | Not returned by Search API |
| [#162](https://github.com/snap-stanford/Biomni/pull/162) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-08-18T18:24:35Z | 2025-08-23T17:39:13Z | 2025-08-23T17:39:12Z | 2025-08-23T17:39:12Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#164](https://github.com/snap-stanford/Biomni/pull/164) | Release/v0.0.6 | [serena2z](https://github.com/serena2z) | 2025-08-20T22:49:41Z | 2025-08-20T22:50:10Z | 2025-08-20T22:50:05Z | 2025-08-20T22:50:05Z | MERGE_ONLY | Not returned by Search API |
| [#165](https://github.com/snap-stanford/Biomni/pull/165) | Hotfix/v0.0.6 param naming | [serena2z](https://github.com/serena2z) | 2025-08-20T23:08:06Z | 2025-08-20T23:12:36Z | 2025-08-20T23:12:35Z | 2025-08-20T23:12:35Z | BUG_FIX | Not returned by Search API |
| [#166](https://github.com/snap-stanford/Biomni/pull/166) | update slack link | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-08-21T16:33:00Z | 2025-08-21T16:33:07Z | 2025-08-21T16:33:07Z | 2025-08-21T16:33:07Z | DOC_ONLY | Not returned by Search API |
| [#168](https://github.com/snap-stanford/Biomni/pull/168) | Fix wrong import in lab_bench.py (bioagentos → biomni) | [amehrjou](https://github.com/amehrjou) | 2025-08-23T19:44:07Z | 2025-08-24T17:01:32Z | 2025-08-24T17:01:32Z | 2025-08-24T17:01:32Z | BUG_FIX | Not returned by Search API |
| [#169](https://github.com/snap-stanford/Biomni/pull/169) | Update llm.py | [SALhik](https://github.com/SALhik) | 2025-08-25T05:22:21Z | 2025-08-26T02:57:51Z | 2025-08-26T02:57:51Z | 2025-08-26T02:57:51Z | UNKNOWN | Not returned by Search API |
| [#171](https://github.com/snap-stanford/Biomni/pull/171) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-08-25T18:21:02Z | 2025-08-26T02:57:34Z | 2025-08-26T02:57:34Z | 2025-08-26T02:57:34Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#173](https://github.com/snap-stanford/Biomni/pull/173) | Feature: Synapse integration with search and download | [anngvu](https://github.com/anngvu) | 2025-08-27T00:20:29Z | 2025-09-12T22:10:14Z | 2025-09-01T21:52:53Z | 2025-09-01T21:52:53Z | FEATURE | Not returned by Search API |
| [#176](https://github.com/snap-stanford/Biomni/pull/176) | Update a1.py to allow download sepcific datasets from data lake | [HelloWorldLTY](https://github.com/HelloWorldLTY) | 2025-08-29T15:19:57Z | 2025-09-01T22:16:01Z | 2025-09-01T22:16:00Z | 2025-09-01T22:16:00Z | FEATURE | Not returned by Search API |
| [#179](https://github.com/snap-stanford/Biomni/pull/179) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-09-01T18:23:30Z | 2025-09-01T22:13:05Z | 2025-09-01T22:13:05Z | 2025-09-01T22:13:05Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#181](https://github.com/snap-stanford/Biomni/pull/181) | Fix required parameter parsing for auto-discovered MCP tools | [Edison-A-N](https://github.com/Edison-A-N) | 2025-09-03T00:42:10Z | 2025-09-22T08:32:11Z | 2025-09-12T22:51:50Z | 2025-09-12T22:51:50Z | BUG_FIX | Not returned by Search API |
| [#199](https://github.com/snap-stanford/Biomni/pull/199) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-09-08T18:29:18Z | 2025-09-12T15:37:40Z | 2025-09-12T15:37:40Z | 2025-09-12T15:37:40Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#200](https://github.com/snap-stanford/Biomni/pull/200) | feat: Add commercial mode configuration for license compliance | [lxasqjc](https://github.com/lxasqjc) | 2025-09-09T12:38:53Z | 2025-09-12T23:00:42Z | 2025-09-12T23:00:42Z | 2025-09-12T23:00:42Z | FEATURE | Not returned by Search API |
| [#201](https://github.com/snap-stanford/Biomni/pull/201) | 🔨 New Tool: 10 SOTA celltype transfer algorithms | [igor-sadalski](https://github.com/igor-sadalski) | 2025-09-10T12:27:33Z | 2025-09-12T22:41:42Z | 2025-09-12T22:41:42Z | 2025-09-12T22:41:42Z | FEATURE | Not returned by Search API |
| [#204](https://github.com/snap-stanford/Biomni/pull/204) | 🔨 New Tool: Convert gene names between species | [igor-sadalski](https://github.com/igor-sadalski) | 2025-09-10T17:24:19Z | 2025-09-25T21:42:09Z | 2025-09-25T21:42:09Z | 2025-09-25T21:42:09Z | FEATURE | Not returned by Search API |
| [#205](https://github.com/snap-stanford/Biomni/pull/205) | 🔨 New Tool: Generate ESM embeddings from human ensembl id gene names | [igor-sadalski](https://github.com/igor-sadalski) | 2025-09-12T21:19:29Z | 2025-09-25T22:18:20Z | 2025-09-25T22:18:20Z | 2025-09-25T22:18:20Z | FEATURE | Not returned by Search API |
| [#207](https://github.com/snap-stanford/Biomni/pull/207) | Add pre-processing, segmentation, and registration under bioimaging tools | [MintaYLu](https://github.com/MintaYLu) | 2025-09-14T21:24:00Z | 2025-09-27T03:29:36Z | 2025-09-27T03:29:36Z | 2025-09-27T03:29:36Z | FEATURE | Not returned by Search API |
| [#208](https://github.com/snap-stanford/Biomni/pull/208) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-09-15T18:28:54Z | 2025-09-26T01:55:35Z | 2025-09-26T01:55:35Z | 2025-09-26T01:55:35Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#209](https://github.com/snap-stanford/Biomni/pull/209) | quick prompt fix | [serena2z](https://github.com/serena2z) | 2025-09-16T04:01:16Z | 2025-09-16T04:02:34Z | 2025-09-16T04:02:34Z | 2025-09-16T04:02:34Z | BUG_FIX | Not returned by Search API |
| [#210](https://github.com/snap-stanford/Biomni/pull/210) | PyLabRobot Integration | [serena2z](https://github.com/serena2z) | 2025-09-16T04:18:56Z | 2025-10-09T05:23:25Z | 2025-10-09T04:58:27Z | 2025-10-09T04:58:27Z | FEATURE | Not returned by Search API |
| [#211](https://github.com/snap-stanford/Biomni/pull/211) | add new literature search function | [serena2z](https://github.com/serena2z) | 2025-09-16T04:52:22Z | 2025-09-16T04:53:04Z | 2025-09-16T04:53:04Z | 2025-09-16T04:53:04Z | FEATURE | Not returned by Search API |
| [#212](https://github.com/snap-stanford/Biomni/pull/212) | Adds glycoengineering tools | [shantanusharma](https://github.com/shantanusharma) | 2025-09-16T17:28:02Z | 2025-09-26T01:26:20Z | 2025-09-26T01:26:20Z | 2025-09-26T01:26:20Z | FEATURE | Not returned by Search API |
| [#216](https://github.com/snap-stanford/Biomni/pull/216) | Update fixed_env.yml to fix the errors of google searching not work | [HelloWorldLTY](https://github.com/HelloWorldLTY) | 2025-09-20T18:49:29Z | 2025-09-26T01:41:45Z | 2025-09-26T01:41:45Z | 2025-09-26T01:41:45Z | ENVIRONMENT | Not returned by Search API |
| [#217](https://github.com/snap-stanford/Biomni/pull/217) | 🧰 New Function: Download conversation with your agent as PDF! | [igor-sadalski](https://github.com/igor-sadalski) | 2025-09-23T00:10:57Z | 2025-09-27T09:54:38Z | 2025-09-27T09:54:38Z | 2025-09-27T09:54:38Z | FEATURE | Not returned by Search API |
| [#222](https://github.com/snap-stanford/Biomni/pull/222) | fix openfda query | [serena2z](https://github.com/serena2z) | 2025-09-26T20:12:35Z | 2025-09-26T20:13:09Z | 2025-09-26T20:13:09Z | 2025-09-26T20:13:09Z | BUG_FIX | Not returned by Search API |
| [#223](https://github.com/snap-stanford/Biomni/pull/223) | patched font for unavailable characters | [serena2z](https://github.com/serena2z) | 2025-09-27T10:21:28Z | 2025-09-27T10:21:45Z | 2025-09-27T10:21:45Z | 2025-09-27T10:21:45Z | BUG_FIX | Not returned by Search API |
| [#224](https://github.com/snap-stanford/Biomni/pull/224) | 🔨 New Tool: Generate embeddings with State | [igor-sadalski](https://github.com/igor-sadalski) | 2025-09-27T15:31:26Z | 2025-10-27T00:07:00Z | 2025-10-27T00:07:00Z | 2025-10-27T00:07:00Z | FEATURE | Not returned by Search API |
| [#226](https://github.com/snap-stanford/Biomni/pull/226) | Avoid blocking in google scholar research | [HelloWorldLTY](https://github.com/HelloWorldLTY) | 2025-09-28T15:14:20Z | 2025-10-26T23:12:10Z | 2025-10-26T23:12:10Z | 2025-10-26T23:12:10Z | BUG_FIX | Not returned by Search API |
| [#227](https://github.com/snap-stanford/Biomni/pull/227) | 🔨 New Tool: Transcripformer embeddings | [igor-sadalski](https://github.com/igor-sadalski) | 2025-09-28T15:40:16Z | 2025-10-27T19:55:12Z | 2025-10-27T19:55:12Z | 2025-10-27T19:55:12Z | FEATURE | Not returned by Search API |
| [#229](https://github.com/snap-stanford/Biomni/pull/229) | [pre-commit.ci] pre-commit autoupdate | [pre-commit-ci[bot]](https://github.com/pre-commit-ci%5Bbot%5D) | 2025-09-29T18:21:11Z | 2025-10-27T05:17:42Z | 2025-10-27T05:17:42Z | 2025-10-27T05:17:42Z | DEPENDENCY_ONLY | Not returned by Search API |
| [#230](https://github.com/snap-stanford/Biomni/pull/230) | release 0.0.7 | [serena2z](https://github.com/serena2z) | 2025-09-29T21:18:39Z | 2025-09-29T21:18:46Z | 2025-09-29T21:18:46Z | 2025-09-29T21:18:46Z | MERGE_ONLY | Not returned by Search API |
| [#232](https://github.com/snap-stanford/Biomni/pull/232) | Fix package names to match correct casing | [zhanxw](https://github.com/zhanxw) | 2025-10-02T00:38:16Z | 2025-10-27T00:10:22Z | 2025-10-27T00:10:22Z | 2025-10-27T00:10:22Z | BUG_FIX | Not returned by Search API |
| [#238](https://github.com/snap-stanford/Biomni/pull/238) | eval | [kexinhuang12345](https://github.com/kexinhuang12345) | 2025-10-12T21:30:03Z | 2025-10-13T01:24:30Z | 2025-10-13T01:24:30Z | 2025-10-13T01:24:30Z | BENCHMARK | Not returned by Search API |
| [#240](https://github.com/snap-stanford/Biomni/pull/240) | update readme for biomni-r0 | [RyanLi1028](https://github.com/RyanLi1028) | 2025-10-13T06:19:22Z | 2025-10-13T06:21:10Z | 2025-10-13T06:21:10Z | 2025-10-13T06:21:10Z | DOC_ONLY | Not returned by Search API |
| [#244](https://github.com/snap-stanford/Biomni/pull/244) | fix: update query_reactome() to use current 2025 Reactome API endpoints | [divyesh-htree](https://github.com/divyesh-htree) | 2025-10-16T06:35:23Z | 2025-10-26T23:21:40Z | 2025-10-26T23:21:40Z | 2025-10-26T23:21:40Z | BUG_FIX | Not returned by Search API |

## Substantive changes

The following are substantive leads based only on PR titles; no patch or runtime audit was performed:

- **Scientific/data tools:** #18 DDI/Ddinter, #42 HyperImpute, #45 ChatNT, #55 Panhuman Azimuth, #68 grounding, #79/#96 Monarch, #82 DepMap, #98 sgRNA datasets, #103 database-query contribution, #117 OpenFDA, #138 CNVkit, #156 Lazyslide, #160 clinical databases, #173 Synapse, #176 selective data-lake download, #201 cell-type transfer, #204 cross-species gene-name conversion, #205 ESM embeddings, #207 bioimaging preprocessing/segmentation/registration, #210 PyLabRobot, #211 literature search, #212 glycoengineering, #224 State embeddings, #227 Transcripformer embeddings.
- **Agent/model/platform capabilities:** #19 Ollama, #32/#74 Gemini, #41 custom model support, #49 Bedrock, #54 dynamic MCP/ToolUniverse, #70 dotenv configuration, #100 Groq, #102 message streaming, #106 DeepSeek, #112 Azure OpenAI, #122 `go_stream`/resource-preparation refactor, #126 function generation from task descriptions, #143 lazy LLM imports, #161 configuration management, #181 MCP parameter parsing, #200 commercial-mode license compliance, #217 conversation-to-PDF.
- **Security/compliance lead:** #60 is titled “update security”; #123 adds a license tracking table; #200 adds commercial-mode configuration. Their exact semantics remain unverified.
- **Benchmark/data lead:** #33 TrialBench data and #238 evaluation work may affect evaluation coverage rather than user-facing tools.

## Potential duplicates

These are unresolved lineage hypotheses, not deduplication conclusions:

- #32 and #74: both advertise Gemini support; may be duplicate, alternative, or follow-up implementations.
- #49 and #77: Bedrock support followed by an AWS Bedrock dependency fix.
- #54, #116, #141, and #181: MCP integration, example, later fix/removal-related change, and parsing fix likely share an MCP lineage.
- #79 and #96: Monarch integration followed by its tool description.
- #48, #98, and #141: dataset additions, sgRNA dataset addition, then dataset removal may share a dataset lineage.
- #102 and #114: streaming/yield behavior followed by an explicit revert.
- #117 and #222: OpenFDA integration followed by a query fix.
- #118 and #119: successive README fixes.
- #123 and #200: license/commercial-compliance metadata may overlap functionally.
- #131, #164/#165, and #230: release and immediate hotfix lineages; likely aggregate existing changes rather than independent features.
- #217 and #223: PDF export followed by a font patch.
- #201, #204, #205, #224, and #227: multiple new-tool PRs by the same author; separate advertised functions but shared implementation conventions are possible.

## Potential feature IDs (leads)

No canonical feature IDs were allocated. Candidate lead labels for parent normalization:

- `LEAD_DDINTER_DRUG_INTERACTIONS` — #18
- `LEAD_LOCAL_OLLAMA_LLM` — #19
- `LEAD_GEMINI_PROVIDER` — #32, #74
- `LEAD_CUSTOM_LLM_PROVIDER` — #41
- `LEAD_HYPERIMPUTE` — #42
- `LEAD_CHATNT_DNA_ANALYSIS` — #45
- `LEAD_BEDROCK_PROVIDER` — #49, #77
- `LEAD_DYNAMIC_MCP_TOOLUNIVERSE` — #54, #116, #141, #181
- `LEAD_PANHUMAN_AZIMUTH` — #55
- `LEAD_GROUNDING` — #68
- `LEAD_MONARCH_DATA_SOURCE` — #79, #96
- `LEAD_DEPMAP_DATA` — #82
- `LEAD_SGRNA_DATA` — #98
- `LEAD_GROQ_PROVIDER` — #100
- `LEAD_DEEPSEEK_PROVIDER` — #106
- `LEAD_AZURE_OPENAI_PROVIDER` — #112
- `LEAD_OPENFDA_QUERIES` — #117, #222
- `LEAD_AGENT_STREAMING` — #102, #114, #122
- `LEAD_TASK_TO_FUNCTION_GENERATION` — #126
- `LEAD_CNVKIT_WORKFLOW` — #138
- `LEAD_LAZYSLIDE` — #156
- `LEAD_CLINICAL_DATABASES` — #160
- `LEAD_SYNAPSE_INTEGRATION` — #173
- `LEAD_SELECTIVE_DATALAKE_DOWNLOAD` — #176
- `LEAD_COMMERCIAL_LICENSE_MODE` — #123, #200
- `LEAD_CELLTYPE_TRANSFER_ALGORITHMS` — #201
- `LEAD_CROSS_SPECIES_GENE_NAMES` — #204
- `LEAD_ESM_EMBEDDINGS` — #205
- `LEAD_BIOIMAGING_PIPELINE` — #207
- `LEAD_PYLABROBOT` — #210
- `LEAD_LITERATURE_SEARCH` — #211
- `LEAD_GLYCOENGINEERING_TOOLS` — #212
- `LEAD_CONVERSATION_PDF_EXPORT` — #217, #223
- `LEAD_STATE_EMBEDDINGS` — #224
- `LEAD_TRANSCRIPFORMER_EMBEDDINGS` — #227

## Evidence URLs

- Search UI (same logical query, deterministic order): https://github.com/snap-stanford/Biomni/pulls?q=is%3Apr+is%3Amerged+sort%3Acreated-asc
- GitHub Search API endpoint used: https://api.github.com/search/issues?q=repo%3Asnap-stanford%2FBiomni%20is%3Apr%20is%3Amerged&sort=created&order=asc&per_page=100&page=1
- Individual Tier-1 PR URLs are linked in the inventory table.

## SHAs

- Merge commit SHAs: `UNKNOWN_NOT_RETURNED_BY_SEARCH_API` for all 100 records.
- Base ref/SHA: `UNKNOWN_NOT_RETURNED_BY_SEARCH_API` for all 100 records.
- Head ref/SHA: `UNKNOWN_NOT_RETURNED_BY_SEARCH_API` for all 100 records.
- No SHA was inferred from PR number, dates, or the frozen main baseline.

## PR numbers

`9, 15, 18, 19, 20, 32, 33, 34, 38, 39, 41, 42, 45, 47, 48, 49, 54, 55, 56, 59, 60, 68, 69, 70, 74, 76, 77, 79, 82, 84, 86, 94, 96, 97, 98, 100, 102, 103, 106, 108, 112, 114, 116, 117, 118, 119, 120, 122, 123, 126, 127, 128, 129, 131, 138, 139, 141, 143, 144, 149, 153, 156, 159, 160, 161, 162, 164, 165, 166, 168, 169, 171, 173, 176, 179, 181, 199, 200, 201, 204, 205, 207, 208, 209, 210, 211, 212, 216, 217, 222, 223, 224, 226, 227, 229, 230, 232, 238, 240, 244`

## Uncertainties

- GitHub search counts and indexing are time-dependent; this is a snapshot at the stated UTC time.
- Title-only classification can mislabel the actual patch (especially #60, #68, #103, #123, #129, #141, #160, #169, and #238).
- Search results do not establish whether a PR was squash-merged, rebased, or merge-committed, nor whether its commits remain reachable from the current main branch.
- PR #82's title is returned by the API with a terminal ellipsis character; the inventory preserves the exact returned title rather than reconstructing it.
- “Merged” is based on the official search predicate and returned `merged_at`; it does not by itself establish that every advertised feature remains present at baseline SHA `400c1f366b96a35ca253e13c9b06c5076af41d65`.
- No comments, diffs, files, checks, or external links embedded in PRs were opened.

## Unresolved questions

- What are the merge commit, base, and head SHAs for each PR, and what exact unique change set does each represent?
- Which title-advertised features are still reachable from the frozen main baseline versus reverted, removed, or superseded?
- Which potential duplicate groups share exact SHAs, ancestry, patch IDs, functions, or semantics?
- Does page 2 contain exactly the remaining 11 records under the same live sort snapshot?
- Which security, dependency, dataset, API-term, and license risks attach to each substantive lead?

## Next action

Fetch `page=2&per_page=100&sort=created&order=asc` for the same query, inventory the remaining records, and mark global merged-PR pagination complete only if that response has no further page. A later dedicated PR-depth phase should retrieve merge/base/head SHAs and diffs in bounded batches, then normalize lineages and allocate canonical feature IDs.
