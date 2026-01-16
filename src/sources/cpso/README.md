# College of Physicians and Surgeons of Ontario

- Slug: `cpso`
- Region: North America
- Scope: Ontario, Canada
- Raw staging: `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_ontario`

## Purpose
Ontario regulator with JSON search endpoint providing CPSO numbers and status.

## Access Snapshot
POST to GetDoctors JSON endpoint; anti-bot headers required.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_ontario`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
