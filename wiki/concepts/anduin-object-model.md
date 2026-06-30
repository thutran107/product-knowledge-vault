---
type: concept
title: "Anduin Object Model"
source_count: 3
last_updated: 2026-06-30
tags: [architecture, integration-hub, anduin-object, idm]
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

### IDM internal object model (fund side)
Within the IDM Firm object, the fund/capital side is itself a four-object chain — "subscriptions onboard, FLEs hold, investments relate, transactions move":

| Object | Role |
|--------|------|
| **Fund subscription** | Onboarding/intake container (paperwork + investor experience). One subscription can feed multiple FLEs. |
| **Fund legal entity (FLE)** | Legal boundary that holds capital and positions; day-to-day operations. |
| **Investment** | Links exactly one investor to one FLE — the linchpin; transactions cannot exist without it. |
| **Transaction** | Records money movement (6 types); always a child of an investment. |
| **Fund family** | Optional umbrella grouping FLEs for aggregated views. |

On the investor side the hierarchy is **firm → client group → investment entity → fund legal entity → transaction**, with custom-ID support at the client and IE levels (the API contract — see [[features/idm-public-api]]). The investment object is the bridge between the client side and the fund side. See [[features/idm-funds-tab]].

## Evidence & Examples
- A FundSub admin for Acme Fund 1 and Acme Fund 2 can create integrations for both funds, but not for funds they don't have access to.
- Neuberger Berman used objects across FundSub, IDM, and Data Room simultaneously.
- A family trust subscribing onshore to Magma Property Fund 3 creates a Delaware FLE investment; a capital call becomes a child transaction of that investment ([[sources/idm-funds-tab-training-video]]).

## Tensions & Open Questions
- Multi-fund integration (single instance → multiple funds) is on the roadmap but not yet released.
- No documentation yet on whether one integration can span multiple object types simultaneously.

## Related
- [[concepts/configuration-vs-permission|Configuration vs Permission]]
- [[products/fundsub|FundSub]], [[products/investor-data-management|IDM]], [[products/data-room|Data Room]]
- [[products/integration-hub|Integration Hub]]
- [[features/idm-funds-tab]], [[features/idm-public-api]]
