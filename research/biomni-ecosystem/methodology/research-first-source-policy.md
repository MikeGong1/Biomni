# Research-first source policy

Status: **ACTIVE**

Effective UTC: `2026-08-24`

This policy governs post-Phase-8 Feature and Implementation discovery for a private, non-commercial research program that studies Biomni and related scientific-agent systems.

## 1. Policy purpose

The earlier deep-audit policy treated unclear or mixed licensing as a reason to reject direct adoption and often deferred Feature/Implementation allocation. That was appropriate for a production-integration decision, but it was too conservative for the current research objective.

The revised objective is to identify useful scientific-agent capabilities, understand their concrete implementations, compare them with Biomni, and build a separate research system. Therefore, source availability and functional value drive research priority. License and provenance remain visible metadata but do not determine whether a capability is studied or normalized.

## 2. Evidence that remains unchanged

The following historical evidence remains authoritative and must not be deleted or weakened:

- repository, branch, PR, tag and immutable commit identity;
- file-level and patch-level lineage;
- scientific-validity findings;
- security and source-to-sink findings;
- privacy and clinical-data findings;
- dependency, model, data and service-term findings;
- attribution and contributor identity;
- runtime limitations and unexecuted-test disclosures.

This policy changes downstream interpretation, not historical facts.

## 3. License and provenance treatment

### 3.1 Research selection

The following values are not research-exclusion conditions:

- `NOASSERTION`;
- no root `LICENSE` file;
- `LICENSE_UNCLEAR`;
- mixed repository/component licenses;
- non-commercial code or model terms;
- unresolved database, model-weight or API-service terms;
- incomplete file-level provenance.

A candidate with one of these values can still receive a Feature ID and an Implementation ID when its behavior and implementation are sufficiently evidenced.

### 3.2 Required provenance ledger

For every source-first implementation studied or reproduced, preserve at minimum:

- repository full name;
- repository ID when available;
- immutable commit SHA;
- branch or PR surface;
- original file path;
- original symbol, class, function or relevant line range;
- original license/provenance observation;
- copied, adapted or rewritten status;
- modification summary;
- related paper, dataset, model and service citations;
- date retrieved and analyst identity.

Do not collapse academic citation, code attribution, model terms and data terms into one field. They are separate provenance dimensions.

### 3.3 Publication and redistribution

Public redistribution, article-associated source release, product release and relicensing are later targeted review gates. A later review may require replacing, rewriting, obtaining permission for, or excluding a specific implementation. That later gate must not remove the implementation from the research catalog.

## 4. Source-first workflow

For each candidate:

1. Freeze the exact source repository and immutable commit.
2. Read the original implementation before designing a replacement.
3. Extract the smallest coherent implementation unit: Skill, tool, workflow, adapter, model wrapper, data layer, UI component or orchestration pattern.
4. Record exact provenance before copying or adapting code.
5. Place reproduced or adapted code only in a research-only workspace until scientific and security validation is complete.
6. Compare behavior with the frozen Biomni baseline.
7. Normalize equivalent implementations under one Feature.
8. Keep materially different approaches as separate Implementations.
9. Run or test only in an isolated environment with no production secrets or sensitive data.
10. Apply a separate publication/redistribution review only to the final small set selected for release.

## 5. Revised classification rules

### `SOURCE_FIRST_RESEARCH_CANDIDATE`

Use when the implementation is functionally relevant and no critical non-license blocker prevents static study or isolated prototyping.

### `SOURCE_FIRST_WITH_REMEDIATION`

Use when source study is valuable but the implementation contains scientific, runtime, security, privacy, dependency or data-governance defects that must be corrected before reliance.

### `REFERENCE_ONLY_BLOCKED`

Use when critical clinical, privacy, security, scientific-validity or supply-chain failures make execution or direct reuse unsafe. Architecture, interface and workflow patterns may still be cataloged.

### `DUPLICATE_OR_SUPERSEDED`

Use when the implementation is equivalent to, derived from, or clearly superseded by another source. Preserve lineage and normalize to the best implementation.

### `PUBLICATION_REVIEW_REQUIRED`

Use as an orthogonal flag whenever copied or adapted code, model weights, data, service-dependent behavior or unclear provenance may appear in a public artifact.

## 6. Feature and Implementation allocation

License clarity is not a prerequisite for Feature or Implementation allocation.

Allocate a Feature when all of the following are available:

- a stable capability statement;
- at least one observable implementation;
- evidence that the capability is not merely documentation noise;
- a comparison point against Biomni or another implementation.

Allocate an Implementation when all of the following are available:

- repository and immutable source identity;
- concrete files or symbols;
- implementation behavior or contract;
- lineage relationship;
- current scientific, security, privacy and runtime status;
- provenance fields, even if unresolved.

## 7. Scoring

Rank candidates using:

1. functional value to the planned scientific-agent system;
2. capability gap versus Biomni;
3. implementation completeness;
4. scientific plausibility and validation evidence;
5. security and privacy posture;
6. runtime reproducibility;
7. maintainability and dependency burden;
8. ease of adaptation;
9. provenance completeness.

License category may influence a later release plan, but it must not lower the functional research score.

## 8. Mandatory boundaries

This policy does not relax:

- patient or controlled-data protections;
- clinical-validity requirements;
- credential handling;
- arbitrary code, shell, SQL or R execution controls;
- model and checkpoint trust controls;
- remote service disclosure and consent;
- dependency and artifact integrity checks;
- reproducibility requirements;
- truthful reporting of tests that were not run.

## 9. Priority application

Apply this policy first to:

1. SciAgent-Skills, including 203 active Skills and the 125 previously retained leads;
2. K-Dense / Kuan scientific skills, BIDS and DataLad;
3. ChatSpatial / DeepSpot-M;
4. ezST;
5. Aquila-next;
6. gnomAD_DB;
7. the remaining 598 `DEEP_AUDIT_CANDIDATE` families after semantic clustering.

Historical batch reports remain unchanged. New dispositions must be written as an overlay or new normalized Feature/Implementation records rather than by deleting earlier findings.
