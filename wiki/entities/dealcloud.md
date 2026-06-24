---
type: entity
entity_type: integration
title: "DealCloud"
source_count: 3
last_updated: 2026-04-20
tags: [dealcloud, crm, third-party, integration]
---

## Overview
A CRM platform commonly used by private equity, credit, and real estate investment firms. The most-referenced third-party system in current sources — Anduin has three distinct integrations with it.

## Key Facts
- Three Integration Hub connections with DealCloud:
  1. **Order Creation** — DealCloud → FundSub (investor onboarding with form prefill).
  2. **Data Retrieval** — FundSub → DealCloud (sync subscription data back to CRM post-signing).
  3. **Data Room alert** — Data Room → DealCloud (sync investor engagement/activity data).
- Requires API key for all integrations.
- Object preparation: customers must create a DealCloud object with specific fields (all text type) to receive Anduin data.
- Publication feature must be enabled on the DealCloud object for Order Creation flow.
- Supports unique ID field mapping for deduplication across all integration types.
- All mapped fields must be text type — numeric/picklist types break integrations.

## Role in This Knowledge Base
The primary CRM integration target. Represents the full bidirectional data flow pattern: CRM → Anduin (onboarding) and Anduin → CRM (post-subscription sync + engagement data).

## Sources
- [[sources/automated-onboarding-fundsub-primary|DealCloud Order Creation]]
- [[sources/retrieve-subscription-data|DealCloud Data Retrieval]]
- [[sources/automated-data-room-insights|DealCloud Data Room Insights]]

## Related
- [[products/fundsub|FundSub]]
- [[products/data-room|Data Room]]
- [[concepts/integration-patterns|Integration Patterns]]
- [[concepts/data-mapping|Data Mapping]]
- [[concepts/crm-integration-playbook|CRM Integration Playbook]]
