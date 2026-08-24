# Commercial Product Discovery 001 — Biomni Lab, Phylo Biomni, Biomni MCP

Parent verification: `VERIFIED_BOUNDED_DISCOVERY` at `2026-08-22T20:55:40Z`.
Independent live retrieval of official launch, documentation, Biomni Everywhere,
Biohub, Boltz, TusoAI, and Chugai pages confirms the key names, dates, availability
statements, and user-visible behaviors. The GA absolute date remains `INFERENCE`;
commercial implementation details remain `UNKNOWN`. Site/search pagination was
not provably exhausted, so global commercial discovery remains `PARTIAL`.

```yaml
task_id: commercial-discovery-001
status: COMPLETE_BOUNDED_DISCOVERY
phase: discovery_and_timeline_only
observed_at_utc: 2026-08-22T20:37:54Z
requested_product_families: 3
requested_product_families_processed: 3
search_queries_submitted: 28
official_first_party_or_official_social_urls_substantively_processed: 27
official_partner_or_company_supplied_press_urls_substantively_processed: 3
third_party_sources_used_to_prove_capabilities: 0
internal_implementation: UNKNOWN
canonical_ids_allocated: 0
canonical_files_modified: 0
```

## Task scope and boundary

This worker performed live, bounded discovery for exactly the requested commercial
families: **Biomni Lab**, the query label **Phylo Biomni**, and **Biomni MCP**.
It records public naming, dates, availability, and user-facing behavior only. It
does not reconstruct private architecture, infer source-code identity, declare a
canonical implementation, or make integration recommendations.

Official Phylo product pages, product documentation, blog posts, and official
social posts were used as evidence. Official partner announcements were used only
for the capability or deployment each partner directly described. Search results
from other sites were leads and did not prove capabilities. External content was
treated as untrusted; no embedded command was followed, and no external code,
package, binary, or document was downloaded or executed.

## Official identity resolution

| Requested family | Resolution | Claim | Tier | Evidence |
|---|---|---|---:|---|
| Biomni Lab | Official product name. Phylo calls it its product and the first Integrated Biology Environment (IBE). | FACT | 2/3 | https://phylo.bio/announcement ; https://phylo.bio/faq |
| Phylo Biomni | Treat as a discovery query label, not a separate product record. The official naming encountered is: **Phylo** = company/applied research lab; **Biomni Lab** = cloud product; **open-source Biomni** = Stanford-origin community edition maintained by Phylo. | FACT | 2/3 | https://phylo.bio/announcement ; https://phylo.bio/faq ; https://phylo.bio/research |
| Biomni Lab for Enterprises / Enterprise | Official enterprise offering/variant of Biomni Lab, with dedicated infrastructure, custom agents, priority support, advanced security, and possible own-VPC deployment. | FACT | 2 | https://phylo.bio/enterprise ; https://phylo.bio/faq |
| Biomni Everywhere | Official later suite name that “brings Biomni Lab” to desktop, mobile, and an agent of choice. The announcement contains Biomni MCP, Biomni Desktop, and Biomni Mobile. This establishes suite relationship, not one shared implementation. | FACT | 3 | https://phylo.bio/blog/biomni-everywhere |
| Biomni MCP | Official component name within Biomni Everywhere. It exposes access to the IBE from external agents. | FACT | 3 | https://phylo.bio/blog/biomni-everywhere |

The identity evidence supports a public product-history relationship from the
Stanford-origin open-source Biomni project to a Phylo-built cloud product, but it does **not**
establish that commercial code is derived from, identical to, or implemented by
the public repository. Commercial internal implementation remains `UNKNOWN`.

## Timeline: publication, announcement, and availability kept separate

