# Public Fork Unique-Change Screening — Batch 022

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query returned all 28 branch
refs without pagination: 24 upstream-known heads and four new SHAs. Four
serialized comparisons succeeded; each contained one commit, no comparison
reached a pagination or file cap, and all requested heads matched. No source,
script, dependency, hook, test, or network endpoint was executed.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000578 | therealtimex/Biomni-med-agent | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000577 | TD2020lilly/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000576 | samseclog/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000574 | yogee11/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000573 | thomascherickal/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000615 | lohith15/Lohith_Biomni | User | 2 | 1 | 0 | 0 | 1 | README_ONLY |
| repo-000586 | nazhar/Biomni | User | 1 | 0 | 0 | 0 | 1 | EMPTY_NET_CHANGE |
| repo-000612 | leegang/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000585 | HisaacH/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000584 | shajiahang/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000651 | zskylarli/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000587 | abhik1368/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000633 | Jagan-07/Jagan_Biomni | User | 2 | 1 | 0 | 0 | 1 | README_ONLY |
| repo-000597 | hengrumay/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000596 | leyugod/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000595 | fazialnjd/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000594 | ikoshos-gland/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000593 | pariskang/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000592 | AnveshW/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000590 | tejaswankalluri/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000589 | SylvainChast/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000588 | cold-eye/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000704 | sbonner0/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000654 | zcq41/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000607 | dctongsheng/Biomni | User | 1 | 0 | 0 | 0 | 1 | DOCS_ONLY_UNRELIABLE_GENERATED_GUIDE |

Classification counts: NO_UNIQUE_CHANGE=21, README_ONLY=2,
EMPTY_NET_CHANGE=1, and DOCS_ONLY_UNRELIABLE_GENERATED_GUIDE=1.

## Non-substantive findings

- `lohith15:dev@3571cfd...` adds only `#Edited by Lohith` to README.
  `Jagan-07:main@8e37c06...` adds only `# JAGAN!!!`. Both are owner-authored
  personal signatures, not Biomni capabilities, bug fixes, or integration work.
- `nazhar:main@5cee83e...` is one merge titled “Pull latest” with zero changed
  files relative to its merge base. It is an empty-net history surface, not a
  substantive change.

### repo-000607 — dctongsheng/Biomni

- One `cursoragent`-authored commit adds only the 572-line Chinese
  `Biomni_技术文档.md`; repository owner `dctongsheng` has no observed authorship
  on this branch delta. No production file, test, dependency, environment, data,
  or license changes.
- The module “tool count” table labels values such as 1,027, 1,388, and 3,894 as
  function counts. These values track source-file line counts, not callable/tool
  counts, and are therefore false capability metrics.
- Several examples do not match the API. `A1.add_tool()` requires a callable and
  calls `inspect.getsource`, while the guide passes a dictionary. Its `add_data()`
  example uses metadata keys (`name`, `description`, `path`, `format`) where the
  API expects a mapping from file paths to description strings, so it registers
  the wrong pseudo-items rather than the intended dataset.
- The documented `ToolRetriever.retrieve_tools(query, k=10)` and
  `update_index(tools)` methods do not exist; the relevant public method is
  `prompt_based_retrieval(query, resources, llm=None)`. By contrast, the listed
  core `ToolRegistry` lookup/list/remove methods are present.
- The guide invents a broad dependency list containing pandas, NumPy, SciPy,
  scikit-learn, Torch, and Transformers; frozen project metadata declares only
  pydantic, langchain, and python-dotenv at the package level. Environment setup
  is much larger and separate. It also presents Linux/macOS/Windows support while
  the environment guide says the setup script was tested only on Ubuntu 22.04.
- Storage advice says at least 15 GB, whereas the full environment guide requires
  at least 30 GB and more than ten hours. Data/benchmark sizes, operating-system
  support, API behavior, tool counts, test coverage, and roadmap statements are
  uncited snapshots or unsupported claims rather than verified documentation.
- Troubleshooting recommends `echo $ANTHROPIC_API_KEY`, which prints a complete
  secret into the terminal and potentially scrollback, logs, recordings, or shared
  support output. Safe guidance should report only presence or a redacted suffix.
  The guide also omits the critical upstream warning that Biomni executes
  LLM-generated code with the current user's filesystem, network, and command
  privileges and therefore requires isolation around sensitive data and secrets.
- The document repeats upstream Apache-2.0 and citation material, but adds no
  independent sources or license issue. It should not be merged or treated as
  evidence of implemented features. If a Chinese guide is desired, regenerate it
  from tested current APIs, machine-counted inventories, exact environment modes,
  and secret-safe procedures.

## Identity boundary

- No person enters P through this batch. README-only owners are non-substantive;
  `nazhar` contributes zero net tree change; `cursoragent` authors a documentation-
  only artifact; and `dctongsheng` is not the observed author of that artifact.
- Upstream-only owners do not enter through this batch.

## Evidence and limits

- Authenticated GraphQL branch/owner inventory covered 25 repositories and all
  28 refs. Four serialized comparisons were complete and independently closed.
- Static patches prove the two README additions, zero-file merge, documentation
  content, and commit attribution. Frozen source/API/environment files support the
  documentation accuracy comparison.
- No claim is made about deleted/private work, runtime behavior, or current
  external service state. The guide was not executed as instructions.

## Next action

Continue the next bounded active-fork batch. This batch produces no new change,
lineage, implementation, feature, or person ID.
