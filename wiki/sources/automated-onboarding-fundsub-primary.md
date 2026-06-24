---
type: source
title: "Automated Onboarding with FundSub — DealCloud (Primary Investor)"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Automated onboarding with FundSub (Primary Investor).md
products: [Integration Hub, FundSub]
target_audience: CS
onboarding_required: No
tags: [integration, dealcloud, fundsub, order-creation, investor-onboarding]
---

## Summary
Describes the DealCloud (Order creation) integration that automatically invites investors to FundSub with subscription forms partially prefilled using data from DealCloud, eliminating manual onboarding steps.

## Key Takeaways
- Pattern: **Order Creation** — DealCloud → FundSub.
- Automatically creates a subscription order in FundSub when a DealCloud record hits a configured trigger field/value.
- Prefills investor forms with mapped DealCloud data.
- Sends investor invitation email automatically.
- Target persona: FundSub customers using DealCloud as their CRM who want to prefill large portions of subscription forms.
- Prerequisites: DealCloud API key, consolidated DealCloud object, Publication feature enabled on that object.
- Two import template types: Anduin Standard Alias (ASA) — limited fields; Custom Template — unlimited fields with complex computation.
- Trigger configuration: trigger field, trigger value, check frequency (e.g., hourly), unique ID for deduplication.
- Contact mapping: must specify which DealCloud fields map to First Name, Last Name, Email for invitation.

## Connections
- [[concepts/integration-patterns|Integration Patterns]] — Order Creation pattern.
- [[concepts/investor-onboarding-workflow|Investor Onboarding Workflow]].
- [[concepts/data-mapping|Data Mapping]] — field mapping between DealCloud and FundSub.
- [[concepts/import-export-templates|Import/Export Templates]].
- [[entities/dealcloud|DealCloud]], [[products/fundsub|FundSub]].

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- "Publication" API feature must be enabled on the DealCloud object — this is a DealCloud-side setup step.
- Unique ID mapping is used for deduplication in future operations.
- Check frequency is configurable (e.g., hourly).
