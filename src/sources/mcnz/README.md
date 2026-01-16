# Medical Council of New Zealand

- Slug: `mcnz`
- Region: Oceania
- Scope: New Zealand
- Raw staging: `data/raw/oceania/new_zealand/medical_council_of_new_zealand`

## Purpose
New Zealand council exposing register via JSON endpoint with scopes of practice.

## Access Snapshot
/umbraco/api/register/search returning JSON payloads.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/oceania/new_zealand/medical_council_of_new_zealand`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
