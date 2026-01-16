# Australian Health Practitioner Regulation Agency

- Slug: `ahpra`
- Region: Oceania
- Scope: Australia
- Raw staging: `data/raw/oceania/australia/australian_health_practitioner_regulation_agency`

## Purpose
Australian regulator with JSON practitioner search covering conditions and scopes.

## Access Snapshot
POST to /api/PractitionerSearch with pagination.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/oceania/australia/australian_health_practitioner_regulation_agency`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
