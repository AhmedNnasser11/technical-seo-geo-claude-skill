# D07 — Sitemap & Robots

## Checks

### robots

- rules do not block intended indexable content;
- disallowed private/utility paths are intentional;
- sitemap reference is present where appropriate;
- distinguish crawl control from indexing removal.

### sitemap

- include intended canonical/indexable URLs;
- use absolute URLs;
- keep entries current and valid;
- shard when limits require it;
- keep localized/variant strategy coherent.

Google's current sitemap guidance states a single sitemap is limited to 50,000 URLs or 50 MB uncompressed, and recommends absolute URLs.

Next.js supports file-based `robots.txt` and `sitemap.xml` conventions in the App Router.
