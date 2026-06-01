---
type: source
title: "Investor Onboarding — Affinity (Primary Investor + Collaborators)"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Investor onboarding (Primary Investor + Collaborators).md
products: [Integration Hub, FundSub]
target_audience: CS
onboarding_required: No
tags: [integration, affinity, fundsub, order-creation, investor-onboarding]
---

## Summary
Describes the Affinity (Order creation) integration that invites investors (Primary + Collaborators) to FundSub with subscription forms prefilled from Affinity CRM data. Adds multi-collaborator support that the DealCloud equivalent lacks.

## Key Takeaways
- Pattern: **Order Creation** — Affinity → FundSub.
- Supports both a Primary Investor and multiple Collaborators per subscription (unlike DealCloud which is Primary only).
- Prefills FundSub subscription forms with Affinity list data.
- Prerequisites: Affinity API key, consolidated Affinity list with all relevant data.
- Two template types: Anduin Standard Fields (limited), Custom Template (unlimited, requires Anduin collaboration).
- Trigger: configurable field + value on the Affinity list; no check frequency setting (unlike DealCloud).
- Unique ID: required for deduplication/future operations.
- Contact fields: customer specifies which Affinity columns are Primary Investor and which are Collaborators.
- Roadmap note: multi-fund integration planned (single instance → multiple funds).

## Connections
- [[wiki/concepts/integration-patterns|Integration Patterns]] — Order Creation pattern.
- [[wiki/concepts/investor-onboarding-workflow|Investor Onboarding Workflow]].
- [[wiki/concepts/data-mapping|Data Mapping]].
- [[wiki/concepts/import-export-templates|Import/Export Templates]].
- [[wiki/entities/affinity|Affinity]], [[wiki/products/fundsub|FundSub]].
- Compare with [[wiki/sources/automated-onboarding-fundsub-primary|DealCloud Order Creation]] — similar pattern, Affinity adds Collaborator support.

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- Key differentiator vs DealCloud integration: Collaborators field support.
- Multi-fund integration is on the roadmap.
