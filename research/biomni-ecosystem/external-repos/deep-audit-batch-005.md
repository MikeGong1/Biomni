# External Deep Audit Batch 005

Observed at: `2026-08-23T18:17:54Z`

Scope: stable external-family queue orders `13`–`62`, inclusive.

## Result

This accelerated checkpoint closes 50 families containing 58 bounded repository
records. The exact result distribution is:

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 22 |
| `NO_UNIQUE` | 22 |
| `DOC_ONLY` | 3 |
| `EMPTY` | 3 |
| **Total** | **50** |

All 50 families are `DEEP_AUDITED` for the bounded static surface. The 22
substantive families preserve `change-000092`–`change-000113`; four exact
PR/derivation relationships preserve `lineage-000036`–`lineage-000039`. No
Feature or Implementation ID was allocated. Every direct-adoption decision is a
rejection; useful elements remain evidence-bounded design or clean-room leads.

The canonical machine record is
`external-repos/deep-audit-batch-005-manifest.jsonl`. It preserves immutable
SHAs, ref/PR/pagination summaries, scientific/security/license findings,
verifier corrections, canonical IDs, and hashes of the parent-reviewed worker
and verifier result files. Temporary local paths are not part of the canonical
record.

## Method and evidence boundary

- Nine mutually exclusive research shards plus rotated verification slots handled
  the family orders; GitHub requests shared the committed four-slot,
  60-request/minute queue.
- Bulk metadata used GraphQL where useful; refs and history used SSH mirrors,
  with DAG, ancestry, diff and patch-id reduction performed locally.
- Native refs and bounded pull/release/fork connections were exhausted or closed
  by an explicit short/empty terminal page where the manifest says complete.
- Third-party code, tests, models, installers and workflows were never executed.
- External repository instructions were treated as untrusted research data.
- Source owners outside the pre-existing person universe were used only to close
  lineage evidence; they did not expand `person_depth=1`.
- Eight independent verification shards rechecked the 50-family reduction. No
  result-class reversal was required. Their wording/count/evidence-boundary
  corrections are applied in the manifest.

## Substantive candidates

### Platforms, agents and workflows

- `Mr-Milk/Aquila-next` (`change-000092`) is a substantive spatial-data platform,
  but unresolved repository licensing, path/file selection, database URL
  logging, unauthenticated resource exhaustion, disabled SSH host verification,
  research-data egress and unvalidated scientific routines block adoption.
- ChatSpatial PR 31 (`change-000093`, `lineage-000036`) adds a DeepSpot-M
  histology workflow, but does not enforce physical scale, relies on fake-model
  tests, leaves timed-out compute running and lacks a closed model/provenance and
  sensitive-image contract.
- `lulaiao/EGVR-Agent` (`change-000094`, `lineage-000037`) derives materially
  from `CAi_copilot`. Removing arbitrary generated-code execution is a security
  improvement; claimed real-tool, verifier, clinical and privacy contracts are
  still not validated.
- `shengyongniu/ai-coscientist-protein` (`change-000098`) contains useful staged
  agent and audit-schema ideas, but does not establish target-specific binding;
  resume/FSDP, checkpoint trust, model/data provenance and network controls fail
  the integration contract.
- `Nigmat-future/Bioagent` (`change-000101`) executes generated host Python and
  exposes SSRF, path-write, tar, package-install and pickle surfaces without a
  real sandbox or approval policy; scientific templates and packaging are also
  incomplete.
- `Nigmat-future/TopoLogos` (`change-000102`) is retained as a prompt/template
  artifact only. Normalization, deconvolution, cell interaction,
  pseudoreplication and plotting contracts fail, while plaintext cross-session
  memory creates a privacy boundary failure.
- `lishengting/PaperInt` (`change-000103`) is a substantive paper pipeline, but
  mixed-provenance deduplication, fail-open PDF validation, partial-result status,
  full-PDF external LLM egress and missing prompt/model provenance block reuse.

### Single-cell, spatial and statistical methods

- scvi-tools PR 2775 (`change-000095`, `lineage-000038`) is the sole substantive
  bounded-owner delta in its family. `Normal.scale` is exposed as normalized
  expression, the latent-library branch can use `pl=None`, and log-normalized
  input retains incompatible count/log/library scaling. The closed PR added no
  validating test or benchmark.
- `KalinNonchev/gnomAD_DB` (`change-000096`) is a possible local frequency-cache
  reference only. Variant normalization/left alignment, PASS defaults,
  build/release provenance, safe SQL/download behavior, data terms and
  release-specific validation are absent.
- `Harrydirk41/UniFlow` (`change-000097`) has token, cache-key, chain-concatenation
  and sequence-length contract defects that can silently corrupt protein-model
  inputs and cached outputs.
- `HelloWorldLTY/scEval` (`change-000100`) contains benchmark leads, but hardcoded
  batch assumptions, reversed Tangram logic, invalid CUDA handling, shell/pickle
  and tracking-service risks, absent tests and absent license block reuse.
