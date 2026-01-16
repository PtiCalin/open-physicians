# Federazione Nazionale degli Ordini dei Medici

- Slug: `fnomceo`
- Region: Europe
- Scope: Italy
- Raw staging: `data/raw/europe/italy/federazione_nazionale_degli_ordini_dei_medici`

## Purpose
Italian federation exposing provincial order data through JSON APIs.

## Access Snapshot
POST to /wp-json/fnomceo/v1/medici with nonce header.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/italy/federazione_nazionale_degli_ordini_dei_medici`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
