# Technical SEO/GEO Knowledge Index

This skill uses a persistent, lazy-loaded knowledge layer so future runs do not depend on model memory.

## Files copied/created in the target project

```text
.claude/
└── technical-seo-geo/
    ├── README.md
    ├── project-graph.json
    ├── source-graph.json
    └── findings.jsonl
```

## What each file means

- `README.md` — compact description of the knowledge layer and how to retrieve data.
- `project-graph.json` — compact graph of project files/routes/configuration and their relationships.
- `source-graph.json` — compact graph of authoritative sources, relevant child links, versions, and short verified conclusions.
- `findings.jsonl` — durable findings that remain useful across runs.

## Important distinction

`project-graph.json` and `source-graph.json` are **indexes and navigation aids**, not replacements for the real project or live web sources.

The agent MUST open the actual project file before making an implementation claim and MUST re-check applicable live sources before relying on a web rule.

## Retrieval pattern

Use:

`question -> node ID -> description -> retrieval_hint -> real file/source -> evidence`

Do not load the complete graph into context.

## Stability rules

- Stable node IDs survive rescans.
- Existing nodes are updated rather than duplicated.
- Descriptions stay concise.
- Full logs stay outside the persistent graph.
- Per-run execution state stays in the temporary run directory and is deleted after completion.
