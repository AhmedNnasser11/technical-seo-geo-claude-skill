# Technical SEO/GEO — Project-Local Runbook

> Durable project instructions only. This file is deliberately compact.
> Persistent scan knowledge lives under `.claude/technical-seo-geo/`.

## Every Run

1. Inspect the project and `git status --short` before making changes.
2. Read this runbook plus the knowledge-layer README; do not load every reference file.
3. Read the compact project/source graph summaries. Load only nodes relevant to the current question.
4. Inspect `package.json` and detect framework/library versions and routing.
5. Create a unique temporary run directory outside the repository for the run ledger and raw logs.
6. Refresh applicable official sources at runtime. The persistent source graph is a map, never the final source of truth.
7. Follow relevant authoritative sub-links recursively until the relevant source frontier is empty.
8. Before auditing a domain, load only that domain's reference module and targeted graph nodes.
9. Scan the actual project files/routes/components needed for the domain.
10. Update persistent project-graph/source-graph nodes with short descriptions, pointers, hashes, and verified conclusions. Never paste whole files/docs.
11. Record material findings in `findings.jsonl` with stable IDs and evidence pointers.
12. Complete every required domain. Never skip because another domain has issues; never stop early.
13. For fixes: edit project files, inspect `git diff`, run narrow validation, then full available validation.
14. Re-audit changed surfaces and adjacent routes/components; update finding state only after verification.
15. After static validation, ask the user once before any server/browser/live HTTP/API verification. If declined, record `USER_DECLINED`; do not run runtime checks or claim runtime verification.
16. If approved, complete all applicable runtime checks, retry transient failures, and re-test affected surfaces.
17. Before final output, confirm every required run-ledger item is terminal and every claimed fix has evidence.
18. Delete only the temporary run directory. Never delete the persistent knowledge layer or other project files.

## Lazy Retrieval Rule

Use the persistent graph to answer **where to look**, not as proof of the current state:

`question -> node -> description -> retrieval_hint -> actual file/source -> fresh evidence`

## Durable-File Rule

`.claude/technical-seo-geo-runbook.md` and `.claude/technical-seo-geo/*` are persistent project documentation/knowledge.

- Create them only if absent.
- Never delete them during run cleanup.
- Never overwrite the whole graph blindly.
- Preserve stable node IDs and existing project-owned notes.
- Keep descriptions short and useful to future agents.
