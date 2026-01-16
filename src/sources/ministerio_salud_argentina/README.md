# Ministerio de Salud Argentina

- Slug: `ministerio_salud_argentina`
- Region: Latin America
- Scope: Argentina
- Raw staging: `data/raw/latin_america/argentina/ministerio_de_salud_argentina`

## Purpose
Argentinian REFEPS dataset accessible via authenticated API.

## Access Snapshot
SOAP/REST hybrid requiring API key and token refresh.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/latin_america/argentina/ministerio_de_salud_argentina`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
