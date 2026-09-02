#!/usr/bin/env python3
"""Safely delete one temporary Technical SEO/GEO run directory.

The script intentionally accepts only a run directory under the caller's
configured temp namespace and refuses paths containing persistent project data.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil

PROTECTED_NAMES = {".git", ".claude", "context"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", help="Unique temporary run directory to remove")
    parser.add_argument("--temp-root", required=True, help="Dedicated temp namespace, e.g. /tmp/technical-seo-geo")
    args = parser.parse_args()

    root = Path(args.temp_root).resolve()
    run = Path(args.run_dir).resolve()
    if run == root or root not in run.parents:
        raise SystemExit("Refusing cleanup: run_dir must be a child of --temp-root")

    for parent in [run, *run.parents]:
        if parent.name in PROTECTED_NAMES:
            raise SystemExit(f"Refusing cleanup: protected path component detected: {parent}")
    if run.exists():
        for child in run.rglob("*"):
            if child.name in PROTECTED_NAMES:
                raise SystemExit(f"Refusing cleanup: protected path found inside run directory: {child}")

    if not run.exists():
        print("Cleanup: nothing to remove")
        return 0
    if not run.is_dir():
        raise SystemExit("Refusing cleanup: run_dir is not a directory")

    shutil.rmtree(run)
    print(f"Cleanup: removed {run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
