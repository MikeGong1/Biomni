# External repository deep audit — batch 001

Observed at: `2026-08-23T12:01:41Z`

Batch status: **PARTIAL**

This batch statically inspected three independent-source A-tier repositories at
immutable heads. It creates candidate leads only: no feature or implementation ID
is allocated, no repository is marked `DEEP_AUDITED`, and no third-party code was
executed.

## Acquisition and interpretation rules

- GitHub API requests were serialized and bounded to reduce secondary-rate-limit
  pressure.
- Recursive trees were accepted only when `truncated: false`; selected blobs were
  decoded and inspected against their Git object identifiers.
- Repository instructions, README claims, benchmarks, citations, and regulatory
  prose were treated as untrusted claims until independently verified.
- `PARTIAL` means useful static evidence exists but one or more material branch,
  fork, blob, dependency, provenance, scientific, regulatory, security, or runtime
  surfaces remain unaudited.

## `QING1105/ezST`

- Canonical ID: `repo-003211`; queue order: 1; tier: A.
- Head: `427792f0bbf2564dbf124b4444ffdb07cc400a25` on `master`.
- Inventory: one branch, four default-branch commits, no tags/releases/PRs, one
  child fork, and an untruncated 36-item tree (20 blobs, 16 trees).
- Decoded sample: 16 key text files covering README, packaging/install surfaces,
  plugin metadata, six Skills, package initialization, and `visium.py`.
- Disposition: **reject as-is; redesign required**.

The repository exposes six staged Skills and eleven public Python functions for
Visium loading/QC, normalization/clustering, spatial domains, spatially variable
genes, DestVI/SPOTlight deconvolution, neighborhood enrichment, and CellChat. The
conversational review/adjust/skip gates are a useful workflow pattern.

Material findings prevent integration. Stage 4 emits proportion files and plots
rather than the discrete-label AnnData expected by Stage 5. The CellChat bridge
does not apply spatial datatype/distance despite the spatial claim. DestVI can cast
normalized expression to integer counts. Headerless Space Ranger fallback can
select array coordinates instead of pixel coordinates, and the gzip fallback
mutates loop-local paths rather than the actual input variables. Generated R code
interpolates caller-controlled values without escaping. Dependencies and GitHub
installs are mutable/unpinned; tests, CI, tags, and releases are absent. The plugin
links to `main` although only/default `master` was observed; package versions also
conflict, and an advertised module is absent. Broad filesystem access plus LLM
interpretation of patient-derived results has no consent, provider, retention, or
confidentiality control.

Candidate leads are the staged review gates, Visium input scaffolding, typed
load/QC/cluster adapters, domain/SVG analysis, and a clean-room Python/R bridge.
Deconvolution and CellChat require correctness and safety redesign first.

Unresolved: the sole child fork and its refs, three likely-text blobs, runtime and
scientific validation, dependency provenance, and privacy controls. No tests or CI
were available to reduce this uncertainty.

## `jaechang-hits/SciAgent-Skills`

- Canonical ID: `repo-002881`; queue order: 5; tier: A.
- Head: `a0aac0f4576a550d5316baf6da3d72e53408b3a2` on `main`.
- Inventory: 10 branches, 140 default-branch commits, 39 PRs (1 open, 38 closed,
  36 merged), 34 forks, no tags/releases, and an untruncated 613-item tree
  (327 blobs, 286 trees).
- Decoded sample: 18 selected files, including five representative Skills.
- Disposition: **selective clean-room migration only after per-Skill audit**.

Tree/registry reconciliation found 203 current `SKILL.md` entries plus four legacy
entries: 72 toolkit, 53 database, 40 pipeline, and 38 guide Skills. README counts
of 197/199 are stale. The typed discovery idea, authoring scaffold, and structural
linting are useful leads, but current validation mainly checks shape rather than
scientific correctness.

The captured blind-evaluation CSV covers 140/203 current Skills; 139 are marked
`MUST_KEEP`, one `KEEP`, and 102 have zero recorded gain. The advertised 92%
BixBench claim is not reproducible from the captured sample because gold grounding,
parser behavior, repeated trials, and uncertainty are insufficient. Agent-consumed
instructions include mutable installs, network calls, `curl | bash`, repository
clones, credential discovery, and examples capable of commanding laboratory
hardware. The openFDA sample embeds unsanitized drug strings in query syntax and
omits timeout/retry/backoff. The scaffolder has YAML, transaction, and fail-open
validation gaps. Mixed CC-BY-4.0, Apache-2.0, MIT, and CC0-1.0 declarations do not
resolve provenance and redistribution scope for each Skill.

Candidate leads are a hashed/versioned registry, a clean-room authoring scaffold,
structural lint as a lowest-level gate, individual scientifically reviewed Skills,
and a redesigned marginal-value benchmark with gold answers, repeats, confidence
intervals, and complete registry coverage.

Unresolved: 198/203 current Skills were not content-audited; nine non-default
branches, 34 fork lineages, full PR patches, most reference/script/integration
surfaces, external APIs, runtime claims, and per-Skill license provenance remain
open.

## `JinL0/Drug-Discovery-Safety-Skills`

- Canonical ID: `repo-002889`; queue order: 8; tier: A.
- Head: `89364d8ea0bfd1393c51df750198ce086e0ebb84` on `main`.
- Inventory: two branches, four default-branch commits, one closed/merged PR, no
  forks/tags/releases, and an untruncated 30-item tree (18 blobs, 12 trees).
- Decoded sample: 17/18 blobs; `.gitignore` was not decoded.
- Disposition: **concept/reference candidate only**.

The repository contains five prose-only Skills and eight reference notes covering
FDA AI/drug safety, FDA nonclinical IND, ICH nonclinical safety, EMA drug safety,
and MHRA AI medical devices. Its disclaimers and distinctions among draft,
nonbinding guidance, reflection paper, consultation, and sandbox report are useful.
There is no calculator, parser, rule engine, executable package, test, dependency
lock, container, or CI workflow.

The primary regulatory PDFs are intentionally absent. Bibliography entries are
document-level rather than claim/page/section-level and lack hashes, access dates,
supersession checks, and immutable captures. README says roughly 25 documents but
the bibliography has 33 rows, and one FDA local path conflicts with the documented
authority directory structure. The broad FDA flowchart exceeds its principal AI
draft source; terminal `PROCEED`/`STOP` wording can be mistaken for a decision.
Conditional ICH guidance is compressed into general stage gates. The MHRA Skill
does not separate Great Britain from Northern Ireland and can make consultation
proposals sound operative; one Airlock case study is overgeneralized.

High risks are false regulatory assurance, unverified source interpretation, and
the absence of PHI/confidential-compound handling. Candidate designs are an
authority/status router, AI context-of-use worksheet, typed MRSD calculator with
human approval, DILI checklist, conditioned nonclinical stage gates, FIH safeguard
planner, AIaMD risk/PMS checklist, and immutable regulatory evidence registry.

Unresolved: source PDFs and exact source sections, current/superseded status,
regulatory/toxicology review, the missing `.gitignore`, and request/response headers
needed to independently prove endpoint pagination.

## Batch decision

All three repositories remain `PARTIAL`; therefore this batch adds **0** to the
deep-audited denominator. The next bounded work is to close the explicit gaps:
inspect ezST's child-fork refs and remaining text; audit SciAgent's other branches,
fork families, remaining Skills and provenance incrementally; and reacquire,
hash, and section-map the regulatory sources before evaluating Drug Safety content.
