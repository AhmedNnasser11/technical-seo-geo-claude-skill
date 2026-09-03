# Agent Architecture

## Recommended topology

Use a **single orchestrator LLM over a deterministic execution pipeline**.

The orchestrator plans and interprets. Deterministic components perform repeatable operations such as repository inspection, measurements, source normalization, URL normalization, version comparisons, deduplication, schema validation, policy enforcement, and verification bookkeeping.

This is deliberately not a planner-plus-specialist swarm. Specialist logic belongs in deterministic domain engines and evaluators unless a future benchmark demonstrates a material quality gain from additional agents.

## Control flow

```text
User
 -> Orchestrator
 -> Policy/Trust Gate
 -> Structured Tool Call
 -> Deterministic Tool
 -> Structured Result
 -> Orchestrator
 -> Evidence Gate
 -> Domain/Finding Engine
 -> Remediation Gate
 -> Verification
 -> Re-audit
 -> Persistent Knowledge
```
