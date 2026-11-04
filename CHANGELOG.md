# Changelog

## v1.3.1 — 2026-11-04

- Default to one Excel workbook, or one online spreadsheet document, containing all required Chinese worksheets.
- Do not silently split normal delivery into separate CSV, JSON, Markdown, or Excel files.
- Add delivery checks for workbook count, worksheet completeness, Chinese headers, and cross-sheet `客户编号` linkage.
- Keep the multi-file standalone package only as an explicitly reported fallback when workbook creation is unavailable.

## v1.3.0 — 2026-11-03

- Default user-facing workbook, online-sheet, CSV-preview, and table-report presentation to Simplified Chinese.
- Add stable Chinese worksheet names, headers, and status labels without changing canonical JSON keys, scoring model v1, or schema v2 business meaning.
- Preserve names, emails, URLs, evidence quotations, product/model names, and English first-email drafts in their source language.

## v1.2.3 — 2026-11-03

- Use the correct GitHub API media type when resolving the immutable stable commit.

## v1.2.2 — 2026-11-03

- Pin manifest and package downloads to the same immutable `stable` commit to avoid GitHub cache races.

## v1.2.1 — 2026-11-03

- Fix migration from a legacy v1.1.0 installation that does not yet contain a release manifest.

## v1.2.0 — 2026-11-03

- Retire and remove `hispeed-global-leads-research`.
- Keep `hispeed-lead-intelligence` as the only official Hispeed customer-development Skill.
- Add manual `check` and `update` operations using the reviewed `stable` branch.
- Add whole-package SHA-256 verification, previous-version backup, and automatic activation rollback.
- Keep the qualification rules, scoring model v1, and company-record schema v2 business fields unchanged.

## v1.1.0 — 2026-11-02

- Incorporate reviewed consistency improvements from the first controlled lead-research run.
- Preserve scoring model v1 and move company records to schema v2.
