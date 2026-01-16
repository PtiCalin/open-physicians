# Conselho Federal de Medicina

- Slug: `cfm`
- Region: Latin America
- Scope: Brazil
- Raw staging: `data/raw/latin_america/brazil/conselho_federal_de_medicina`

## Purpose
Brazilian federal council offering AJAX search returning CRM numbers.

## Access Snapshot
WP admin-ajax buscar_medicos endpoint with JSON payloads.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/latin_america/brazil/conselho_federal_de_medicina`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
