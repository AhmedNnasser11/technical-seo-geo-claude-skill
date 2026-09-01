# Audit Run Ledger Template

Use one copy per run. This file is execution state, not the final report.

## Run metadata

- Started:
- Target:
- Target type: website / URL / codebase / both
- Detected framework:
- Detected version(s):
- Package manager:
- Audit mode: audit-only / audit-and-fix

## Source families

| Family | Seed | Status | Visited | Relevant followed | Rejected | Frontier empty | Selected rule/version | Recovery |
|---|---|---|---:|---:|---:|---|---|---|
| Google Search | | pending | 0 | 0 | 0 | no | | |
| Next.js | | pending | 0 | 0 | 0 | no | | |
| Web Performance | | pending | 0 | 0 | 0 | no | | |
| Security | | pending | 0 | 0 | 0 | no | | |
| Accessibility | | pending | 0 | 0 | 0 | no | | |
| Schema.org | | pending | 0 | 0 | 0 | no | | |
| Radix UI | | N/A until detected | 0 | 0 | N/A | N/A | | |
| GEO/AEO industry | | pending | 0 | 0 | 0 | no | | |

## Audit domains

| ID | Domain | Required? | Status | Evidence refs | Finding IDs | Recovery |
|---|---|---:|---|---|---|---|
| D1 | Live source refresh | yes | pending | | | |
| D2 | Crawl/indexability | yes | pending | | | |
| D3 | Semantic HTML | yes | pending | | | |
| D4 | Accessibility | yes | pending | | | |
| D5 | Metadata/social | yes | pending | | | |
| D6 | Structured data | yes | pending | | | |
| D7 | Sitemap/robots/canonical | yes | pending | | | |
| D8 | Internal links | yes | pending | | | |
| D9 | Performance/CWV | yes | pending | | | |
| D10 | Ecommerce | conditional | pending | | | |
| D11 | GEO/AEO/AI search | yes | pending | | | |
| D12 | Next.js | conditional | pending | | | |
| D13 | Security/hardening | conditional | pending | | | |
| D14 | Validation gates | yes | pending | | | |

## Validation results

| Check | Available? | Command/tool | Result | Evidence | Recovery |
|---|---:|---|---|---|---|
| lint | | | | | |
| typecheck | | | | | |
| build | | | | | |
| tests | | | | | |
| link crawl | | | | | |
| browser/render | | | | | |
| structured-data validation | | | | | |
| accessibility automation | | | | | |
| HTTP/header checks | | | | | |
| dependency/security audit | | | | | |

## Findings

Each finding must have evidence and a source.

| ID | Domain | Severity | Classification | Confidence | Status | Evidence | Source | Fix | Post-fix evidence |
|---|---|---|---|---|---|---|---|---|---|

## Recovery log

| Time | Operation | Failure | Attempt 1 | Attempt 2 / alternative | Final disposition |
|---|---|---|---|---|---|

## Finalization invariant

The run may be finalized only when:

- every required domain is terminal;
- every conditional domain is audited or explicitly `NOT_APPLICABLE` with evidence;
- every applicable source family has an empty relevant frontier;
- every finding has evidence and source support;
- every requested fix has post-fix verification or is explicitly blocked after recovery;
- no `pending`, `in_progress`, `TODO`, `SKIP`, or `unknown` state remains;
- the final report is generated from this ledger.
