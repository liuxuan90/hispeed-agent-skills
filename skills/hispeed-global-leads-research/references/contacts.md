# Decision makers and email evidence

## Roles by ICP
- Distributor: Founder/Owner, Managing Director, Product Manager, Sales Director, Business Development Director, purchasing decision maker only when justified.
- Integrator: Engineering Director, Head of Automation, Technical Director, Project Lead, Procurement if actual sourcing role is evident.
- Industrial manufacturer: Process Engineer, Production Engineering Lead, Manufacturing/Plant Manager; commercial purchasing may handle later purchase process.

## Identity states
- `ROLE_CONFIRMED`: employer and current role supported by public attributable source.
- `ROLE_POSSIBLE`: name/role listed in old or third-party sources; requires review.
- `CONTACT_NOT_FOUND`: no reliable person found.

## Email states (do not collapse)
- `NOT_FOUND`: no address.
- `PUBLIC_UNVERIFIED`: source visibly published it; no mailbox check.
- `PATTERN_GUESSED`: speculative address; never label valid.
- `VALID`: an email verification provider reported valid; record provider, date and source result.
- `UNKNOWN` or `CATCH_ALL`: inconclusive; not valid.
- `INVALID`: provider reported invalid; do not mail.

Store `email_source_url`, `verification_provider`, `verified_at`, `raw_verification_status` and `role_source_url` separately. Don't invent verification percentages or treat an MX check as proof a specific mailbox exists.

## Existing tools and fallback
- Snov.io website batch verification is acceptable as a weekly **manual** step; never assume unstable MCP is currently available.
- Optional later Snov.io API integration belongs to a separate, reviewed connector. This research skill never embeds API secrets.
- Validity does not establish legal permission to contact; apply geographic outreach rules and do-not-contact lists.