- `leezx/RToolbox` (`change-000106`) has no license or package/test boundary,
  sources mutable remote code, and contains two material PPI analysis defects.
- `little2b/COMET` (`change-000107`) has a degenerate single-token attention
  fusion and undefined/possibly non-finite all-zero-mask behavior, with no
  weights, training provenance or external validation.
- `KalinNonchev/azimuthpy` (`change-000108`) is a small clean-room wrapper lead,
  not a reusable implementation: `use_layer` is ignored, caller strings reach
  executable R syntax, dense conversion/order alignment is unsafe, and versions
  and tests are absent.
- `HelloWorldLTY/scELMo` (`change-000109`) leaks training/ground-truth information
  into claimed zero-shot evaluation, while remote pickle/unverified archive,
  shell path and external gene-list flows create execution and privacy blockers.
- `mickaelleclercq/BioDiscML` (`change-000112`) performs supervised filtering
  before cross-validation, adaptively reuses the same CV and can use the test set
  for selection. Java deserialization, bundled jars, GPL/provenance and privacy
  boundaries add independent blockers.

### Skills, MCP and CRISPR

- `vlln/bio-skills` (`change-000099`) is a three-Skill bundle without a root
  license. Production Zenodo publication/deletion, certificate bypass and bearer
  handling lack approval and safety boundaries; only design requirements remain.
- `Nigmat-future/biomedical-skill-suite` (`change-000104`) contains 35 Skills but
  no repository license and scientific contracts too shallow for direct use.
- `Nigmat-future/biomedical-codex-skills` (`change-000105`) contains nine Skills;
  fixed QC thresholds, silent sample selection, reversed status logic, no resource
  headroom, unredacted configuration and path escape require a corrected rewrite.
- `de-grave/onekgpd-mcp` (`change-000110`) uses plaintext gRPC, trust-all TLS and
  maps failures to empty biological results. Genotype/kinship privacy and
  scientific completeness require an authoritative clean-room design.
- CRISPR-GPT open PR 2 (`change-000111`, `lineage-000039`) replaces one
  LLM-to-`eval` path with a whitelist, but the released source still has global
  multi-user state, public sharing, plaintext logs, unlicensed software and
  unsafe experimental claims. Closed PR 3's plasmid output is not
  synthesis-ready.
- `PabloPauling/posebusters-mcp-server` (`change-000113`) is a small licensed
  wrapper lead, but its MCP contract is custom, behavior depends on an unpinned
  external executable, subprocess failure can appear as green `0/0`, and upload
  privacy/concurrency controls are insufficient.

## Complete family ledger

