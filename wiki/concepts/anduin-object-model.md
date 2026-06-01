---
type: concept
title: "Anduin Object Model"
source_count: 2
last_updated: 2026-04-20
tags: [architecture, integration-hub, anduin-object]
---

## Definition
The abstraction Anduin uses to refer to connection points across its product suite. An "Anduin Object" is a container of investor data within a specific Anduin product — it is the unit to which integrations are connected and permissions are granted.

## Key Dynamics

| Anduin Product | Object Type | What it contains |
|----------------|-------------|-----------------|
| FundSub | Fund | All subscription information for a fund |
| IDM | Firm | Investor entities, contacts, documents, profile data |
| Data Room | Data Room | Investor document access and activity data |

- Integrations are always scoped to specific Anduin Objects, never org-wide.
- Permissions are granted per object, not per integration type.
- The same integration can be connected to multiple objects (e.g., multiple funds) by creating separate instances or (via upcoming multi-fund feature) a single instance.
- "Integration Card" is the template; an "Integration" (instance) is one activation of that card tied to one or more specific Anduin Objects.

## Evidence & Examples
- A FundSub admin for Acme Fund 1 and Acme Fund 2 can create integrations for both funds, but not for funds they don't have access to.
- Neuberger Berman used objects across FundSub, IDM, and Data Room simultaneously.

## Tensions & Open Questions
- Multi-fund integration (single instance → multiple funds) is on the roadmap but not yet released.
- No documentation yet on whether one integration can span multiple object types simultaneously.

## Related
- [[wiki/concepts/configuration-vs-permission|Configuration vs Permission]]
- [[wiki/products/fundsub|FundSub]], [[wiki/products/investor-data-management|IDM]], [[wiki/products/data-room|Data Room]]
- [[wiki/products/integration-hub|Integration Hub]]
