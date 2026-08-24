# Open PR Inventory — `open-pr-inventory-001`

Parent verification: `VERIFIED` at `2026-08-22T20:41:03Z`. Fresh official REST
requests returned 38 records on page 1 and zero on page 2. All PR numbers are
unique; all 38 base and 38 head identities are full 40-character SHAs; first and
last records are `#177` and `#330`. Metadata is `FACT`; title-based classes and
relevance remain `INFERENCE` pending diff review.

## Task ID

`open-pr-inventory-001`

## Scope

Inventory every pull request observed in the `open` state for
`snap-stanford/Biomni`, using the official GitHub REST API. This is a
breadth-first metadata inventory, not a deep audit. Change classes and relevance
are preliminary inferences from PR titles and list metadata; no code, workflow,
package, or other external content was executed.

## Collection summary

- `observed_at UTC`: `2026-08-22T20:35:28Z`
- `discovered_count`: `38`
- `processed_count`: `38`
- Entities discovered/processed: 38 open PRs by 27 distinct author usernames.
- Pagination completed?: **yes**. Page 1 with `per_page=100` returned 38
  records and no `rel="next"`; an explicit page 2 request returned an empty
  array and reported page 1 as `rel="last"`.
- Labels: no labels were present on any of the 38 list records.
- Drafts: all 38 list records reported `draft=false`.
- Mergeability: not present in the list response, so recorded as `NA` rather
  than inferred.
- Commit/file counts and file lists: not present in the list response. They were
  not collected because doing so through REST would require high-volume
  per-PR requests. Counts are recorded as `NA`; preliminary relevance therefore
  uses primary list metadata only.

## Per-PR inventory

Legend for `D/L/M/C/F`: `draft / labels / mergeability / commit count / changed
file count`; `N` = false, `—` = none, `NA` = not available in the batched list
response. `Class; relevance` is an `INFERENCE`, not a code-level conclusion.

