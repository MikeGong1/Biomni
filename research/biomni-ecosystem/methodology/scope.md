# Research Scope

## Objective

Build a recoverable and measurable public-evidence database that maximizes the
discovery of independent capabilities useful to Biomni while minimizing missed
changes, duplication, unsupported attribution, license risk, and security risk.

This phase is research, audit, and integration planning only. It does not modify
`biomni/`, `biomni_env/`, `tutorials/`, or other production source.

## Bounded universe

Let `B = snap-stanford/Biomni`.

`P`, the code-visible GitHub people set, contains only:

1. publicly visible members of the `snap-stanford` GitHub organization;
2. contributors and commit authors in `B`;
3. authors of pull requests against `B`;
4. contributors to relevant public branches of `B`; and
5. owners of public forks with substantive unique commits.

`R` contains all public repositories owned by `snap-stanford`, plus all public
repositories owned by people already in `P`. Repositories are inventoried first;
only `HIGH_RELEVANCE` and unresolved `POSSIBLE_RELEVANCE` repositories receive a
deep audit.

`C` contains public technical material for Biomni commercial products, including
Biomni Lab, Phylo Biomni, Biomni MCP, and later official names for the same
products or components.

The research universe is `U = public history(B) + screened(R) + public(C)`.

## Hard stop boundary

`person_depth = 1`. A contributor to an external repository does not enter `P`
unless that person independently satisfies a code relationship above. Paper
authors, collaborators, lab rosters, company colleagues, and social connections
do not expand the universe. They may be retained only as `OUT_OF_SCOPE_LEAD`.

People are repository-discovery entry points, not biography subjects. A verified
GitHub username is sufficient; real-name mappings remain `UNVERIFIED` unless
supported by direct evidence.

## Research order

Use breadth-first inventory, then relevance screening, then deep audit. Collection
precedes normalization, feature decomposition, lineage construction, comparison,
deduplication, and canonical implementation selection.

In this research phase, `DEEP_AUDITED` means the bounded public branches, commit
history, PR/tag/release surfaces, discoverable fork lineage, current and historical
source, dependencies, license/provenance signals, and static security/scientific
contracts were inspected and normalized. It does **not** mean third-party code was
executed, results were scientifically validated, licensing was cleared, or the
implementation is integration-ready. Those conclusions require separate status
fields; runtime testing remains prohibited by `security-policy.md`.

Important conclusions are classified as `FACT`, `INFERENCE`, or
`RECONSTRUCTION_CANDIDATE` under `evidence-policy.md`.
