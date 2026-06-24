---
type: concept
title: "CRM Integration Playbook"
source_count: 3
last_updated: 2026-04-20
tags: [crm, implementation, playbook, cs-process]
---

## Definition
The standard process Anduin's Customer Success team follows to roll out CRM integrations via the Integration Hub — from access provisioning through monitoring.

## Key Dynamics

### Phase 1: Access Provisioning
1. Open Admin Tool → Entities → select customer entity → Change settings.
2. Add customer email domain → save.
3. Share Hub URL (US: `https://integrations.anduin.app/` | UK: `https://integrations.eu.anduin.app/`).
4. If customer needs help: invite Anduin support as Member via Hub → Members → Invite members.

### Phase 2: Enable Paid Integrations (if applicable)
1. Admin Tool → Integration Platform → find entity → Manage Integration.
2. Set Quota on desired integrations (e.g., "10") to unlock.
3. To disable: set Quota back to 0.

### Phase 3: Pre-Setup Checklist (customer-side)
Standard prerequisites for CRM integrations:
- CRM API key (customer retrieves; Anduin consults).
- CRM object/list preparation (customer creates with Anduin guidance).
- Fund/object access in Anduin (customer sets up with Anduin consultation).
- Data & mapping definition (Anduin leads).
- Import/Export template creation (Anduin leads).

### Phase 4: Customer Self-Configuration
- Customer selects integration card in Hub → follows on-screen prompts.
- Learning materials: "View setup guide" button on each integration card.
- Card suffix tells CS and customer the pattern: Order creation / Data retrieval / Document retrieval.

### Phase 5: Validation
- Customer tests end-to-end by triggering the integration and verifying the outcome.
- E.g., for Order Creation: change CRM record trigger field → verify subscription created in FundSub → verify form prefilled → verify invitation sent.

### Phase 6: Monitoring
- Hub → integration card → Monitor → Execution tab.
- Filter by date/time for troubleshooting.
- View successful and failed runs.

## Evidence & Examples
- IH Implementation Guide describes this entire playbook for Anduin CSMs.
- Neuberger Berman is the flagship example of a full multi-product + integration deployment.

## Tensions & Open Questions
- Pre-setup checklist items owned by Anduin (data mapping, templates) can create dependencies/delays.
- Upcoming automatic domain assignment will eliminate Phase 1 manual provisioning.

## Related
- [[concepts/configuration-vs-permission|Configuration vs Permission]]
- [[concepts/import-export-templates|Import/Export Templates]]
- [[products/integration-hub|Integration Hub]]
