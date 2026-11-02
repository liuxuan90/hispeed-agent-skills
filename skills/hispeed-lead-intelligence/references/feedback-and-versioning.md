# Feedback and versioning

## Three learning layers

### Core guardrails

Evidence labels, anti-fabrication rules, hard-gate semantics, privacy, legal access, and safe-write behavior do not change automatically.

### Calibrated parameters

Industry-signal weights, thresholds, role priority, query patterns, and email angles may receive versioned proposals based on reviewed outcomes.

### Batch adaptation

An authorized run may use approved historical patterns to prioritize discovery. Record which prior findings influenced the run.

## Outcome labels

Positive labels include `VALID_LEAD`, `VALID_CONTACT`, `POSITIVE_REPLY`, `QUALIFIED_OPPORTUNITY`, `SAMPLE_TEST`, `QUOTE`, and `ORDER`.

Negative labels include `WRONG_COMPANY`, `WRONG_INDUSTRY`, `WRONG_CONTACT`, `INVALID_EMAIL`, `BOUNCE`, `NO_RELEVANT_NEED`, `DUPLICATE`, `UNSUBSCRIBE`, and `COMPLAINT`.

Treat `NO_REPLY` as neutral unless delivery, contact correctness, observation period, message quality, timing, and sample size support a stronger conclusion.

## Proposal thresholds

- fewer than 30 human-reviewed leads: record observations only;
- 30–99: propose low-risk adjustments;
- 100 or more across multiple batches: propose weight or threshold changes;
- every accepted change records version, evidence, sample size, reason, and before/after evaluation.

The agent may produce an `Optimization Proposal`; a human approves the next rule or scoring version.

## Accepted rule release: skill v1.1.0 / schema v2

Source observation: one 2026-11-02 USA industrial-plastics end-manufacturer run reported 21 reviewed candidates. This sample is below the 30 human-reviewed-lead threshold and is recorded as an observation, not a calibrated weight or threshold change. The underlying 21 records were not independently re-adjudicated during rule maintenance.

Accepted consistency fixes:

- contract manufacturers and CDMOs operating the production line count as end manufacturers unless the Run Brief explicitly requires own-brand ownership;
- `research_completeness` has explicit criteria and blocker reporting;
- the known-customer gate is independent from general exclusions;
- contact relevance and contact currency are separate conclusions;
- email pattern evidence records dates and domain-lifecycle risk;
- first drafts use an approved sender or a literal signature placeholder;
- already-equipped prospects remain scorable with a non-greenfield angle;
- scores 75–79 retain `QUALIFIED` with a `BORDERLINE` band and priority constraint;
- delivery packages verify complete draft presence rather than relying on summaries.

Scoring model v1 weights and the 75-point qualification threshold remain unchanged.


