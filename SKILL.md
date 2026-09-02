# technical-seo-geo

Automated auditor for technical SEO, semantic HTML, accessibility, metadata, Open Graph, structured data, sitemaps, robots.txt, canonicals, internal linking, Core Web Vitals, Next.js SEO, ecommerce SEO, GEO, AEO, LLM visibility, AI search optimization, and information retrieval optimization.

## NON-NEGOTIABLE EXECUTION CONTRACT

This skill is a **live audit workflow**, not a static checklist.

### 1. LIVE / LATEST SOURCE REQUIREMENT

At the beginning of every audit, you MUST retrieve and verify the latest relevant guidance from the web.

Do not assume that the bundled `.md` files are current. They are the baseline knowledge only.

For every applicable audit domain:

1. Open the seed sources in `source-registry.md`.
2. Verify that the page is reachable and current.
3. Check the source's changelog, updates, release notes, "What's new", or equivalent when available.
4. Follow relevant first-party sub-links discovered inside the source.
5. Continue following relevant sub-links recursively until there are no additional relevant authoritative references that can change the rule being audited.
6. Prefer the newest applicable version of a specification or documentation page.
7. Record the source URL, source date/version when available, and what rule it supports.
8. If a source is unavailable, retry and/or find the authoritative replacement before continuing. Never silently skip it.

### 2. SOURCE HIERARCHY

Use this authority order:

1. Google Search Central / Google web standards
2. W3C / WCAG / WAI / WHATWG
3. Schema.org
4. Next.js official documentation and release/changelog documentation
5. MDN
6. OWASP
7. Official library/framework documentation relevant to the detected stack
8. Reputable industry sources
9. Research papers / experimental GEO-AI sources

A lower-authority source MUST NOT override a directly applicable higher-authority source.

If sources conflict:
- Prefer the newer authoritative source.
- Record the conflict.
- Explain which source won and why.
- Never silently choose one.

### 3. NO-SKIP / NO-EARLY-STOP POLICY

The agent MUST NOT:
- skip an audit category because another category already found problems;
- skip source verification because the bundled reference looks sufficient;
- skip a sub-link because the parent page was already read;
- stop after finding a few critical issues;
- replace required verification with assumptions;
- report "not checked" without a documented blocker and recovery attempt.

The audit is complete only when every applicable category has a recorded status:

- `PASS`
- `ISSUES_FOUND`
- `NOT_APPLICABLE` with evidence
- `BLOCKED_AFTER_RETRY` with evidence of attempts and an alternative source/path where possible

A category cannot be silently omitted.

### 4. COMPLETION GATE

Before producing the final report, run a completion check against the mandatory run ledger. The report is generated only from terminal ledger states.

Required gates:

- [ ] Latest-source refresh completed for every applicable domain.
- [ ] Relevant sub-links were recursively inspected.
- [ ] Source conflicts were resolved or explicitly documented.
- [ ] SEO/indexability audit completed.
- [ ] Semantic HTML audit completed.
- [ ] Accessibility audit completed.
- [ ] Metadata/Open Graph/canonical audit completed.
- [ ] Structured-data audit completed.
- [ ] Sitemap/robots audit completed.
- [ ] Internal-link audit completed, including crawl depth and orphan detection.
- [ ] Performance/Core Web Vitals audit completed.
- [ ] Ecommerce audit completed when applicable.
- [ ] GEO/AEO/AI-search audit completed.
- [ ] Next.js audit completed when Next.js is detected.
- [ ] Relevant security/hardening checks completed when the application exposes web/server functionality.
- [ ] Static validation (lint/typecheck/build) was run when the environment supports it.
- [ ] Runtime/live verification is either `COMPLETED` after explicit user approval or `USER_DECLINED` with runtime claims explicitly excluded.
- [ ] Every finding has evidence.
- [ ] Every finding has severity and classification.
- [ ] Remediation order is complete.
- [ ] No unresolved `TODO`, `SKIP`, or unverified claim remains in the final audit unless explicitly marked as blocked.

If a gate fails, continue working. Do not finalize the report merely because a plausible report can already be written.

### 4A. LIVE RUNTIME VERIFICATION — EXPLICIT USER CONSENT REQUIRED

Live/runtime verification is optional and MUST NOT begin automatically.

After static validation is complete (`lint`, `typecheck`, `build` when applicable), determine whether runtime verification would materially improve confidence. Before doing any of the following, ASK THE USER ONCE for permission:

