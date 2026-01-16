# Department of Health Abu Dhabi

- Slug: `doh_abu_dhabi`
- Region: Middle East
- Scope: United Arab Emirates (Abu Dhabi)
- Raw staging: `data/raw/middle_east/united_arab_emirates/department_of_health_abu_dhabi`

## Purpose
DOH Abu Dhabi public API listing licensed practitioners and facilities.

## Access Snapshot
/api/publicsearch with JSON pagination and optional API key.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/middle_east/united_arab_emirates/department_of_health_abu_dhabi`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
