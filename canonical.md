# Canonical

## Scope

This file covers duplicate-content canonicalization from the report.

## Rules

### 1) Use a canonical URL for duplicate or parameterized pages
- **Rule name:** Canonical URL
- **Description:** Add `<link rel="canonical">` when the same content is reachable through multiple URLs.
- **Source URL:** https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Canonicals consolidate ranking signals and reduce duplicate-index confusion.
- **Expected impact:** Cleaner indexing and signal consolidation.
- **Implementation guidance:** Point the canonical to the preferred URL.
- **Example:** `<link rel="canonical" href="https://acme.com/products/widget-12345">`
- **Exceptions:** Unique pages can canonicalize to themselves or omit if clearly single-instance.
- **Potential drawbacks:** Wrong canonicals can suppress the intended page.
- **Conflicting opinions:** Some setups prefer redirects; the report treats canonicals as the flexible option.
- **Notes:** Use for filter variants, tracking parameters, and duplicate shells.

### 2) Do not block canonical targets if you expect them to rank
- **Rule name:** Canonical accessibility
- **Description:** The preferred URL must remain crawlable and indexable.
- **Source URL:** https://developers.google.com/search/docs/appearance/title-link
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** A blocked canonical target cannot reliably accumulate signals.
- **Expected impact:** Better consolidation reliability.
- **Implementation guidance:** Make sure the canonical URL is accessible.
- **Example:** Do not canonicalize to a URL that is disallowed in robots.txt.
- **Exceptions:** None in the report.
- **Potential drawbacks:** None beyond setup discipline.
- **Conflicting opinions:** None in the report.
- **Notes:** This rule follows the report’s crawl/index separation guidance.