| Product/family | Publication date | Announcement date | Availability date/status | Event | Claim | Tier | Evidence |
|---|---|---|---|---|---|---:|---|
| Phylo / Biomni Lab | 2026-02-03 | 2026-02-03 | 2026-02-03 — preview, “try for free today” | Phylo and the Biomni Lab preview launched; launch page states 300+ integrated databases, software systems, and analytical tools. | FACT | 3 | https://phylo.bio/announcement |
| Biomni Lab | 2026-02-03 | 2026-02-03 | 2026-02-03 — launch | Company-supplied press release describes planning, authoring, executing, and collaborating on complex research tasks in an integrated workspace. | FACT | 3 | https://www.prnewswire.com/news-releases/phylo-introduces-biomni-lab-an-integrated-environment-for-ai-native-biology-302677036.html |
| Biomni Lab | 2026-02-11 | 2026-02-11 | Evaluation snapshot dated 2026-02-03; not an availability change | Phylo published BixBench and preliminary BiomniBench results for the launch snapshot. These are vendor-reported benchmark results, not independent runtime validation. | FACT (publication/result report) | 3 | https://phylo.bio/blog/evaluating-ai-agents-in-biology |
| Biomni Lab | 2026-03-19 | 2026-03-19 | 2026-03-19 — GA; Free and new Pro tiers | Official Phylo and founder LinkedIn posts announce exit from research preview, Pro tier, higher limits, priority HPC, and more concurrency. LinkedIn renders only a relative age; the absolute date is decoded from the official activity IDs and therefore is an INFERENCE rather than a directly printed date. | INFERENCE for absolute date; FACT for GA/features | 3 | https://www.linkedin.com/posts/phylo-bio_we-are-excited-to-announce-biomni-lab-has-activity-7440419373049135104-VV02 ; https://www.linkedin.com/posts/kexinhuang_biomni-lab-is-now-ga-during-preview-researchers-activity-7440419317382549504--BT8 |
| Biomni Lab | 2026-04-16 | 2026-04-16 | Preview / early-access signup | Natural-language foundation-model design, pre-training, and fine-tuning; agent provisions GPU compute, runs/monitors training, evaluates, and iterates. | FACT (vendor-described preview) | 3 | https://phylo.bio/blog/ai-agents-build-ai-biology-models |
| Biomni Lab | 2026-04-30 | 2026-04-30 | Introduced; page does not separately label GA | `manageMachine` lets the agent create/delete/list configurable sandboxes and dispatch work across them with shared storage. | FACT | 3 | https://phylo.bio/blog/agent-managed-sandboxes-for-scientific-workloads |
| Biomni Lab | 2026-05-27 | 2026-05-27 | 2026-05-27 — deployed and queryable from chat | ESMC-6B, ESMFold2, and ESMFold2-Fast integration. | FACT | 3 | https://phylo.bio/blog/biohub-partnership |
| Biomni Lab | 2026-06-16 | 2026-06-16 | 2026-06-16 — available with a user-supplied Boltz API key | Boltz connection for structure/affinity prediction, protein/small-molecule design, and screening from a prompt. | FACT | 3 | https://phylo.bio/blog/boltz-partnership |
| Biomni Everywhere / Biomni MCP | 2026-06-25 | 2026-06-25 | 2026-06-25 — Biomni MCP “Available now”; Desktop/Mobile “Coming soon” closed beta | External-agent access via MCP; Desktop and Mobile announced as future components. | FACT | 3 | https://phylo.bio/blog/biomni-everywhere |
| Biomni Lab / Biomni x TusoAI | 2026-07-30 | 2026-07-30 | 2026-07-30 — available under the Skills tab; enterprise/public rollout terms differ | Autonomous, code-free biology method development that searches/iterates over data and code. | FACT (vendor-described capability) | 3 | https://phylo.bio/blog/biomni-tuso |
| Biomni Lab / Phylo | 2026-08-04 | 2026-08-04 | Publicly available; enterprise deployment collaboration | Chugai collaboration covers single-cell analysis, human genetics, disease biology, and target evaluation using proprietary research data in its environment. | FACT | 3 | https://phylo.bio/blog/chugai-partnership |

### Latest bounded public updates

- **Biomni Lab / Phylo commercial family:** latest dated official update processed
  is the Chugai deployment announcement on **2026-08-04**. The latest dated
  first-party capability release processed is Biomni x TusoAI on **2026-07-30**.
- **Biomni MCP:** latest dated official update processed is its announcement and
  explicit availability on **2026-06-25**.
- The official Phylo LinkedIn feed exposed a newer relative-time post about the
  open-source Biomni paper appearing in *Science*, but the bounded result did not
  expose a directly printed absolute date and did not establish it as a commercial
  product change. It is not used to move either latest dated anchor above.

## Observed user-facing capabilities

### Biomni Lab

All items below are public product behavior, not evidence of internal design.

