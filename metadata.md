# Metadata

## Scope

This file covers titles, meta descriptions, and metadata correctness from the report.

## Rules

### 1) Give every page a unique, descriptive title
- **Rule name:** Unique page title
- **Description:** Every page must have a `<title>` element that is concise, descriptive, and distinct from other pages.
- **Source URL:** https://developers.google.com/search/docs/appearance/title-link
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Titles strongly affect search result understanding and click behavior.
- **Expected impact:** Better snippet quality and CTR.
- **Implementation guidance:** Put the page topic first and avoid boilerplate.
- **Example:** `<title>Men's Running Shoes – AcmeSports</title>`
- **Exceptions:** None for indexable pages.
- **Potential drawbacks:** Maintenance overhead at scale.
- **Conflicting opinions:** The report rejects keyword stuffing and boilerplate titles even when multiple keywords are desired.
- **Notes:** Google may truncate long titles.

### 2) Avoid keyword stuffing and repeated boilerplate in titles
- **Rule name:** Clean title text
- **Description:** Do not repeat keywords or use generic boilerplate that makes pages indistinguishable.
- **Source URL:** https://developers.google.com/search/docs/appearance/title-link
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Overly repetitive titles look spammy and reduce usefulness.
- **Expected impact:** More readable, trustable titles.
- **Implementation guidance:** Write one title for one page purpose.
- **Example:** Avoid `Cheap products for sale` on every commerce page.
- **Exceptions:** None in the report.
- **Potential drawbacks:** None beyond fixing existing templates.
- **Conflicting opinions:** Some industry advice pushes longer titles, but the report follows Google’s caution.
- **Notes:** The report treats this as a hard no.

### 3) Give every page a unique meta description
- **Rule name:** Unique meta description
- **Description:** Use a distinctive `<meta name="description">` for each page where it helps search snippets.
- **Source URL:** https://developers.google.com/search/docs/appearance/snippet
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Descriptions can appear in snippets and improve click understanding.
- **Expected impact:** Better CTR and more relevant search previews.
- **Implementation guidance:** Summarize the page honestly and concisely.
- **Example:** `Acme Sports' men's running shoes: lightweight, breathable, sizes 7–13.`
- **Exceptions:** Google may generate its own snippet.
- **Potential drawbacks:** Bad descriptions can be ignored.
- **Conflicting opinions:** The report notes some SEOs de-emphasize meta descriptions, but Google still recommends quality descriptions.
- **Notes:** Long keyword strings are less likely to be shown.

### 4) Keep meta descriptions clear and non-spammy
- **Rule name:** Clean meta description text
- **Description:** Avoid long strings of keywords or vague one-word descriptions.
- **Source URL:** https://developers.google.com/search/docs/appearance/snippet
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Clear descriptions are more likely to be useful to users.
- **Expected impact:** Better snippet quality.
- **Implementation guidance:** Write for humans first.
- **Example:** A concise summary of the page’s value proposition.
- **Exceptions:** None noted.
- **Potential drawbacks:** Minimal.
- **Conflicting opinions:** None in the report.
- **Notes:** The report treats very short descriptions as bad.

### 5) Do not rely on robots.txt to remove content from search results
- **Rule name:** Metadata robots caution
- **Description:** Blocking crawling is not the same as preventing indexing; use `noindex` when you need a URL removed from search.
- **Source URL:** https://developers.google.com/search/docs/appearance/title-link
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** A blocked URL can still be indexed from external signals.
- **Expected impact:** Better index control and fewer surprises.
- **Implementation guidance:** Do not use `robots.txt` as the only exclusion mechanism for index removal.
- **Example:** Use `noindex` instead of depending only on disallow.
- **Exceptions:** The report does not specify exceptions.
- **Potential drawbacks:** Misunderstanding crawl vs index can leave URLs visible.
- **Conflicting opinions:** None in the report.
- **Notes:** This is an indexing-control rule, not a crawling rule.
