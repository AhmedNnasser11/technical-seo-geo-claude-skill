# Sitemap

## Scope

This file covers sitemap strategy and Next.js sitemap generation from the report.

## Rules

### 1) Provide a sitemap for important indexable URLs
- **Rule name:** XML sitemap
- **Description:** List important URLs in a sitemap so crawlers can discover them efficiently.
- **Source URL:** https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap
- **Source organization:** Next.js
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Sitemaps help search engines discover deep or new pages.
- **Expected impact:** Better crawl discovery and index coverage.
- **Implementation guidance:** Include key URLs and keep it current.
- **Example:** A root `sitemap.xml` with product, category, and content URLs.
- **Exceptions:** Very small sites may not depend on it as much, but the report still recommends it.
- **Potential drawbacks:** Maintenance overhead.
- **Conflicting opinions:** None in the report.
- **Notes:** Dynamic generation is acceptable.

### 2) Use sitemap.ts or sitemap.js in Next.js when applicable
- **Rule name:** Next.js sitemap generation
- **Description:** Next.js can generate sitemaps programmatically with `sitemap.(js|ts)`.
- **Source URL:** https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap
- **Source organization:** Next.js
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Programmatic generation reduces drift on dynamic sites.
- **Expected impact:** More reliable sitemap maintenance.
- **Implementation guidance:** Return an array of URLs from the sitemap file convention.
- **Example:** A TypeScript sitemap file returning route entries.
- **Exceptions:** Smaller applications may use a static file in the app root.
- **Potential drawbacks:** Requires integration with routing data.
- **Conflicting opinions:** None in the report.
- **Notes:** The report notes this Next.js convention explicitly.

### 3) Keep sitemap entries aligned with canonical, indexable URLs
- **Rule name:** Canonical sitemap alignment
- **Description:** Include only URLs intended for indexing and ranking.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Moderate
- **Why it matters:** Mixing duplicate or blocked URLs into a sitemap weakens crawl efficiency.
- **Expected impact:** Cleaner discovery.
- **Implementation guidance:** Keep filtered, duplicate, or utility URLs out of the sitemap unless they are intentionally indexable.
- **Example:** Include the main product URL, not tracking variants.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Requires careful URL governance.
- **Conflicting opinions:** None in the report.
- **Notes:** This follows the report’s broader indexability rules.
