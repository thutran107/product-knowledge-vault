---
type: concept
title: "Investor Onboarding Workflow"
source_count: 4
last_updated: 2026-04-20
tags: [investor-onboarding, fundsub, order-creation, workflow]
---

## Definition
The end-to-end process by which an investor is invited to and completes a subscription in FundSub. The Integration Hub's Order Creation pattern automates the first stage of this workflow using CRM data.

## Key Dynamics

### Manual (baseline)
1. GP manually enters investor data in FundSub to create subscription order.
2. GP sends invitation email.
3. Investor receives blank or partially filled form.
4. Investor fills out, signs, submits.

### Automated via Integration Hub (Order Creation)
1. CRM record reaches configured trigger value (e.g., Fundraise Status = "Due Diligence").
2. Integration Hub reads investor data from CRM via API.
3. FundSub subscription order is created automatically.
4. Form is prefilled with mapped CRM data.
5. Investor invitation email is sent automatically (using First Name, Last Name, Email from CRM).
6. Investor completes only the remaining fields; signs and submits.

### With Collaborators (Affinity)
- Same as above, but the invitation can include a Primary Investor + multiple Collaborators.
- DealCloud Order Creation currently supports Primary Investor only.

### Post-subscription
- Completed subscription data can be synced back to CRM automatically via Data Retrieval integration.
- Documents can be pushed to storage (Box, SFTP) via Document Retrieval integration.

## Evidence & Examples
- Neuberger Berman: ~3,000 LPs onboarded; 90% initiation rate; 78% completion within days.
- DealCloud and Affinity both have Order Creation integrations with slightly different capabilities.

## Tensions & Open Questions
- Affinity supports Collaborators; DealCloud does not (as of current sources).
- Multi-fund integration (single instance → multiple funds) is on the Affinity roadmap.
- Complex prefill requiring transformation logic requires Custom Import Templates built with Anduin.

## Related
- [[concepts/integration-patterns|Integration Patterns]]
- [[concepts/import-export-templates|Import/Export Templates]]
- [[concepts/data-mapping|Data Mapping]]
- [[products/fundsub|FundSub]], [[entities/dealcloud|DealCloud]], [[entities/affinity|Affinity]]
- [[customers/neuberger-berman|Neuberger Berman]]
