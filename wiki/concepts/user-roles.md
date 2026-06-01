---
type: concept
title: "User Roles"
source_count: 2
last_updated: 2026-04-20
tags: [user-roles, access-control, integration-hub]
---

## Definition
The two roles within an Integration Hub: Admin (default for all authenticated Anduin GP users in the same email domain) and Member (external collaborators invited by admins).

## Key Dynamics

| Capability | Admin | Member |
|-----------|-------|--------|
| Create integrations | ✓ | ✓ |
| Modify integrations | ✓ | ✓ |
| Remove integrations | ✓ | ✓ |
| Invite members | ✓ | ✗ |
| Remove members | ✓ | ✗ |

- All users with the same email domain are automatically admins in the same Hub.
- Members are invited by domain email — typically external consultants, IT service providers, or implementation partners.
- Members can be removed by admins at any time.
- Typical lifecycle: Member sets up integrations during implementation → customer admin takes over for ongoing management → Member removed.
- Anduin support staff can also be invited as Members when customers need direct assistance.

## Evidence & Examples
- IH Implementation Guide describes the invite flow: Hub → Members tab → Invite members → add email.
- User Role source explicitly mentions Salesforce support consultants as a Member example.

## Tensions & Open Questions
- No role below Member — no read-only access. Members have near-full admin rights.
- No documented way to restrict Members to specific integrations or objects only.

## Related
- [[wiki/concepts/configuration-vs-permission|Configuration vs Permission]]
- [[wiki/products/integration-hub|Integration Hub]]
