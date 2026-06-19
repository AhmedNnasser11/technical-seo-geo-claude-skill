# Next.js SEO

## Scope

This file covers the report-backed Next.js guidance: metadata, sitemaps, robots, and rendering strategy.

## Rules

### 1) Use `generateMetadata` or route metadata objects per page
- **Rule name:** Next.js metadata API
- **Description:** Use the Next.js Metadata API to set titles, descriptions, Open Graph data, and canonical hints per route.
- **Source URL:** https://nextjs.org/docs/app/building-your-application/optimizing/metadata
- **Source organization:** Next.js
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** It makes route-level metadata manageable and consistent.
- **Expected impact:** Better SEO and social metadata coverage.
- **Implementation guidance:** Define metadata at the page or layout level according to route needs.
- **Example:** `generateMetadata({ params })` returning title and description.
- **Exceptions:** Older Next.js versions use older metadata patterns.
- **Potential drawbacks:** Mis-scoped metadata can duplicate site-wide titles.
- **Conflicting opinions:** None in the report.
- **Notes:** The report treats this as the canonical Next.js SEO path.

### 2) Use `sitemap.ts` and `robots.ts` in the App Router
- **Rule name:** Next.js metadata files
- **Description:** Generate sitemap and robots files using the Next.js file conventions.
- **Source URL:** https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap
- **Source organization:** Next.js
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** These conventions reduce custom plumbing and keep metadata near the app.
- **Expected impact:** Easier SEO maintenance.
- **Implementation guidance:** Place these in the app root using the documented conventions.
- **Example:** `app/sitemap.ts` and `app/robots.ts`
- **Exceptions:** Smaller apps may use static root files when simpler.
- **Potential drawbacks:** Requires consistent route generation.
- **Conflicting opinions:** None in the report.
- **Notes:** The report explicitly calls out both conventions.

### 3) Prefer static generation or ISR when possible
- **Rule name:** SEO-safe rendering
- **Description:** Static generation and ISR are preferred when they fit the content model.
- **Source URL:** https://developers.google.com/search/docs/appearance/title-link
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** Medium
- **Evidence strength:** Moderate
- **Why it matters:** Pre-rendered content is safer for indexing than client-only rendering.
- **Expected impact:** More reliable discovery and faster first meaningful content.
- **Implementation guidance:** Use SSR/SSG/ISR patterns that expose the important content in the HTML response.
- **Example:** Static product pages with ISR for price updates.
- **Exceptions:** Highly dynamic interactions may need client rendering after the main content is available.
- **Potential drawbacks:** More caching and revalidation logic.
- **Conflicting opinions:** The report notes dynamic rendering as a fallback when needed.
- **Notes:** The report does not establish a separate PPR rule.

### 4) Balance dynamic rendering with SEO visibility
- **Rule name:** Rendering tradeoff
- **Description:** If client-side rendering would hide important content from crawlers, prefer a server-rendered approach.
- **Source URL:** https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Search engines and AI systems need access to the meaningful content.
- **Expected impact:** Safer indexation and extractability.
- **Implementation guidance:** Ensure essential content exists in rendered HTML.
- **Example:** Server-rendered product details instead of late-only client fetches.
- **Exceptions:** Rich interactions can hydrate after content is visible.
- **Potential drawbacks:** More server work.
- **Conflicting opinions:** None in the report.
- **Notes:** The report frames SSR/SSG as the safer default.

### 5) Use Next.js `<Image>` and `<Link>` in SEO-sensitive routes
- **Rule name:** Next.js internal primitives
- **Description:** Use the framework’s native image and linking primitives for SEO-sensitive navigation and LCP handling.
- **Source URL:** https://nextjs.org/docs
- **Source organization:** Next.js
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Moderate
- **Why it matters:** These primitives support optimized navigation and image loading patterns.
- **Expected impact:** Better performance and safer link handling.
- **Implementation guidance:** Use `<Link>` for internal navigation and correctly sized images for key visuals.
- **Example:** A product hero image with explicit dimensions.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Incorrect usage can still degrade performance.
- **Conflicting opinions:** None in the report.
- **Notes:** This file follows the report’s Next.js SEO section.
