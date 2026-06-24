---
type: concept
title: "Import/Export Templates"
source_count: 4
last_updated: 2026-04-20
tags: [templates, data-management, import, export, integration]
---

## Definition
Templates are predefined sets of data points that govern how data moves between external systems and Anduin. Import Templates define what external data Anduin ingests (for form prefill); Export Templates define what Anduin data is sent out (post-subscription).

## Key Dynamics

### Import Templates (external → Anduin)
Used in **Order Creation** integrations to prefill FundSub subscription forms.

| Type | Description | Who creates |
|------|-------------|-------------|
| Anduin Standard Alias (ASA) | Limited, standardized set of data points | Anduin |
| Custom Template | Unlimited fields, complex computation supported | Anduin (in collaboration with customer) |

### Export Templates (Anduin → external)
Used in **Data Retrieval** integrations to push subscription data to CRM or other systems.

| Type | Description | Who creates |
|------|-------------|-------------|
| Anduin Standard Alias (ASA) | Limited, standardized set of data points | Anduin |
| Self-service Template | Customer-configurable via FundSub UI — pick and choose fields | Customer (self-service) |
| Custom Template | Unlimited fields, complex computation | Anduin (in collaboration with customer) |

- Self-service Export Template is available now; self-service Import Template is not yet supported.
- Templates must be set up before integration configuration — they are a prerequisite.
- The "Data" and "Export template" tasks in integration pre-setup checklists are owned by Anduin.

## Evidence & Examples
- DealCloud Order Creation and Affinity Order Creation both use Import Templates (ASA or Custom).
- DealCloud Data Retrieval uses Export Templates (ASA, Self-service, or Custom).
- Neuberger Berman developed a data standard via Anduin collaboration as part of their IDM deployment.

## Tensions & Open Questions
- Self-service Import Templates not yet available — customers must involve Anduin for all import template setup.
- Complex transformations (non-1-to-1 mapping) require Custom Templates built with Anduin.
- UI currently supports 1-to-1 field mapping only in the integration configuration screen.

## Related
- [[concepts/data-mapping|Data Mapping]]
- [[concepts/integration-patterns|Integration Patterns]]
- [[products/fundsub|FundSub]]
