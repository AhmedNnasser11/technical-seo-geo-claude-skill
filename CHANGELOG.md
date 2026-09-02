# Changelog

## 2026-09-02 — Execution / Context / Persistence Hardening

- Removed the persistent `run-ledger-template.md` from the skill package.
- Run ledgers are now explicitly temporary and must live outside the repository in a unique per-run temp directory.
- Added cleanup rules that remove only temporary run state; repository files are never deleted for ledger cleanup.
- Added a compact project-local runbook at `PROJECT-LOCAL-STEPS.md`.
- The skill may create `.claude/technical-seo-geo-runbook.md` only when absent; it must never overwrite or delete it automatically.
- Added a context-budget policy: load reference modules on demand instead of loading all markdown files at once.
- Added mandatory Git diff verification after project changes so fixes cannot exist only in temporary state.
- Added explicit reporting of changed project files and meaningful diff verification.
- Preserved the no-skip, no-early-stop, recursive authoritative-source verification, retry/recovery, evidence, and re-audit requirements.

## 2026-09-02 — Persistent Knowledge Graph

- Added a durable lazy-loaded project/source knowledge layer under `.claude/technical-seo-geo/`.
- Added stable graph node IDs, concise descriptions, retrieval hints, hashes, relationships, and evidence pointers.
- Added durable `findings.jsonl` for cross-run continuity without retaining raw run logs.
- Added JSON schemas for project graph, source graph, and findings.
- Kept the per-run ledger temporary and outside the repository.
- Updated project-local steps to use graph-first, evidence-second retrieval.
