# Qualification and scoring

## Batch-specific ICP

Before searching, define:

- target market and local language;
- whether a local headquarters, local manufacturing site, or market presence is required;
- narrow industry or application;
- one customer type;
- Hispeed product or process focus;
- observable need or channel signals;
- hard exclusions;
- role ladder;
- query matrix;
- interpretation of each scoring dimension.

## Company type lenses

### Distributor

Look for industrial equipment sales, complementary laser or automation lines, service capability, geographic coverage, channel gaps, and OEM/private-label potential.

### System integrator

Look for automation engineering, machine vision, PLC/MES integration, conveyors, fixtures, safety systems, production-line projects, and a need for laser subsystems or complete equipment.

### End manufacturer

Look for actual parts, materials, lines, traceability, coding, marking, welding, cleaning, precision, throughput, quality, expansion, or automation needs.

## Peer classification

Evaluate competition and opportunity separately:

- `DIRECT_COMPETITOR`: confirmed direct overlap in product, market, and customer pursuit;
- `POTENTIAL_CUSTOMER`: plausible equipment or subsystem buyer;
- `CHANNEL_PARTNER`: reseller or regional channel opportunity;
- `OEM_ODM_OPPORTUNITY`: private-label, supply, or portfolio-completion opportunity;
- `SYSTEM_INTEGRATION_PARTNER`: technical integration opportunity;
- `HYBRID_REVIEW`: both competition and cooperation signals;
- `INSUFFICIENT_EVIDENCE`: classification cannot yet be defended.

Selling laser equipment is not an automatic rejection. Reject a peer only when the run's exclusions and evidence establish a disqualifying direct conflict.

## Hard gates

Record `PASS`, `FAIL`, or `UNKNOWN` for:

1. resolved real company identity;
2. evidence of current operation;
3. target-market match;
4. target-industry or application match;
5. target customer-type match;
6. observable manufacturing, integration, or channel activity;
7. defensible Hispeed process, product, or cooperation fit;
8. process feasibility evidence or an explicit `sample_test_required` conclusion;
9. at least two independent sources, not both `S5`;
10. exclusion and known-customer check;
11. material negative-evidence review.

The known-customer check passes only when a list was provided and checked, or the user explicitly confirmed that no list exists. Otherwise it remains `UNKNOWN`.

Use `REJECTED` for confirmed gate failure. Use `REVIEW` when a potentially good company has material, recoverable unknowns. Do not manufacture a pass to reach quota.

## Scoring model v1

Score gated candidates only:

| Dimension | Points |
|---|---:|
| ICP and narrow-industry match | 25 |
| Observable process, project, or channel need | 30 |
| Fit with the specified Hispeed capability | 25 |
| Evidence quality, independence, and freshness | 15 |
| Concrete personalization signal | 5 |

Store each component, evidence IDs, and rationale. Do not assign a score from impression alone.

## Statuses

- `QUALIFIED`: 75–100 and all required hard gates pass;
- `REVIEW`: 60–74 after all required gates pass, or any material recoverable gate remains `UNKNOWN` with no score assigned;
- `REJECTED`: below 60 after scoring, or confirmed hard-gate failure;
- `DUPLICATE`: already represented by the same company identity;

Track operational state separately:

- `research_completeness`: `COMPLETE` or `PARTIAL`;
- `write_status`: `NOT_REQUESTED`, `NOT_ATTEMPTED`, `WRITTEN`, `PARTIAL`, or `FAILED`.

If required gates do not all pass, set score status to `NOT_SCORED`, score to `null`, and record the reason.

The thresholds are versioned calibration defaults, not permanent truth.


