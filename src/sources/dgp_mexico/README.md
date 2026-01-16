# Direccion General de Profesiones

- Slug: `dgp_mexico`
- Region: North America
- Scope: Mexico
- Raw staging: `data/raw/north_america/mexico/direccion_general_de_profesiones`

## Purpose
Mexican federal license lookup for cedula-professional mapping.

## Access Snapshot
cedulaprof portal with reCAPTCHA-protected JSON responses.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/north_america/mexico/direccion_general_de_profesiones`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
