# Drug-Discovery-Safety-Skills static deep audit

Observed at: `2026-08-23T14:46:21Z`

## Canonical decision

- Repository: `JinL0/Drug-Discovery-Safety-Skills` (`repo-002889`)
- Default head: `89364d8ea0bfd1393c51df750198ce086e0ebb84`
- Latest public branch head: `830057e02bf629d3b634fe74e18a341aba2ceb17`
- Audit status: **DEEP_AUDITED — STATIC_ONLY**
- Regulatory fidelity: **MIXED; multiple direct contradictions and stale sources**
- Integration disposition: **REJECT AS-IS; concept/evidence-schema leads only**
- Runtime status: **no regulatory calculator, rule engine, API, or tested software
  implementation exists**

This is a high-stakes prose/agent-instruction audit. `DEEP_AUDITED` means all
bounded public repository surfaces and the cited official-source set were
statically processed. It does not make the Skills legal, regulatory, medical, or
scientific advice, and it does not validate their outputs for real decisions.

## Live repository and Git coverage

The initial batch report froze two branches. A fresh live mirror found a third
branch pushed after that snapshot, while default `main` remained unchanged:

| Branch | Head | Relation to main | Canonical status |
|---|---|---|---|
| `main` | `89364d8ea0bfd1393c51df750198ce086e0ebb84` | default | current merged prose package |
| `feat/fda-drug-safety-skill` | `d51308899c376010d2e15c0d1028d75694501b64` | ahead 0, behind 1 | merged PR #1 lineage |
| `worktree-readme-install-gifs` | `830057e02bf629d3b634fe74e18a341aba2ceb17` | ahead 1, behind 0 | active unmerged docs/demo branch |

The unique DAG contains five commits and is complete in the frozen mirror. PR #1
is the only PR and is closed/merged; forks and releases returned page 1/page 2 as
0/0, while pulls returned 1/0. No tag exists. `git fsck --full --no-reflogs`
reported no broken/unreachable object.

Across all refs, 24 unique blobs are reachable: 22 text blobs were read line by
line and two GIFs were inspected as media metadata. Default main contains all 18
blobs, including the previously missing `.gitignore`. The docs branch adds a
272-line Pillow renderer and two generated GIFs; the script has fixed local
inputs/outputs and no network, subprocess, shell, credential, or upload path. The
GIFs are explicitly illustrative recreations, not execution/test evidence.

## Change decomposition

| Commit(s) | Change | Treatment |
|---|---|---|
| `1de023e4acd0fc2866709fd26c5698c1776c0622` | initial README + MIT license | inventory/root only |
| `5a2eed8e1b3d4f3a058e4e4a0fc6fb910346a74a` | FDA AI credibility Skill, repository-authored triage flowchart, source notes | `change-000079` |
| `d51308899c376010d2e15c0d1028d75694501b64` | four additional FDA/ICH/EMA/MHRA Skills, eight authority notes, bibliography | `change-000080` |
| `89364d8ea0bfd1393c51df750198ce086e0ebb84` | merge PR #1; tree equals its feature parent | merge surface, no duplicate change |
| `830057e02bf629d3b634fe74e18a341aba2ceb17` | installation/sample-question README, fixed-text GIF generator and two GIFs | indexed `DOC_ONLY/DEMO_MEDIA`; no Feature/change ID |

`lineage-000030` retains the two substantive prose changes, merge identity, and
active docs branch. No formal Feature or Implementation ID is assigned before
Phase 10 cross-repository normalization.

## Actual behavior

The five Skills are Markdown instructions interpreted by an LLM. They provide:

1. FDA AI context-of-use and credibility questions;
2. a repository-authored four-terminal safety triage flowchart;
3. FDA MRSD/HED, DILI/Hy's Law, Phase 1 IND, IND-exemption and combination-tox
   prose/calculation steps;
4. an ICH M3/S-series nonclinical gate matrix;
5. EMA AI-lifecycle and FIH-risk checklists;
6. MHRA AI Airlock lessons and proposed SaMD/AIaMD workflow; and
7. a bibliography/provenance skeleton.

There is no deterministic calculator, unit type, source-status router, validation
schema, rule engine, test suite, CI, executable clinical workflow, or mandatory
approval gate. Correctness depends entirely on the consuming model preserving
nuance from prose.

## Official-source acquisition and QA

The committed bibliography has 33 rows, not the README's “~25 documents.” All 33
were independently checked against official authority sources. Serialized parent
acquisition froze 29 PDFs and one official landing HTML with SHA-256 hashes; three
official TGA/Health Canada pages timed out in the local curl queue but were
separately verified live by authority-specific agents. Exact URLs, sizes, hashes,
and status corrections are in `drug-safety-source-manifest.jsonl`.

