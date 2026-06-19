# Internal Linking

## Scope

This file covers crawlable links, anchor text, orphan-page avoidance, and breadcrumbs from the report.

## Rules

### 1) Use crawlable `<a href>` links for navigation and context
- **Rule name:** Crawlable internal links
- **Description:** Important navigation and contextual references should be standard links that crawlers can follow.
- **Source URL:** https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Crawlable links help discovery and site understanding.
- **Expected impact:** Better crawling and navigation.
- **Implementation guidance:** Use real anchor elements, not script-only or inaccessible substitutes.
- **Example:** `<a href="/category/shoes">Running shoes</a>`
- **Exceptions:** None in the report.
- **Potential drawbacks:** Overly complex navigation can still be hard to parse.
- **Conflicting opinions:** None in the report.
- **Notes:** Use crawlable links consistently across the site.

### 2) Make anchor text descriptive and context relevant
- **Rule name:** Descriptive anchor text
- **Description:** Anchor text should describe the target page and its purpose.
- **Source URL:** https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Descriptive anchors help users and Google understand link destinations.
- **Expected impact:** Better relevance and usability.
- **Implementation guidance:** Avoid “click here” when the target topic can be stated directly.
- **Example:** `<a href="/blog/seo-tips">Top SEO Tips for 2026</a>`
- **Exceptions:** Generic labels like Home may be acceptable when tied to the logo or obvious navigation context.
- **Potential drawbacks:** Exact-match stuffing can look spammy.
- **Conflicting opinions:** The report prefers clarity over aggressive variation strategies.
- **Notes:** Surrounding text also matters.

### 3) Every important page should have at least one internal link
- **Rule name:** No orphan pages
- **Description:** Pages that matter should be linked from at least one other page on the site.
- **Source URL:** https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Orphan pages are harder to discover and understand.
- **Expected impact:** Better indexing coverage.
- **Implementation guidance:** Audit content and category pages for missing inbound internal links.
- **Example:** A new blog post linked from a category hub.
- **Exceptions:** Utility pages may not need heavy internal prominence.
- **Potential drawbacks:** Requires architecture discipline.
- **Conflicting opinions:** None in the report.
- **Notes:** The report frames this as a key crawlability rule.

### 4) Use breadcrumbs to clarify site hierarchy
- **Rule name:** Breadcrumb navigation
- **Description:** Visible breadcrumbs and BreadcrumbList schema improve both navigation and hierarchy clarity.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Industry Best Practice
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Breadcrumbs help users and crawlers understand where a page sits in the site.
- **Expected impact:** Better navigation and structural context.
- **Implementation guidance:** Keep the visible trail and structured data aligned.
- **Example:** Home > Category > Product
- **Exceptions:** Flat sites may not need deep breadcrumb trails.
- **Potential drawbacks:** Misalignment between UI and schema is confusing.
- **Conflicting opinions:** None in the report.
- **Notes:** This overlaps with structured data and internal architecture.
