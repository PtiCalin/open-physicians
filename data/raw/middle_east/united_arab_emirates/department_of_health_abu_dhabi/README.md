# Department of Health Abu Dhabi

- Region: Middle East
- Country: United Arab Emirates
- Coverage: Good but fragmented

## Access
- URL: https://www.doh.gov.ae/en/Professionals/Healthcare-Professionals/Licensing
- Access method: Shafaf portal REST API `/api/publicsearch` with JSON pagination
- Recommended rate limit: 1 request per second; API includes explicit quota headers
- Authentication: API key issued upon request for higher limits

## Legal & Compliance
- Reference: https://www.doh.gov.ae/en/terms-and-conditions
- Notes: Terms require prior written consent for automated collection.

## Implementation Notes
- Coordinate with DHA dataset for UAE-wide dedupe
- Capture facility affiliations
- Track data lineage for FOI compliance
