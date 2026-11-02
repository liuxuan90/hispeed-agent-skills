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


