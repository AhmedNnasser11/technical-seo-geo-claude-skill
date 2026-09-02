# Migration note — Source Refresh Hard Gate

Version 2.0.1 tightens source freshness semantics. Existing source graph nodes may remain useful as historical/navigation metadata, but they do not satisfy current-run freshness on their own. On the next run, each applicable source family must obtain external retrieval evidence or be marked `BLOCKED_AFTER_RETRY` when no external source tool is available.

# Migration Notes

## From the previous package

The new version keeps the durable knowledge concept but changes its contracts.

### Persistent files

Continue using:

- `.claude/technical-seo-geo/project-graph.json`
- `.claude/technical-seo-geo/source-graph.json`
- `.claude/technical-seo-geo/findings.jsonl`
- `.claude/technical-seo-geo-runbook.md`

Back up these files before the first migration run.

### Run ledger

A project-local `run-ledger-template.md` is no longer part of the architecture. Runtime state is temporary and external to the repository. The new schema describes that state without installing it.

### Findings

Map the previous combined state `FIXED_VERIFIED` to:

- `status: FIXED`
- `verification_status: VERIFIED`

Only keep `VERIFIED` when the existing record contains post-fix evidence. Otherwise downgrade it to `FIXED`/`UNVERIFIED` and revalidate.

### Source registry

Rebuild or normalize old flat source records into source nodes using `source-registry.json` and the source-node schema. URLs that no longer resolve should not be treated as current merely because they existed in the old registry.

### Project-local runbook

Create the new compact runbook only when it does not exist. Do not overwrite an existing project-owned runbook automatically.
