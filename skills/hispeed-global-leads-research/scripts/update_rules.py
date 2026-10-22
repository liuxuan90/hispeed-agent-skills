#!/usr/bin/env python3
"""Update approved Markdown business rules from a reviewed GitHub branch.

Never downloads/executes remote scripts; bootstrap entry SKILL.md remains fixed.
Private repos: set HISPEED_SKILL_GITHUB_TOKEN in the local environment.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = frozenset({
    'references/company-context.md', 'references/targeting.md',
    'references/research.md', 'references/contacts.md',
    'references/scoring.md', 'references/outreach.md',
    'references/schema.md', 'references/quality-control.md',
    'references/workflow.md', 'references/evaluation.md',
})
MAX_BYTES = 130_000


def fetch_github(repo, ref, path, token):
    quoted = urllib.parse.quote(path, safe='/')
    query = urllib.parse.urlencode({'ref': ref})
    url = f'https://api.github.com/repos/{repo}/contents/{quoted}?{query}'
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'Hispeed-Lead-Skill-Updater/1.0',
        **({'Authorization': f'Bearer {token}'} if token else {}),
    })
    with urllib.request.urlopen(req, timeout=15) as res:
        raw = res.read(MAX_BYTES * 3)
    payload = json.loads(raw)
    if payload.get('encoding') != 'base64' or not isinstance(payload.get('content'), str):
        raise ValueError('GitHub contents API returned unexpected encoding or file type')
    result = base64.b64decode(payload['content'], validate=False)
    if len(result) > MAX_BYTES:
        raise ValueError(f'File too large: {path}')
    return result


def apply_manifest(root, manifest, fetch_rule, check_only=False):
    if not isinstance(manifest, dict) or not re.fullmatch(r'\d+\.\d+\.\d+', str(manifest.get('version', ''))):
        raise ValueError('Invalid rules manifest version')
    items = manifest.get('files')
    if not isinstance(items, dict) or not items or set(items) - ALLOWED:
        raise ValueError('Manifest includes unauthorized or missing file list')
    updates = {}
    for path, expected in items.items():
        if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected):
            raise ValueError(f'Invalid sha256 for {path}')
        current = root / path
        if current.is_file() and not current.is_symlink():
            cached = current.read_bytes()
            if hashlib.sha256(cached).hexdigest() == expected:
                continue  # Fast path: this approved rule is already current.
        data = fetch_rule(path)
        if len(data) > MAX_BYTES or not data or b'\x00' in data:
            raise ValueError(f'Invalid data for {path}')
        data.decode('utf-8', errors='strict')
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f'Checksum mismatch for {path}; no changes applied')
        updates[path] = data
    if check_only:
        return {'version': manifest['version'], 'verified': len(items), 'updated': False}
    # All content verified first; stage files before changing any live rule.
    staged = []
    try:
        for name, data in updates.items():
            destination = (root / name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            # Never resolve through an unexpected pre-existing symbolic link.
            if destination.is_symlink() or destination.parent.is_symlink():
                raise ValueError(f'Unsafe target path: {name}')
            with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False, prefix='.hispeed-update-') as f:
                f.write(data)
                staged.append((Path(f.name), destination))
        for tmp, dest in staged:
            os.replace(tmp, dest)
        state = {'rules_version': manifest['version'], 'verified_files': len(items)}
        (root / '.rules-version.json').write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')
    finally:
        for tmp, _ in staged:
            if tmp.exists():
                tmp.unlink()
    return {'version': manifest['version'], 'verified': len(items), 'updated': bool(updates)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--quiet', action='store_true')
    p.add_argument('--check-only', action='store_true')
    args = p.parse_args()
    conf = json.loads((ROOT / 'config/update.json').read_text(encoding='utf-8'))
    if not conf.get('enabled'):
        if not args.quiet:
            print('RULES_LOCAL: update source not configured; using bundled rules')
        return 0
    repo = conf.get('github_repo', '')
    ref = conf.get('ref', 'stable')
    prefix = conf.get('skill_path', '')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        print('RULES_UPDATE_FAILED: invalid GitHub owner/repo', file=sys.stderr)
        return 1
    if (not re.fullmatch(r'[A-Za-z0-9._/-]+', ref) or '..' in ref or
        prefix != 'skills/hispeed-global-leads-research'):
        print('RULES_UPDATE_FAILED: unsafe ref or path', file=sys.stderr)
        return 1
    token = os.environ.get('HISPEED_SKILL_GITHUB_TOKEN', '')
    get = lambda path: fetch_github(repo, ref, f'{prefix}/{path}', token)
    try:
        manifest = json.loads(get('rules-manifest.json').decode('utf-8'))
        result = apply_manifest(ROOT, manifest, get, args.check_only)
        if not args.quiet:
            print(f"RULES_OK: {result['version']} ({result['verified']} verified rules; "
                  f"{'checked' if args.check_only else ('synced' if result['updated'] else 'unchanged')})")
        return 0
    except (OSError, ValueError, KeyError, UnicodeError, urllib.error.URLError, json.JSONDecodeError) as exc:
        print(f'RULES_UPDATE_FAILED: {type(exc).__name__}: {exc}; using cached rules', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
