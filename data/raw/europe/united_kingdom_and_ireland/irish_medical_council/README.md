# Irish Medical Council

- Region: Europe
- Country: Ireland
- Coverage: Excellent national register

## Access
- URL: https://www.medicalcouncil.ie/public-information/check-the-register/
- Access method: AJAX request to `/RegisterSearch/api/Doctors` returning JSON
- Recommended rate limit: 1 request per second; avoid parallel pagination
- Authentication: None, but requires anti-forgery token extracted from landing page

## Legal & Compliance
- Reference: https://www.medicalcouncil.ie/footer/terms-conditions/
- Notes: Terms permit verification use; redistribution must cite Medical Council.

## Implementation Notes
- Persist anti-forgery token per run
- Capture registration division and specialty
- Track voluntary withdrawal notices
