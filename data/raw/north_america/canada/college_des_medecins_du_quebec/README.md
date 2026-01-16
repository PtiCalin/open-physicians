# College des medecins du Quebec

- Region: North America
- Country: Canada
- Coverage: Excellent, provincial but consistent

## Access
- URL: https://www.cmq.org/bottin?sc_lang=en
- Access method: Public searchable register with CSV export after accepting terms
- Recommended rate limit: 1 request per second; sleep 5 seconds between CSV pulls
- Authentication: Session cookie stored after accepting legal notice

## Legal & Compliance
- Reference: https://www.cmq.org/en/a-propos/politique-du-site-web.aspx
- Notes: Respect CMQ website policy and attribute CMQ as the source.

## Implementation Notes
- Store daily CSV snapshots as cmq_YYYYMMDD.csv
- Log download metadata in data/metadata/scrape_log.csv
- Monitor CMQ news feed for schema revisions
