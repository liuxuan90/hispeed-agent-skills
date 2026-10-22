# Company research and evidence

## Source reliability
1. Primary: company official site and official public catalogs, current company press releases and case studies.
2. Supporting: credible trade association pages, exhibition listings, accessible public business profile, recent public job descriptions or interviews.
3. Weak: scraping directories, unsourced aggregator descriptions, email-pattern generators.

For each material claim, store `claim`, `source_url`, `observed_at`, `confidence_class`:
- `FACT` — directly confirmed and linked to specific evidence.
- `INFERENCE` — reasoned opportunity, clearly marked hypothesis.
- `UNKNOWN` — cannot establish.

## Minimum company dossier
- Legal/trading name, canonical domain, country, business type, products/services, verified industrial application, channel/brand evidence (if any), most relevant Hispeed solution **as a hypothesis**, reasons to disqualify, next research question, sources and time.
- Current partner/exclusivity status is often unknown; do not infer from absence of a website statement.
- Distinguish manufacturing location, sales office and shipping market when publicly described.

## Research discipline
- Verify company domain by actual official website, not SERP result text alone.
- If an official site blocks access, write `NOT_VERIFIED`, collect only other attributable facts, and hold for review.
- Cite links to exact product and application pages where possible.
- Time-sensitive facts (contacts, catalog lines, partner status) need observation dates.
- Never print private personal phone data or social accounts from questionable scrapes.
