#!/usr/bin/env python3
"""Build the stable release manifest for Hispeed Lead Intelligence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "hispeed-lead-intelligence"
MANIFEST = SKILL_ROOT / "release-manifest.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
match = re.search(r"(?m)^\s*version:\s*([0-9]+\.[0-9]+\.[0-9]+)\s*$", text)
if not match:
    raise SystemExit("SKILL.md has no semantic metadata.version")

files = {}
for path in sorted(SKILL_ROOT.rglob("*")):
    if not path.is_file() or path == MANIFEST or "__pycache__" in path.parts:
        continue
    files[path.relative_to(SKILL_ROOT).as_posix()] = sha256(path)

payload = {
    "skill": "hispeed-lead-intelligence",
    "version": match.group(1),
    "source_repo": "liuxuan90/hispeed-agent-skills",
    "source_ref": "stable",
    "source_path": "skills/hispeed-lead-intelligence",
    "change_types": ["rules", "output-format"],
    "review_before_update": False,
    "release_notes": [
        "Default user-facing workbook and table presentation to Simplified Chinese.",
        "Keep canonical JSON keys, scoring model v1, schema v2 meaning, evidence text, identities, URLs, and English email drafts unchanged."
    ],
    "files": files,
}
MANIFEST.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"WROTE {MANIFEST} ({len(files)} files, version {payload['version']})")
