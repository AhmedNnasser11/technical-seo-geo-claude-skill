# Live Source Registry

This registry is a **runtime seed graph**, not a frozen source of truth.

At every run, the agent MUST refresh the applicable sources, inspect official update/version history, and recursively follow relevant authoritative sub-links until the relevant frontier is exhausted.

## Google Search / SEO / AI Search

**Description:** Primary normative source family for Google crawling, indexing, search appearance, structured-data eligibility, spam policies, and current AI-search/generative-AI guidance.

**Retrieval hint:** Open this family for any question about Google Search behavior, indexability, rich results, AI features, Search policies, or whether an SEO/GEO tactic is officially supported.


### Seeds
- https://developers.google.com/search/docs
- https://developers.google.com/search/updates
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/appearance/structured-data/intro
- https://developers.google.com/search/docs/crawling-indexing/overview
- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- https://developers.google.com/search/docs/essentials/spam-policies

### Runtime requirements
- Inspect the current Search Central updates page.
- Follow current AI-search/generative-AI guidance and any linked feature-specific documentation.
- Re-check structured-data feature support before recommending a type or property.
- Check deprecations, feature removals, and policy updates.
- Treat GEO/AEO industry claims as secondary unless Google explicitly supports them.

## Next.js

**Description:** Version-sensitive first-party source family for Next.js routing, metadata, rendering, sitemap/robots conventions, caching, and framework security/release changes.

**Retrieval hint:** Open after detecting Next.js, or whenever a proposed implementation depends on a Next.js API, file convention, rendering behavior, cache behavior, or release/security change.


### Seeds
- https://nextjs.org/docs
- https://nextjs.org/blog
- https://nextjs.org/docs/app/api-reference/functions/generate-metadata
- https://nextjs.org/docs/app/api-reference/file-conventions/metadata
- https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap
- https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots
- https://nextjs.org/docs/app/api-reference/next-config-js/headers
- https://nextjs.org/docs/app/building-your-application/optimizing
- https://nextjs.org/docs/app/building-your-application/rendering

### Runtime requirements
- Detect the exact installed Next.js version from the project.
- Prefer version-matched official docs.
- Inspect Next.js release notes/security notices relevant to the detected major/minor/patch line.
- Do not assume the newest major is the correct upgrade target; distinguish current, active LTS, maintenance LTS, and unsupported versions.

## Web Performance / Core Web Vitals

**Description:** Current web.dev guidance for user-centric performance metrics and measurement methodology, including LCP, INP, and CLS.

**Retrieval hint:** Open when assessing performance, Core Web Vitals, loading/rendering behavior, or whether a code-level optimization is supported by current performance guidance.


### Seeds
- https://web.dev/performance
- https://web.dev/vitals/
- https://web.dev/articles/lcp
- https://web.dev/articles/inp
- https://web.dev/articles/cls

### Runtime requirements
- Verify current metric definitions and thresholds.
- Prefer field/user data where available; clearly label lab measurements.
- Do not declare a pass from code inspection alone.

## Security

**Description:** OWASP and related authoritative security guidance used to identify applicable web-application attack surfaces and hardening requirements.

**Retrieval hint:** Open when the application exposes forms, APIs, server-side fetches, authentication/session boundaries, HTML injection surfaces, redirects, or security-sensitive configuration.


### Seeds
- https://owasp.org/www-project-top-ten/
- https://owasp.org/Top10/2025/
- https://cheatsheetseries.owasp.org/IndexTopTen.html
- https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html

### Runtime requirements
- Detect the application's actual attack surface first.
- Check current OWASP material and current framework/library advisories when relevant.
- Keep security findings evidence-based and applicability-aware.

## Accessibility

**Description:** W3C WAI/WCAG/ARIA normative and supporting guidance for accessible structure, keyboard interaction, focus, names/roles/states, and conformance claims.

**Retrieval hint:** Open when auditing a11y behavior, semantic structure, custom controls, dialogs/menus/tabs, keyboard operation, or WCAG conformance.


### Seeds
- https://www.w3.org/WAI/
- https://www.w3.org/WAI/standards-guidelines/
- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://www.w3.org/WAI/WCAG22/quickref/
- https://www.w3.org/WAI/standards-guidelines/aria/
- https://www.w3.org/TR/wai-aria/
- https://www.w3.org/TR/wai-aria-1.2/

