# Hispeed Skill Release & Maintenance SOP

## Roles
- Marketing owner: approves targeting, contact and outreach changes.
- Maintainer: reviews changes, updates rule files and manifest, tests on five representative sample companies.
- Runtime operator: confirms the local agent reloads the updated rules; never supplies secrets in chat.

## Initial publication
1. Create private `liuxuan90/hispeed-agent-skills` repository. Upload this repository root (not just ZIP as a single file).
2. Confirm the default `main` branch includes `SKILL.md`, updater, manifest and CSV headers.
3. Create branch `stable` from the approved release commit. This is the rule update source configured in `config/update.json`.
4. Install and authorize this skill **only** in the runtime that has read-only access to the repo.
5. Smoke-test manual update and observe the `rules_version` in one research run.

## Publishing improved rules
1. Edit **only** the relevant `references/*.md` files on a feature branch; PR to `main`.
2. Validate English/Chinese marketing copy, source discipline, current channel exclusions, data schema, and legal compliance.
3. Run `python -m unittest discover -s skills/hispeed-global-leads-research/tests -v`.
4. Recalculate SHA-256 for every listed file and update `rules-manifest.json`, increasing `version` (e.g. 1.0.0 → 1.1.0). **Do not omit this step**, because the updater checks SHA-256.
5. Compare before/after on a five-company evaluation batch using `references/evaluation.md`; record change in CHANGELOG.
6. Merge approved PR into `main` and promote its vetted commit to `stable` (prefer protected branches and required reviews).
7. Start the installed skill in a script-capable runtime, confirm it reports the new `rules_version`, and check report quality.

## What updates automatically
- `references/*.md` only. The checked-in updater restricts the allowlist, verifies hashes, and keeps the last usable local files on errors.
- `SKILL.md`, `scripts/*.py`, schema CSVs, and package metadata **do not auto-replace**; changes to these need a reviewed installer/redeployment or platform-supported skill update.

## Rollback
- Restore a prior known-good `stable` commit, with matching `rules-manifest.json` and rules, then invoke the skill again.
- If offline, the cached local rules remain usable.

## Security reminders
- A SHA-256 manifest hosted in the **same repo** protects consistency/corruption, **not** a malicious repository maintainer. Only trusted reviewers may update `stable`; consider branch protection.
- Private GitHub source needs `contents:read` at runtime; never embed PATs, customer data or credentials in this repository.
- Changes must not expand the skill's permission to send marketing emails or collect sensitive data.