- starting or restarting a development server;
- browser automation;
- live HTTP route probing;
- live API integration testing;
- route crawling against a running application;
- checking rendered runtime behavior.

Use this prompt:

> Static validation is complete. Live runtime verification can test actual routes, HTTP status codes, rendered pages, API integration, and browser behavior. Do you want me to continue with live/runtime verification? (yes/no)

Rules:

1. Do not start a server, browser session, live route crawl, or live integration probe before explicit approval.
2. Ask only once per run. A clear `yes` means proceed with the complete runtime verification scope that is applicable; a clear `no` means do not perform runtime verification.
3. If the user declines, record `USER_DECLINED` in the temporary run ledger. This is not a failure and MUST NOT be converted into `BLOCKED_AFTER_RETRY`.
4. If the user declines, continue all remaining non-runtime checks that can be completed safely, then report runtime verification as not performed. Never claim runtime behavior was verified.
5. If the user approves, complete the full applicable runtime scope. Do not stop at the first runtime failure. Diagnose, retry transient failures, continue independent checks, and re-test affected surfaces after fixes.
6. The final report MUST distinguish `STATIC VERIFIED`, `RUNTIME VERIFIED`, and `RUNTIME USER-DECLINED`.
7. Runtime verification is never a reason to skip static checks, source refresh, source-link traversal, project scanning, or other mandatory domains.

## 5. RECOVERY / RETRY POLICY

When a required operation fails:

1. Diagnose the failure.
2. Retry using the same reliable path when appropriate.
3. Try an equivalent authoritative source/path.
4. Continue with independent audit work that does not depend on the failure.
5. Return to the blocked item.
6. Record the final status and evidence.

A temporary web failure is not permission to use stale knowledge without disclosure.

### 6. SOURCE GRAPH / SUB-LINK CRAWLING

Treat every authoritative documentation page as a node in a source graph.

For each opened source page:

- inspect links to specifications, API references, changelogs, migration guides, updates, validation tools, and related official guidance;
- follow relevant links that can materially change the implementation rule;
- avoid irrelevant navigation, marketing, comments, or unrelated product pages;
- deduplicate URLs and canonicalize obvious URL variants;
- keep a visited-source ledger;
- do not revisit a URL unless its content/version changed or a conflicting claim requires re-checking.

The goal is **relevant-source completeness**, not an arbitrary crawl-depth limit.

### 7. EVIDENCE-FIRST RULE

Do not convert a recommendation into a finding without evidence.

For each finding, capture:

- exact code/page/URL evidence;
- source supporting the rule;
- source date/version when available;
- why the current implementation violates or misses the rule;
- concrete remediation.

Distinguish clearly between:
- confirmed defect;
- risk;
- recommendation;
- emerging practice;
- experimental idea.

### 7A. CONTEXT BUDGET / ON-DEMAND REFERENCE LOADING

The bundled reference files are intentionally modular. Do NOT load every `.md` file into context at the start of a run.

Use this loading order:
1. Read `SKILL.md` and `source-registry.md`.
2. Inspect the project and determine which audit domains are applicable.
3. Load only the reference file(s) needed for the domain currently being audited.
4. After a domain is completed, keep its result in the run ledger instead of retaining the full reference text in active context.
5. Load additional modules only when a finding, framework version, source conflict, or implementation detail requires them.

The project-local runbook defined below is the compact operational memory for future runs. It MUST be preferred over copying this entire skill into project context.

## 7B. PROJECT-LOCAL RUNBOOK (DURABLE, NEVER AUTO-DELETED)

On first use in a project, create a compact file at `.claude/technical-seo-geo-runbook.md` **only if it does not already exist**.

Rules for this file:
- It is durable project documentation, not run state.
- Never overwrite it automatically after creation.
- Never delete it during ledger cleanup.
- Keep it short (target: <= 120 lines).
- It contains only the execution sequence, project-specific decisions, and pointers—not copied reference documentation.
- Update it only when a project-specific workflow decision is genuinely changed, and preserve existing project-owned content.

The initial runbook content should be the compact step sequence shown in `PROJECT-LOCAL-STEPS.md`.


## 7C. PERSISTENT PROJECT KNOWLEDGE GRAPH (DURABLE, LAZY-LOADED)

The skill MUST persist the useful results of project scanning and source discovery so future runs do not depend on model memory.

Create this directory only if absent:

`.claude/technical-seo-geo/`

Required durable files:

- `README.md` — compact description of the knowledge layer and retrieval contract.
- `project-graph.json` — compact graph of project files/routes/configuration.
- `source-graph.json` — compact graph of authoritative source pages and relevant child links.
- `findings.jsonl` — durable material findings that are useful across runs.

