---
type: source
title: "Integration Hub Implementation Guide (Internal CS Playbook)"
date_ingested: 2026-04-20
as_of_date: undated
source_type: implementation-guide
trust_level: 2
original_file: raw/Integration Hub Implementation Guide.md
products: [Integration Hub]
target_audience: CS
onboarding_required: Yes
tags: [integration-hub, implementation, cs-playbook, internal]
---

## Summary
Internal Customer Success playbook for rolling out the Integration Hub to customers. Covers granting access, learning materials, enabling paid integrations, configuration support, and monitoring/troubleshooting.

## Key Takeaways
- **Access granting**: done via Admin Tool → Entities → Change settings → add customer email domain.
- Domain-based access: anyone with the registered domain shares the same Hub.
- US URL: `https://integrations.anduin.app/` | UK URL: `https://integrations.eu.anduin.app/`
- Anduin support can be invited as a Member to assist directly in customer's Hub.
- Integration card suffixes convey the pattern: "Order creation" / "Data retrieval" / "Document retrieval."
- **Premium/paid integrations**: enabled via Admin Tool → Integration Platform → select entity → Manage Integration → set Quota.
- Quota = max instances allowed; Deployed = instances already installed. Set Quota to 0 to disable.
- Monitoring: Integration Hub has a Monitor → Execution tab showing all successful and failed runs with date/time filters.
- Upcoming change: automatic domain assignment to all existing customers (no manual step needed in future).

## Connections
- [[wiki/products/integration-hub|Integration Hub]].
- [[wiki/concepts/crm-integration-playbook|CRM Integration Playbook]].
- [[wiki/concepts/integration-patterns|Integration Patterns]] — card suffix naming convention.
- [[wiki/concepts/user-roles|User Roles]] — Member invite flow.

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- Internal note: access to "Entities" and "Integration Platform" tabs in Admin Tool requires specific permissions — contact @Duc Tam Nguyen if missing.
- Customers are expected to self-configure; Anduin support can be invited if they get stuck.
