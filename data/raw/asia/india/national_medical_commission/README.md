# National Medical Commission

- Region: Asia
- Country: India
- Coverage: Improving; national register with occasional outages

## Access
- URL: https://www.nmc.org.in/MCIRest/verifyDetails
- Access method: REST endpoint taking registration number or name returning JSON
- Recommended rate limit: 1 request per second; throttle lower due to server instability
- Authentication: None but requires CAPTCHA token per session

## Legal & Compliance
- Reference: https://www.nmc.org.in/terms-of-use
- Notes: Usage subject to Indian IT Act; cite NMC and avoid data resale.

## Implementation Notes
- Rotate IPs to mitigate throttling
- Store CAPTCHA solving logs
- Normalize state medical council codes