### What the graphs are

The graphs are **navigation/index layers**, not copies of the project or the web.

Every project node MUST have:

- stable `id`;
- canonical `path` or route;
- concise `description` explaining what the node is and why it matters;
- `retrieval_hint` explaining when an AI should open it;
- status/hash/last-scanned metadata when available;
- evidence pointers rather than copied file contents.

Every source node MUST have:

- stable `id`;
- canonical URL;
- concise `description` explaining why the source matters;
- `retrieval_hint` explaining which question should cause the agent to open it;
- authority/scope;
- version/date/last-checked metadata when available;
- short conclusions only;
- edges to relevant child sources;
- no full copied documentation.

Every durable finding MUST have:

- stable finding ID;
- concise title and description;
- linked project/source node IDs;
- evidence pointers;
- severity/classification;
- remediation;
- verification state.

### Lazy-loading contract

Do NOT load the full graph into context.

At run start load only:

1. the compact runbook;
2. graph README/metadata;
3. a summary of project nodes;
4. a summary of source nodes;
5. relevant open findings.

Then retrieve details using:

`question -> node ID -> description -> retrieval_hint -> actual file/source -> evidence`

The agent MUST open the actual project file before making a code-level claim.
The agent MUST revalidate applicable web sources before treating a source-node conclusion as current.

### Graph update rules

- Preserve stable IDs across rescans.
- Update existing canonical nodes instead of creating duplicates.
- Add edges when relationships are discovered.
- Replace stale descriptions/conclusions with the newer verified ones.
- Store hashes/version markers so deeper inspection can be skipped only when the underlying entity has not changed and the audit does not require a fresh re-check.
- Do not store full logs, full source pages, or full project files in the persistent graph.
- Keep transient command output and the mandatory run ledger in the temporary run directory only.

### Source graph is NOT a substitute for LIVE verification

A persisted source node can answer **where and why to look**. It cannot make an old conclusion current.
Every applicable audit still requires runtime source refresh, recursive relevant-link verification, and recording the newly selected authoritative version/date.

### Findings are durable; run state is not

Persistent findings survive across runs because they provide useful continuity.
The per-run execution ledger does NOT survive and MUST remain outside the repository.

## 8. DETECT THE ACTUAL STACK

Before applying framework-specific rules:

- inspect `package.json`;
- detect Next.js version;
- detect React version;
- detect TypeScript;
- detect routing model;
- detect UI/accessibility libraries;
- detect schema/SEO libraries;
- detect testing/build tooling.

Apply the latest rules appropriate to the detected versions. Do not force Next.js rules onto a non-Next.js project.

## 8A. NO-VOLUNTARY-STOP RULE

The agent MUST NOT voluntarily terminate the run because the task is large, many issues have already been found, one tool failed, or a plausible report can already be produced. Continue all independent work and return to blocked work before finalization. If an external constraint truly prevents completion, record the exact constraint, completed coverage, recovery attempts, and remaining unverified items rather than implying completion.

## 9. MANDATORY RUN LEDGER (ANTI-SKIP / ANTI-EARLY-STOP)

Every run MUST maintain an explicit audit ledger in memory or in a temporary working file. The ledger is the execution state machine for the audit; a prose report is not a substitute.

### Run-ledger storage and cleanup (MANDATORY)
- Do NOT keep a per-run ledger template or run-state file inside the user's project repository.
- Do NOT create, overwrite, or delete a persistent project file merely to track the current run.
- Store run state only in a temporary run directory outside the repository, for example `$TMPDIR/technical-seo-geo/<run-id>/`.
- The temporary directory MUST be unique per run.
- On normal completion, delete the temporary run directory.
- On a crash/interruption, a subsequent run MUST clean up stale `technical-seo-geo/*` temp run directories before starting a new run.
- Never delete user project files, `.git`, `context/`, `.claude/`, or any other persistent project content as part of ledger cleanup.
- The old bundled `run-ledger-template.md` is intentionally NOT required and MUST NOT be installed into the project.

This separation is deliberate: the project keeps only durable instructions; transient execution state never pollutes the repository or inflates future context.

The ledger MUST contain at least:

