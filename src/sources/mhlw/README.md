# Ministry of Health Labour and Welfare

- Slug: `mhlw`
- Region: Asia
- Scope: Japan
- Raw staging: `data/raw/asia/japan/ministry_of_health_labour_and_welfare`

## Purpose
Japanese ministry publishing aggregate physician statistics (no per-license rows).

## Access Snapshot
Static PDF/XLS releases converted to CSV for reference.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/asia/japan/ministry_of_health_labour_and_welfare`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
