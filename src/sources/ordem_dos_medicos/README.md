# Ordem dos Medicos

- Slug: `ordem_dos_medicos`
- Region: Europe
- Scope: Portugal
- Raw staging: `data/raw/europe/portugal/ordem_dos_medicos`

## Purpose
Portuguese order with form-based lookup returning HTML records.

## Access Snapshot
GET/POST workflows under /ver-medico/ with query params.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/portugal/ordem_dos_medicos`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
