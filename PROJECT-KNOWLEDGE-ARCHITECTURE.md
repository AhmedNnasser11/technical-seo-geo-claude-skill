# Persistent Project Knowledge Architecture

## Design goal

Preserve enough structured knowledge to avoid repeatedly scanning the entire repository while never allowing stale graph data to become false proof.

## Storage model

```text
.claude/technical-seo-geo/
├── README.md
├── project-graph.json
├── source-graph.json
└── findings.jsonl
```

## Project graph

Use stable IDs such as:

- `route:/products/[slug]`
- `file:app/products/[slug]/page.tsx`
- `component:ProductCard`
- `config:next.config.ts`
- `endpoint:/api/search`

Nodes contain compact metadata, relationships, retrieval hints, hashes, and evidence pointers. Do not store file bodies.

## Source graph

Use stable IDs such as:

- `google.search.technical-requirements`
- `google.search.ai-features`
- `nextjs.metadata.generate-metadata`
- `schema.release.latest`
- `w3c.wcag.2.2`
- `owasp.top10.2025`

Edges explain provenance and navigation, not authority by themselves.

## Findings

Each line in `findings.jsonl` is one current material finding record. New evidence updates the finding rather than creating duplicate records for the same underlying issue.

## Freshness

A source node has a freshness state that can be:

`FRESH | RECHECK_REQUIRED | STALE | SUPERSEDED | UNAVAILABLE`

A source node can be re-used as a navigation hint even when stale, but its claims cannot be used as the current source of truth until rechecked.

## Incremental scanning

Use content hashes and graph relationships to prioritize unchanged areas, but re-open actual files when:

- the target domain requires current behavior;
- an upstream dependency changed;
- an affected finding is being revalidated;
- the node is missing or stale;
- a route/config boundary changed.

## Migration / preservation

Project-owned additions and notes must not be deleted automatically. Graph compaction may remove only records proven obsolete by current project structure and only when stable identity and relevant history remain preserved.
