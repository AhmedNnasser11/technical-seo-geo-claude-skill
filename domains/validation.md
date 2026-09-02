# D14 — Validation

## Required separation

Record each validation gate independently:

- lint;
- typecheck;
- build;
- tests;
- static route/config checks;
- structured-data validation;
- source/reference consistency checks;
- runtime verification gate.

## Rules

- A failed gate does not end the run.
- A passing build does not prove SEO/security/accessibility/runtime correctness.
- `FIXED` requires implementation evidence.
- `VERIFIED` requires post-change verification evidence.
- Runtime is `COMPLETED` only after explicit `yes` and successful completion of applicable checks; otherwise it is `USER_DECLINED` or `BLOCKED_AFTER_RETRY`.
