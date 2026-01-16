# Ministerio de Salud Argentina

- Region: Latin America
- Country: Argentina
- Coverage: Good national coverage

## Access
- URL: https://sisa.msal.gov.ar/sisa/
- Access method: SOAP-like API for Registro Federal de Profesionales de la Salud (REFEPS)
- Recommended rate limit: 1 request per second; tokens expire every 30 minutes
- Authentication: Requires API key tied to institutional agreement

## Legal & Compliance
- Reference: https://www.argentina.gob.ar/aviso-legal
- Notes: National transparency rules still require attribution and lawful use.

## Implementation Notes
- Store REFEPS IDs and province codes
- Capture specialty authorizations
- Track contract requirements for API key renewal
