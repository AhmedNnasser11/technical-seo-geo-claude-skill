# Ecommerce SEO

## Scope

This file covers product pages, category pages, faceted navigation, and inventory handling from the report.

## Rules

### 1) Give product pages unique titles, descriptions, and visible product detail
- **Rule name:** Product page completeness
- **Description:** Product pages should not be thin; they need unique metadata and meaningful visible content.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Thin product pages are weak for search and users.
- **Expected impact:** Better product-page relevance.
- **Implementation guidance:** Include detailed descriptions, pricing, and images.
- **Example:** A shoe page with brand, materials, sizes, price, and reviews.
- **Exceptions:** Discontinued products should reflect their status honestly.
- **Potential drawbacks:** More content maintenance.
- **Conflicting opinions:** None in the report.
- **Notes:** This is a foundational commerce rule.

### 2) Mark up products with Product, Offer, AggregateRating, and Review when applicable
- **Rule name:** Product rich results
- **Description:** Use product schema on eligible product pages and keep it aligned with visible page data.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Commerce rich results can improve visibility and click appeal.
- **Expected impact:** Better product presentation in search.
- **Implementation guidance:** Keep offers, price, currency, availability, and rating data current.
- **Example:** Product with `availability`, `price`, and `aggregateRating`.
- **Exceptions:** If a product is out of stock, mark that status accurately.
- **Potential drawbacks:** Stale data is harmful.
- **Conflicting opinions:** None in the report.
- **Notes:** The report treats Product schema as core.

### 3) Canonicalize filtered and faceted URLs
- **Rule name:** Facet canonicalization
- **Description:** Use canonicalization or exclusion logic to prevent duplicate category/filter combinations from fragmenting signals.
- **Source URL:** https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Facets can generate many near-duplicate URLs.
- **Expected impact:** Cleaner indexing and signal consolidation.
- **Implementation guidance:** Canonical filtered variants back to the main category or use noindex when appropriate.
- **Example:** `?color=red` canonicalizes to the base category page.
- **Exceptions:** Distinct landing pages intentionally built for indexing may be handled differently.
- **Potential drawbacks:** Wrong handling can hide useful pages.
- **Conflicting opinions:** The report resolves the tradeoff toward crawl clarity.
- **Notes:** This is a common ecommerce duplication issue.

### 4) Use inventory status honestly in schema and visible copy
- **Rule name:** Inventory accuracy
- **Description:** Availability should reflect actual stock status.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Stale stock data creates misleading search previews.
- **Expected impact:** Better trust and fewer mismatches.
- **Implementation guidance:** Update availability promptly in page content and structured data.
- **Example:** `OutOfStock` for a discontinued item.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Requires data synchronization.
- **Conflicting opinions:** None in the report.
- **Notes:** The report explicitly warns about inaccurate schema data.

### 5) Keep category pages unique and link-rich
- **Rule name:** Category page quality
- **Description:** Category pages should have unique titles/H1s and enough internal links to expose products and subcategories.
- **Source URL:** https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Industry Best Practice
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Moderate
- **Why it matters:** Category pages anchor ecommerce information architecture.
- **Expected impact:** Better crawling and browsing.
- **Implementation guidance:** Make categories descriptive and logically linked.
- **Example:** `Men's Running Shoes` as a category title and H1.
- **Exceptions:** Very small catalogs may have simpler structures.
- **Potential drawbacks:** Over-linking can clutter the page.
- **Conflicting opinions:** None in the report.
- **Notes:** The report encourages logical hierarchy and shallow navigation.
