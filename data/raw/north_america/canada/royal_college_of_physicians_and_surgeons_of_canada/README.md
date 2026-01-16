# Royal College of Physicians and Surgeons of Canada

- Region: North America
- Country: Canada
- Coverage: Excellent certification coverage (non-licensing)

## Access
- URL: https://www.royalcollege.ca/rcsite/specialty-certification/certified-specialist-directory-e
- Access method: POST search form returning HTML tables; parse with BeautifulSoup
- Recommended rate limit: 1 request per second; pause 10 seconds per 100 results
- Authentication: None

## Legal & Compliance
- Reference: https://www.royalcollege.ca/rcsite/terms-and-conditions-e
- Notes: Directory may only confirm certification status; include attribution.

## Implementation Notes
- Use certification data as join table, not licensing authority
- Capture specialty, subspecialty, and certification year
- Flag entries for revalidation when specialty list changes
