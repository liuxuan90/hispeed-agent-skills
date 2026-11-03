---
name: hispeed-lead-intelligence
description: Research and qualify evidence-backed industrial laser prospects for Hispeed Laser, or check and update this installed Skill from its reviewed stable release. Use for company discovery, fit investigation, decision-relevant contacts, email evidence, prioritization, researched first-email drafts, and explicit Skill maintenance requests. Do not use for sending campaigns, monitoring replies, assigning sales owners, or later-stage follow-up sequences.
metadata:
  version: 1.2.2
---

# Hispeed Lead Intelligence

Find fewer, defensible prospects rather than filling a quota with weak names. Treat company fit, contact relevance, and email confidence as separate conclusions.

## Start with a run brief

Require these inputs before discovery:

- country or market;
- one narrow industry or application;
- one customer type: distributor, system integrator, or end manufacturer;
- Hispeed product or process focus;
- target count;
- target count basis: candidates reviewed or qualified companies delivered;
- exclusions and known-customer list;
- output language;
- destination table or an explicit request for a standalone data package.

Use [assets/run-brief-template.md](assets/run-brief-template.md). Ask only for missing decisions; find public facts yourself. Never broaden the segment to meet the requested count.

## Preflight capabilities

List the capabilities actually available for the run: web search, page access, LinkedIn or other authenticated sources, spreadsheet access, DNS/MX, SMTP, and Catch-all detection. Record unavailable capabilities as `NOT_AVAILABLE`. A claimed check must have a real tool result.

## Load the relevant rules

Read these references before researching:

- [references/hispeed-company-facts.md](references/hispeed-company-facts.md) for the approved company and product context;
- [references/evidence-policy.md](references/evidence-policy.md) for source quality and FACT/INFERENCE/UNKNOWN handling;
- [references/qualification-and-scoring.md](references/qualification-and-scoring.md) for batch ICP, peer classification, gates, and scoring;
- [references/contact-email-policy.md](references/contact-email-policy.md) before identifying people or email addresses;
- [references/workbook-schema.md](references/workbook-schema.md) before formatting, deduplicating, or writing records.

Additionally read:

- [references/first-email-policy.md](references/first-email-policy.md) when a first-email draft is requested;
- [references/feedback-and-versioning.md](references/feedback-and-versioning.md) when prior outcomes or optimization are in scope;
- [references/example-record.md](references/example-record.md) when calibrating a new implementation or reviewing output shape.

For rule maintenance rather than lead research, read [references/maintenance-zh.md](references/maintenance-zh.md).

## Check or update this Skill

Do not modify the installation during ordinary lead research. Only run maintenance when the user explicitly asks to check or update the Hispeed Skill.

- Check: run `python scripts/manage_skill.py check` from this Skill directory.
- Update: first run `python scripts/manage_skill.py check`. For an ordinary rule release, run `python scripts/manage_skill.py update`. If the check reports `REVIEW_BEFORE_UPDATE: YES`, summarize the script, permission, dependency, or workflow changes first, then run `python scripts/manage_skill.py update --accept-reviewed-changes` when the requested update is within the user's authorization.
- Stable source: `liuxuan90/hispeed-agent-skills`, branch `stable`, path `skills/hispeed-lead-intelligence`.
- The updater verifies the release manifest and every packaged file, keeps a recoverable previous version outside the live Skill directory, and restores it if activation fails.
- If the installed files have local modifications or untracked business files, stop instead of overwriting them. Never upload local customer data, credentials, sales records, or business files.
- After a successful update, tell the user the installed version and whether the current Agent must start a new conversation or reload its Skill index.

## Run the research pipeline

### 1. Build the batch rubric

Translate the brief into a batch-specific ICP, hard gates, exclusions, observable process or channel signals, role ladder, local-language query matrix, and scoring interpretation. Keep distributors, system integrators, and end manufacturers in separate runs.

### 2. Discover candidates

Search in English and the market's working language. Combine industry, product, material, process, application, company-type, association, trade-show, hiring, expansion, and automation terms. Keep a query log and deduplicate repeated discoveries.

### 3. Establish company identity and evidence

Confirm the official domain, operating status, market, actual business, customer type, and manufacturing, integration, or channel activity. Open source pages; search snippets are discovery clues, not final evidence. Save URL, title, quotation or faithful paraphrase, publication date when available, access date, source tier, and evidence label.

### 4. Classify peers before excluding them

An overseas laser-equipment peer may also be a buyer, channel partner, integrator, or OEM/ODM opportunity. Assess direct competition and commercial opportunity independently. Route mixed or unclear cases to `REVIEW`; do not reject a company merely because it sells laser equipment.

### 5. Apply gates, then score

Apply hard gates before scoring. Route missing but potentially recoverable evidence to `REVIEW`, not invented certainty. Score only candidates whose required gates pass. Keep `Company Fit Score`, `Contact Relevance`, `Email Confidence`, research completeness, and write status separate.

### 6. Research contacts and email evidence

Use the role ladder for the selected customer type. A person needs evidence for name, role, and company relationship. Search public email evidence, match the company domain, infer a pattern only from real published examples, and record technical checks only when executed. Never turn a pattern guess into a verified address or invent a percentage.

### 7. Draft one researched first email

For each delivered company with enough evidence and a selected primary contact, draft at most one first email. Follow the leader-approved body sequence:

1. `Personalized Problem`
2. `Show You Solve It`
3. `CTA`

Ground the problem in evidence and use exploratory language for inference. Produce three subject options, one recommended subject, the main draft, `evidence_used`, and `reason_for_angle`. Do not send the email.

### 8. Deduplicate and write safely

Use normalized company domain as the primary identity key, with legal name, country, and company LinkedIn as secondary signals. Update an existing record rather than duplicating it. Preserve human scores, sales ownership, follow-up status, notes, and conflicting values. If destination access or schema mapping is uncertain, return a standard data package instead of guessing a write.

### 9. Report the run

Use [assets/run-report-template.md](assets/run-report-template.md). Report requested count and its basis, candidates reviewed, `QUALIFIED`, `REVIEW`, `REJECTED`, and `DUPLICATE` counts, research completeness, write status, unavailable capabilities, unresolved conflicts, and required human or downstream actions.

Before delivery, reconcile the package rather than trusting a coordinator summary. Every delivered company that requires a draft must have the complete draft body, exactly three subject options, one recommended subject, evidence IDs, angle rationale, signature placeholder, and draft-presence check in the package. A reference such as “see subagent file” does not satisfy delivery.

## Completion criteria

A run is complete only when every delivered company has:

- a resolved identity and deduplication result;
- gate decisions with evidence;
- separate business, contact, and email conclusions;
- traceable sources for consequential claims;
- an explicit qualification status and rationale;
- a structurally valid record matching [assets/company-record.schema.json](assets/company-record.schema.json);
- a first-email draft only when requested and supported by sufficient evidence.
- every completeness blocker and required downstream action recorded explicitly;
- every requested draft present in full, not only summarized or referenced.

Return fewer leads when the evidence bar is not met. Mark incomplete external writes or unavailable checks as `PARTIAL`; never report them as completed.