| Order | Family source | Bounded repository IDs | Result | Change | Lineage |
|---:|---|---|---|---|---|
| 13 | `Mr-Milk/Aquila-next` | repo-003113 | DEEP_AUDIT_CANDIDATE | change-000092 | N/A |
| 14 | `TissueImageAnalytics/tiatoolbox` | repo-003023 | NO_UNIQUE | N/A | N/A |
| 15 | `cafferychen777/ChatSpatial` | repo-002993 | DEEP_AUDIT_CANDIDATE | change-000093 | lineage-000036 |
| 16 | `jdidion/biotools` | repo-002991, repo-007256 | NO_UNIQUE | N/A | N/A |
| 17 | `lulaiao/EGVR-Agent` | repo-003095 | DEEP_AUDIT_CANDIDATE | change-000094 | lineage-000037 |
| 18 | `scverse/scvi-tools` | repo-001348, repo-002939, repo-007292 | DEEP_AUDIT_CANDIDATE | change-000095 | lineage-000038 |
| 19 | `p-gueguen/Spatial_transcriptomics_tools` | repo-003020 | NO_UNIQUE | N/A | N/A |
| 20 | `hurry060215-tech/spatial-transcriptomics-python-methods` | repo-003019 | NO_UNIQUE | N/A | N/A |
| 21 | `KalinNonchev/gnomAD_DB` | repo-003001 | DEEP_AUDIT_CANDIDATE | change-000096 | N/A |
| 22 | `SindiLab/Deep-Learning-in-Spatial-Transcriptomics-Analysis` | repo-002996 | NO_UNIQUE | N/A | N/A |
| 23 | `hrlblab/computer_vision_spatial_omics` | repo-002995 | DOC_ONLY | N/A | N/A |
| 24 | `crazyhottommy/awesome_spatial_omics` | repo-002986 | NO_UNIQUE | N/A | N/A |
| 25 | `LiudengZhang/awesome-spatial-omics` | repo-002981 | NO_UNIQUE | N/A | N/A |
| 26 | `mikelove/awesome-multi-omics` | repo-002965 | DOC_ONLY | N/A | N/A |
| 27 | `minzhao2011/marinegenomeai` | repo-004277 | EMPTY | N/A | N/A |
| 28 | `sallyqus/awesome-AI4SingleCell` | repo-002946 | DOC_ONLY | N/A | N/A |
| 29 | `Harrydirk41/UniFlow` | repo-002733 | DEEP_AUDIT_CANDIDATE | change-000097 | N/A |
| 30 | `ucscGenomeBrowser/cellBrowser` | repo-004543 | NO_UNIQUE | N/A | N/A |
| 31 | `shengyongniu/ai-coscientist-protein` | repo-002101 | DEEP_AUDIT_CANDIDATE | change-000098 | N/A |
| 32 | `vlln/bio-skills` | repo-002229 | DEEP_AUDIT_CANDIDATE | change-000099 | N/A |
| 33 | `HelloWorldLTY/scEval` | repo-001339 | DEEP_AUDIT_CANDIDATE | change-000100 | N/A |
| 34 | `Nigmat-future/Bioagent` | repo-003172 | DEEP_AUDIT_CANDIDATE | change-000101 | N/A |
| 35 | `Nigmat-future/TopoLogos` | repo-003206 | DEEP_AUDIT_CANDIDATE | change-000102 | N/A |
| 36 | `lishengting/paperint` | repo-007222 | DEEP_AUDIT_CANDIDATE | change-000103 | N/A |
| 37 | `hubayirp/agentic-science` | repo-002270 | NO_UNIQUE | N/A | N/A |
| 38 | `google-deepmind/science-skills` | repo-007008 | NO_UNIQUE | N/A | N/A |
| 39 | `lindsay-barret/neuro-analyzer` | repo-005169 | NO_UNIQUE | N/A | N/A |
| 40 | `Nigmat-future/biomedical-skill-suite` | repo-003174 | DEEP_AUDIT_CANDIDATE | change-000104 | N/A |
| 41 | `Nigmat-future/biomedical-codex-skills` | repo-003173 | DEEP_AUDIT_CANDIDATE | change-000105 | N/A |
| 42 | `leezx/RToolbox` | repo-007201 | DEEP_AUDIT_CANDIDATE | change-000106 | N/A |
| 43 | `little2b/COMET` | repo-006125 | DEEP_AUDIT_CANDIDATE | change-000107 | N/A |
| 44 | `satijalab/seurat` | repo-002201, repo-002381, repo-003087, repo-003312 | NO_UNIQUE | N/A | N/A |
| 45 | `kalinnonchev/azimuthpy` | repo-002989 | DEEP_AUDIT_CANDIDATE | change-000108 | N/A |
| 46 | `charlesxu90/ProteinMCP` | repo-006145 | NO_UNIQUE | N/A | N/A |
| 47 | `HelloWorldLTY/scELMo` | repo-001338 | DEEP_AUDIT_CANDIDATE | change-000109 | N/A |
| 48 | `GPTomics/bioSkills` | repo-007055 | NO_UNIQUE | N/A | N/A |
| 49 | `de-grave/onekgpd-mcp` | repo-002664 | DEEP_AUDIT_CANDIDATE | change-000110 | N/A |
| 50 | `Nigmat-future/SC-single-cell-analysis-web` | repo-003201 | EMPTY | N/A | N/A |
| 51 | `zaixizhang/STELLA` | repo-001548, repo-006405, repo-006759 | NO_UNIQUE | N/A | N/A |
| 52 | `PapenfussLab/proteindj` | repo-006998 | NO_UNIQUE | N/A | N/A |
| 53 | `cong-lab/crispr-gpt-pub` | repo-001868 | DEEP_AUDIT_CANDIDATE | change-000111 | lineage-000039 |
| 54 | `BryantLiu123/MCP-Biomedical-Agent` | repo-002335 | NO_UNIQUE | N/A | N/A |
| 55 | `fedbiomed/fedbiomed` | repo-004816 | NO_UNIQUE | N/A | N/A |
| 56 | `scverse/decoupler` | repo-003121 | NO_UNIQUE | N/A | N/A |
| 57 | `mickaelleclercq/BioDiscML` | repo-001631 | DEEP_AUDIT_CANDIDATE | change-000112 | N/A |
| 58 | `PabloPauling/posebusters-mcp-server` | repo-001683 | DEEP_AUDIT_CANDIDATE | change-000113 | N/A |
| 59 | `person-c/easybio` | repo-003062 | NO_UNIQUE | N/A | N/A |
| 60 | `genomoncology/biomcp` | repo-006602 | NO_UNIQUE | N/A | N/A |
| 61 | `mahmoodlab/CLAM` | repo-006835 | NO_UNIQUE | N/A | N/A |
| 62 | `HasanAldhahi/drug-discovery-platform` | repo-001110 | EMPTY | N/A | N/A |

## Canonical decision

The batch increases deep-audited external families from 12 to 62 and bounded
repository records from 18 to 76. It reduces unresolved external families from
2,057 to 2,007 and queued HIGH records from 2,143 to 2,085. Queue orders are
stable and are not renumbered. The next accelerated shard is orders `63`–`112`.
