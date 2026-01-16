# Ministry of Health Israel

- Slug: `israel_moh`
- Region: Middle East
- Scope: Israel
- Raw staging: `data/raw/middle_east/israel/ministry_of_health_israel`

## Purpose
Israeli practitioner portal with REST backend returning Hebrew metadata.

## Access Snapshot
/api/Practitioner endpoints; requires locale-aware headers.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/middle_east/israel/ministry_of_health_israel`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
