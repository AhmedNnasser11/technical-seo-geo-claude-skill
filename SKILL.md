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

Before producing the final report, run a completion check.

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
- [ ] Validation/build/lint/typecheck/runtime checks were run when the environment supports them.
- [ ] Every finding has evidence.
- [ ] Every finding has severity and classification.
- [ ] Remediation order is complete.
- [ ] No unresolved `TODO`, `SKIP`, or unverified claim remains in the final audit unless explicitly marked as blocked.

If a gate fails, continue working. Do not finalize the report merely because a plausible report can already be written.

### 5. RECOVERY / RETRY POLICY

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

### 8. DETECT THE ACTUAL STACK

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