| ID | Domain | Required? | Source status | Audit status | Evidence | Recovery status |
|---|---|---:|---|---|---|---|
| D1 | Live source refresh | yes | pending/verified/blocked | pending/pass/issues/blocked | URL(s) | attempts |
| D2 | Crawl/indexability | yes | ... | ... | ... | ... |
| D3 | Semantic HTML | yes | ... | ... | ... | ... |
| D4 | Accessibility | yes | ... | ... | ... | ... |
| D5 | Metadata/social | yes | ... | ... | ... | ... |
| D6 | Structured data | yes | ... | ... | ... | ... |
| D7 | Sitemap/robots/canonical | yes | ... | ... | ... | ... |
| D8 | Internal links | yes | ... | ... | ... | ... |
| D9 | Performance/CWV | yes | ... | ... | ... | ... |
| D10 | Ecommerce | conditional | ... | ... | ... | ... |
| D11 | GEO/AEO/AI search | yes | ... | ... | ... | ... |
| D12 | Next.js | conditional | ... | ... | ... | ... |
| D13 | Security/hardening | conditional | ... | ... | ... | ... |
| D14 | Validation gates | yes | ... | ... | ... | ... |

Rules:

1. A domain starts as `pending` and cannot be considered complete without an explicit terminal status.
2. `pending`, `in_progress`, `TODO`, `SKIP`, `unknown`, and blank are non-terminal states and forbid finalization.
3. If work is interrupted by an error, timeout, rate limit, missing dependency, or tool failure, mark the affected item `BLOCKED_AFTER_RETRY` only after recovery attempts are exhausted; continue all independent domains first, then retry the blocked item again.
4. The agent MUST NOT mark a whole domain `PASS` because a subset of checks passed.
5. If an item is not applicable, attach concrete evidence for why it is not applicable.
6. Before final output, every required ledger row must be terminal and every conditional row must be explicitly marked `NOT_APPLICABLE` or audited.
7. The final report MUST be generated from the ledger, not from memory or intuition.

### Ledger completion invariant

`FINALIZABLE = all(required items are terminal) AND all findings have evidence AND all mandatory source refreshes are terminal AND all applicable validations have explicit results`.

If `FINALIZABLE = false`, do not produce the final audit report. Continue execution or report the exact blocker only after all allowed recovery paths have been exhausted.

## 10. MANDATORY LIVE-SOURCE EXPIRY / FRESHNESS RULE

"Latest" means latest authoritative information discoverable at runtime, not latest information known by the model and not latest bundled markdown.

For each applicable source family:

1. Open the seed/current page.
2. Read its last-updated/publication/version information when available.
3. Inspect the official change log, updates page, release notes, history, or version index.
4. Follow relevant first-party links recursively.
5. Re-check the current source after following newer references when the older page points to them.
6. Record the selected authoritative version/date in the ledger.

Never hardcode a current framework version, Core Web Vitals threshold, structured-data feature, accessibility status, or Google Search behavior into the final recommendation without runtime verification.

### Source freshness precedence

When multiple pages cover the same rule, choose in this order:

1. Current normative specification / official documentation for the detected version.
2. Current official release/changelog/security advisory.
3. Current official implementation guide.
4. Secondary documentation only when first-party sources do not cover the issue.
5. Industry/marketing sources for supplementary or experimental practices only.

A newer draft does NOT automatically override an existing finalized recommendation. Record standards status (`Recommendation`, `Working Draft`, `Deprecated`, etc.) and apply the appropriate normative authority.

## 11. RECURSIVE SUB-LINK VERIFICATION — WITH A REAL STOP CONDITION

The recursive crawl MUST be breadth/depth safe and complete for relevant authoritative links.

For every source node, inspect links whose destination could change an audit rule, including:

- standards/specifications;
- API references;
- versioned documentation;
- migration guides;
- changelogs and release notes;
- security advisories;
- deprecation notices;
- validation requirements/tools;
- official examples that define behavior;
- official Google Search feature documentation;
- official framework/library compatibility documentation.

Use a visited-set keyed by normalized URL. Do not count duplicate query-string variants as new evidence unless the query changes the document content or version.

A source family is exhausted only when:

`frontier == empty`

where `frontier` contains all newly discovered, relevant, authoritative links not yet inspected.

Do NOT use a fixed crawl-depth such as "follow 2 levels" as the completion criterion.

Do NOT crawl unrelated navigation, ads, comments, social links, or generic marketing content merely to claim deeper crawling.

For every source family, record:
- seed URL;
- visited URLs;
- relevant links followed;
- links intentionally rejected as irrelevant (brief reason);
- source/version selected for each audited rule;
- whether the family reached an empty relevant frontier.

## 11A. PERSISTENT KNOWLEDGE WRITE-BACK

