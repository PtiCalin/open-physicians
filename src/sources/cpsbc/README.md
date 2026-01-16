# College of Physicians and Surgeons of British Columbia

- Slug: `cpsbc`
- Region: North America
- Scope: British Columbia, Canada
- Raw staging: `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_british_columbia`

## Purpose
BC regulator with JSON-backed directory containing status history.

## Access Snapshot
Form POST hitting /physician_directory/search returning JSON pages.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_british_columbia`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
