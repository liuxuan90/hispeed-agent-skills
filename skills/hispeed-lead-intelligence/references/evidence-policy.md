# Evidence policy

## Evidence labels

### FACT

A source directly supports the statement. Store the source URL, page title, quotation or faithful paraphrase, publication date when available, access date, and source tier.

### INFERENCE

The conclusion follows from named facts but is not directly stated. Store the supporting fact IDs, reasoning, confidence (`HIGH`, `MEDIUM`, or `LOW`), and what would confirm or disprove it. Phrase it as a possibility in external writing.

### UNKNOWN

Evidence is missing or contradictory. Leave the field empty or mark `UNKNOWN`; do not complete it from model memory or industry convention.

## Source tiers

- `S1`: company website, government or corporate registry, regulator filing;
- `S2`: official company social account, official job posting, contact's current professional profile;
- `S3`: industry association, trade-show organizer, named partner site, reputable news;
- `S4`: reputable commercial database;
- `S5`: directory, aggregator, or search-result summary.

A `QUALIFIED` company needs at least two independent pieces of evidence and cannot rely only on `S5`. Two pages repeating the same syndicated text are one source, not two.

## Freshness and conflicts

- Record the publication date and access date separately.
- Prefer current evidence for operating status and contact employment.
- Preserve conflicting values with both sources and route material uncertainty to `REVIEW`.
- Search snippets, generated summaries, and model recollection are discovery aids, not final evidence.

## Negative evidence

Actively test disqualifying alternatives: closed business, wrong industry, consumer-only activity, directory-only identity, no relevant process or channel activity, stale contact, direct competitive conflict, or exclusion-list match. Keep the rejection reason and evidence in the rejected log.


