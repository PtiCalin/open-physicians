# Royal College of Physicians and Surgeons of Canada

- Slug: `rcpsc`
- Region: North America
- Scope: Canada (certification)
- Raw staging: `data/raw/north_america/canada/royal_college_of_physicians_and_surgeons_of_canada`

## Purpose
Certification directory used as specialty join table rather than licensing authority.

## Access Snapshot
HTML form returning tables; parse via BeautifulSoup or lxml.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/north_america/canada/royal_college_of_physicians_and_surgeons_of_canada`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
