# Workbook schema and write rules

Map these logical tables to the destination platform. Names and column order may adapt; field meaning and identity rules remain stable.

## 1. Run Brief

`run_id`, skill version, scoring version, date, market, market-presence requirement, local language, industry/application, customer type, Hispeed focus, exclusions, known-customer-list state, target count, target count basis, destination, capability preflight, query summary.

## 2. Lead Summary

One row per company: `lead_id`, legal/display name, normalized domain, country, customer type, qualification status, Company Fit Score and score status, Contact Relevance, Email Confidence, peer classification, research completeness, write status, priority, core rationale, next review action, source coverage, last researched date.

## 3. Company Research

Company identity, operating evidence, products, materials, parts, manufacturing/integration/channel activity, trigger signals, Hispeed fit, hard-gate decisions, facts, inferences, unknowns, negative evidence, score components, and sources.

## 4. Contacts & Emails

Person identity, title, role relevance, evidence, primary/backup status, email, discovery method, public source, pattern basis, email evidence level, MX/SMTP/Catch-all states, verification tool, verification time, and Snov.io follow-up status.

## 5. Email Drafts

Primary contact, three subjects, recommended subject, Personalized Problem, Show You Solve It, CTA, complete draft, evidence used, angle rationale, and review flags.

## 6. Rejected & Duplicates

Candidate identity, status, rejection or duplicate reason, matched existing lead, evidence, run ID, and review date.

## Optional 7. Optimization Feedback

Human validation and downstream outcome labels. Do not add sales follow-up tasks here; that belongs to a separate follow-up workflow.

## Identity and deduplication

Use normalized official domain as the primary key. Use legal name, country, company LinkedIn, and registry identity as secondary signals. A contact uses a professional profile URL or person name plus company domain; email alone is not sufficient identity.

## Idempotent writes

- Read the destination before writing.
- Add a new company only when no identity match exists.
- Update evidence and research timestamps on an existing record.
- Preserve old and new values when sources conflict.
- Preserve human scores, ownership, follow-up state, sales notes, and outcome labels unless the task explicitly authorizes their update.
- Record `run_id`, skill version, scoring version, and update time.
- If mapping or permission is uncertain, return a standard package and set `write_status` to `PARTIAL` or `FAILED` without changing qualification status.

Use [../assets/standalone-package-manifest.md](../assets/standalone-package-manifest.md) when no destination table is supplied.


