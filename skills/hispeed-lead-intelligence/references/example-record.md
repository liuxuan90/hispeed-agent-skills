# Synthetic example record

This example demonstrates structure, not a real prospect.

```json
{
  "lead_id": "exampleco.com",
  "run_id": "example-run",
  "skill_version": "1.1.0",
  "schema_version": "v2",
  "company_identity": {
    "name": "Example Components Ltd.",
    "domain": "exampleco.com",
    "country": "Exampleland",
    "customer_type": "end_manufacturer"
  },
  "qualification_status": "REVIEW",
  "qualification_band": "NOT_APPLICABLE",
  "research_completeness": "PARTIAL",
  "completeness_blockers": ["Independent evidence remains incomplete", "No current primary contact was identified"],
  "write_status": "NOT_REQUESTED",
  "known_customer_list_state": "USER_CONFIRMED_NONE",
  "hard_gates": {
    "identity": "PASS",
    "operating_status": "PASS",
    "market": "PASS",
    "industry": "PASS",
    "customer_type": "PASS",
    "observable_activity": "PASS",
    "hispeed_fit": "PASS",
    "process_feasibility": "UNKNOWN",
    "independent_evidence": "UNKNOWN",
    "exclusions": "PASS",
    "known_customer": "PASS",
    "negative_evidence_review": "PASS"
  },
  "company_fit": {
    "score_status": "NOT_SCORED",
    "score": null,
    "model_version": "v1",
    "equipment_state": "UNKNOWN",
    "components": {
      "icp_match": null,
      "observable_need": null,
      "hispeed_fit": null,
      "evidence_quality": null,
      "personalization_signal": null
    },
    "rationale": "Not scored because required gates remain UNKNOWN."
  },
  "peer_classification": "POTENTIAL_CUSTOMER",
  "contact_relevance": "UNKNOWN",
  "contact_currency": "UNKNOWN",
  "email_confidence": "NOT_EVALUATED",
  "contacts": [
    {
      "name": null,
      "title": null,
      "contact_relevance": "UNKNOWN",
      "role_evidence_date": null,
      "contact_currency": "UNKNOWN",
      "reverify_title_before_send": true,
      "relationship_source_ids": [],
      "email": null,
      "email_confidence": "NOT_EVALUATED",
      "pattern_example_dates": [],
      "email_reverify_required": false,
      "mx": "NOT_AVAILABLE",
      "smtp": "NOT_AVAILABLE",
      "catch_all": "NOT_AVAILABLE"
    }
  ],
  "facts": [
    {
      "id": "F1",
      "statement": "The company states that it manufactures serialized metal components.",
      "source_ids": ["S1"]
    }
  ],
  "inferences": [
    {
      "id": "I1",
      "statement": "Permanent laser marking may be relevant to its traceability workflow.",
      "supports": ["F1"],
      "confidence": "MEDIUM"
    }
  ],
  "unknowns": ["Current marking technology", "Active purchase project"],
  "negative_evidence": [],
  "sources": [
    {
      "id": "S1",
      "url": "https://exampleco.com/manufacturing",
      "title": "Synthetic manufacturing page",
      "excerpt_or_paraphrase": "The company states that it manufactures serialized metal components.",
      "source_tier": "S1",
      "published_at": null,
      "accessed_at": "2026-01-01"
    }
  ],
  "email_draft": null,
  "deduplication": {
    "normalized_domain": "exampleco.com",
    "result": "NEW",
    "known_customer_list_state": "USER_CONFIRMED_NONE",
    "matched_lead_id": null
  },
  "next_action": "Find an independent source and confirm the contact's current role.",
  "researched_at": "2026-01-01T00:00:00Z"
}
```


