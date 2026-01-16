# Dubai Health Authority

- Region: Middle East
- Country: United Arab Emirates
- Coverage: Good but fragmented

## Access
- URL: https://services.dha.gov.ae/en/Pages/ProfessionalSearch.aspx
- Access method: ASP.NET form posting to `ProfessionalSearchService.svc/GetProfessionals`
- Recommended rate limit: 1 request every 2 seconds; DHA blocks faster traffic
- Authentication: Requires session cookie and hidden viewstate tokens

## Legal & Compliance
- Reference: https://www.dha.gov.ae/en/Pages/PrivacyPolicy.aspx
- Notes: DHA policy prohibits unauthorized commercial reuse; seek approval for automation.

## Implementation Notes
- Capture license type, facility, and expiration
- Store emirate/location metadata
- Coordinate with DOH Abu Dhabi job to dedupe
