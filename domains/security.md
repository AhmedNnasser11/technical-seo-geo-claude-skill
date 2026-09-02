# D13 — Security / Hardening

## Attack-surface driven

First identify actual surfaces:

- forms and untrusted input;
- API routes/route handlers;
- authentication/session boundaries;
- server-side fetches and URL inputs;
- HTML injection/dangerous HTML;
- redirects;
- security headers;
- secrets/environment exposure;
- dependencies and framework advisories.

## OWASP 2025 lens

Use OWASP Top 10:2025 and relevant cheat sheets. The current Top 10 includes Broken Access Control, Security Misconfiguration, Software Supply Chain Failures, Cryptographic Failures, Injection, Insecure Design, Authentication Failures, Software/Data Integrity, Security Logging/Alerting Failures, and Mishandling of Exceptional Conditions.

## Checks

Do not flag a generic control merely because it is common advice. Tie every finding to an actual attack surface and evidence. Runtime exploit-style verification requires explicit runtime consent and must stay within safe, non-destructive checks.
