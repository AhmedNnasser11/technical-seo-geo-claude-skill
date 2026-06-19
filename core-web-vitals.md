# Core Web Vitals

## Scope

This file covers performance targets and page experience guidance from the report.

## Rules

### 1) Target LCP, INP, and CLS thresholds from Google
- **Rule name:** Core Web Vitals thresholds
- **Description:** Aim for LCP under 2.5 seconds, INP under 200 milliseconds, and CLS under 0.1.
- **Source URL:** https://developers.google.com/search/docs/appearance/core-web-vitals
- **Source organization:** Google Search Central
- **Source type:** Official documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** These metrics represent loading, responsiveness, and visual stability.
- **Expected impact:** Better user experience and alignment with Google’s page experience expectations.
- **Implementation guidance:** Measure real-user performance and optimize the critical path.
- **Example:** Reserve image dimensions to reduce layout shift.
- **Exceptions:** Some interactive experiences may need design tradeoffs.
- **Potential drawbacks:** Extreme optimization can increase engineering cost.
- **Conflicting opinions:** None in the report.
- **Notes:** Treat these as the report’s accepted targets.

### 2) Optimize images, scripts, and layout stability
- **Rule name:** Performance hygiene
- **Description:** Compress images, preload critical assets, defer non-critical scripts, and stabilize layout.
- **Source URL:** https://web.dev/vitals
- **Source organization:** web.dev / Google
- **Source type:** Official performance guidance
- **Classification:** Industry Best Practice
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Good performance supports usability and the core web vital targets.
- **Expected impact:** Better page speed and smoother interaction.
- **Implementation guidance:** Reserve space for media and ads and reduce render-blocking work.
- **Example:** Preload the LCP image and set explicit image dimensions.
- **Exceptions:** None in the report.
- **Potential drawbacks:** Over-optimizing can complicate the stack.
- **Conflicting opinions:** None in the report.
- **Notes:** This is the practical implementation layer behind the thresholds.
