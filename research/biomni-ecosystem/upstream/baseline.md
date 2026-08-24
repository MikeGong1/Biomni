# snap-stanford/Biomni Upstream Baseline

## Snapshot identity

Evidence classification: `FACT`

Observed at: `2026-08-22T20:28:36Z`

| Field | Value |
|---|---|
| Repository | `snap-stanford/Biomni` |
| Visibility | public |
| Archived | no |
| Default branch | `main` |
| Main HEAD | `400c1f366b96a35ca253e13c9b06c5076af41d65` |
| HEAD author/committer date | `2026-01-15T04:23:42Z` |
| HEAD subject | `Merge pull request #259 from snap-stanford/protocols_database` |
| Package version at HEAD | `0.0.8` |
| Code license | Apache-2.0 |
| Latest public release | `v0.0.8` / `biomni 0.0.8` |
| Release published | `2025-10-27T21:33:37Z` |
| Latest tag | annotated tag `v0.0.8` |
| Tag object | `b5d1f34ace96a4114c50b53a902999fc162f4139` |
| Tag target commit | `d15b3c9277b8945f3bfa6af8faf20bae92c09628` |

The GitHub commit API, a direct fetch of `upstream/main`, and
`MikeGong1/Biomni`'s current `main` all resolve to the same full HEAD SHA. The
research branch is based on that commit and contains research-only commits.

## Major architecture

At this SHA, `biomni.agent.A1` is the primary configurable agent. It loads the
academic or commercial-mode environment description, tool schemas, a tool
registry/retriever, know-how documents, and an LLM provider, then builds a
LangGraph workflow. Tool use is code-oriented: the agent can select described
functions and has utilities for Python, Bash, and R execution. `biomni.agent.react`
also implements a LangGraph model/tool cycle.

Main source areas:

- `biomni/agent/`: A1 and ReAct orchestration, tool registration, and execution;
- `biomni/tool/`: scientific functions, database/API functions, schemas, and
  protocol retrieval;
- `biomni/model/`: tool retrieval;
- `biomni/know_how/`: task guidance and bundled resources;
- `biomni/task/` and `biomni/eval/`: benchmark/evaluation task interfaces;
- `biomni/env_desc.py` and `biomni/env_desc_cm.py`: academic and
  commercial-compatible data/library descriptions; and
- `biomni_env/`: Conda, pip, R, and command-line environment specifications.

This is a static architecture observation, not a runtime validation. The execution
surfaces above are security-relevant and will receive dedicated static analysis
before any integration recommendation.

## Tool inventory

The canonical tool-description files expose 224 uniquely named tool schemas across
22 scientific modules. The implementation directory has 260 top-level function
definitions across 23 Python modules; this larger count includes private helpers
and functions that are not exposed as agent tools.

| Tool module | Exposed descriptions |
|---|---:|
| biochemistry | 6 |
| bioengineering | 7 |
| bioimaging | 10 |
| biophysics | 3 |
| cancer biology | 6 |
| cell biology | 5 |
| database | 40 |
| genetics | 9 |
| genomics | 19 |
| glycoengineering | 3 |
| immunology | 10 |
| lab automation | 3 |
| literature | 8 |
| microbiology | 12 |
| molecular biology | 18 |
| pathology | 7 |
| pharmacology | 25 |
| physiology | 11 |
| protocols | 4 |
| support tools | 3 |
| synthetic biology | 8 |
| systems biology | 7 |
| **Total** | **224** |

Counts come from static AST parsing of `biomni/tool/tool_description/*.py` at the
frozen SHA. They establish inventory size, not runtime availability or correctness.

## Database and data inventory

- 40 exposed database/API-oriented tool descriptions are present in the
  `database` module.
- 33 serialized API schema files are present under `biomni/tool/schema_db/`.
- The academic environment describes 76 data-lake files; commercial mode describes
  a 41-file subset.
- The academic environment advertises 113 libraries/command tools; commercial mode
  advertises 111.
- 82 local protocol text files are present under `biomni/tool/protocols/`.

The repository-level Apache-2.0 license does not resolve component licensing.
`license_info.md` identifies datasets with commercial, non-commercial, controlled,
or custom terms. Every future integration candidate therefore requires separate
code, model, dataset, database, and API-term checks.

## Model inventory

`biomni/llm.py` implements eight runtime provider routes: OpenAI, Azure OpenAI,
Anthropic, Ollama, Gemini, Bedrock, Groq, and a custom OpenAI-compatible endpoint.
Concrete hosted model names are runtime configuration rather than a fixed bundled
model inventory.

The README separately documents `Biomni-R0-32B-Preview`, described there as a
Qwen-32B-based biology reasoning model trained with reinforcement learning from
agent interaction data. The README points to public model weights and recommends
serving them through an SGLang/OpenAI-compatible endpoint. No weights are stored in
this Git repository, and this audit did not download or execute them.

## MCP capability

The code and official repository documentation expose both directions of MCP use:

1. `A1.add_mcp(...)` loads configured external MCP servers, discovers/wraps their
   tools, and adds them to Biomni's registry.
2. `A1.create_mcp_server(...)` exposes selected Biomni tool modules over MCP.

Examples exist for importing a server and exposing Biomni through stdio. Because
MCP configuration can name Docker, npm, Python, or binary commands and interpolate
environment variables, presence of the feature is a fact while safety of any
particular server remains unassessed.

## Dependency inventory

- `pyproject.toml` requires Python 3.11 or newer and declares `pydantic`,
  `langchain`, and `python-dotenv`; Gradio is optional.
- `biomni_env/environment.yml` defines the main Python 3.11 environment with 30 pip
  entries, including LangGraph/provider integrations, MCP, ToolUniverse, scientific
  computing, notebooks, and tests.
- `biomni_env/bio_env.yml` adds command-line bioinformatics programs and 51 pip
  entries spanning single-cell, genomics, imaging, cheminformatics, simulation,
  and statistics.
- `biomni_env/bio_env_py310.yml` isolates tools needing Python 3.10.
- `biomni_env/cli_tools_config.json` defines seven additional platform-specific
  installers.
- `biomni_env/r_packages.yml` requests R 4.4 or newer and `r-essentials`; the
  repository also includes an expanded R package list and a pinned environment
  export.

This baseline records declared dependencies only. No setup or installation command
was executed.

## Primary evidence

- Repository metadata: https://api.github.com/repos/snap-stanford/Biomni
- Main commit: https://github.com/snap-stanford/Biomni/commit/400c1f366b96a35ca253e13c9b06c5076af41d65
- Latest release: https://github.com/snap-stanford/Biomni/releases/tag/v0.0.8
- Tags API: https://api.github.com/repos/snap-stanford/Biomni/tags?per_page=100
- Package version: `biomni/version.py` at the frozen SHA
- Tool descriptions: `biomni/tool/tool_description/*.py` at the frozen SHA
- Environment inventory: `biomni/env_desc.py`, `biomni/env_desc_cm.py`, and
  `biomni_env/*` at the frozen SHA
- MCP source/docs: `biomni/agent/a1.py`, `README.md`, and
  `docs/mcp_integration.md` at the frozen SHA

Detailed evidence records are in `database/evidence.jsonl`.
