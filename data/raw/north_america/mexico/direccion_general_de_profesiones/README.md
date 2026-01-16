# Direccion General de Profesiones

- Region: North America
- Country: Mexico
- Coverage: Partial; national professional license lookup

## Access
- URL: https://www.gob.mx/cedulaprof
- Access method: Browser automation posting CURP/name to cedula lookup JSON endpoint
- Recommended rate limit: 1 request every 3 seconds; portal throttles bursts
- Authentication: Requires reCAPTCHA token; integrate manual solving queue

## Legal & Compliance
- Reference: https://www.gob.mx/terminos
- Notes: Federal portal terms restrict commercial resale and mandate attribution.

## Implementation Notes
- Store raw JSON payloads per query
- Maintain mapping between cedula number and physician_id
- Document CAPTCHA solving cost and throughput
