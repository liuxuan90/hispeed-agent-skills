# Hispeed Skill release process

## Source of truth

- Official Skill: `skills/hispeed-lead-intelligence/`
- Development branch: `main`
- Reviewed installation and update branch: `stable`
- Version: `metadata.version` in `SKILL.md`
- Package integrity: `release-manifest.json`

No release may add customer lists, personal contact exports, credentials, API keys, internal prices, margins, sales records, or other business data.

## Prepare a release on `main`

1. Make the smallest required change without changing approved business rules unless the owner approved that change.
2. Select the semantic version: patch for compatible fixes, minor for compatible features/rule releases, major for incompatible behavior or schema changes.
3. Update `metadata.version` and any schema/example constants that intentionally track it.
4. Add a concise entry to `CHANGELOG.md`.
5. Run `python tools/build_skill_manifest.py` after all Skill files are final.
6. Validate the Skill and updater:
   - `python -X utf8 %USERPROFILE%\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\hispeed-lead-intelligence`
   - `python skills\hispeed-lead-intelligence\scripts\manage_skill.py self-test`
   - verify the manifest checksums against the package.
7. Scan the tracked files for secrets and prohibited business data.
8. Commit normally to `main`; never rewrite published history.

## Promote to `stable`

1. Review the `main` commit and its diff, especially scripts, dependencies, permissions, schemas, and workflow changes.
2. Promote the exact approved commit to `stable` through a pull request when branch protection is active.
3. Tag the stable commit using the Skill version, for example `v1.2.0`.
4. Run the updater's live `check` against GitHub and test an update in a temporary installation.
5. Open the installed `SKILL.md`, confirm the version, and start a new Agent conversation for a load test.

Ordinary Markdown rule changes still receive a semantic version and manifest refresh, but users update the existing installation in place; they do not uninstall or create a second version-named Skill folder.

## Rollback

- Local activation failure restores the previous installation automatically.
- A successful update leaves the prior package under the sibling `.hispeed-skill-backups` directory (maximum three managed backups).
- To roll back the public stable release, promote a reviewed corrective commit or prior known-good commit to `stable`, publish a new patch version when appropriate, and run the updater again.
- Do not force-push or erase Git history to roll back.

## Environment compatibility

The bundled updater requires Python 3.10+, HTTPS access to public GitHub, and write permission to the installed Skill directory. Codex on this Windows device satisfies those requirements. Other Agents may use their native Skill manager instead; verify that environment's installation path, GitHub support, reload behavior, and script permission before updating.
