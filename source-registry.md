# Live Source Registry

This registry is intentionally a set of **seed URLs**, not a frozen source of truth.

At every skill run, verify these sources and follow relevant first-party sub-links recursively.

## Google Search / SEO / AI Search

- https://developers.google.com/search/docs
- https://developers.google.com/search/updates
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/appearance/structured-data/intro
- https://developers.google.com/search/docs/crawling-indexing/overview
- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview

Runtime rule: inspect the Search Central updates/changelog and follow relevant documentation links from the current AI-search guidance before applying GEO/AEO rules.

## Next.js

- https://nextjs.org/docs
- https://nextjs.org/docs/app/api-reference/functions/generate-metadata
- https://nextjs.org/docs/app/getting-started/metadata-and-og-images
- https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap
- https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots
- https://nextjs.org/docs/app/api-reference/next-config-js/headers
- https://nextjs.org/docs/app/building-your-application/optimizing

Runtime rule: detect the project's installed Next.js version and inspect the current documentation plus relevant release notes/changelog. Prefer version-matched official documentation.

## Web Performance

- https://web.dev/performance
- https://web.dev/vitals/
- https://web.dev/articles/lcp
- https://web.dev/articles/inp
- https://web.dev/articles/cls

Runtime rule: verify the current Core Web Vitals definitions and thresholds from current web.dev documentation instead of assuming a value from this repository.

## Security

- https://cheatsheetseries.owasp.org/IndexTopTen.html
- https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html

Runtime rule: inspect current OWASP guidance relevant to the detected application surface. Do not introduce a security requirement merely because a checklist mentions it; establish applicability and evidence.

## Accessibility

- https://www.w3.org/WAI/fundamentals/
- https://www.w3.org/WAI/standards-guidelines/
- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://www.w3.org/WAI/standards-guidelines/aria/
- https://www.w3.org/TR/wai-aria/
- https://www.w3.org/WAI/WCAG22/quickref/

Runtime rule: inspect current WCAG/WAI-ARIA status and relevant W3C changelogs. Prefer finalized standards over drafts unless the audit explicitly asks for future/draft compatibility.

## Radix UI

- https://www.radix-ui.com/primitives/docs/overview/accessibility
- https://www.radix-ui.com/primitives/docs/overview/releases

Runtime rule: if Radix is detected, inspect its current accessibility guidance and releases for relevant fixes.

## GEO / AEO industry guidance

- https://writer.com/blog/geo-aeo-optimization

Runtime rule: use industry GEO guidance only as secondary evidence. Verify publication/update date and compare its claims against current Google guidance. Never treat marketing claims or experimental GEO tactics as guaranteed ranking factors.

## Recursive sub-link rule

For every seed or discovered authoritative page:

1. Record the page.
2. Extract links.
3. Keep links that are relevant to the audit topic or implementation rule.
4. Open those links.
5. Repeat until no new relevant authoritative source remains.
6. If a discovered link points to a newer version, migration guide, changelog, specification, API reference, or official validation guidance, it takes precedence over the older page.
7. Maintain a visited URL ledger to prevent loops.
8. Report source coverage in the final audit.

Do not interpret "recursive" as "crawl every hyperlink on the internet". It means recursively exhaust the **relevant authoritative source graph**.
