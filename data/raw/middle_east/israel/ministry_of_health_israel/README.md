# Ministry of Health Israel

- Region: Middle East
- Country: Israel
- Coverage: Good but fragmented

## Access
- URL: https://practitioners.health.gov.il/Practitioners/
- Access method: SPA calling `/api/Practitioner` REST endpoints
- Recommended rate limit: 1 request per second; site enforces throttling via gateway
- Authentication: None, but requires Hebrew locales in headers

## Legal & Compliance
- Reference: https://www.gov.il/en/terms-of-use
- Notes: Government ToU require lawful use and prohibit bulk republication without consent.

## Implementation Notes
- Capture license class and issuing office
- Store Hebrew and English transliterations
- Track practitioners lacking public consent flag
