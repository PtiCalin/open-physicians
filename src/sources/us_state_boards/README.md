# United States State Medical Boards

- Slug: `us_state_boards`
- Region: North America
- Scope: United States
- Raw staging: `data/raw/north_america/united_states/state_medical_boards`

## Purpose
Container for state-specific adapters (California, New York, Texas, etc.).

## Access Snapshot
Varies per board: CSV, HTML, PDF, SOAP, or portal logins.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/north_america/united_states/state_medical_boards`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
