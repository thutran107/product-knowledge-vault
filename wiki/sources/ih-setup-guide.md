---
type: source
title: "IH Setup Guide — How to Set Up the Integration Hub Platform"
date_ingested: 2026-05-11
as_of_date: 2026-04-01
source_type: implementation-guide
trust_level: 2
original_file: notion://2153f653-b1df-80b1-895e-e2a518c98b11
products: [Integration Hub]
target_audience: All teams
onboarding_required: Yes
tags: [integration-hub, onboarding, implementation]
---

## Summary
Step-by-step playbook for CS to provision, configure, enable premium integrations, and monitor the Integration Hub for a customer. As of April 2026 — most current setup reference.

## Key Takeaways
- **Granting access (3 steps)**:
  1. In Admin Tool → Entities → select customer → Change settings → confirm no domains listed.
  2. Add customer's email domain (e.g., `eqt.com`) — all users with that domain share one Hub.
  3. If customers need CS help: invite CS support email from Hub's Members tab.
- **Customer URLs**: US: `https://integrations.anduin.app/` | UK: `https://integrations.eu.anduin.app/`
- **Note**: Anduin plans to automatically assign email domains to all existing customers — removing need for manual provisioning.
- **Enabling paid/premium integrations**: Admin Tool → Integration Platform → find Entity → Manage Integration → Edit → set Quota (e.g., 10) → save. Setting Quota back to 0 disables.
- **Learning materials for customers**: encourage them to use the "View setup guide" button within each integration card in the Hub UI.
- **Integration card suffixes**: Order creation = CRM data → FundSub order; Data retrieval = Anduin → CRM; Document retrieval = Anduin docs → CRM.
- **Configuration**: customers are expected to self-configure each integration; Anduin or external consultants can be invited as members.
- **Monitoring**: Monitor tab → Execution → filter by date/time for troubleshooting failed runs.

## Connections
- [[wiki/products/integration-hub]] — operational setup for this product
- [[wiki/sources/ih-knowledge-hub]] — reference for what integrations are available
- [[wiki/sources/ih-intro-overview]] — conceptual overview that complements this setup guide

## Conflicts & Supersessions
- No conflicts. Adds CS provisioning steps not covered in existing implementation guides.
- **Upcoming change flagged**: automatic domain assignment to all customers — once live, Steps 1–2 may become unnecessary for new customers.

## Raw Notes
- Admin portal Integration Platform tab contact for access: referenced internal user ID.
- Each integration card for the Hub includes external setup documentation linked from within the UI.
- Public developer docs: https://developers.anduintransact.com/docs/introduction-1
