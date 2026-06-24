---
type: source
title: "IH Knowledge Hub — Guide to All Available Implementations"
date_ingested: 2026-05-11
as_of_date: 2026-03-31
source_type: implementation-guide
trust_level: 2
original_file: notion://2153f653-b1df-8050-8ca8-fccedd213b24
products: [Integration Hub]
target_audience: All teams
onboarding_required: Yes
tags: [integration-hub, onboarding, implementation]
---

## Summary
A Notion database listing every integration use case available through the Integration Hub, organized by third-party app, Anduin app, direction, category, and status. Serves as the canonical library of what the Hub can do.

## Key Takeaways
- **Database columns**: 3rd party app, Anduin app, Direction (Inbound/Outbound), Category (type + free/paid), Ready (live in production), Use case, and Materials (internal + external guides).
- **Direction definitions**: Outbound = data flows Anduin → external system; Inbound = data/docs flow external system → Anduin.
- **Card naming conventions**: suffix indicates integration type:
  - "Order creation" = automates using 3rd-party data to create a FundSub subscription
  - "Data retrieval" = pushes subscription data from Anduin to 3rd party
  - "Document retrieval" = pushes investor docs from Anduin to 3rd party
- Free integrations available by default; paid integrations shown with "Send Request" CTA.
- Customers can access per-integration setup guides directly from integration card UI.
- Each integration card in the Hub includes a "View setup guide" button.

## Connections
- [[products/integration-hub]] — this is the canonical capability reference for the Hub
- [[concepts/integration-patterns]] — the card naming conventions described here define patterns
- [[sources/ih-setup-guide]] — companion guide for how to set up the Hub platform itself
- [[sources/mission-and-core-components]] — broader architectural overview

## Conflicts & Supersessions
- No conflicts. Extends the integration patterns concept with operational naming conventions.

## Raw Notes
- Database URL: https://www.notion.so/20d3f653b1df802c8072ec6a662d6c3b
- Note: "Ready" flag = live and in production. Upcoming integrations exist in the database but are not marked Ready.