At the end of each completed audit domain, write back only durable, reusable knowledge:

1. Update existing project/source nodes by stable ID when they already exist.
2. Add new nodes only for new canonical files/routes/sources.
3. Add or update edges that explain dependency, route, ownership, source->rule, or source->child relationships.
4. Keep each node description short enough to scan quickly.
5. Store the exact evidence pointer, not a copied transcript.
6. Write durable findings to `findings.jsonl` only when they remain useful beyond the current run.
7. Leave raw logs, full HTML dumps, browser traces, and run-ledger state in the temporary run directory.
8. If a prior node is stale, mark it stale/replaced and point to the new node instead of silently keeping contradictory facts.

The knowledge graph is a **retrieval layer**. The actual project files and live sources remain the evidence layer.

## 12. FIX / REMEDIATION LOOP (WHEN THE TASK REQUESTS CHANGES)

When the user asks the skill to fix or improve the project, auditing alone is incomplete.

After discovering issues:

1. Group findings by root cause.
2. Apply the safest minimal change that satisfies the current authoritative rule.
3. Prefer framework-native and documented solutions over custom workarounds.
4. Re-run the affected static/runtime checks.
5. Re-audit the changed surface.
6. Check for regressions in adjacent routes/components.
7. Update the ledger finding from `OPEN` to `FIXED_VERIFIED` only after evidence supports the fix.
8. If the fix cannot be safely verified, keep it open or blocked; never label it fixed based only on code inspection.

Never stop after the first successful fix. Continue until all requested and applicable findings have terminal verification states.

## 13. COMMAND / TOOL FAILURE MATRIX

A failed command is evidence about the command, not evidence that the audited condition passes.

For each failed operation record:
- command/tool;
- exit/error;
- attempted recovery;
- alternative command/tool/source;
- final disposition.

Examples:

- `npm` command unavailable → inspect package manager files and use the detected package manager or `corepack` path.
- Browser audit unavailable → use static HTML plus HTTP/source checks; mark browser-only assertions as blocked if they cannot be established.
- Network fetch fails → retry, then use an authoritative mirror/version index if one exists; do not silently fall back to stale bundled guidance.
- One URL fails → continue crawling independent URLs and return to the failed URL later.
- Build fails because of an unrelated pre-existing issue → distinguish the pre-existing blocker from the SEO finding; still complete all independent audits.

The agent MUST continue independent work after a failure. A single failed tool call is never a valid reason to terminate the entire audit.

## 14. MODIFICATION SAFETY RULES

When changing code/configuration:

- preserve existing project conventions unless they conflict with authoritative requirements;
- do not invent unsupported SEO tags, schema types, or AI-specific metadata;
- do not add security controls that break legitimate application behavior without documenting compatibility impact;
- do not weaken security, accessibility, caching, or indexability just to make a check pass;
- do not rewrite unrelated files merely for formatting;
- keep diffs focused and reviewable;
- run the narrowest relevant validation first, then the full available validation suite.

## 14A. CHANGE VISIBILITY / GIT SAFETY

When the task requests code/configuration changes:

1. Before editing, inspect `git status --short` and the relevant file history when available.
2. Make focused changes; do not hide changes in generated or temporary files.
3. After editing, run `git diff --` on every changed project file and verify the intended diff is actually present.
4. Confirm no required change exists only inside the temporary run directory or inside the skill package itself.
5. Run relevant validation after the diff check.
6. At the end, report the exact changed project files and summarize the meaningful diff.
7. Never run destructive cleanup commands against the repository to clean audit state.

A successful tool call does not prove that a persistent project change exists; the final verification must inspect the repository diff.

## 15. FALSE-CONFIDENCE GUARDRAILS

The agent MUST NOT claim:

- "all links are valid" after checking only a sitemap;
- "accessible" after running only an automated scanner;
- "Core Web Vitals pass" without an actual measurement or clearly labeled code-risk assessment;
- "Google ranking factor" for unsupported or speculative GEO/AEO advice;
- "AI visibility guaranteed" from metadata, llms.txt, schema, or similar tactics;
- "secure" from headers alone;
- "schema valid" merely because JSON parses.

Use explicit evidence levels:
- `OBSERVED` — directly measured/inspected.
- `VERIFIED` — observed and independently validated.
- `INFERRED` — logically inferred from code/config; not runtime-proven.
- `UNVERIFIED` — insufficient evidence.
- `BLOCKED` — verification could not be completed after recovery attempts.

## Audit behavior

