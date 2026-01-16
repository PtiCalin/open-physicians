# Medical Council of New Zealand

- Region: Oceania
- Country: New Zealand
- Coverage: Excellent national coverage

## Access
- URL: https://www.mcnz.org.nz/registration/list-of-registered-doctors/
- Access method: Search interface with JSON endpoint `/umbraco/api/register/search`
- Recommended rate limit: 1 request per second; comply with NZST quiet hours
- Authentication: None

## Legal & Compliance
- Reference: https://www.mcnz.org.nz/privacy/
- Notes: Respect MCNZ privacy statement and include attribution.

## Implementation Notes
- Capture scope of practice and vocational status
- Save registration number and expiry
- Monitor site for structural changes after 2024 redesign
