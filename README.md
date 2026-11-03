# Hispeed Agent Skills

Public, reviewed Skill source for Hispeed Laser.

## Official Skill

[`hispeed-lead-intelligence`](skills/hispeed-lead-intelligence/SKILL.md) is the only maintained customer-development Skill. Version **1.2.0** supports evidence-backed company discovery, company research, batch-specific ICP qualification, decision-relevant contact research, email-evidence classification, separate fit/contact/email conclusions, prioritization, a researched first-email draft, and structured handoff.

The Skill does not send campaigns, monitor replies, assign sales owners, or perform later-stage follow-up. Customer databases, contact exports, credentials, API keys, pricing, margin data, and internal sales records must never be committed here.

## Branches and releases

- `main`: development and release preparation.
- `stable`: reviewed source used by installers and the updater.
- Semantic versions (`v1.2.0`, `v1.2.1`, `v2.0.0`) identify formal releases.

Do not copy the Skill into version-named installation folders. The live folder remains `hispeed-lead-intelligence`; the updater keeps up to three recoverable backups outside it.

## First installation

With the bundled Codex installer:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo liuxuan90/hispeed-agent-skills --ref stable --path skills/hispeed-lead-intelligence
```

If the Agent has a compatible Skills CLI, this public GitHub path may also be installed through that tool. Confirm the actual installation path and supported flags in that environment rather than assuming every Agent behaves like Codex.

## Check and update

From the installed Skill folder:

```powershell
python scripts/manage_skill.py check
python scripts/manage_skill.py update
```

The check is read-only. Update downloads the `stable` branch, verifies the release manifest and every Skill file, preserves the previous version, activates the new package, and restores the old package if activation fails. It refuses to overwrite unexpected local changes unless a maintainer deliberately uses `--force`. A release that changes scripts, permissions, dependencies, or important workflow requires review of the check output and the explicit `--accept-reviewed-changes` flag.

After updating, start a new Agent conversation or reload its Skill index so the current process does not continue using cached instructions.

See [docs/RELEASE_PROCESS.md](docs/RELEASE_PROCESS.md) for publishing and rollback.

## Repository layout

```text
hispeed-agent-skills/
├── CHANGELOG.md
├── README.md
├── docs/RELEASE_PROCESS.md
├── tools/build_skill_manifest.py
└── skills/hispeed-lead-intelligence/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── scripts/manage_skill.py
    ├── release-manifest.json
    ├── references/*.md
    └── assets/*
```

## Security boundary

The SHA-256 manifest detects incomplete or corrupted packages; it does not make an untrusted maintainer trustworthy. Treat `stable` as executable instructions, review script/permission/dependency/workflow changes before promotion, and protect the branch from force-pushes and accidental deletion.
