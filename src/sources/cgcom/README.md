# Organizacion Medica Colegial

- Slug: `cgcom`
- Region: Europe
- Scope: Spain
- Raw staging: `data/raw/europe/spain/organizacion_medica_colegial`

## Purpose
Spanish national council integrating provincial colegiados lists.

## Access Snapshot
Province-specific HTML/CSV endpoints; requires sequential access.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/spain/organizacion_medica_colegial`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
