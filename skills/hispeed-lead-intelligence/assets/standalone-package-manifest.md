# Standalone lead research package

Use this layout when no online table is supplied:

```text
<run-id>/
├── manifest.json
├── run-brief.md
├── run-report.md
├── lead-summary.csv
├── company-research.jsonl
├── contacts-emails.csv
├── email-drafts.md
└── rejected-duplicates.csv
```

`manifest.json` records run ID, skill version, company-record schema version, scoring version, creation time, output language, file list, record counts, and checksums when available. Every company JSON object follows `company-record.schema.json`.

The stable filenames may remain in English for automation compatibility. User-facing Markdown and CSV tables use the Simplified Chinese worksheet/header mapping in `references/workbook-schema.md`; canonical JSON keys remain English. Company/person names, emails, URLs, evidence quotations, product/model names, and English email drafts remain in their source language.

It also records `draft_presence_check` for every delivered company requiring an email draft:

```json
{
  "lead_id": "example.com",
  "draft_present": true,
  "subject_count": 3,
  "recommended_subject_present": true,
  "body_word_count": 104,
  "signature_state": "PLACEHOLDER"
}
```

The package is incomplete when a required draft is only referenced, summarized, or absent.

