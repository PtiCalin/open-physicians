# Health Professions Council of South Africa

- Slug: `hpcsa`
- Region: Africa
- Scope: South Africa
- Raw staging: `data/raw/africa/south_africa/health_professions_council_of_south_africa`

## Purpose
South African regulator requiring CAPTCHA/FOI for bulk exports.

## Access Snapshot
hpcsaonline.co.za form with CAPTCHA; prefer FOI export ingestion.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/africa/south_africa/health_professions_council_of_south_africa`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
