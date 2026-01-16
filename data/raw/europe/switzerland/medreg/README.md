# MedReg

- Region: Europe
- Country: Switzerland
- Coverage: Very good national coverage

## Access
- URL: https://www.medregom.admin.ch/CRS/
- Access method: Public REST API `api/Medreg/v1/persons` returning JSON
- Recommended rate limit: 2 requests per second; follow `X-RateLimit-Remaining` headers
- Authentication: API key optional; anonymous allowed with lower quotas

## Legal & Compliance
- Reference: https://www.admin.ch/gov/en/start/terms-and-conditions.html
- Notes: Swiss federal terms demand attribution and forbid misuse.

## Implementation Notes
- Capture canton codes
- Persist multilingual descriptions
- Track professional card numbers
