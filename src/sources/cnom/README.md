# Conseil National de l'Ordre des Medecins

- Slug: `cnom`
- Region: Europe
- Scope: France
- Raw staging: `data/raw/europe/france/conseil_national_de_l_ordre_des_medecins`

## Purpose
French regulator exposing RPPS identifiers, addresses, and specialties via GraphQL.

## Access Snapshot
GraphQL POST requests to /graphql with session cookie + CSRF token.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/france/conseil_national_de_l_ordre_des_medecins`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
