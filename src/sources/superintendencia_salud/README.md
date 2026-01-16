# Superintendencia de Salud

- Slug: `superintendencia_salud`
- Region: Latin America
- Scope: Chile
- Raw staging: `data/raw/latin_america/chile/superintendencia_de_salud`

## Purpose
Chilean regulator providing XLS downloads per profession.

## Access Snapshot
Download XLS registers listed on supersalud.gob.cl.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/latin_america/chile/superintendencia_de_salud`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
