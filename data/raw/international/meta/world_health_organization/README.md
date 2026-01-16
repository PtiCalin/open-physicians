# World Health Organization

- Region: International
- Country: International
- Coverage: Workforce density and macro indicators

## Access
- URL: https://ghoapi.azureedge.net/api/
- Access method: REST API for Global Health Observatory datasets
- Recommended rate limit: 100 requests per minute default quota
- Authentication: None

## Legal & Compliance
- Reference: https://www.who.int/about/policies/privacy
- Notes: Use data consistent with WHO open license and cite WHO.

## Implementation Notes
- Pull physician density indicators per country
- Store metadata describing indicator codes
- Join to canonical country table for analytics
