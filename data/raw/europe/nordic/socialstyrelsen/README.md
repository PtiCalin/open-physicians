# Socialstyrelsen

- Region: Europe
- Country: Sweden
- Coverage: Excellent national coverage

## Access
- URL: https://legitimation.socialstyrelsen.se/
- Access method: Form posts to `/api/search` returning JSON arrays
- Recommended rate limit: 1 request per second; throttle heavier during 09:00-17:00 CET
- Authentication: None

## Legal & Compliance
- Reference: https://www.socialstyrelsen.se/om-webbplatsen/anvandningsvillkor/
- Notes: Comply with Swedish PSI licensing and cite Socialstyrelsen.

## Implementation Notes
- Fetch per starting letter to ensure completeness
- Store Swedish titles and normalized English labels
- Monitor API schema version header