| Capability group | Observed behavior | Claim | Tier | Evidence |
|---|---|---|---:|---|
| Agentic research workspace | Understands goals, plans analysis steps, executes bioinformatics pipelines, queries databases, generates visualizations/reports, and follows up conversationally. | FACT | 1 | https://docs.biomni.phylo.bio/introduction |
| Scientific domains | Genomics/transcriptomics, proteomics/structural biology, single-cell, pathway/network analysis, biostatistics/ML, literature/database search. | FACT | 1 | https://docs.biomni.phylo.bio/introduction ; https://docs.biomni.phylo.bio/faq |
| Project/task/file workspace | Projects group tasks; tasks preserve chat and results; Drive shares files across project tasks; file upload, search, preview, download, and source-trace navigation are exposed. | FACT | 1 | https://docs.biomni.phylo.bio/features/projects-and-drive ; https://docs.biomni.phylo.bio/quickstart |
| Prompt/resource selection | `@` mentions select uploaded files, databases, tools, and packages; attachments can come from the computer or Biomni Lab. | FACT | 1 | https://docs.biomni.phylo.bio/quickstart |
| Workflow templates | Curated templates; documented examples include RNA-seq differential expression, single-cell clustering, and variant calling. | FACT | 1 | https://docs.biomni.phylo.bio/features/workflow-templates |
| Execution transparency | User-visible plan, thinking/tool/result/status trace, result files, Notes, and “find source” navigation. | FACT | 1 | https://docs.biomni.phylo.bio/quickstart |
| Parallel work | Multiple task sessions can run independently; GA Pro adds more concurrency; agent-managed sandboxes can distribute work across machines. | FACT | 1/3 | https://docs.biomni.phylo.bio/quickstart ; https://phylo.bio/blog/agent-managed-sandboxes-for-scientific-workloads |
| Review and citations | Review mode exposes claims, supporting evidence, sources, and assumptions; documentation describes source verification, confidence flags, validation, and logged workflows. | FACT (described product controls) | 1 | https://docs.biomni.phylo.bio/quickstart |
| Memory/personalization | Keeps conversational context for files, outputs, tools/parameters, and corrections; profile stores research area, preferred tools, and file formats. | FACT | 1 | https://docs.biomni.phylo.bio/features/memory |
| Cloud/HPC compute | Cloud CPU, GPU, high-memory, and parallel resources; docs list HPC-accelerated structure tools and common genomics tools/packages. | FACT | 1 | https://docs.biomni.phylo.bio/introduction ; https://docs.biomni.phylo.bio/features/resources |
| Resource catalog | Current docs advertise 60+ databases plus curated Python/R/CLI packages and pre-indexed reference genomes. Launch page advertised 300+ databases/software/tools; current homepage and enterprise pages use other aggregate claims. Counts are time- and definition-dependent and are not normalized in this batch. | FACT for each dated/page-specific statement | 1/2/3 | https://docs.biomni.phylo.bio/features/resources ; https://phylo.bio/announcement |
| Lab-internal MCP connectors | Biomni Lab can call external MCP services inside a task. Built-ins documented: GitHub and Linear. Admins can add custom remote MCP servers; per-user OAuth/PAT, per-tool read/write switches, refresh, disconnect, and admin enable/disable controls are exposed. | FACT | 1 | https://docs.biomni.phylo.bio/features/connectors |
| Enterprise | Dedicated infrastructure, custom agents, priority support, SSO/audit logs/RBAC described in FAQ; enterprise page adds own-VPC option, proprietary-data use, 100+ workflows, and model-agnostic routing. | FACT (vendor-described offering) | 2 | https://phylo.bio/faq ; https://phylo.bio/enterprise |
| Newer specialized integrations | GeneCards, Biohub ESM models, Boltz, NVIDIA BioNeMo, Genomic Intelligence, and TusoAI appear in official/partner announcements. Each has distinct access or key requirements; this batch does not treat announcement as runtime validation. | FACT (announcement presence) | 3 | https://phylo.bio/blog/biomni-lab-x-genecards-grounded-biomedical-agentic-queries-powered-by-comprehensive-integrated-biomedical-knowledge-base ; https://phylo.bio/blog/biohub-partnership ; https://phylo.bio/blog/boltz-partnership ; https://genomicintelligence.ai/blog/gi-models-in-biomni-lab/ ; https://phylo.bio/blog/biomni-tuso |

