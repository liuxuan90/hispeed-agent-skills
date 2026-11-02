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

`manifest.json` records run ID, skill version, scoring version, creation time, output language, file list, record counts, and checksums when available. Every company JSON object follows `company-record.schema.json`.

