---
type: entity
entity_type: integration
title: "Affinity"
source_count: 1
last_updated: 2026-04-20
tags: [affinity, crm, third-party, integration]
---

## Overview
A relationship intelligence CRM popular with venture capital and growth equity firms. Anduin has one Integration Hub connection: Order Creation (Affinity → FundSub).

## Key Facts
- One Integration Hub connection: **Order Creation** — Affinity list → FundSub (investor onboarding with prefill).
- Requires API key.
- Uses Affinity "lists" as the data source (not objects like DealCloud).
- Supports both Primary Investor and multiple Collaborators per subscription — differentiator vs DealCloud Order Creation.
- Trigger: a configurable field + value on the Affinity list.
- Template types: Anduin Standard Fields or Custom Template.
- No check frequency setting (unlike DealCloud) — trigger is evaluated differently.
- Roadmap: multi-fund integration (single instance → multiple funds) is planned.

## Role in This Knowledge Base
Second CRM with Order Creation support. Key differentiator: Collaborator field support that DealCloud integration lacks.

## Sources
- [[wiki/sources/investor-onboarding-primary-collaborators|Affinity Order Creation]]

## Related
- [[wiki/products/fundsub|FundSub]]
- [[wiki/entities/dealcloud|DealCloud]]
- [[wiki/concepts/integration-patterns|Integration Patterns]]
- [[wiki/concepts/investor-onboarding-workflow|Investor Onboarding Workflow]]
