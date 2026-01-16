# Medical and Dental Council of Nigeria

- Region: Africa
- Country: Nigeria
- Coverage: Registry exists but limited

## Access
- URL: https://portal.mdcngov.ng/verify
- Access method: Form submission calling `/api/Practitioner/Verify`
- Recommended rate limit: 1 request every 3 seconds; manual CAPTCHA solving
- Authentication: reCAPTCHA token plus verification code

## Legal & Compliance
- Reference: https://www.mdcngov.ng/privacy-policy/
- Notes: Nigerian privacy policy restricts reuse without consent.

## Implementation Notes
- Capture license category and validity
- Record evidence of consent for automation
- Track outages and needed manual interventions
