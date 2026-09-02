#!/usr/bin/env python3
"""Offline integrity checks for the skill package."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        ERRORS.append(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")
        return None


def require(path: str) -> None:
    if not (ROOT / path).is_file():
        ERRORS.append(f"Missing required file: {path}")


def check_no_forbidden() -> None:
    forbidden = {"run-ledger-template.md"}
    for p in ROOT.rglob("*"):
        if p.is_file() and p.name in forbidden:
            ERRORS.append(f"Forbidden runtime artifact present: {p.relative_to(ROOT)}")
        if p.name.startswith(".git"):
            ERRORS.append(f"Git artifact present: {p.relative_to(ROOT)}")


def check_internal_refs() -> None:
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for ref in re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", text):
            if ref.startswith(("http://", "https://", "mailto:")):
                continue
            target = (md.parent / ref).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not target.exists():
                ERRORS.append(f"Broken Markdown reference in {md.relative_to(ROOT)}: {ref}")


def check_registry() -> None:
    data = load_json(ROOT / "source-registry.json")
    if not data:
        return
    ids: set[str] = set()
    for family in data.get("families", []):
        for seed in family.get("seeds", []):
            sid = seed.get("id")
            if sid in ids:
                ERRORS.append(f"Duplicate source seed id: {sid}")
            if sid:
                ids.add(sid)
            if not str(seed.get("url", "")).startswith("https://"):
                ERRORS.append(f"Source seed is not HTTPS: {sid}")


def check_manifest() -> None:
    data = load_json(ROOT / "audit-manifest.json")
    if not data:
        return
    seen: set[str] = set()
    for d in data.get("domains", []):
        did = d.get("id")
        if did in seen:
            ERRORS.append(f"Duplicate domain id: {did}")
        if did:
            seen.add(did)
        module = d.get("module")
        if not module or not (ROOT / module).is_file():
            ERRORS.append(f"Domain module missing for {did}: {module}")
        for key in ("applies_when", "pass", "issue", "revalidate"):
            if key not in d:
                ERRORS.append(f"Domain {did} missing manifest field: {key}")


def check_schema_json() -> None:
    for path in (ROOT / "schemas").glob("*.schema.json"):
        load_json(path)


def main() -> int:
    required = [
        "SKILL.md", "README.md", "KNOWLEDGE-INDEX.md", "PROJECT-KNOWLEDGE-ARCHITECTURE.md",
        "PROJECT-LOCAL-STEPS.md", "CHANGELOG.md", "MIGRATION.md", "audit-manifest.json", "source-registry.json"
    ]
    for path in required:
        require(path)
    check_no_forbidden()
    check_schema_json()
    check_manifest()
    check_registry()
    check_internal_refs()
    if ERRORS:
        print("PACKAGE VALIDATION: FAIL")
        for err in ERRORS:
            print(f"- {err}")
        return 1
    print("PACKAGE VALIDATION: PASS")
    print(f"Root: {ROOT}")
    print(f"Markdown files: {len(list(ROOT.rglob('*.md')))}")
    print(f"Schemas: {len(list((ROOT / 'schemas').glob('*.json')))}")
    print(f"Domain modules: {len(list((ROOT / 'domains').glob('*.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