### Runtime requirements
- Prefer finalized Recommendations for normative conformance claims.
- Inspect W3C change logs for relevant updates to supporting material and techniques.
- If a newer draft exists, record it as a draft and do not treat it as a normative replacement unless the audit specifically requests draft readiness.

## Schema.org

**Description:** Current schema vocabulary and release information; use it to understand available types/properties, while Google documentation determines Google Search feature eligibility.

**Retrieval hint:** Open when reviewing JSON-LD vocabulary, type/property availability, schema version changes, or whether a proposed schema structure exists.


### Seeds
- https://schema.org/docs/releases.html
- https://schema.org/version/latest
- https://schema.org/docs/schemas.html

### Runtime requirements
- Detect the current stable release at runtime.
- Use Google Search documentation, not Schema.org alone, to determine whether a particular type/property is eligible or useful for a Google Search feature.

## Radix UI

**Description:** First-party accessibility and release guidance for Radix primitives used by the project.

**Retrieval hint:** Open only when Radix primitives are detected or a custom control wraps Radix behavior and the audit needs primitive-specific a11y/release details.


### Seeds
- https://www.radix-ui.com/primitives/docs/overview/accessibility
- https://www.radix-ui.com/primitives/docs/overview/releases

### Runtime requirements
- Only apply Radix-specific checks when Radix is actually used.
- Inspect relevant release notes for accessibility fixes affecting detected primitives.

## GEO / AEO / Industry Guidance

**Description:** Secondary industry guidance used for emerging AI-search optimization ideas that must be separated from officially documented Google behavior.

**Retrieval hint:** Open when exploring GEO/AEO opportunities, but compare every material claim against current first-party search guidance before treating it as normative.


### Seeds
- https://writer.com/blog/geo-aeo-optimization

### Runtime requirements
- Record publication/update date.
- Compare claims against current Google Search guidance.
- Classify unsupported tactics as `EMERGING_GEO` or `EXPERIMENTAL`.
- Never present marketing claims as guaranteed ranking, indexing, citation, or AI-visibility behavior.

## Source-node description contract

When a seed or discovered authoritative page becomes a persistent source-graph node, store a compact descriptor instead of copying the page:

- `description`: 1–3 sentences explaining what the source governs and why it matters to this skill;
- `retrieval_hint`: the question/event that should cause the agent to reopen the source;
- `scope`: rule families covered by the source;
- `authority`: normative/official/secondary/experimental classification;
- `version` / `updated_at` / `last_checked`: freshness metadata when available;
- `conclusions`: short verified conclusions only;
- `content_hash`: optional hash for detecting meaningful changes;
- `edges`: relationships to relevant child sources.

Example descriptor:

```json
{
  "id": "google.search.ai-features",
  "description": "Official Google Search documentation describing supported generative AI search features and the guidance that applies to eligible content.",
  "retrieval_hint": "Open when auditing AI-search visibility, generative-AI search behavior, or claims about Google AI features.",
  "scope": ["ai-search", "search-appearance", "content-guidance"],
  "authority": "official",
  "edges": ["google.search.updates"]
}
```

The descriptor is the memory-friendly explanation. It is never a substitute for reopening the live source when the rule is applicable to the current audit.

## Recursive source-graph protocol

For every seed/discovered page:

1. Normalize the URL.
2. Record it in the source ledger.
3. Inspect the page's relevant links.
4. Add new relevant authoritative destinations to the frontier.
5. Follow newer version/spec/changelog/security/deprecation/validation links first.
6. Continue until the relevant frontier is empty.
7. Record rejected links when they were inspected but intentionally excluded as irrelevant.
8. Report the number of visited nodes, followed relevant links, rejected links, and source families fully exhausted.

A fixed crawl depth is NOT a completion criterion.

## Source conflict protocol

When sources disagree:

1. Compare normative status.
2. Compare applicability to the detected version/surface.
3. Compare publication/update date.
4. Prefer the current authoritative source.
5. Record the losing claim and why it was rejected.

Never silently merge contradictory rules.
