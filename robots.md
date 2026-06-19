# Robots.txt

## Scope

This file covers crawl management and robots.txt handling from the report.

## Rules

### 1) Use robots.txt to block non-public or duplicate areas
- **Rule name:** Crawl management
- **Description:** Disallow crawling of non-public or duplicate sections while allowing public content to remain crawlable.
- **Source URL:** https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots
- **Source organization:** Next.js
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Robots rules save crawl budget and keep irrelevant URLs out of crawl paths.
- **Expected impact:** Better crawl efficiency.
- **Implementation guidance:** Block admin, cart, account, API, and similar non-public paths if they are not meant for indexing.
- **Example:** `Disallow: /cart/`
- **Exceptions:** Do not block assets needed for rendering.
- **Potential drawbacks:** Overblocking can hurt visibility.
- **Conflicting opinions:** None in the report.
- **Notes:** Use this for crawling, not for guaranteed deindexing.

### 2) Reference the sitemap from robots.txt
- **Rule name:** Sitemap reference
- **Description:** Include a Sitemap directive in robots.txt.
- **Source URL:** https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots
- **Source organization:** Next.js
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Low
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** It helps crawlers discover the sitemap location.
- **Expected impact:** Slightly easier discovery.
- **Implementation guidance:** Point the directive to the sitemap URL.
- **Example:** `Sitemap: https://example.com/sitemap.xml`
- **Exceptions:** None noted.
- **Potential drawbacks:** None material.
- **Conflicting opinions:** None in the report.
- **Notes:** Keep the URL current.

### 3) Prefer noindex for content you do not want indexed
- **Rule name:** Index control
- **Description:** When you need a URL excluded from search results, do not rely on robots.txt alone.
- **Source URL:** https://developers.google.com/search/docs/appearance/title-link
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Robots blocking does not always prevent indexing.
- **Expected impact:** Better index control.
- **Implementation guidance:** Use `noindex` where appropriate.
- **Example:** A private or thin page that should not appear in search.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Misapplied noindex can remove useful pages.
- **Conflicting opinions:** None in the report.
- **Notes:** The report explicitly warns about crawl versus index separation.