When given a website, page, or codebase, assess:

1. SEO structure and indexability.
2. Semantic HTML and document structure.
3. Accessibility and keyboard support.
4. Metadata, canonical, and social sharing tags.
5. Structured data completeness and validity.
6. Sitemap and robots behavior.
7. Internal linking, crawl depth, broken links, and orphan pages.
8. Core Web Vitals and performance risks.
9. Ecommerce SEO signals where product/category pages exist.
10. GEO / AEO readiness and AI extractability.
11. Next.js SEO conventions when Next.js is detected.
12. Relevant web security/hardening controls when applicable.

## Validation requirements

When technically possible, use multiple evidence types:

- source inspection;
- static code analysis;
- route/page inspection;
- rendered HTML inspection;
- HTTP response/header inspection;
- link crawling;
- sitemap/robots retrieval;
- structured-data validation;
- accessibility checks;
- build/typecheck/lint;
- runtime/browser verification.

Do not treat a single successful command as proof that the entire audit passed.

## Output format

### Executive Summary

- Overall Score (0–100)
- SEO Score
- Accessibility Score
- Performance Score
- GEO Score
- AEO Score
- LLM Visibility Score
- Security/Hardened Surface status when applicable

### Verification Coverage

Show every audit domain with one of:

- PASS
- ISSUES_FOUND
- NOT_APPLICABLE
- BLOCKED_AFTER_RETRY

Also report:

- number of authoritative sources inspected;
- number of relevant sub-links followed;
- number of URLs/pages/routes inspected;
- validations/checks executed;
- any remaining blockers.

### Issues grouped by severity

For each issue include:

- Category
- Severity
- Why It Matters
- Impact
- Evidence
- Fix
- Example
- Classification
- Source(s)

### Recommended remediation order

1. Critical issues that block indexing, accessibility, security, or rendering.
2. High-priority issues affecting ranking, snippets, crawlability, security, or AI visibility.
3. Medium-priority structural, accessibility, and performance issues.
4. Low-priority refinements.
5. Opportunity items for GEO / AEO experimentation.

## Scoring guidance

- Start from 100 and subtract for confirmed issues.
- Critical issues reduce the score the most.
- High severity issues materially affect visibility, security, or usability.
- Medium issues affect structure, consistency, accessibility, or performance.
- Low issues are polish items.
- Opportunity items do not reduce score unless they also create a concrete defect.
- Never manufacture a numeric score from missing evidence. If evidence is insufficient, mark the relevant area as blocked and explain why.

## Mandatory source protocol

See `source-registry.md` for the seed sources and runtime refresh protocol.

The bundled reference files are implementation guidance and a fallback baseline. They MUST NOT prevent the agent from checking newer official guidance.

## File map

- `source-registry.md` — live source seeds, authority hierarchy, recursive source verification
- `PROJECT-LOCAL-STEPS.md` — compact steps to install into `.claude/technical-seo-geo-runbook.md`; persistent and never auto-deleted
- `PROJECT-KNOWLEDGE-ARCHITECTURE.md` — persistent project/source knowledge-graph contract
- `KNOWLEDGE-INDEX.md` — compact index of persistent graph files and retrieval rules
- `project-graph.schema.json` — schema for the project graph
- `source-graph.schema.json` — schema for the source graph
- `finding.schema.json` — schema for durable findings
- `semantic-html.md` — document structure, landmarks, headings, forms
- `accessibility.md` — labels, keyboard, focus, ARIA, WCAG usage
- `metadata.md` — titles, meta descriptions, robots directives in metadata
- `open-graph.md` — OG tags and social metadata
- `schema.md` — structured data rules and validation
- `sitemap.md` — sitemap.xml and sitemap strategy
- `robots.md` — robots.txt crawl control and indexability
- `canonical.md` — canonicalization and duplicate handling
- `internal-links.md` — crawlable links, anchor text, breadcrumbs
- `core-web-vitals.md` — LCP, INP, CLS and performance logic
- `nextjs-seo.md` — Next.js metadata, routing, sitemap/robots, rendering
- `ecommerce-seo.md` — product/category pages, facets, inventory handling
- `geo.md` — GEO practices
- `aeo.md` — answer-engine content patterns
- `llm-visibility.md` — extractability, citation readiness, entity clarity
- `ai-search.md` — AI Overviews and AI search positioning
- `audit-checklist.md` — step-by-step audit and completion gates

## Required caution

If a finding is supported only by emerging or experimental evidence, label it clearly and do not present it as a guaranteed ranking factor.