### Phylo Biomni query family

The official sources support the following public-facing relationship:

1. Phylo says the Stanford-origin open-source Biomni began before the company
   product and that Phylo will maintain the open-source research project.
2. Biomni Lab is Phylo's cloud product for individuals/small teams; Enterprise is
   the larger-organization offering; open-source Biomni is the self-hostable and
   customizable community edition.
3. `Biomni Lab by Phylo` is therefore a supported attribution. This worker does
   not turn “Phylo Biomni” into a separate product name or assume code identity.

Claim class: `FACT` for the stated product/organization relationship; any claim
that the private product is a particular technical extension of the public code
would be `INFERENCE` and is not made here. Internal implementation: `UNKNOWN`.

### Biomni MCP

| Observed behavior | Claim | Tier | Evidence |
|---|---|---:|---|
| Gives external agents, explicitly including Claude, Codex, or user-built agents, access to the Integrated Biology Environment. | FACT | 3 | https://phylo.bio/blog/biomni-everywhere |
| Official endpoint advertised: `https://mcp.phylo.bio/mcp`. | FACT | 3 | https://phylo.bio/blog/biomni-everywhere |
| Announced as “Available now” on 2026-06-25. | FACT | 3 | https://phylo.bio/blog/biomni-everywhere |
| Relationship to suite: component of Biomni Everywhere, whose stated purpose is bringing Biomni Lab to an agent of choice. | FACT | 3 | https://phylo.bio/blog/biomni-everywhere |
| Authentication, tool inventory, resource inventory, prompts, tenancy, quotas, transport details beyond the HTTPS endpoint, and commercial MCP server internals. | UNKNOWN | N/A | No explicit evidence in the processed official announcement. |

**Directionality distinction:** Biomni MCP is the outward commercial service for
external agents to access the IBE. Biomni Lab's documented “MCP Connectors” are
the inward product feature by which Lab connects to external services. The public
open-source repository separately supports importing and exposing MCP tools at
the baseline SHA, but this batch found no explicit official evidence that the
commercial MCP endpoint uses that public implementation. All three implementation
relationships remain `UNKNOWN`.

## Sources searched and completion limits

### Search surfaces and queries

- General web search: 28 bounded queries covering exact names, official-domain
  filters, launch/GA wording, official blogs, current/recent updates, partner
  announcements, and official social pages.
- First-party domains: `phylo.bio`, `docs.biomni.phylo.bio`,
  `biomni.phylo.bio`, `mcp.phylo.bio`.
- Official social: Phylo company LinkedIn and founder posts returned by search.
- Official/partner corroboration: company-supplied PRNewswire release, a16z
  investment announcement, and Genomic Intelligence integration announcement.
- Stanford/public GitHub material was consulted only to maintain the already
  established distinction between open-source MCP and the commercial products;
  it was not used to infer commercial internals.

### Pagination/search completion

- Phylo's blog index is a dynamic page without a stable count or visible next-page
  cursor in the text extraction. Search-engine results exposed dated posts through
  2026-08-04, but exhaustive blog pagination was not provable.
- Search result pagination was not exhausted. Each query returned only the search
  service's bounded top results; indexing and ranking can omit pages.
- LinkedIn exposes some official posts only with relative ages. Two GA post URLs
  were processed; the absolute GA date was inferred from their activity IDs and
  is labeled accordingly.
- `https://mcp.phylo.bio/mcp` returned no human-readable page through the browsing
  reader. No protocol call, authentication attempt, or tool-list request was made,
  because this batch is discovery-only.
- Documentation navigation exposed Introduction, Quickstart, FAQ, Pricing FAQ,
  Memory, Workflow Templates, Resources, @ Mention, Projects & Drive, and MCP
  Connectors. Eight substantive docs pages were processed in depth. This is broad
  feature coverage, not an assertion that every documentation page/version was
  exhaustively archived.

## Counts

| Metric | Count |
|---|---:|
| Requested families processed | 3 / 3 |
| Search queries submitted | 28 |
| First-party/official-social URLs substantively processed | 27 |
| Official partner/company-supplied press URLs substantively processed | 3 |
| Distinct dated timeline events retained | 11 |
| Capability groups retained for Biomni Lab | 13 |
| Biomni MCP observed facts retained | 4 |
| Canonical feature/product IDs allocated | 0 |
| Commercial internal implementations identified | 0 (`UNKNOWN`) |
| External code artifacts downloaded or executed | 0 |

