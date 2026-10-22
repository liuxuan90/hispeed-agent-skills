# Current Hispeed operating workflow (separate agents)

## Existing / proposed components
- **Gemini**: regular discovery, web research, evidence capture, personalized English email drafting; preferably outputs structured Google Sheets rather than only Google Docs.
- **Google Sheets**: staging/handoff for research records; one continuously maintained dataset.
- **Snov.io**: currently potential weekly manual batch email verification and contact enrichment. MCP authorization has been unstable in this project; do not require MCP to run this research skill. Optional API connector can be added later.
- **ChatGPT Work**: reads Sheets where authorized, reconciles lead IDs, deduplicates and transfers status to WeCom; ability to run unattended and write the source must be tested in the user's plan/runtime.
- **WeCom enterprise smart sheet/bot**: management view; tool permissions needed for read/write. Do not assume successful writes.
- **Muse / other mail executor**: separate sending/receiving roles, only after actual capability, approval and deliverability tested; may require user approval. Do not assume fully autonomous sending.

## Separation of tasks
- Skill V1 is **research only**. It does not own any send/receive operation.
- Weekly validation hold: `VALID` must come from named checker; other states remain pending. Research progress should continue despite validator/MCP outage.
- Each newly researched record: `send_approval_status=NOT_APPROVED`, `send_status=NOT_SENT`.
- When receiver replies, mail tool updates `reply_status` via attributable message data; Work writes to management sheet and proposes human follow-up.

## Daily vs weekly
- Research: once on selected workdays, if scheduled environment supports this Skill.
- Execution agent: once/twice daily for read/check/sync; this does **not** guarantee real-time mail tracking.
- Snov.io verification: weekly as currently planned, or immediate exception for a time-sensitive legitimate lead.
- Human verification of contact and legal basis, and approved sending remain mandatory.
