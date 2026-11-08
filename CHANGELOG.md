# Changelog

## 3.1.0 — Skill packaging and usability fixes

- Added YAML frontmatter (`name`, `description`) to `SKILL.md` so the skill is discoverable.
- Reduced `SKILL.md` to a short workflow; full rules moved to `references/execution-contract.md`.
- Capped source-frontier crawling (8 pages/family, 40/run, 2 hops) with a `PASS_PARTIAL` status.
- Clarified that gates without a script are procedural; made knowledge-layer writes opt-in.
- Scoped the skill explicitly to Next.js; removed hard-coded release numbers and provider-specific wording.
- Validator now checks frontmatter, `SKILL.md` size, and parses policy JSON.
- Added `scripts/validate-run-state.py`: validates temporary run state (ledger, plan, evidence, findings) against the schemas, with a `--final` completeness-gate check.
- Fixed the duplicate `# Changelog` heading.

## 2.0.1 — Source Refresh Hard Gate

- Added a hard external-retrieval gate for SOURCE_REFRESH.
- Reading local registries/runbooks no longer qualifies as live source refresh.
- Added explicit `NO_EXTERNAL_SOURCE_TOOL_AVAILABLE` blocked state.
- Added current-run retrieval evidence requirements and anti-false-pass rules.
- Extended source graph nodes with retrieval state so freshness cannot be inferred from stale timestamps alone.

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

## 3.0.0 — Hybrid Agent Architecture Upgrade

- Added single-orchestrator/deterministic-pipeline architecture contract.
- Added trust-boundary and hostile-repository rules.
- Added tool and source policy files.
- Added provider-neutral external web-search/open contracts with provenance.
- Added dynamic retrieval/query-planner contract.
- Added remediation autonomy tiers and verification schema.
- Added evaluation and adversarial fixture guidance.
