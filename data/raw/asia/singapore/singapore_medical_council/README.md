# Singapore Medical Council

- Region: Asia
- Country: Singapore
- Coverage: Excellent national register

## Access
- URL: https://prs.moh.gov.sg/prs/internet/profSearch/mcPractitionerSearch.action
- Access method: POST form returning HTML table; parse with BeautifulSoup
- Recommended rate limit: 1 request per second; respect MOH monitoring
- Authentication: None

## Legal & Compliance
- Reference: https://www.moh.gov.sg/terms-of-use
- Notes: Reuse only for verification; cite SMC and MOH.

## Implementation Notes
- Capture practice place type and register category
- Track conditional registrations
- Localize timezone for updated_at field
