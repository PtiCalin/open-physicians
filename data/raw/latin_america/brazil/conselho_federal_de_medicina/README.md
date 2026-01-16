# Conselho Federal de Medicina

- Region: Latin America
- Country: Brazil
- Coverage: Good national coverage

## Access
- URL: https://portal.cfm.org.br/busca-medicos/
- Access method: AJAX search hitting `/wp-admin/admin-ajax.php?action=buscar_medicos`
- Recommended rate limit: 1 request per second; abide by robots.txt
- Authentication: None

## Legal & Compliance
- Reference: https://portal.cfm.org.br/termos-de-uso/
- Notes: Brazilian LGPD applies; cite CFM and honor opt-outs.

## Implementation Notes
- Capture CRM number and UF (state)
- Store specialty board recognition
- Track consent status for publishing contact info
