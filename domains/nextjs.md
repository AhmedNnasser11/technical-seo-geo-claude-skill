# D12 — Next.js

## Version detection

Read the installed Next.js version from the project before applying framework-specific rules. Prefer version-matched official docs and release/security guidance.

## Checks

- App Router/Pages Router detection;
- Metadata API and server-component boundaries;
- file-based robots/sitemap/OG conventions;
- rendering strategy and indexable content availability;
- client/server boundaries;
- caching/revalidation;
- route handlers/server actions;
- `proxy.ts` interactions with metadata files when applicable;
- dependency/version security advisories.

Next.js documentation currently shows metadata APIs and file-based metadata conventions for App Router, and its blog records active security releases that are version-sensitive.

Do not declare a framework upgrade mandatory unless current project impact and current official release/support information justify it.
