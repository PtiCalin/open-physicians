# College of Physicians and Surgeons of Alberta

- Slug: `cpsa`
- Region: North America
- Scope: Alberta, Canada
- Raw staging: `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_alberta`

## Purpose
Alberta regulator exposing AJAX lookup results with practice locations.

## Access Snapshot
AJAX calls to /PhysicianSearch/Lookup requiring ASP.NET session.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_alberta`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
