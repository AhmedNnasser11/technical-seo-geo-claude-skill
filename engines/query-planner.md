# Query Planner Contract

The orchestrator derives research tasks from the project graph, active domain, current question, evidence gaps, freshness needs, and source conflicts.

## Query classes

- `exact_fact`: official documentation/specification/API lookup
- `version_applicability`: version, release, affected/fixed behavior
- `implementation`: current framework/library implementation behavior
- `measurement`: metric definitions and measurement methodology
- `emerging_research`: recent changes or practices not yet normalized
- `conflict_resolution`: explicit disagreement between sources

## Required fields

`query_id`, `class`, `query`, `generated_from`, `domain`, `rationale`, `preferred_domains`, `freshness_required`, `requires_open`, `priority`.

## Rules

1. Prefer structured APIs for exact package/version/advisory facts.
2. Prefer official documentation for normative SEO/platform behavior.
3. Use trusted web search when structured data is insufficient, ambiguous, stale, or unable to explain observed behavior.
4. Never promote a search snippet directly to evidence.
5. A web result used materially must be opened, authority-checked, and recorded in provenance.
6. Keep search count bounded by evidence value; do not search every package or topic indiscriminately.
