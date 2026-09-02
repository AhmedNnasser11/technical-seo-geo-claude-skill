# D01 — Crawl & Indexability

## Applies when

All public/indexable web projects.

## Open

- Google Search Essentials / technical requirements.
- JavaScript SEO documentation.
- Project route graph, robots, rendering, redirects, metadata, and authentication boundaries.

## Checks

- Intended public pages are technically accessible to Google-style crawlers.
- Server/client rendering does not remove essential indexable content.
- Accidental auth walls, error statuses, or blocked assets do not prevent indexing.
- Noindex/nosnippet controls are intentional and consistent with the page's role.
- URL structure does not depend on unsupported fragments for distinct content.

## Pass evidence

Code/config evidence is sufficient for static claims; runtime HTTP/rendering evidence is required for actual response/status/rendered-output claims.

## Do not claim

Do not claim that a page is indexed merely because it satisfies technical requirements; indexing and serving are not guaranteed.
