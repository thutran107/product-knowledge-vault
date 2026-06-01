---
type: entity
entity_type: integration
title: "Salesforce"
source_count: 3
last_updated: 2026-04-20
tags: [salesforce, crm, third-party]
---

## Overview
The world's largest CRM platform. Anduin has a full bidirectional integration with Salesforce via the Integration Hub, covering all three patterns: Order Creation, Data Retrieval, and Document Retrieval.

## Key Facts
- **Full bidirectional flow** (documented in Sales Deck):
  1. **Order Creation** (SF → FundSub): GP logs into Salesforce → triggers subscription creation → FundSub order created → form prefilled → investor invitation sent → LP accesses pre-filled form.
  2. **Data Retrieval** (FundSub → SF): subscription data synced back to Salesforce on completion.
  3. **Document Retrieval** (FundSub → SF): investor documents pushed to Salesforce.
- Neuberger Berman integrated Salesforce with IDM via Integration Hub for subscription initiation and cross-team tracking.
- Uses Investor Data Management (IDM) API for the bidirectional data flows.
- Used as a Member invite example: external Salesforce consultants can be invited to help configure.

## Role in This Knowledge Base
The most fully featured CRM integration — all three patterns documented. Serves as the reference architecture for full bidirectional CRM connectivity.

## Sources
- [[wiki/sources/neuberger-berman-case-study|Neuberger Berman Case Study]]
- [[wiki/sources/mission-and-core-components|Mission and Core Components]]
- [[wiki/sources/ih-sales-deck-feb-2025|Integration Hub Sales Deck (Feb 2025)]]

## Related
- [[wiki/products/investor-data-management|IDM]]
- [[wiki/entities/dealcloud|DealCloud]]
- [[wiki/entities/affinity|Affinity]]
