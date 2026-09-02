# Knowledge Index

Minimal entry point for future runs.

## Persistent location

```text
.claude/technical-seo-geo/
├── README.md
├── project-graph.json
├── source-graph.json
└── findings.jsonl
```

Project-local operational instructions live at `.claude/technical-seo-geo-runbook.md`.

## Retrieval rule

Use:

`question -> node id -> retrieval_hint -> actual file/source -> fresh evidence`

Load summaries and relevant open findings first. Load detailed nodes and domain references only on demand.

## State rule

Graphs are indexes, not truth. Live project files prove project state. Live authoritative sources prove current external rules. Findings are durable and must keep implementation state separate from verification state.

## Temporary state

Per-run execution state, raw captures, browser traces, crawls, and retries live outside the repository in a unique run directory. This package contains no run-state template.
