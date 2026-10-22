# Quality gates — every run

## Before qualification
[ ] Target country confirmed; target customer type confirmed or pilot default explicitly noted.
[ ] Official company domain accessible or limitation marked; identify false directory pages.
[ ] Country and product/service evidence include source URLs and observation date.
[ ] Historical dedup and current distributor territory checks attempted; when inaccessible => `REVIEW_REQUIRED`.
[ ] Facts vs hypotheses differentiated; no imaginary active purchase request.

## Before handoff
[ ] Role evidence and email evidence separately sourced.
[ ] VALID only when provider result available with verification date and raw status.
[ ] `send_approval_status=NOT_APPROVED` for all newly created records.
[ ] Emails are distinct and fact-based, no inflated product claims, no invented certifications/model parameters.
[ ] Every row has stable `lead_id`, `company_domain`, source, and target segment.
[ ] Four logical sheets match headers and key links. No duplicate company-domain/contact-email pairs.
[ ] Summary counts: discovered, rejected, shortlisted, named-contact found, verified emails, drafts produced, dedup pending, blocked.
[ ] Mention missing capabilities (Snov.io disconnected, Google Sheets read-only, WeCom not authorized).
[ ] Note bootstrap skill version and refreshed rules version.

## Failure behavior
Never invent. Make a partial report with `NEEDS_REVIEW`; do not substitute unrelated companies or padded data. If email verification is pending, do not transfer to an auto-send queue. If the GitHub update mechanism fails, proceed with last locally verified rules and mention version. Compliance requirements may vary by country.
