# Danish Patient Safety Authority

- Slug: `danish_patient_safety_authority`
- Region: Europe
- Scope: Denmark
- Raw staging: `data/raw/europe/nordic/danish_patient_safety_authority`

## Purpose
Danish authorization register accessible via OData JSON endpoints.

## Access Snapshot
/api/Authorisation with API key support and Retry-After headers.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/nordic/danish_patient_safety_authority`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
