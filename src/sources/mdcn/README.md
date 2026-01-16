# Medical and Dental Council of Nigeria

- Slug: `mdcn`
- Region: Africa
- Scope: Nigeria
- Raw staging: `data/raw/africa/nigeria/medical_and_dental_council_of_nigeria`

## Purpose
Nigerian council offering verification API requiring CAPTCHA tokens.

## Access Snapshot
portal.mdcngov.ng API /api/Practitioner/Verify.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/africa/nigeria/medical_and_dental_council_of_nigeria`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
