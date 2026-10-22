# Hispeed Agent Skills

**Private skill source for Hispeed Laser (Dongguan Hispeed Laser Technology Co., Ltd.) marketing team.**

This repository is intended to house multiple reusable agent skills. Only one skill is included in this initial release:

- [`hispeed-global-leads-research`](skills/hispeed-global-leads-research/SKILL.md) — evidence-based overseas B2B prospect discovery, company qualification, public contact research, personalized English **drafts**, and structured handoff.

## Scope

Target industrial **Fiber, MOPA, CO₂, UV, 3D and Rotary / 360°** laser marking/engraving applications. Prioritize distributors/resellers in the first pilot; integrators and industrial manufacturers are optional segments. Welding/cutting/cleaning are outside the default scope.

**This skill does not automatically verify email deliverability or send emails.** `VALID` means a named provider returned that result, with evidence and timestamp. Existing-channel checks, do-not-contact screening, and human approval are mandatory before outreach.

## Layout

```text
hispeed-agent-skills/
├── README.md
├── .gitignore
├── docs/RELEASE_PROCESS.md
└── skills/hispeed-global-leads-research/
    ├── SKILL.md                    # fixed entrypoint & safety limits
    ├── references/*.md             # auto-refreshable reviewed research rules
    ├── rules-manifest.json         # SHA-256 hashes and rules version
    ├── config/update.json          # source repository and stable ref
    ├── scripts/update_rules.py     # trusted local updater only
    ├── assets/sheets/*.csv         # four-sheet schema
    └── tests/test_updater.py
```

## Install and update

Supported local agents can install a skills-compatible repository through the corresponding Skills CLI, or can place the skill folder in their local skills directory. **Check support for private GitHub repositories and actual installation path first.**

For a trusted local agent with Python 3.10+, file-write and Internet access, invoking the skill includes an instruction to run `scripts/update_rules.py` before research. This fetches reviewed Markdown rules from the `stable` branch. **The agent must actually have permission to run the script; merely installing SKILL.md cannot force automatic execution on every platform.**

A private repository requires a scoped read-only token in environment variable `HISPEED_SKILL_GITHUB_TOKEN` when using the standalone updater. Do not place tokens in prompts, files, Sheets or Git history.

Until the `stable` branch exists and the environment is authorized, startup falls back to bundled local rules. This is safe and expected. See [release guide](docs/RELEASE_PROCESS.md) and [skill guide](skills/hispeed-global-leads-research/README_使用说明.md).

## Pilot

Ask your supported agent to use `hispeed-global-leads-research`, research **5 industrial laser marking distributors in a specified country**, cite company evidence, find public role/contact information, draft English outreach, and export four worksheets. Do not send messages.

## Privacy

Do **not** commit customer databases, purchased contact lists, validation CSVs, email addresses of individual prospects, API secrets, or internal channel agreements. Keep those in access-controlled business systems. Use GitHub for **rules and code only**.
