# Medical Council of Hong Kong

- Slug: `mchk`
- Region: Asia
- Scope: Hong Kong
- Raw staging: `data/raw/asia/hong_kong/medical_council_of_hong_kong`

## Purpose
Hong Kong council distributing XLS register exports for manual parsing.

## Access Snapshot
Downloadable XLS/PDF register refreshed monthly.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/asia/hong_kong/medical_council_of_hong_kong`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
