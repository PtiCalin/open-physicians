# Federation of State Medical Boards

- Slug: `fsmb`
- Region: North America
- Scope: United States (index)
- Raw staging: `data/raw/north_america/united_states/federation_of_state_medical_boards`

## Purpose
National index of US state boards powering downstream per-state jobs.

## Access Snapshot
Static HTML directory; scrape board metadata and contact info.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/north_america/united_states/federation_of_state_medical_boards`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
