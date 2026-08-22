# Structured Database

Each nonblank line in a `.jsonl` file is one JSON object. Canonical IDs are stable
and allocated only after identity resolution by the parent research coordinator.

Prefixes:

- `person-github-`: GitHub identities
- `repo-`: repositories
- `change-`: unique change sets
- `impl-`: feature implementations
- `feature-`: normalized user-facing features
- `evidence-`: public evidence records
- `lineage-`: implementation or feature lineage records

An empty JSONL file means that no canonical record of that type has been created
yet; it does not mean that the entity type does not exist in the research universe.
Worker notes are provisional and never allocate canonical IDs directly.