Using the PDF workflow, primary documents were text-searched by page/section and
representative pages were rendered and visually checked. These included FDA AI
scope, the Phase 1 120-day Q&A, ICH S11 weight-of-evidence factors, EMA
interpretability/sentinel dosing, the MHRA Airlock comparison table, and the MHRA
consultation question page. Rendering was legible; extracted passages and visual
pages agreed.

## FDA and CFR findings

### Directly supported

- The January 2025 AI document is still draft/not for implementation. Its seven
  COU/credibility steps, influence × consequence risk framing, independent test
  data, and risk-commensurate evidence plan are directly supported.
- FDA MRSD guidance supports NOAEL→HED body-surface-area conversion, the listed Km
  values, a default safety factor of 10 with justified adjustment, and selection
  informed by species relevance.
- DILI guidance supports the repository's core Hy's Law signal and monitoring/
  discontinuation thresholds, but explicitly says there is no exact consensus
  stopping rule and the thresholds were not prospectively validated as an
  autonomous algorithm.
- The marketed-drug IND exemption is conjunctive, and commercial/noncommercial
  purpose alone does not decide applicability.

### Material contradictions or overreach

- **AI scope:** the FDA draft explicitly excludes drug discovery unless output is
  information/data used to support a regulatory decision. The general
  `fda-drug-safety` trigger applies the framework directly to drug-discovery
  design/tox triage, which exceeds the source scope.
- **120-day clock:** the repository says final QA toxicology reports are due
  within 120 days of study start. FDA's October 2000 Q&A says the period starts
  at FDA receipt/date stamp of the integrated summary, not clinical-study start.
- **PAD:** FDA says it may be appropriate to decrease a starting dose when the
  pharmacologically active HED is lower; it does not mandate lowering to that
  exact value, and PAD selection is outside the MRSD guidance's core scope.
- **Combination toxicology:** the Skill collapses marketed+marketed,
  marketed+NME and all-NME pathways into one shared-toxicity trigger. FDA gives
  materially different pathways.
- **Flowchart authority:** `PROCEED`, `MITIGATE`, `ESCALATE`, and `STOP` terminals
  are repository-authored heuristics, not FDA decisions. A positive genotoxicity,
  hERG, or DILI signal cannot be converted mechanically into an FDA “stop.”
- The 2024 CFR PDFs are official annual snapshots, not live current law. Current
  legal claims need live eCFR; repository status metadata does not make this clear.

## ICH findings

All 11 listed ICH files were checked. The core content is often directionally
correct, but a fixed “required at gate” engine is not justified because the
guidelines use modality, indication, duration, geography, population and
exploratory/serious-disease exceptions.

Material corrections include:

- M3(R2) WOCBP/pregnancy and study-timing pathways are region- and context-specific;
  the Skill's universal FIH/Phase III list is too strong.
- S7A/S7B do not impose the same standalone battery on every product; the current
  E14/S7B Q&A is missing.
- S5(R3)'s one-species and biologic exceptions require conditions omitted by the
  local summary.
- S9 applies to advanced/serious cancer contexts; its reproductive and safety-
  pharmacology exceptions cannot be generalized. The current S9 Q&A is missing.
- **S11 direct contradiction:** the two highest-weight WoE factors are youngest
  intended age and suspected effects on developing organ systems. The repository
  substitutes amount/type of existing data for the second factor.
- The cited E6(R3) file has since received an October 2025 correction and a June
  2026 Annex 2. The nonclinical Skill contains no E6-derived claim, so its “used
  by” mapping is unsupported.

## EMA findings

The AI reflection paper remains the current adopted paper; the FIH Rev.1 guideline
was adopted in 2017, became effective 2018-02-01, and remains current. Core COU,
risk, prospective pivotal testing, single-use holdout, MABEL/PAD/NOAEL, exposure,
escalation, sentinel and stopping-rule summaries have direct support.

The Skill strengthens source modality beyond what EMA says:

- GMLP is not named in the reflection paper.
- SHAP/LIME are examples to use “whenever possible,” not mandatory methods.
- Close human supervision/QC is explicit for product-information drafting, not a
  universal rule for every LLM use.
- There is no source rule to always select the “most conservative” dose anchor or
  an “earlier stopping rule” under uncertainty.
- Sentinel treatment is expected for all single- and multiple-dose cohorts, with
  a placebo option and risk-proportionate flexibility; it is not merely a repeat
  at later high-risk points.
- The new docs branch calls nonbinding reflection-paper content “rules that now
  bind you,” directly contradicting its own final disclaimer.

## MHRA / United Kingdom findings

The Airlock Phase 1 report is a historical sandbox report, explicitly not formal
guidance, and has been followed by a 2026 Phase 2 report. Its SmartGuideline
comparison did observe 0/436 hallucinations versus 23/436 for baseline GPT-4o,
but the complete proprietary system also used curated sources, knowledge graph,
safety rules and greedy decoding. This is not a controlled proof that RAG alone
eliminates hallucinations or produces exact determinism.

