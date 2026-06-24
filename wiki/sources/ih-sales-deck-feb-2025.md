---
type: source
title: "Integration Hub Sales Deck (Feb 2025)"
date_ingested: 2026-04-20
as_of_date: 2025-02-01
source_type: sales-deck
trust_level: 5
original_file: raw/Integration Hub Sales Deck.pdf
products: [Integration Hub, FundSub, Data Room, IDM]
target_audience: Sales + RM
onboarding_required: No
tags: [integration-hub, sales, positioning, use-cases]
---

## Summary
The Feb 2025 external-facing sales deck for the Integration Hub. Covers positioning, value propositions, three popular use cases (Salesforce, DealCloud, file storage), feature highlights, and the Hub provisioning roadmap. Contains significant details not in other sources.

## Key Takeaways

### Positioning
- Tagline: "Discover the power of simplicity: a single gateway to all your app integrations."
- "A centralized place for no-code integrations compatible with leading apps and embedded within the Anduin platform."
- 20+ app integrations available; continuously adding new direct integrations.
- DealCloud integration launched as part of the Integration Hub.

### Three Adoption Pillars
1. **Anyone can set up** — no coding required, ideal for teams with little/no dev resources.
2. **Faster time to value** — pre-built templates and intuitive setup wizard for self-serve.
3. **Scale with complexity** — customization services for advanced needs.

### Three Setup Steps
1. Access → browse target apps in Hub.
2. Install → select use case, configure with wizard.
3. Test and deploy → end-to-end testing, then production.

### Anduin Offers
- Implementation support
- Standardized integration flows
- Customization services

### Popular Use Cases
1. **Salesforce** — full bidirectional flow: Order Creation (SF → FundSub) + Data Retrieval (FundSub → SF) + Document Retrieval (FundSub → SF). GPs log into Salesforce → create order → prefill subscription → send invitation → LP accesses pre-filled form → data synced back on completion.
2. **DealCloud** — bidirectional sync. Implementation requirements: Publication API must be enabled; unique DealCloud ID required; target object must exist in DealCloud for receiving Anduin data.
3. **File storages** — automates document retrieval process (Box, SFTP implied).

### Feature Highlights
- **Hub discoverability**: hooks at touch points in FundSub, Data Room, IDM; public landing page.
- **Integration cards**: two types — (1) Operational cards (ready to configure) and (2) Dummy cards (logos displayed to collect interest/requests before the integration is built).
- **Card details page**: self-service materials, overview, docs link, deploy instance (self-deploy or contact-us), monitor existing instances.
- **Instance deployment**: powered by Prismatic (underlying integration platform).

### Hub Provisioning Roadmap
- **Current**: one Hub per entity email domain; Anduin manually provisions.
- **Jan 2025 enhancement**: more flexibility, separate views per entity within shared Hub.
- **Mar 2025 (tentative)**: different orgs sharing the same Integration Hub.

## Connections
- [[products/integration-hub|Integration Hub]] — primary subject.
- [[entities/salesforce|Salesforce]] — now has documented full use case.
- [[entities/dealcloud|DealCloud]] — implementation requirements confirmed.
- [[concepts/integration-patterns|Integration Patterns]] — all three patterns shown for Salesforce.
- [[concepts/crm-integration-playbook|CRM Integration Playbook]] — three-step setup flow.
- [[concepts/anduin-object-model|Anduin Object Model]] — provisioning model evolution.

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- Prismatic is the underlying integration platform (not previously documented).
- "Dummy cards" concept is key for product roadmap communication — shows logos before integrations are built to gauge demand.
- Salesforce use case is more fully documented here than anywhere else in current sources.
- Public landing page exists — Hub is not purely internal-only.
