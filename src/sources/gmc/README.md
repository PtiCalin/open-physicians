# General Medical Council

- Slug: `gmc`
- Region: Europe
- Scope: United Kingdom
- Raw staging: `data/raw/europe/united_kingdom_and_ireland/general_medical_council`

## Purpose
UK regulator with JSON API including sanctions and status history.

## Access Snapshot
REST endpoint /api/gmc/Registrations supporting pagination.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/united_kingdom_and_ireland/general_medical_council`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
