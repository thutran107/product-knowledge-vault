---
type: concept
title: "Configuration vs Permission Model"
source_count: 2
last_updated: 2026-04-20
tags: [integration-hub, permissions, architecture, access-control]
---

## Definition
The architectural principle that separates integration setup (owned by the Integration Hub) from access control (enforced by individual Anduin apps). You configure integrations in the Hub, but you grant permissions in each Anduin app separately.

## Key Dynamics
- **Integration Hub** = workspace for selecting, naming, and configuring integrations. Does not enforce permissions itself.
- **Anduin apps** (FundSub, IDM, Data Room) = each enforces its own access rules per object.
- **Flow**: Install integration in Hub → Hub shows a list of accessible Anduin objects → user opens each object → grants permission in that app's Settings > Integrations → returns to Hub where object is now "Linked."
- A user can only configure integrations for objects they are permitted to access in the underlying app.
- If a target object (e.g., fund) is not listed, the user must either get admin access or have an admin grant permission from within the Anduin app.

## Evidence & Examples
- FundSub: Settings > Integrations → add integration name to fund.
- IDM: Settings > Integrations → add integration name to firm.
- Data Room: permission management is "TBD" per current docs.
- Neuberger Berman deployment required navigating multi-fund permissions across a large portfolio.

## Tensions & Open Questions
- Data Room permission management is unresolved/TBD.
- External consultants (Members) need the same permission flow — they must be invited first, then granted access to relevant objects.

## Related
- [[wiki/concepts/user-roles|User Roles]] — who can grant permissions.
- [[wiki/products/integration-hub|Integration Hub]]
- [[wiki/products/fundsub|FundSub]], [[wiki/products/investor-data-management|IDM]], [[wiki/products/data-room|Data Room]]
