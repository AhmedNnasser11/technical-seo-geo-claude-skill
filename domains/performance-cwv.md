# D09 — Performance / Core Web Vitals

## Measurement discipline

Prefer field/user data when available. Label lab measurements clearly. Code inspection can identify causes and risks but cannot prove a field metric passed.

## Metrics

Audit current LCP, INP, and CLS definitions/thresholds from web.dev at runtime. Do not hard-code stale thresholds into the audit logic.

## Checks

- LCP resource discovery and loading;
- image dimensions/formats/loading;
- font loading and layout stability;
- client JavaScript and hydration cost;
- third-party scripts;
- render-blocking work;
- caching/revalidation;
- data-fetch waterfalls;
- route-specific differences.

## Evidence

For metric findings, keep the measurement environment, source, percentile, route, and timestamp. For causal code findings, identify the mechanism that can produce the observed cost.
