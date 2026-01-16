# Dubai Health Authority

- Slug: `dha`
- Region: Middle East
- Scope: United Arab Emirates (Dubai)
- Raw staging: `data/raw/middle_east/united_arab_emirates/dubai_health_authority`

## Purpose
Dubai licensing portal enumerating professionals, facilities, and license classes.

## Access Snapshot
ASP.NET service ProfessionalSearchService.svc/GetProfessionals with throttling.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/middle_east/united_arab_emirates/dubai_health_authority`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
