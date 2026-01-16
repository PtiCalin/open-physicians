# College of Physicians and Surgeons of Alberta

- Region: North America
- Country: Canada
- Coverage: Excellent, provincial but consistent

## Access
- URL: https://search.cpsa.ca/PhysicianSearch
- Access method: AJAX search returning JSON blocks via /PhysicianSearch/Lookup
- Recommended rate limit: 1 request every 2 seconds; obey Retry-After headers
- Authentication: Anonymous; maintain ASP.NET session cookie

## Legal & Compliance
- Reference: https://cpsa.ca/privacy-terms/
- Notes: Use data only for transparency purposes; cite CPSA as source.

## Implementation Notes
- Fetch alphabetically to avoid server throttling
- Track practice location coordinates when present
- Ensure inactive records remain for longitudinal audits
