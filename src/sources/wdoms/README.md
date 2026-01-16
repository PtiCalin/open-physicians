# World Directory of Medical Schools

- Slug: `wdoms`
- Region: International
- Scope: Global
- Raw staging: `data/raw/international/meta/world_directory_of_medical_schools`

## Purpose
School-level directory for training provenance joins.

## Access Snapshot
search.wdoms.org GraphQL API (token required for bulk).

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/international/meta/world_directory_of_medical_schools`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