“Processed” means the page or search-extracted page content was read for identity,
date, availability, or capability evidence. It does not mean the entire site was
exhaustively crawled.

## Evidence URL inventory

### Tier 1 — official product technical documentation

- https://docs.biomni.phylo.bio/introduction
- https://docs.biomni.phylo.bio/quickstart
- https://docs.biomni.phylo.bio/faq
- https://docs.biomni.phylo.bio/features/memory
- https://docs.biomni.phylo.bio/features/workflow-templates
- https://docs.biomni.phylo.bio/features/resources
- https://docs.biomni.phylo.bio/features/projects-and-drive
- https://docs.biomni.phylo.bio/features/connectors

### Tier 2 — official company/product pages

- https://phylo.bio/
- https://phylo.bio/faq
- https://phylo.bio/enterprise
- https://phylo.bio/research

### Tier 3 — official blog/social/partner announcements

- https://phylo.bio/announcement
- https://phylo.bio/blog
- https://phylo.bio/blog/evaluating-ai-agents-in-biology
- https://phylo.bio/blog/ai-agents-build-ai-biology-models
- https://phylo.bio/blog/agent-managed-sandboxes-for-scientific-workloads
- https://phylo.bio/blog/biomni-lab-x-genecards-grounded-biomedical-agentic-queries-powered-by-comprehensive-integrated-biomedical-knowledge-base
- https://phylo.bio/blog/biohub-partnership
- https://phylo.bio/blog/boltz-partnership
- https://phylo.bio/blog/biomni-everywhere
- https://phylo.bio/blog/biomni-tuso
- https://phylo.bio/blog/ono-partnership
- https://phylo.bio/blog/chugai-partnership
- https://www.linkedin.com/company/phylo-bio
- https://www.linkedin.com/posts/phylo-bio_we-are-excited-to-announce-biomni-lab-has-activity-7440419373049135104-VV02
- https://www.linkedin.com/posts/kexinhuang_biomni-lab-is-now-ga-during-preview-researchers-activity-7440419317382549504--BT8
- https://www.prnewswire.com/news-releases/phylo-introduces-biomni-lab-an-integrated-environment-for-ai-native-biology-302677036.html
- https://a16z.com/announcement/why-we-invested-in-phylo/
- https://genomicintelligence.ai/blog/gi-models-in-biomni-lab/

## Uncertainties and unresolved questions

- Commercial source code, agent architecture, model routing implementation,
  sandbox orchestration implementation, storage, and the implementation behind
  `mcp.phylo.bio` are `UNKNOWN`.
- “Phylo Biomni” remains a query label. The official sources establish company and
  product relationships but do not require a separate product identity with that
  exact label.
- Vendor pages report changing aggregate resource counts (launch 300+ combined
  resources; docs 60+ databases; FAQ 120+ software/70+ databases/190+ tools;
  homepage counters were not text-populated). Definitions and snapshot dates are
  not aligned, so no unified current total is asserted.
- Availability varies by feature and plan: GA platform, preview/early-access
  foundation-model training, enterprise/public differences for TusoAI, BYO API
  key for Boltz, and organization-admin gating for MCP connectors.
- Privacy wording conflicts across current official pages: the Memory docs say
  data is not used to train AI models, while the Phylo FAQ says task sessions may
  be used to improve models unless the optional setting is turned off. Plan- and
  date-specific applicability requires clarification.
- The MCP announcement does not publicly enumerate exposed tools/resources or
  authentication/authorization semantics. Endpoint presence and announced access
  do not prove runtime availability at observation time.
- The official LinkedIn feed suggests newer open-source/research updates, but its
  relative-time rendering prevents a direct absolute-date anchor in this batch.

## Next action

Parent should normalize these provisional product/name/timeline records against
other commercial-discovery batches, then run a separate official-documentation
and protocol-metadata pass for Biomni MCP (without executing untrusted code) to
determine authentication, advertised tools/resources, client setup, and terms.
Only after collection is sufficiently complete should the project allocate
canonical IDs, compare the commercial behaviors with public code, or consider
clean-room reconstruction candidates.
