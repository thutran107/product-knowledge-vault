---
type: concept
title: "Integration Patterns"
source_count: 7
last_updated: 2026-04-20
tags: [integration-hub, patterns, order-creation, data-retrieval, document-retrieval]
---

## Definition
The three standard workflow types available in the Integration Hub, each named with a consistent suffix on the Integration Card. The suffix tells users and CSMs the direction and nature of the data flow at a glance.

## Key Dynamics

### 1. Order Creation (`<CRM> (Order creation)`)
- **Direction**: CRM → FundSub
- **What it does**: Reads investor data from a CRM when a trigger fires, creates a subscription order in FundSub, prefills the form, and sends an investor invitation email.
- **Supported CRMs**: DealCloud, Affinity (others likely exist)
- **Trigger mechanism**: a configurable field + value on a CRM record; check frequency is configurable (DealCloud) or event-driven (Affinity).
- **Form prefill**: uses Import Templates (ASA or Custom) to map CRM fields → FundSub fields.

### 2. Data Retrieval (`<System> (Data retrieval)`)
- **Direction**: FundSub or Data Room → CRM/External System
- **What it does**: Pushes data from Anduin into an external system when a trigger fires (e.g., subscription status change or investor activity event).
- **Two sub-types**:
  - *Subscription data*: FundSub → CRM (e.g., DealCloud Data retrieval). Triggered by subscription status.
  - *Engagement data*: Data Room → CRM (e.g., DealCloud Data Room alert). Triggered by investor activity events.
- **Templates**: Export Templates (ASA, Self-service, or Custom) define data points.

### 3. Document Retrieval (`<System> (Document retrieval)`)
- **Direction**: FundSub → Document Storage
- **What it does**: Transfers completed subscription and supporting documents to a customer's storage system in organized folder structures.
- **Supported storage**: Box (others likely exist, e.g., SFTP)
- **Self-configured**: customers supply their own credentials.

## Evidence & Examples
- **Salesforce**: all three patterns — Order Creation, Data Retrieval, Document Retrieval (most complete CRM integration).
- **DealCloud**: all three patterns — Order Creation, Data Retrieval (subscription), Data Retrieval (Data Room).
- **Affinity**: Order Creation only (as of current sources).
- **Box**: Document Retrieval only.
- Integration Card naming convention is used in the IH Implementation Guide as a training aid for CSMs.
- "Dummy cards" also exist — logo-only cards that collect interest before an integration is built.

## Tensions & Open Questions
- Salesforce supports all three patterns (per Sales Deck). Affinity Data Retrieval not yet documented — does it exist?
- Data Room permission management for Integration Hub listed as "TBD."

## Related
- [[concepts/investor-onboarding-workflow|Investor Onboarding Workflow]] — uses Order Creation.
- [[concepts/import-export-templates|Import/Export Templates]] — defines what data flows.
- [[entities/dealcloud|DealCloud]], [[entities/affinity|Affinity]], [[entities/box|Box]]
