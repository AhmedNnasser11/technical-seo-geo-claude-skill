# Verification Engine Contract

`FIXED` means the intended change exists. `VERIFIED` requires post-change evidence.

Verification chooses the narrowest applicable checks first, then broadens as required:

`static -> domain checks -> build/typecheck/lint/tests -> runtime (consent required) -> re-audit`

A failed check cannot silently become a pass. Transient failures are retried and recorded.
