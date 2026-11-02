# Contact and email research policy

## Role ladders

### Distributor

Owner/Founder → Managing Director → Sales Director → Business Development/Partnerships → Product Manager → Technical Director.

### System integrator

Owner/Founder → General Manager → Engineering/Technical Director → Automation/Project leadership → Business Development.

### End manufacturer

Owner/General Manager for smaller firms, otherwise Plant/Operations/Production → Manufacturing/Engineering → Automation/Process/Quality → Procurement/Purchasing.

Choose one primary contact and at most one backup with a meaningfully different role. HR, finance, administration, and unrelated sales roles are not decision-relevant merely because they are discoverable.

Collect public business contact details only. Do not collect private personal email addresses, private phone numbers, family details, or unrelated personal data.

## Contact evidence

Require evidence for the person's name, current role, and company relationship. Save the source and access date. A guessed email pattern never proves that a person works at the company.

Record `role_evidence_date` and `contact_currency` separately from role relevance:

- `CURRENT`: current official team page, or evidence no older than 24 months;
- `AGING`: newest evidence is over 24 and up to 48 months old; set `reverify_title_before_send=true`;
- `STALE`: newest evidence is over 48 months old; it cannot support a confirmed current contact until reverified;
- `CONFLICT`: a current source contradicts the recorded title or company relationship;
- `UNKNOWN`: no defensible evidence date or current official page is available.

Role relevance describes whether the role is appropriate; contact currency describes whether the person-role relationship is current. Do not lower relevance merely because evidence is old. `AGING`, `STALE`, `CONFLICT`, and `UNKNOWN` require explicit review, and all except `CURRENT` prevent `research_completeness=COMPLETE`. Aggregator listings alone do not refresh contact currency.

## Email discovery

Search, in order:

1. company website and official documents;
2. current professional or company profiles;
3. credible public business material;
4. published company email examples that establish a pattern;
5. technical checks available in the current environment.

Match the domain to the resolved company identity. Preserve source and method for every address.

## Email evidence levels

- `E5`: public individual company email with multi-source person, role, and domain agreement;
- `E4`: individual company email from a reliable public source with domain agreement;
- `E3`: pattern inference supported by multiple real published company addresses;
- `E2`: weak or single-example pattern inference;
- `E1`: generic department or company inbox;
- `E0`: no usable email found.

Use `NOT_EVALUATED` when email research was not performed or could not be performed. `E0` means the research was performed and found no usable address.

Record `pattern_example_dates` and any acquisition, rebrand, or domain change. An example older than five years, or from a pre-acquisition or pre-rebrand domain, is one weak example unless a current address on the same active domain confirms the pattern. It cannot independently establish E3. A single published individual address older than five years is capped at E4 and requires `email_reverify_required=true`; age alone never upgrades an address to E5.

Store technical state separately:

- syntax check;
- domain match;
- MX result;
- SMTP result;
- Catch-all result;
- verification tool and timestamp.

`Catch-all` means the mailbox cannot be confirmed. SMTP acceptance is evidence, not a delivery guarantee. Never create a numeric confidence percentage unless a named tool actually returned that metric and its meaning is preserved.

Snov.io is a downstream bulk supplement. The first research pass still performs public-source discovery, cross-checking, pattern analysis, and any genuinely available technical checks.


