---
type: source
title: "Retrieve Subscription Data (DealCloud)"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Retrieve subscription data.md
products: [Integration Hub, FundSub]
target_audience: CS
onboarding_required: No
tags: [integration, dealcloud, fundsub, data-retrieval, crm-sync]
---

## Summary
Describes the DealCloud (Data retrieval) integration that automatically syncs completed subscription data from FundSub to the customer's DealCloud CRM, triggered by subscription status changes.

## Key Takeaways
- Pattern: **Data Retrieval** — FundSub → DealCloud CRM.
- Triggered when a subscription reaches a configured status (e.g., signed, completed).
- Creates or updates a DealCloud object record with mapped subscription fields.
- Deduplication: checks Anduin custom ID; falls back to Anduin system-generated ID if blank.
- Three export template types: Anduin Standard Alias (limited), Self-service Template (customer-configurable via FundSub UI), Custom Template (unlimited, requires Anduin collaboration).
- Currently supports 1-to-1 field mapping only (no transformation logic in UI).
- Prerequisites: DealCloud API key, DealCloud object with unique ID field + all target data fields (text type only).
- Target persona: FundSub customers using DealCloud as CRM needing to sync high volumes of subscription data.

## Connections
- [[wiki/concepts/integration-patterns|Integration Patterns]] — Data Retrieval pattern.
- [[wiki/concepts/import-export-templates|Import/Export Templates]] — export templates used here.
- [[wiki/concepts/data-mapping|Data Mapping]].
- [[wiki/entities/dealcloud|DealCloud]], [[wiki/products/fundsub|FundSub]].

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- Self-service Export Template is a differentiator — customers don't need Anduin to create standard export templates.
- The CRM record is meant to become "the central, authoritative repository" for investor data post-subscription.
