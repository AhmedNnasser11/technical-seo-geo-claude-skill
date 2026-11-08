# Technical SEO / GEO Claude Skill — Production Architecture

Version: 3.1.0

This package is an evidence-driven Claude skill for auditing and safely improving modern Next.js websites across technical SEO, GEO/AEO/AI Search, metadata, structured data, internal linking, performance, security, accessibility, and ecommerce.

## Core design

The skill separates four kinds of state:

1. **Persistent project knowledge** — `.claude/technical-seo-geo/` in the target project.
2. **Persistent source knowledge** — source nodes and relationships stored in the same durable knowledge layer.
3. **Persistent findings** — `findings.jsonl`, with implementation and verification kept separate.
4. **Temporary run state** — unique outside-repository state used only while a run is executing; it is never installed by this package.

The graphs are indexes/navigation aids, not replacements for live project files or authoritative web sources.

## Package map

- `SKILL.md` — short skill entry point (frontmatter and workflow).
- `references/execution-contract.md` — full execution rules, loaded on demand.
- `KNOWLEDGE-INDEX.md` — minimal entry point for agents.
- `PROJECT-KNOWLEDGE-ARCHITECTURE.md` — persistence/retrieval design.
- `PROJECT-LOCAL-STEPS.md` — concise runbook to install in a project when absent.
- `source-registry.json` — authoritative source families and seed nodes.
- `audit-manifest.json` — domain applicability, dependencies, evidence, and revalidation contracts.
- `domains/*.md` — domain-specific audit knowledge loaded on demand.
- `schemas/*.schema.json` — machine-checkable contracts for plan, evidence, ledger, graphs, and findings.
- `scripts/validate-package.py` — offline package integrity validator; no network access required.
- `CHANGELOG.md` — changes from the previous architecture.
- `MIGRATION.md` — migration notes for existing installations.

## Runtime source policy

Bundled references are baseline knowledge only. Applicable rules must be rechecked against current authoritative sources during the audit. Google Search currently documents AI Overviews/AI Mode as using the same foundational SEO requirements, with no special AI-only technical requirement; this skill therefore treats GEO/AEO as a retrieval/content-quality analysis layer rather than as a set of guaranteed ranking tricks.

The source registry also tracks current framework/security sources. Version-sensitive security checks must inspect the project's installed version and the current release/security guidance fetched during the run, not versions quoted in this package.

## Important safety behavior

Runtime verification is never started automatically. Static validation must finish first, then the skill asks once for explicit permission before starting servers, browsers, live HTTP/API checks, or runtime crawling.

The package also includes `scripts/cleanup-run.py`, a path-constrained helper for removing one temporary run directory. It refuses to delete the temp namespace root or paths containing protected project-state directories.

## 3.0 agent architecture upgrade

This release adopts a hybrid architecture: one orchestrator LLM over deterministic tools. The repository is explicitly untrusted input. External web search is a discovery/corroboration layer; material claims require opening the canonical source and preserving provenance.

Provider integrations are runtime-configurable. The package never assumes a search provider; if the host supplies none, source refresh is recorded as blocked.

## Scope

Targets Next.js projects (App Router and Pages Router). For other stacks only framework-independent domains apply.

## Persistence

Writing `.claude/technical-seo-geo/` into a target project is opt-in.
