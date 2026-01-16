# Danish Patient Safety Authority

- Region: Europe
- Country: Denmark
- Coverage: Excellent national coverage

## Access
- URL: https://autregweb.sst.dk/
- Access method: JSON endpoint `/api/Authorisation` paginated via OData
- Recommended rate limit: 2 requests per second; respect `Retry-After`
- Authentication: API key issued via open data portal recommended

## Legal & Compliance
- Reference: https://stps.dk/en/about-this-website/
- Notes: Reuse permitted if crediting Danish Patient Safety Authority.

## Implementation Notes
- Capture authorization type and validity
- Map municipality codes to ISO-3166-2
- Store Danish characters in UTF-8
