# Audit Checklist

## 1) Crawlability and indexability
- Check whether important pages are accessible via crawlable links.
- Check robots.txt for accidental blocking.
- Check canonical tags on duplicate or parameterized URLs.
- Check sitemap coverage for important URLs.

## 2) Semantic structure
- Check that each page has a single clear `<main>`.
- Check landmark usage for header, nav, main, aside, article, and footer.
- Check heading order and the presence of one top-level `<h1>`.

## 3) Accessibility
- Check labels for every form control.
- Check keyboard accessibility for every interactive element.
- Check focus order and visible focus styles.
- Check alt text for meaningful images.

## 4) Metadata
- Check unique page titles.
- Check unique meta descriptions where useful.
- Check Open Graph tags for shareable pages.
- Check that metadata matches page content.

## 5) Structured data
- Check JSON-LD is present where the page qualifies.
- Check required properties and visible-content alignment.
- Check product, offer, review, aggregate rating, breadcrumb, article, organization, and website markup where appropriate.
- Validate before and after deployment.

## 6) Internal linking
- Check that important pages are linked from at least one other page.
- Check that anchor text is descriptive and contextual.
- Check breadcrumb visibility and schema alignment.
- Check for orphan pages.

## 7) Performance
- Check Core Web Vitals logic: LCP, INP, CLS.
- Check image sizing, layout stability, and script blocking risks.
- Check whether the main content appears quickly enough for users and crawlers.

## 8) Ecommerce
- Check product pages for rich detail and current inventory status.
- Check category pages for unique metadata and strong internal links.
- Check faceted navigation for duplicate URL handling.

## 9) GEO / AEO / AI visibility
- Check answer-first structure.
- Check entity clarity.
- Check content chunking and descriptive headings.
- Check citations and trust signals.
- Check organization and author signals.
- Check whether the content is easy to extract as a direct answer.

## 10) Next.js-specific
- Check `generateMetadata` or route metadata.
- Check `sitemap.ts` and `robots.ts`.
- Check whether important content is rendered in HTML.
- Check whether rendering strategy matches SEO needs.

## 11) Severity mapping
- **Critical:** blocks indexing, accessibility, or rendering.
- **High:** strong impact on ranking, snippets, or AI visibility.
- **Medium:** structural or performance improvement.
- **Low:** polish.
- **Opportunity:** experimental GEO / AI-oriented ideas.

## 12) Report output
For every issue, record:
- Category
- Severity
- Why It Matters
- Impact
- Fix
- Example
- Classification
