# Persistent Project Knowledge Architecture

> This file explains the durable knowledge layer used by the Technical SEO/GEO skill.
> It is a map and retrieval contract, not a copy of the project or web documentation.

## Purpose

The skill MUST NOT depend on model memory to remember what it scanned, what it learned from sources, or what it changed.
Instead, it keeps a small persistent knowledge graph under:

`.claude/technical-seo-geo/`

The graph is the project's durable navigation layer. Full source pages and full project files remain outside the graph and are loaded only when needed.

## Persistent graph files

### `project-graph.json`

Describes the inspected project as nodes and edges.

A node should answer, in a few lines:

- What is this file/route/component/config?
- Why does it matter to SEO/GEO/security/accessibility/performance?
- What other nodes does it depend on or affect?
- Where is the detailed implementation evidence?
- When was it last scanned and what changed?

Each node MUST include a concise `description` and a `retrieval_hint` so an AI agent can understand why to open it later.

### `source-graph.json`

Describes the authoritative web knowledge graph.

A source node should answer:

- What source is this?
- Why is it authoritative for this rule family?
- Which rule/question does it support?
- Which version/date was observed?
- Which child sources are relevant?
- What short conclusion was extracted?
- Where should the agent go to re-check the source?

The graph stores short conclusions and pointers, NOT copied documentation. The live web remains the source of truth.

### `findings.jsonl`

One durable record per material finding. Each record MUST include:

- stable finding ID;
- concise title and `description`;
- project node IDs and source node IDs;
- evidence pointers;
- severity/classification;
- remediation;
- verification state;
- last verified timestamp.

Do not store huge logs here. Store pointers to files, commands, URLs, or the temporary run ledger instead.

## Graph rules

1. Persistent graph files are documentation/state for future runs, not per-run scratch space.
2. Do not copy full source pages into the graph.
3. Do not copy whole project files into the graph.
4. Prefer one compact node over a long narrative.
5. Update an existing node when the same entity is re-scanned; do not create duplicates for the same canonical path/URL.
6. Preserve stable IDs when updating a node.
7. Use hashes/version markers to decide whether a node needs deeper re-inspection.
8. Source nodes are advisory navigation only: every new audit MUST revalidate applicable sources at runtime.
9. Project nodes are an index only: open the actual project file/route before making a code-level claim.
10. Findings are durable only when they are useful for future work; transient tool output belongs in the temporary run directory.

## Lazy retrieval contract

At the start of a run, load only:

1. `.claude/technical-seo-geo-runbook.md`
2. `.claude/technical-seo-geo/project-graph.json` metadata/summary
3. `.claude/technical-seo-geo/source-graph.json` metadata/summary
4. unresolved/open `findings.jsonl` entries relevant to the current task

Then retrieve details on demand:

`question -> graph node ID -> description -> retrieval_hint -> actual file/source -> evidence`

Never load the entire graph or all source details into context merely because they exist.

## Update policy

### Project graph

Update when:

- a file/route/config is added, removed, renamed, or materially changed;
- a dependency/framework version changes;
- a previous node was based on stale structure.

### Source graph

Update when:

- a source is visited during a live refresh;
- its version/date changes;
- a relevant child source is discovered;
- a rule conclusion is corrected or superseded.

### Findings

Update when:

`OPEN -> FIXING -> FIXED_VERIFIED`

or

`OPEN -> BLOCKED_AFTER_RETRY`

A finding MUST NOT become `FIXED_VERIFIED` without post-fix evidence.

## Safety

The skill MUST never use graph cleanup as a reason to delete user project content.
Only graph records that are obsolete by explicit graph-maintenance rules may be compacted, and deletions must be narrowly scoped.
