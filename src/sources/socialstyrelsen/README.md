# Socialstyrelsen

- Slug: `socialstyrelsen`
- Region: Europe
- Scope: Sweden
- Raw staging: `data/raw/europe/nordic/socialstyrelsen`

## Purpose
Swedish register accessible through JSON search, including authorization types.

## Access Snapshot
POST to /api/search returning paginated JSON arrays.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/nordic/socialstyrelsen`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
