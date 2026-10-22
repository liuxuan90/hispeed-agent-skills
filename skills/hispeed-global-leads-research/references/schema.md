# Four-sheet data contract (Google Sheets → ChatGPT Work → WeCom)

Use four logical worksheets; see `assets/sheets/` for UTF-8 CSV headers. Add records, never recreate the entire workbook daily. Canonical `lead_id` stays stable; normalize `company_domain` (lowercase; remove www and URL path) and keep `contact_id` distinct where multiple people work at one company.

1. **01_Lead_Summary**: lead_id, company, country, domain, ICP, role/contact, work email, verification, score, evidence link, research date, dedup status.
2. **02_Company_Research**: dossier details, verified source evidence, application hypothesis, uncertainties, evidence dates; never present inferred purchase needs as fact.
3. **03_Personalized_Emails**: English subject/body plus rationale and approval. Draft only; `send_approval_status=NOT_APPROVED` initially.
4. **04_Priority_Execution**: score component totals, rank, suggested next step, owner, planned action, email/response state, status timestamps, current review notes.

## Status vocabulary
- `research_status`: NEW, RESEARCHED, NEEDS_REVIEW, REJECTED
- `contact_status`: ROLE_CONFIRMED, ROLE_POSSIBLE, CONTACT_NOT_FOUND
- `email_verification_status`: NOT_FOUND, PUBLIC_UNVERIFIED, PATTERN_GUESSED, VALID, UNKNOWN, CATCH_ALL, INVALID
- `dedupe_status`: CLEAR, DUPLICATE, REVIEW_REQUIRED
- `send_approval_status`: NOT_APPROVED, APPROVED, BLOCKED
- `send_status`: NOT_SENT, SCHEDULED, SENT, FAILED, CANCELLED
- `reply_status`: NOT_CHECKED, NO_REPLY, REPLIED, BOUNCED, OPTED_OUT

## Synchronization ownership
Gemini (or research agent) creates/updates research and draft fields only. Weekly Snov.io manual verification updates only verification evidence. ChatGPT Work reconciles identities, checks dedup and approved records, and updates the WeCom management view if connection is working. Muse or another mail executor owns the actual sending/receiving states. Never assume a platform has written a row until its tool confirms success.

## Import/export safety
- Escape spreadsheet formula-leading values (=,+,-,@) if generated from untrusted external text before importing into CSV or Sheets.
- Do not expose access tokens, passwords, or internal suppression list details in external handoffs.
- Use UTF-8 CSV, preserve record IDs, and annotate `sync_status` / last sync timestamp.
