# Changelog

## 2.0.0 — Production architecture

### Replaced

- Flat source-list thinking with an explicit source knowledge graph and relevance frontier.
- Prose-only completion with a machine-checkable audit state machine.
- Combined `FIXED_VERIFIED` finding state with separate implementation and verification state.
- Weak/unexplained `UNKNOWN` handling with explicit terminal domain statuses.
- Generic runtime wording with a hard post-static consent boundary.
- Ambiguous temp cleanup with a dedicated, path-scoped temporary-state contract.

### Added

- `audit-manifest.json` for domain applicability, inputs, evidence, pass/issue criteria, and revalidation triggers.
- `schemas/audit-plan.schema.json`.
- `schemas/evidence.schema.json`.
- `schemas/run-ledger.schema.json`.
- Stronger project/source/finding schemas.
- Source authority and freshness metadata.
- Source conflict records and recursive frontier accounting.
- Git attribution model for pre-existing vs intended/unrelated changes.
- Offline package self-validator.
- Migration notes and concise project-local runbook.

### Retained/improved

- Persistent project graph.
- Persistent source graph.
- Persistent findings.
- On-demand domain reference loading.
- Retry/recovery and no-early-stop behavior.
- Runtime consent requirement.
