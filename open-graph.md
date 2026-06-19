# Open Graph

## Scope

This file covers the report-backed social metadata rules.

## Rules

### 1) Add Open Graph metadata to shareable pages
- **Rule name:** Open Graph tags
- **Description:** Include `og:title`, `og:description`, `og:image`, `og:url`, and `og:type` on pages that may be shared.
- **Source URL:** https://ogp.me/
- **Source organization:** Open Graph protocol
- **Source type:** Official protocol specification
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Social metadata controls how links appear when shared.
- **Expected impact:** Better social previews and click appeal.
- **Implementation guidance:** Mirror the page’s real content and purpose.
- **Example:** `<meta property="og:title" content="The Rock">`
- **Exceptions:** Non-shareable pages may not need full OG coverage.
- **Potential drawbacks:** Incorrect OG data creates misleading previews.
- **Conflicting opinions:** None in the report.
- **Notes:** The report stresses accuracy and alignment with page content.

### 2) Use a clear image description for og:image
- **Rule name:** Open Graph image alt text
- **Description:** If `og:image` is present, include `og:image:alt`.
- **Source URL:** https://ogp.me/
- **Source organization:** Open Graph protocol
- **Source type:** Official protocol specification
- **Classification:** Official Standard
- **Severity:** Low
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** It improves accessibility and descriptive clarity for social previews.
- **Expected impact:** More understandable social cards.
- **Implementation guidance:** Describe the image rather than caption it.
- **Example:** `og:image:alt="Red running shoe on white background"`
- **Exceptions:** None noted in the report.
- **Potential drawbacks:** Minimal.
- **Conflicting opinions:** None in the report.
- **Notes:** The report also recommends 1.91:1 images at 1200×630 for clarity.
