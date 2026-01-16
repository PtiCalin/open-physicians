# Irish Medical Council

- Slug: `imc`
- Region: Europe
- Scope: Ireland
- Raw staging: `data/raw/europe/united_kingdom_and_ireland/irish_medical_council`

## Purpose
Irish regulator returning JSON rows with registration division and specialty.

## Access Snapshot
AJAX posts to /RegisterSearch/api/Doctors with anti-forgery token.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/united_kingdom_and_ireland/irish_medical_council`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
