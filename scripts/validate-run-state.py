#!/usr/bin/env python3
"""Validate temporary audit-run state against the package schemas.

Offline, standard library only. Checks the files found in a run directory:

  ledger.json        -> schemas/run-ledger.schema.json
  plan.json          -> schemas/audit-plan.schema.json
  evidence.jsonl     -> schemas/evidence.schema.json     (one JSON object per line)
  findings.jsonl     -> schemas/finding.schema.json
  verification.jsonl -> schemas/verification.schema.json
  provenance.jsonl   -> schemas/provenance.schema.json

Usage:
  validate-run-state.py RUN_DIR [--final] [--project-root PATH]

--final additionally enforces the completeness gate: every domain and source
frontier is terminal, the runtime gate is resolved with a consent record where
needed, every referenced evidence id exists, and findings are not left in progress
or FIXED without verification.

Exit code 0 = valid, 1 = invalid, 2 = usage error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "ledger.json": ("run-ledger", False),
    "plan.json": ("audit-plan", False),
    "evidence.jsonl": ("evidence", True),
    "findings.jsonl": ("finding", True),
    "verification.jsonl": ("verification", True),
    "provenance.jsonl": ("provenance", True),
}

TERMINAL_DOMAIN = {"PASS", "ISSUES_FOUND", "NOT_APPLICABLE", "BLOCKED_AFTER_RETRY", "USER_DECLINED"}
TERMINAL_FRONTIER = {"EXHAUSTED", "BLOCKED_AFTER_RETRY"}
TERMINAL_RUNTIME = {"COMPLETED", "USER_DECLINED", "BLOCKED_AFTER_RETRY"}

TYPES = {
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "string": lambda v: isinstance(v, str),
    "boolean": lambda v: isinstance(v, bool),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "null": lambda v: v is None,
}


def resolve_ref(root: dict, ref: str) -> dict:
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported $ref: {ref}")
    node = root
    for part in ref[2:].split("/"):
        node = node[part.replace("~1", "/").replace("~0", "~")]
    return node


def check(value, schema: dict, root: dict, path: str, errors: list[str]) -> None:
    """Validate "value" against the JSON Schema subset used by this package."""
    if "$ref" in schema:
        check(value, resolve_ref(root, schema["$ref"]), root, path, errors)
    if "type" in schema:
        wanted = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(TYPES[t](value) for t in wanted):
            errors.append(f"{path}: expected {'/'.join(wanted)}, got {type(value).__name__}")
            return
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected {schema['const']!r}, got {value!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in {schema['enum']}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: shorter than minLength {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: does not match pattern {schema['pattern']}")
    if TYPES["number"](value):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: above maximum {schema['maximum']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than minItems {schema['minItems']}")
        if "items" in schema:
            for i, item in enumerate(value):
                check(item, schema["items"], root, f"{path}[{i}]", errors)
    if isinstance(value, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required property '{key}'")
        for key, sub in props.items():
            if key in value:
                check(value[key], sub, root, f"{path}.{key}", errors)
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{path}: unexpected property '{key}'")
    for sub in schema.get("allOf", []):
        check(value, sub, root, path, errors)
    if "if" in schema:
        probe: list[str] = []
        check(value, schema["if"], root, path, probe)
        if not probe and "then" in schema:
            check(value, schema["then"], root, path, errors)
        elif probe and "else" in schema:
            check(value, schema["else"], root, path, errors)


def load_schema(name: str) -> dict:
    return json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text(encoding="utf-8"))


def load_records(path: Path, jsonl: bool, errors: list[str]) -> list:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{path.name}: cannot read: {exc}")
        return []
    if not jsonl:
        try:
            return [json.loads(text)]
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            return []
    records = []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}:{n}: invalid JSON: {exc}")
    return records


def inside_git_repo(path: Path) -> bool:
    return any((p / ".git").exists() for p in [path, *path.parents])


def final_gate(data: dict, errors: list[str]) -> None:
    ledger = (data.get("ledger.json") or [None])[0]
    evidence_ids = {e.get("id") for e in data.get("evidence.jsonl", []) if isinstance(e, dict)}
    if ledger is None:
        errors.append("final: ledger.json is required")
        return
    for d in ledger.get("domains", []):
        if d.get("status") not in TERMINAL_DOMAIN:
            errors.append(f"final: domain {d.get('id')} is not terminal ({d.get('status')})")
        if d.get("status") in {"PASS", "ISSUES_FOUND", "NOT_APPLICABLE"} and not d.get("evidence_ids"):
            errors.append(f"final: domain {d.get('id')} has status {d.get('status')} but no evidence_ids")
        if d.get("status") == "BLOCKED_AFTER_RETRY" and not d.get("recovery_ids"):
            errors.append(f"final: domain {d.get('id')} is BLOCKED_AFTER_RETRY without recovery_ids")
    manifest = json.loads((ROOT / "audit-manifest.json").read_text(encoding="utf-8"))
    present = {d.get("id") for d in ledger.get("domains", [])}
    for d in manifest.get("domains", []):
        if d.get("id") not in present:
            errors.append(f"final: manifest domain {d.get('id')} missing from ledger")
    for f in ledger.get("source_frontiers", []):
        if f.get("status") not in TERMINAL_FRONTIER:
            errors.append(f"final: source frontier {f.get('family_id')} is not terminal ({f.get('status')})")
    gate = ledger.get("runtime_gate", {})
    if gate.get("status") not in TERMINAL_RUNTIME:
        errors.append(f"final: runtime gate not resolved ({gate.get('status')})")
    if gate.get("status") in {"APPROVED", "COMPLETED", "USER_DECLINED"} and not gate.get("asked_once"):
        errors.append("final: runtime gate resolved but asked_once is false")
    if gate.get("status") in {"COMPLETED", "USER_DECLINED"} and not gate.get("consent_record"):
        errors.append("final: runtime gate resolved without consent_record")
    if not ledger.get("cleanup", {}).get("persistent_paths_protected"):
        errors.append("final: cleanup.persistent_paths_protected is empty")
    if data.get("evidence.jsonl") is not None:
        for d in ledger.get("domains", []):
            for eid in d.get("evidence_ids", []):
                if eid not in evidence_ids:
                    errors.append(f"final: domain {d.get('id')} references unknown evidence id {eid}")
        for f in data.get("findings.jsonl", []):
            for key in ("evidence_ids", "verification_evidence_ids"):
                for eid in f.get(key, []) or []:
                    if eid not in evidence_ids:
                        errors.append(f"final: finding {f.get('id')} references unknown evidence id {eid}")
    for f in data.get("findings.jsonl", []):
        fid = f.get("id")
        if f.get("verification_status") == "VERIFIED" and not f.get("verification_evidence_ids"):
            errors.append(f"final: finding {fid} is VERIFIED without verification_evidence_ids")
        if f.get("status") in {"INVESTIGATING", "FIXING"}:
            errors.append(f"final: finding {fid} is still in progress ({f.get('status')})")
        if f.get("status") == "FIXED" and f.get("verification_status") in {"UNVERIFIED", "FAILED"}:
            errors.append(f"final: finding {fid} is FIXED but not verified ({f.get('verification_status')})")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir")
    ap.add_argument("--final", action="store_true", help="also enforce the completeness gate")
    ap.add_argument("--project-root", help="audited project root; the run dir must be outside it")
    args = ap.parse_args()

    run_dir = Path(args.run_dir).resolve()
    if not run_dir.is_dir():
        print(f"error: not a directory: {run_dir}", file=sys.stderr)
        return 2

    errors: list[str] = []
    if args.project_root:
        proj = Path(args.project_root).resolve()
        if run_dir == proj or proj in run_dir.parents:
            errors.append("run directory is inside the project root; temporary state must live outside the repository")
    if inside_git_repo(run_dir):
        errors.append("run directory is inside a git repository; temporary state must live outside the repository")

    data: dict[str, list] = {}
    checked = []
    for fname, (schema_name, jsonl) in FILES.items():
        path = run_dir / fname
        if not path.is_file():
            continue
        schema = load_schema(schema_name)
        records = load_records(path, jsonl, errors)
        data[fname] = records
        checked.append(f"{fname} ({len(records)} record{'s' if len(records) != 1 else ''}, {schema_name})")
        for i, rec in enumerate(records):
            check(rec, schema, schema, f"{fname}[{i}]", errors)

    if not checked:
        errors.append("no run-state files found (expected ledger.json, plan.json, evidence.jsonl, ...)")
    if args.final:
        final_gate(data, errors)

    if errors:
        print("RUN STATE VALIDATION: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1
    print("RUN STATE VALIDATION: PASS" + (" (final gate)" if args.final else ""))
    for c in checked:
        print(f"  checked {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
