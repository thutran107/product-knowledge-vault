---
type: source
title: "Integration SOP"
date_ingested: 2026-05-11
as_of_date: 2026-05-07
source_type: sop
trust_level: 2
original_file: notion://1ab3f653-b1df-80a2-8410-ebbe8a976dea
products: [Integration Hub]
target_audience: CS | Digi
onboarding_required: No
tags: [integration-hub, implementation, sop]
---

## Summary
Comprehensive internal SOP for the Digitization and CS teams covering all Integration types, the requirement gathering process, and the full workflow for setting up both Integration Hub and Internal Integration. As of May 2026 — the most recently updated IH process document.

## Key Takeaways
- **Three integration tiers:**
  1. **Integration Hub — Free**: Basic 3rd-party tools (Slack, Gmail); 100% self-service; no team involvement required.
  2. **Integration Hub — Paid/Premium**: Salesforce, DealCloud, etc. Subtypes: Out-of-box (OOTB), Customized, Customized-Partnership. Requires client payment and optional Import/Export Data Customization Add-in.
  3. **Internal Integration**: Cross-fund data transfers (Fund A → Fund B). Always requires Data Customization. OOTB or Customized.
- **Four workflow patterns**: Order creation (3rd party → FundSub), Data retrieval (FundSub → 3rd party), Document retrieval (FundSub → 3rd party), AML/KYC check (FundSub → 3rd party).
- **Data mapping template** = IP team's main deliverable for integration; maps import/export fields for investor data from FundSub workflow.
- Every request must be tagged @team_integration in Slack.
- Sales process: AE/RM + Sales Engineer collect business needs → CS+DS/DC develop implementation plan → CS finalizes solution and logs in SFDC.
- OOTB standard path: AE+RM Demo → kick-off call → customer self-service.

## Connections
- [[products/integration-hub]] — defines all integration types available
- [[concepts/integration-patterns]] — elaborates on Order Creation, Data Retrieval, Document Retrieval patterns
- [[concepts/data-mapping]] — the "data mapping template" central to premium/internal integrations
- [[products/fundsub]] — source/destination for most integration workflows
- [[products/investor-data-management]] — IDM as Anduin object in Internal Integration

## Conflicts & Supersessions
- No conflicts. Adds more granularity (free vs. paid tiers, internal integration) not covered in existing sources.

## Raw Notes
- Internal SOP workbook at: https://www.notion.so/cd80dd78246a4eb39db5359642c31bbc
- Salesforce example: track opportunities → invite investors → update SFDC with subscription data → download docs to SFDC.
- "Customized-Partnership" subtype: pre-defined partner platform (e.g., FundSub ↔ CRM) with pre-built ASA templates.