| PR | Title | Author | Created / updated (UTC) | Base ref @ full SHA | Head ref @ full SHA | D/L/M/C/F | Preliminary class; relevance |
|---:|---|---|---|---|---|---|---|
| [#177](https://github.com/snap-stanford/Biomni/pull/177) | Feature: Add comprehensive reasoning trace tracking and reporting system with batch and interactive agent | `amehrjou` | 2025-08-29T19:28:29Z / 2025-09-30T18:52:19Z | `main@b5ad0c7bf4c6c3386b9d73da9656f4d6f257d36a` | `amehrjou:eval-reasoning-trace-local@56e6272f30e560d23e327b92f5766d316434c9d6` | N/—/NA/NA/NA | FEATURE; HIGH — reasoning trace/evaluation |
| [#182](https://github.com/snap-stanford/Biomni/pull/182) | Fix: a1 agent pass empty message to AWSbedrock error | `changwn` | 2025-09-03T18:39:51Z / 2025-09-03T18:40:40Z | `main@b5ad0c7bf4c6c3386b9d73da9656f4d6f257d36a` | `changwn:fix-AWSbedrock-emptyMessage@1ff2629c221c58175301cb7fe97ccc506ba6a296` | N/—/NA/NA/NA | BUG_FIX; MEDIUM — Bedrock route correctness |
| [#228](https://github.com/snap-stanford/Biomni/pull/228) | Adapt MCP schemas for OpenAI | `vladsavelyev` | 2025-09-29T09:57:22Z / 2025-09-29T09:57:31Z | `main@b769281b14f53ea9670d71028d1f38449a5e4f53` | `vladsavelyev:tmp-navari-adapt@94749c146799347e33eb5f2a95510ae35185cbe1` | N/—/NA/NA/NA | BUG_FIX/FEATURE; HIGH — MCP/OpenAI interoperability |
| [#231](https://github.com/snap-stanford/Biomni/pull/231) | New Tool: Geneformer embeddings | `igor-sadalski` | 2025-09-30T12:34:34Z / 2025-09-30T22:30:35Z | `main@eb22cef6f35ddaf10cefd7f25c4b9f816eaf3fce` | `igor-sadalski:geneformer_embeddings@91244ff63976a07a291ad1e9cf3b16529ffe42c4` | N/—/NA/NA/NA | FEATURE; HIGH — new scientific tool |
| [#235](https://github.com/snap-stanford/Biomni/pull/235) | feat: add data sandbox mode for isolated file operations | `lxasqjc` | 2025-10-06T09:05:31Z / 2025-10-06T12:49:37Z | `main@eb22cef6f35ddaf10cefd7f25c4b9f816eaf3fce` | `lxasqjc:data-sandbox@ca2953d694b1ad965dd8e3ccf28917aae4cc1eaa` | N/—/NA/NA/NA | SECURITY/FEATURE; HIGH — filesystem isolation |
| [#236](https://github.com/snap-stanford/Biomni/pull/236) | feat: Add human-in-the-loop interactive mode for Biomni agents | `lxasqjc` | 2025-10-07T08:18:15Z / 2025-10-19T00:34:09Z | `main@eb22cef6f35ddaf10cefd7f25c4b9f816eaf3fce` | `lxasqjc:human-in-the-loop@8a23551df9a7f79ff8c14f4a68f60c3ffc0a70c1` | N/—/NA/NA/NA | FEATURE; HIGH — agent interaction/control |
| [#245](https://github.com/snap-stanford/Biomni/pull/245) | Add HuggingFace support | `ryanDing26` | 2025-10-19T18:25:27Z / 2025-10-19T18:28:21Z | `main@8fd7b218c43b78538f79cd93d05db43d8a8073c6` | `ryanDing26:huggingface_integration@e1a9cc3372eb6ebb798a550ba6944521481c4fc5` | N/—/NA/NA/NA | FEATURE; HIGH — model/provider integration |
| [#273](https://github.com/snap-stanford/Biomni/pull/273) | [pre-commit.ci] pre-commit autoupdate | `pre-commit-ci[bot]` | 2026-01-19T18:50:09Z / 2026-08-17T19:17:42Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `snap-stanford:pre-commit-ci-update-config@03c7bcf2cbb73e9a66ce563e4ba3393f66496b30` | N/—/NA/NA/NA | DEPENDENCY_ONLY/ENVIRONMENT; LOW |
| [#275](https://github.com/snap-stanford/Biomni/pull/275) | chore: add codespell support (config, workflow to detect/not fix) and make it fix some typos | `yarikoptic` | 2026-01-21T03:05:09Z / 2026-01-21T03:05:09Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `yarikoptic:enh-codespell@4f7edeced4570b6c7050a4d02f397f1933520663` | N/—/NA/NA/NA | ENVIRONMENT/FORMAT_ONLY; LOW |
| [#276](https://github.com/snap-stanford/Biomni/pull/276) | Refactor genomics.py: lazy-load optional dependencies | `andrewsu` | 2026-01-23T20:33:26Z / 2026-01-23T20:33:26Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `andrewsu:fix/lazy-import-optional-dependencies-clean@9701cee9cde9c8f65a756d132ad02a39083755f1` | N/—/NA/NA/NA | REFACTOR/BUG_FIX; MEDIUM — optional dependency loading |
| [#277](https://github.com/snap-stanford/Biomni/pull/277) | BioThings / SmartAPI KPClient tool | `ahueb` | 2026-01-27T15:59:34Z / 2026-02-22T02:14:31Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `andrewsu:biothings_tools@0ed9958ba0da54d0d5f652a8fdfdc761c5bc2cfd` | N/—/NA/NA/NA | FEATURE; HIGH — new database/API tool |
| [#278](https://github.com/snap-stanford/Biomni/pull/278) | feat: Add AlphaFold3 structure prediction tool | `yaswanth169` | 2026-01-27T19:24:48Z / 2026-01-27T19:24:59Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `yaswanth169:main@c5dbf05d804d3ad6bc8f8ddf117bc68fe432d69f` | N/—/NA/NA/NA | FEATURE; HIGH — new structure tool |
| [#280](https://github.com/snap-stanford/Biomni/pull/280) | Add multi-provider LLM support and two-tier model configuration | `goodb` | 2026-02-11T22:33:39Z / 2026-03-01T06:02:34Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `goodb:goodb-wobd@b5bf07aa9a2d8bdf71f91d32f0d55bcad1c9c090` | N/—/NA/NA/NA | FEATURE/REFACTOR; HIGH — LLM routing/configuration |
| [#281](https://github.com/snap-stanford/Biomni/pull/281) | feat: Add adaptive tool execution analytics and intelligent retry system | `Rakshitha-Ireddi` | 2026-02-13T18:21:40Z / 2026-02-13T18:25:10Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `Rakshitha-Ireddi:feature/execution-analytics-adaptive-retry@5607841205943a8eb9b8904d08db00d549355c30` | N/—/NA/NA/NA | FEATURE; HIGH — execution analytics/retry |
| [#286](https://github.com/snap-stanford/Biomni/pull/286) | Fix UnicodeDecodeError when loading know-how docs on Windows | `aevo98765` | 2026-03-02T21:05:09Z / 2026-03-02T21:08:00Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `aevo98765:fix/windows-utf8-encoding-knowhow@36739a242b867564696ec34c5f05e2f993b5e220` | N/—/NA/NA/NA | BUG_FIX; MEDIUM — Windows portability |
| [#288](https://github.com/snap-stanford/Biomni/pull/288) | Add DISGENET API integration as a new database tool | `MoiraClimentGispert` | 2026-03-12T11:08:23Z / 2026-03-12T11:45:11Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `MoiraClimentGispert:feature/disgenet@9fb948695d1b26eec82c2a41380b2c246ef61d3b` | N/—/NA/NA/NA | FEATURE; HIGH — new database/API tool |
| [#291](https://github.com/snap-stanford/Biomni/pull/291) | feat: add TruthSeq gene regulatory validation tools | `rsflinn` | 2026-03-24T04:40:45Z / 2026-03-24T04:40:55Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `rsflinn:feature/truthseq-regulatory-validation@6bc88cd10afc6801a18f9624aeaa81835c90d90a` | N/—/NA/NA/NA | FEATURE; HIGH — new scientific tools |
| [#292](https://github.com/snap-stanford/Biomni/pull/292) | Add Dockerfile and entrypoint for containerized deployment | `inodb` | 2026-03-24T17:19:08Z / 2026-05-21T15:57:28Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `knowledgesystems:biomni-deploy@e670aba33afd6fa85676f50887ade591ab85682d` | N/—/NA/NA/NA | ENVIRONMENT; HIGH — deployment surface, security review needed |
| [#293](https://github.com/snap-stanford/Biomni/pull/293) | display and save plots, keep files in session memory, add stop button | `yohyoh-wang` | 2026-03-25T14:52:15Z / 2026-04-27T13:46:36Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `yohyoh-wang:local_ui@9eff2202e7192997c842fe5355aa1ec509a956de` | N/—/NA/NA/NA | FEATURE; HIGH — UI/session artifact handling |
| [#299](https://github.com/snap-stanford/Biomni/pull/299) | Feature/frap analysis | `r-siddiqi` | 2026-05-03T00:23:55Z / 2026-05-03T00:23:55Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `r-siddiqi:feature/frap-analysis@5602554200033ab1f2a17b49c42e88647e062869` | N/—/NA/NA/NA | FEATURE; HIGH — new bioimaging analysis |
| [#301](https://github.com/snap-stanford/Biomni/pull/301) | setup.sh: pre-install numpy and cython before pystan | `starboy-3` | 2026-06-11T18:50:06Z / 2026-06-11T18:50:06Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `starboy-3:fix/283-setup-numpy-cython@061ae499cfb6a484a935be59df693b7beaa1d9a3` | N/—/NA/NA/NA | ENVIRONMENT/BUG_FIX; MEDIUM — installation ordering |
| [#303](https://github.com/snap-stanford/Biomni/pull/303) | feat: add Research Knowledge Graph module (Phase 1) | `Nigmat-future` | 2026-06-12T08:28:45Z / 2026-06-12T08:29:55Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `Nigmat-future:feature/knowledge-graph@7dcd124142ac78b8422a36e0f057eab9111c3e88` | N/—/NA/NA/NA | FEATURE; HIGH — new knowledge-graph module |
| [#306](https://github.com/snap-stanford/Biomni/pull/306) | feat(database): add 1000 Genomes Project individual-level query tools | `de-grave` | 2026-07-11T07:01:28Z / 2026-07-11T07:01:28Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `de-grave:1000G@87a0a7e387142902cc6fbf3c2cad95f9017e364e` | N/—/NA/NA/NA | FEATURE; HIGH — new database tools/data terms review |
| [#308](https://github.com/snap-stanford/Biomni/pull/308) | Fix missing biomni.agent.base_agent module (#285) | `jissen706` | 2026-07-20T20:25:23Z / 2026-07-20T20:25:23Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `jissen706:fix/missing-base-agent-module@199b595ba2220a7708e06a632f4664dd313671d0` | N/—/NA/NA/NA | BUG_FIX; HIGH — agent import/runtime surface |
| [#312](https://github.com/snap-stanford/Biomni/pull/312) | Add DeepSpot-M tool: predict spatial gene expression from an H&E histology tile | `KalinNonchev` | 2026-08-03T18:00:01Z / 2026-08-03T19:12:32Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `KalinNonchev:add-deepspotm@054ca8bef4cb768ec82067a7882b87a014642a32` | N/—/NA/NA/NA | FEATURE; HIGH — new pathology/spatial tool |
| [#315](https://github.com/snap-stanford/Biomni/pull/315) | feat: make marsilea visible to the agent | `Mr-Milk` | 2026-08-15T15:59:38Z / 2026-08-15T16:01:31Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `Mr-Milk:add-marsilea-library@02e4541a04fbb7bad5dedfd420df2eabada2e2a4` | N/—/NA/NA/NA | FEATURE/ENVIRONMENT; MEDIUM — expose visualization library |
| [#316](https://github.com/snap-stanford/Biomni/pull/316) | Add gene symbol to Ensembl ID conversion tool | `reacher-z` | 2026-08-18T14:16:03Z / 2026-08-18T14:16:03Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:feat/gene-symbol-ensembl-converter@5eadf56dd8943bcfe132f2ad80c6b5847230ef70` | N/—/NA/NA/NA | FEATURE; HIGH — new identifier conversion tool |
| [#317](https://github.com/snap-stanford/Biomni/pull/317) | Implement missing registration visualization tool | `reacher-z` | 2026-08-18T14:28:01Z / 2026-08-18T14:28:01Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:fix/registration-visualization@dd8652dbd193b68b276dbfd2188d2c47383ffc78` | N/—/NA/NA/NA | BUG_FIX/FEATURE; HIGH — missing implementation |
| [#318](https://github.com/snap-stanford/Biomni/pull/318) | Fix custom provider environment variable mismatch | `reacher-z` | 2026-08-18T14:33:36Z / 2026-08-20T03:32:46Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:fix/custom-provider-env-aliases@5ba4b3868538fd6950a007ef077075da38577804` | N/—/NA/NA/NA | BUG_FIX; HIGH — provider configuration |
| [#319](https://github.com/snap-stanford/Biomni/pull/319) | Fix observation tag mismatch in agent prompt | `reacher-z` | 2026-08-18T14:39:09Z / 2026-08-18T14:39:09Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:fix/observation-tag@db8e5ed26438692d4941a861dc7c3d5c9318055e` | N/—/NA/NA/NA | BUG_FIX; HIGH — agent protocol correctness |
| [#320](https://github.com/snap-stanford/Biomni/pull/320) | Fix Cellpose 4 segmentation and output handling | `reacher-z` | 2026-08-18T15:08:32Z / 2026-08-18T15:08:32Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:fix/cellpose-v4-segmentation@dd04cc4876205c5256292c6084fd8f497814241f` | N/—/NA/NA/NA | BUG_FIX; HIGH — bioimaging tool correctness |
| [#321](https://github.com/snap-stanford/Biomni/pull/321) | Add CIViC mutation-aware evidence retrieval tool | `reacher-z` | 2026-08-18T15:23:33Z / 2026-08-18T15:23:33Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:feat/civic-variant-evidence@f2653bd59ad5d563f07a720b8f5c7a8843661009` | N/—/NA/NA/NA | FEATURE; HIGH — new cancer evidence tool |
| [#322](https://github.com/snap-stanford/Biomni/pull/322) | Fix schema prompt rendering with literal JSON examples | `reacher-z` | 2026-08-18T15:29:08Z / 2026-08-18T15:29:08Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:fix/schema-template-substitution@3c67054ef54e1974711834997cbd501472ea9c7b` | N/—/NA/NA/NA | BUG_FIX; HIGH — schema/prompt correctness |
| [#323](https://github.com/snap-stanford/Biomni/pull/323) | Add GlyGen glycosylation evidence query tool | `reacher-z` | 2026-08-18T15:51:26Z / 2026-08-18T15:51:26Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:feat/glygen-query@280991f01cdf22f21efdbc4a45c1baf75ad8e666` | N/—/NA/NA/NA | FEATURE; HIGH — new glycosylation database tool |
| [#325](https://github.com/snap-stanford/Biomni/pull/325) | Expose optional parameters in agent tool schemas | `reacher-z` | 2026-08-18T15:58:53Z / 2026-08-20T03:32:36Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `reacher-z:fix/optional-tool-parameters@6efd5b31e7548ea63593adfbaf45433d665755e9` | N/—/NA/NA/NA | BUG_FIX/FEATURE; HIGH — tool-schema fidelity |
| [#328](https://github.com/snap-stanford/Biomni/pull/328) | Fix ClinicalTrials.gov API v2 parameter handling | `QING1105` | 2026-08-20T05:16:00Z / 2026-08-20T05:16:29Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `QING1105:fix/clinicaltrials-params@10e94bf968179824a26d57aedc776b486f66891b` | N/—/NA/NA/NA | BUG_FIX; HIGH — database API correctness |
| [#329](https://github.com/snap-stanford/Biomni/pull/329) | fix: handle GRAPH_RECURSION_LIMIT gracefully and prevent state buildup (#237) | `QING1105` | 2026-08-20T07:42:32Z / 2026-08-20T08:01:09Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `QING1105:fix/recursion-limit-summary@250593271721e87e4a6d02896dbfea9d16fa9b99` | N/—/NA/NA/NA | BUG_FIX; HIGH — agent state/resource handling |
| [#330](https://github.com/snap-stanford/Biomni/pull/330) | Spatial Transcriptomics (10x Visium) Analysis Tools | `QING1105` | 2026-08-21T17:05:08Z / 2026-08-21T17:05:20Z | `main@400c1f366b96a35ca253e13c9b06c5076af41d65` | `QING1105:feat/spatial-transcriptomics-tools@ef75a199f4786704520bd16a4bce4da0ad2ef4ee` | N/—/NA/NA/NA | FEATURE; DEEP_AUDITED STATIC — `change-000076`, ezST-derived `lineage-000029`; reject as-is |

## Substantive changes

The title/metadata screen flagged 36 of 38 PRs. PR #330 is now statically
deep-audited and lineage-normalized; 35 flagged PRs remain for later diff review.
The highest-value capability families are:

- Agent architecture and control: #177, #236, #281, #293, #303, #308, #319,
  #329.
- Security/deployment/session boundaries: #235, #292, #293.
- LLM/MCP/tool-schema interoperability: #182, #228, #245, #280, #318, #322,
  #325.
- New scientific/database capabilities: #231, #277, #278, #288, #291, #299,
  #306, #312, #316, #317, #321, #323, #330.
- Runtime, dependency, and platform correctness: #276, #286, #301, #315, #320,
  #328.

PRs #273 and #275 appear low relevance to independent Biomni capabilities and
can remain indexed without priority deep audit unless their diffs reveal more
than their titles indicate.

## Potential duplicates

These are only lineage leads; no duplicate relation is established without SHA,
patch-ID, diff, and function-level comparison.

- #245 and #280 both touch the model/provider integration family. #280 also
  overlaps conceptually with the eight provider routes already present at the
  frozen upstream baseline, so it may be partially superseded or alternative.
- #228, #322, and #325 all concern schema adaptation/rendering/fidelity. They may
  be complementary fixes on one implementation surface rather than three
  independent features.
- #235 and #293 both affect file/session handling, but their titles suggest
  isolation versus persistence/UI concerns, respectively.
- #277 and #316 may share gene-identifier normalization behavior; compare at the
  function level before assigning separate canonical implementations.

## Potential feature IDs (leads)

These are provisional lead labels, not canonical database IDs:

- `LEAD-PR177-REASONING-TRACE`
- `LEAD-PR235-DATA-SANDBOX`
- `LEAD-PR236-HUMAN-IN-LOOP`
- `LEAD-PR245-HUGGINGFACE-PROVIDER`
- `LEAD-PR277-BIOTHINGS-SMARTAPI`
- `LEAD-PR278-ALPHAFOLD3-TOOL`
- `LEAD-PR281-ADAPTIVE-RETRY-ANALYTICS`
- `LEAD-PR288-DISGENET-TOOL`
- `LEAD-PR291-TRUTHSEQ-TOOLS`
- `LEAD-PR293-LOCAL-UI-SESSION-ARTIFACTS`
- `LEAD-PR299-FRAP-ANALYSIS`
- `LEAD-PR303-RESEARCH-KNOWLEDGE-GRAPH`
- `LEAD-PR306-1000-GENOMES-TOOLS`
- `LEAD-PR312-DEEPSPOT-M`
- `LEAD-PR321-CIVIC-VARIANT-EVIDENCE`
- `LEAD-PR323-GLYGEN-QUERY`
- `LEAD-PR330-SPATIAL-TRANSCRIPTOMICS`

## Evidence URLs

- Official collection page 1 (38 records):
  https://api.github.com/repos/snap-stanford/Biomni/pulls?state=open&sort=created&direction=asc&per_page=100&page=1
- Official exhaustion check, page 2 (0 records):
  https://api.github.com/repos/snap-stanford/Biomni/pulls?state=open&sort=created&direction=asc&per_page=100&page=2
- Each PR number in the inventory table links to its official GitHub PR page.
- Full head and base SHAs are preserved per PR in the table; the list API is the
  primary source for those identities.

## Uncertainties

- `mergeable`, `commits`, `changed_files`, file paths, additions/deletions, and
  commit ancestry were not directly available in the batched list response.
- A PR's listed base SHA records the base at the response's PR metadata, not
  necessarily the current `main` HEAD; several early PRs have pre-baseline base
  SHAs and may be stale or conflict-prone.
- Titles can overstate, understate, or misclassify actual patches. All relevance,
  substantive-change, and potential-duplicate judgments remain `INFERENCE`.
- The result captures publicly observable GitHub state at one timestamp; state,
  labels, heads, and counts may change later.

## Unresolved questions

- Which 36 flagged PRs contain unique patches after comparison with main, merged
  PRs, closed-unmerged PRs, branches, forks, and one another?
- Which PR heads are mergeable or have conflicts against current main?
- What are the exact file/function surfaces, dependencies, tests, licenses, and
  security implications of each high-relevance candidate?
- Is #280 an alternative or superseded model-routing implementation relative to
  current main, and are #228/#322/#325 independent changes or one schema lineage?

## Next action

Perform a request-budgeted static diff audit of the high-relevance PRs, beginning
with #235, #228/#322/#325, #177, #236, #281, #292/#293, and the new scientific
tool PRs. Capture file lists and commit ancestry in batches where possible, then
deduplicate against the frozen main baseline and the merged/closed PR inventories
before assigning canonical feature or implementation IDs.
