# World Health Organization

- Slug: `who`
- Region: International
- Scope: Global
- Raw staging: `data/raw/international/meta/world_health_organization`

## Purpose
WHO Global Health Observatory indicators for workforce density.

## Access Snapshot
REST API at ghoapi.azureedge.net/api.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/international/meta/world_health_organization`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