Chapter 10 is a closed 2021 consultation with a 2022 government outcome, not
current amended law. The Skill operationalizes proposals as current requirements:
IMDRF mapping, temporary Airlock classification, voluntary PCCP, SaMD-specific
cyber minimums, logging, and a mandatory Yellow Card link. Government outcome
material specifically did not adopt mandatory logging or the mandatory link.

The Skill also omits the essential jurisdiction split:

- Great Britain uses UK MDR 2002 as amended; the new GB PMS Part 4A took effect
  2025-06-16.
- Northern Ireland follows EU MDR/IVDR under the Windsor Framework, with CE/
  CE+UKNI and different classification/conformity/PMS routes.

An authority router must ask GB, NI, or both before offering any device pathway.
Airlock's continuous AI monitoring/tiered thresholds are recommendations, not the
text of the binding GB PMS rules.

## OECD, WHO, PMDA, TGA, and Health Canada

- The OECD row mixes identities: its URL is the 2005 omnibus *Good Laboratory
  Practice: OECD Principles and Guidance for Compliance Monitoring*, not a “2005
  edition” of Series No. 1. The actual Series No. 1 revised Principles publication
  is from 1998; later supporting documents also update the corpus.
- WHO's 2001 handbook is historical and was updated by a 2009 second edition; it
  should not be marked current Final.
- PMDA's PDF is the current *Profile of Services* posted 2024-10-18, an agency
  brochure/context source rather than guidance.
- TGA's M3(R2) adoption page is current and includes a local-law caveat.
- Both Health Canada guidance pages remain current/final, but guidance is not law
  and product/submission scopes must be preserved.
- “Most authorities adopt or align with ICH” was not proven across every authority
  in the broader table. Use verified jurisdiction-by-jurisdiction statements.

## Safety, privacy, supply chain, license, and provenance

- Main contains no code, network client, credential, subprocess, dynamic install,
  model, dataset, or executable. No secret was found. The docs renderer is inert
  unless manually run and only writes fixed GIF assets.
- Skills solicit participant laboratory values, patient-risk scenarios, trial
  results and confidential compound information without a PHI/PII/confidential-
  data minimization, authorization, retention, provider, or cross-border policy.
- Installation guidance clones a mutable default branch and copies/symlinks all
  agent instructions, then recommends `git pull` updates without tag/commit/hash
  pinning or pre-update review. This is an agent-instruction supply-chain risk.
- Root code/content license is MIT. Regulatory PDFs are intentionally excluded,
  reducing redistribution exposure, but the derived summaries lack per-claim
  page/section, source hash, access date, extraction log and reviewer approval.
  MIT does not establish rights in authority source documents or prove faithful
  paraphrase.
- No tests, CI, schema validator, link checker, source-version checker, or
  deterministic calculation tests exist. Demo GIFs are drawn illustrations, not
  functional validation.

## Candidate designs and disposition

No formal Feature/Implementation ID is allocated. Potential clean-room designs:

1. authority/jurisdiction/status router separating law, adopted guidance, draft,
   reflection, consultation, outcome, report, and case-study evidence;
2. immutable source registry with authority, version, effective/superseded state,
   access time, hash, page/section claim mapping and reviewer approval;
3. AI COU/credibility worksheet that never expands beyond the source scope;
4. typed MRSD/HED **calculation draft** with units, population/modality limits,
   deterministic arithmetic and mandatory toxicologist approval;
5. DILI/Hy's Law evidence checklist that never diagnoses or issues an autonomous
   treatment/trial stop;
6. conditioned ICH nonclinical matrix with modality, indication, duration,
   region, population and exception fields;
7. FIH safeguard planner that records source-supported options and requires human
   protocol/regulatory review; and
8. GB/NI-aware AIaMD/PMS checklist with binding/nonbinding status on every rule.

Do not copy the terminal flowchart or categorical MRSD/DILI/IND/device decisions.
Do not treat the current Skills as a regulatory answer engine. They are evidence
and workflow leads only, and any future implementation must fail closed on missing
inputs, stale sources, jurisdiction ambiguity, or absent expert sign-off.

## Evidence boundary

Primary evidence is `evidence-000144` through `evidence-000150`. An independent
verifier reproduced the Git/REST/blob counts, all 30 body hashes, the three live
web verifications, and the major authority contradictions; it separately returned
static-coverage PASS, regulatory-fidelity FAIL, and integration FAIL. The verifier
also repeated older 1995 “study start” wording for the 120-day issue, but the later
October 2000 FDA Q&A explicitly resolves the ambiguity in favor of FDA receipt/
date stamp of the integrated summary; the rendered Q&A page is controlling here.

Public sources can change, so current status must be refreshed at future use time.
Runtime execution was neither necessary nor permitted: the repository has no
decision implementation to test, and the audit found source-contract failures
directly.
