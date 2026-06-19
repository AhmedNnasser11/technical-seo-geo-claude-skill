# Structured Data

## Scope

This file covers schema.org and Google structured data guidance from the report.

## Rules

### 1) Use JSON-LD as the default structured data format
- **Rule name:** JSON-LD default
- **Description:** Prefer JSON-LD for structured data unless the site’s setup makes another format more practical.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** JSON-LD is the easiest format to implement and maintain at scale.
- **Expected impact:** Lower implementation error rate and cleaner markup.
- **Implementation guidance:** Place a JSON-LD script block on the page that contains the described content.
- **Example:** `<script type="application/ld+json">…</script>`
- **Exceptions:** The report says all supported formats are acceptable if valid and properly implemented.
- **Potential drawbacks:** Invalid JSON or incomplete fields can break eligibility.
- **Conflicting opinions:** The report notes that JSON-LD is preferred, although other formats are allowed.
- **Notes:** Use the easiest maintainable format.

### 2) Mark up only visible, page-relevant content
- **Rule name:** Visible-content constraint
- **Description:** Structured data must describe content that is actually visible on the page.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Critical
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Hidden or invented markup violates Google’s guidance.
- **Expected impact:** Safer eligibility for enhanced display.
- **Implementation guidance:** Do not add markup for blank pages or invisible content.
- **Example:** Mark up the displayed product price, not a hidden or hypothetical price.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Reduces temptation to over-mark up.
- **Conflicting opinions:** None in the report.
- **Notes:** This is a hard requirement.

### 3) Include all required properties and keep recommended properties accurate
- **Rule name:** Complete schema
- **Description:** Include all required properties, and add recommended properties only when they remain complete and correct.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Incomplete or inaccurate markup is less likely to qualify.
- **Expected impact:** Better eligibility for rich results.
- **Implementation guidance:** Prefer fewer complete properties over many shaky ones.
- **Example:** Product markup with name, image, and offers fully filled out.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Poor data hygiene can create invalid markup.
- **Conflicting opinions:** None in the report.
- **Notes:** Accuracy matters more than property count.

### 4) Validate structured data before and after deployment
- **Rule name:** Structured data validation
- **Description:** Test structured data during development and monitor after deployment.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Templating or serving issues can break markup after release.
- **Expected impact:** Fewer production regressions.
- **Implementation guidance:** Use the Rich Results Test and Search Console reports.
- **Example:** Re-run validation after template changes.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Ongoing maintenance.
- **Conflicting opinions:** None in the report.
- **Notes:** The report explicitly recommends checking after deployment.

### 5) Use Product schema on eligible ecommerce product pages
- **Rule name:** Product schema
- **Description:** Product pages should use `Product` schema with `offers`, and when available `aggregateRating` and `review`.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Product rich results can improve visibility and CTR.
- **Expected impact:** Better search presentation for commerce pages.
- **Implementation guidance:** Keep the schema synchronized with visible page data.
- **Example:** Product with price, currency, and availability.
- **Exceptions:** If a page is a category listing, use category/navigation markup instead.
- **Potential drawbacks:** Out-of-date offers or ratings can mislead.
- **Conflicting opinions:** None in the report.
- **Notes:** The report treats Product as a core schema type.

### 6) Use BreadcrumbList for site hierarchy
- **Rule name:** Breadcrumb schema
- **Description:** Add breadcrumb structured data when visible breadcrumbs exist.
- **Source URL:** https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Breadcrumbs clarify site structure and navigation context.
- **Expected impact:** Better user navigation and clearer hierarchy.
- **Implementation guidance:** Keep visible breadcrumbs and schema aligned.
- **Example:** Home > Category > Product
- **Exceptions:** Pages without hierarchical navigation may not need it.
- **Potential drawbacks:** Mismatched breadcrumbs create confusion.
- **Conflicting opinions:** None in the report.
- **Notes:** This overlaps with internal linking but is still a structured data rule.

### 7) Use FAQ content for users, but do not depend on FAQ rich results
- **Rule name:** FAQ content utility
- **Description:** FAQ-style content can still help users and AI extract answers, but the report notes FAQ rich results are no longer supported in Google Search.
- **Source URL:** https://developers.google.com/search/updates#removing-faq-rich-result
- **Source organization:** Google Search Central
- **Source type:** Official documentation update
- **Classification:** Experimental
- **Severity:** Opportunity
- **Confidence level:** Medium
- **Evidence strength:** Moderate
- **Why it matters:** FAQ content may still help answer extraction even without special search display.
- **Expected impact:** Possible AI usefulness, but not guaranteed Search benefit.
- **Implementation guidance:** Keep FAQ sections only when they serve actual user needs.
- **Example:** A product page FAQ about shipping, sizing, and returns.
- **Exceptions:** Do not add empty or forced FAQ sections.
- **Potential drawbacks:** Page bloat if overused.
- **Conflicting opinions:** The report explicitly notes the Search feature is deprecated while content utility remains.
- **Notes:** Do not treat FAQ markup as a current Google rich-result strategy.
