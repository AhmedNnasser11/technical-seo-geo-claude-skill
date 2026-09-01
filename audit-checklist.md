# Audit Checklist — Mandatory Execution

This checklist is a completion contract. Every applicable item must receive evidence and a status.

## Phase 0 — Project and scope discovery

- [ ] Identify whether the target is a website, URL, page, repository, or both.
- [ ] Inspect project structure when source code is available.
- [ ] Inspect `package.json` and detect framework/library versions.
- [ ] Detect Next.js App Router vs other routing.
- [ ] Identify relevant SEO, schema, accessibility, testing, and performance tooling.

## Phase 1 — Live source refresh

- [ ] Load `source-registry.md`.
- [ ] Verify every applicable seed source.
- [ ] Inspect current changelog / updates / release notes where available.
- [ ] Follow relevant first-party sub-links recursively.
- [ ] Record source versions/dates.
- [ ] Resolve conflicts by authority and recency.
- [ ] Do not continue with stale assumptions when a current authoritative source is available.

## Phase 2 — Crawl and indexability

- [ ] Inspect robots.txt.
- [ ] Inspect sitemap(s).
- [ ] Validate sitemap URLs and discoverability.
- [ ] Inspect canonical URLs.
- [ ] Check noindex/nofollow directives.
- [ ] Check HTTP status codes and redirects.
- [ ] Check important pages are crawlable.
- [ ] Crawl internal links.
- [ ] Detect broken internal links.
- [ ] Detect orphan pages.
- [ ] Measure important-page crawl depth.
- [ ] Inspect pagination/faceted navigation where applicable.

## Phase 3 — On-page / semantic structure

- [ ] Validate title and description.
- [ ] Validate heading hierarchy.
- [ ] Validate semantic landmarks.
- [ ] Validate `<main>`, navigation, header/footer usage.
- [ ] Validate meaningful link text.
- [ ] Validate image alternatives.
- [ ] Inspect rendered HTML, not only source JSX, when possible.

## Phase 4 — Accessibility

- [ ] Check form labels.
- [ ] Check keyboard operation.
- [ ] Check visible focus.
- [ ] Check accessible names/roles/states.
- [ ] Check dialogs/menus/tabs/custom controls.
- [ ] Check contrast where tooling permits.
- [ ] Check reduced-motion behavior where relevant.
- [ ] Check current WCAG guidance applicable to the project.

## Phase 5 — Metadata / social

- [ ] Check route-level metadata.
- [ ] Check canonical metadata.
- [ ] Check robots metadata.
- [ ] Check Open Graph.
- [ ] Check Twitter/X card metadata where relevant.
- [ ] Check localization/hreflang where applicable.
- [ ] Check duplicate/conflicting metadata.

## Phase 6 — Structured data

- [ ] Identify all applicable Schema.org types.
- [ ] Validate syntax.
- [ ] Validate required properties for the applicable Google feature.
- [ ] Confirm structured data matches visible content.
- [ ] Check Product / Offer / Breadcrumb / Organization / Article / LocalBusiness types where applicable.
- [ ] Re-check current Google documentation before calling a schema feature required.

## Phase 7 — Performance

- [ ] Check LCP.
- [ ] Check INP.
- [ ] Check CLS.
- [ ] Inspect image dimensions/loading.
- [ ] Inspect font loading.
- [ ] Inspect JavaScript/client boundaries.
- [ ] Inspect render-blocking work.
- [ ] Inspect caching/revalidation strategy.
- [ ] Use current web.dev guidance rather than frozen thresholds.

## Phase 8 — Ecommerce

When applicable:

- [ ] Product pages.
- [ ] Category/collection pages.
- [ ] Product variants.
- [ ] Inventory/availability.
- [ ] Price/currency consistency.
- [ ] Faceted navigation.
- [ ] Internal links.
- [ ] Breadcrumbs.
- [ ] Product structured data.
- [ ] Merchant/search appearance guidance current at audit time.

## Phase 9 — GEO / AEO / AI Search

- [ ] Apply current Google generative-AI guidance first.
- [ ] Separate official guidance from industry GEO claims.
- [ ] Check helpful/original content.
- [ ] Check answer clarity and content structure.
- [ ] Check entity clarity.
- [ ] Check source/citation quality where factual claims require evidence.
- [ ] Check brand/entity consistency.
- [ ] Treat experimental tactics as experimental.
- [ ] Do not claim special AI schema unless current official documentation supports it.

## Phase 10 — Next.js

When Next.js is detected:

- [ ] Detect exact Next.js version.
- [ ] Inspect current version-matched metadata documentation.
- [ ] Check `metadata` / `generateMetadata`.
- [ ] Check file-based metadata.
- [ ] Check sitemap.
- [ ] Check robots.
- [ ] Check rendering strategy.
- [ ] Check server/client boundaries affecting SEO.
- [ ] Check caching/revalidation behavior.
- [ ] Check current Next.js release notes for relevant SEO/security changes.

## Phase 11 — Security / hardening

When applicable:

- [ ] Inspect security headers.
- [ ] Inspect input validation and output encoding.
- [ ] Inspect authentication/session boundaries.
- [ ] Inspect CSRF protections where applicable.
- [ ] Inspect SSRF-sensitive server-side fetches where applicable.
- [ ] Inspect XSS-sensitive HTML rendering.
- [ ] Inspect open redirects and URL handling.
- [ ] Inspect dependency/security advisories when tooling is available.
- [ ] Use current OWASP and framework guidance.

## Phase 12 — Verification

- [ ] Run lint when available.
- [ ] Run typecheck when available.
- [ ] Run build when available.
- [ ] Run tests when available.
- [ ] Run link/route checks when available.
- [ ] Inspect runtime output when possible.
- [ ] Re-check fixes after modifications.
- [ ] Do not call a fix verified until the relevant check passes.

## Phase 13 — Final completion gate

Every section must be marked:

`PASS` / `ISSUES_FOUND` / `NOT_APPLICABLE` / `BLOCKED_AFTER_RETRY`

Before final output:

- [ ] No audit section silently skipped.
- [ ] No required source silently skipped.
- [ ] Relevant sub-links exhausted.
- [ ] All findings have evidence.
- [ ] All findings have sources.
- [ ] All findings have severity.
- [ ] All findings have classification.
- [ ] All blockers have retry/recovery evidence.
- [ ] Remediation order is complete.
- [ ] Final report explicitly states verification coverage.

If any checkbox is not satisfied, **continue the audit instead of finalizing**.
