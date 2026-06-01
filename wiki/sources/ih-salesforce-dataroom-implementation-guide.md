---
type: source
title: "Automated Onboarding to Data Room from Salesforce (Implementation Guide)"
date_ingested: 2026-05-11
as_of_date: undated
source_type: implementation-guide
trust_level: 2
original_file: raw/notion-fetch
products: [Integration Hub]
target_audience: CS, Sales + RM
onboarding_required: No
tags: [integration-hub, salesforce, data-room, implementation, #integration]
---

## Summary
Full internal CS rollout guide for the Salesforce → Data Room automated onboarding integration. Covers prerequisites on both the Salesforce and Anduin sides, a 6-step CS rollout process, and external materials to share with customers.

## Key Takeaways
- **Purpose:** Let fund managers invite investors to Data Room directly from Salesforce with a single click — eliminates manual data entry and errors
- **Direction:** Inbound (Salesforce → Data Room); **Paid** integration
- **Target customers:** Any Data Room customer using Salesforce as their CRM
- **Salesforce prerequisites:** Connected App (OAuth, client ID/secret, scopes, callback URLs); max **5 active sessions per Connected App**; Screen Flow; Custom Button; consolidated Salesforce object with investor email data
- **Anduin prerequisites:** Admin access to target data rooms; pre-created user groups in data rooms (groups define what permissions invited investors inherit — configure carefully)
- **Setup flow (CS):**
  1. Grant IH access to customer and enable this paid integration
  2. Customer locates "Salesforce (Invite to Dataroom)" in IH Browse tab
  3. Customer installs: names integration, grants permission to target datarooms
  4. Customer configures: enters Connected App credentials, selects target dataroom, specifies Salesforce email field
  5. Customer validates: triggers screen flow via custom button → investor invitation email sent
- **Key caution:** Customers should select the correct group before triggering — any invited investor automatically inherits that group's permissions
- If target dataroom not listed in IH: customer needs admin role, or a team member with admin access performs the linking step via Settings > Integrations in the Data Room app

## Connections
- [[wiki/products/integration-hub]] — this is one of the IH Paid integrations
- [[wiki/products/data-room]] — target system
- [[wiki/sources/ih-salesforce-dataroom-release-notes]] — companion release notes entry

## Conflicts & Supersessions
None identified.

## Raw Notes
- Integration is in IH Knowledge Library under "Salesforce (Invite to Dataroom)" — Paid, Inbound, CRM category
- External CS docs: developers.anduintransact.com/docs/automated-onboarding-with-dataroom
- Appendix: permission setup for Salesforce at developers.anduintransact.com/docs/appendix-permission-setup-for-salesforce
- 5-session limit for Salesforce Connected App is a critical constraint to communicate proactively
