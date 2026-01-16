# OECD

- Region: International
- Country: International
- Coverage: Physician per capita and specialty statistics

## Access
- URL: https://stats.oecd.org/
- Access method: RESTful SDMX queries via `https://stats.oecd.org/SDMX-JSON/data/`
- Recommended rate limit: Unlimited for small pulls; throttle to 10 requests per minute for bulk
- Authentication: None

## Legal & Compliance
- Reference: https://www.oecd.org/termsandconditions/
- Notes: OECD license permits non-commercial reuse with attribution.

## Implementation Notes
- Document SDMX query templates
- Store dataset code, measure, and unit
- Align country codes with ISO alpha-3
