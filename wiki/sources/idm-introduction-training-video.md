---
type: source
title: "IDM — Introduction (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-data-management/1-introduction/"
products: [IDM]
target_audience: CS | Sales + RM
onboarding_required: Yes
tags: [idm, onboarding, sales-motion, implementation]
---

## Summary
Internal enablement video introducing IDM as the centralized investor-data layer and how to sell/scope it. IDM is positioned not as a standalone database but as infrastructure that earns its value through three workflows — **onboarding** (centralize and reuse data), **compliance** (track/renew AML/KYC), and **integrations** (one connection point to CRM/warehouse). The back half is a scoping playbook: classify the client scenario, identify CRM presence, and — most critically — ask the **sequencing/priority question** and the **single-vs-multiple-IDM** decision before any demo.

## Key Takeaways
- **Sell the workflow, not the product.** "You need a compelling workflow to sell IDM effectively." Anchor every conversation in onboarding, compliance, or integrations.
- **One-sentence definition (worth memorizing):** "IDM is the centralized investor data layer that powers reuse through onboarding, tracking through compliance, and provides a single integration point out to the client's CRM or warehouse."
- **Best-fit clients:** existing FundSub clients with scattered data are the easiest win; CRM clients are strong (IDM becomes their hub); CRM-less clients work but need more profile-design conversation.
- **Engagement scenarios:** classify as (a) existing fund client, (b) new client with a fundraise, or (c) combination case with offline data — each has a distinct migration path.
- **Priority question is critical:** when a client needs both a fundraise and IDM at once, ask up front *which must be ready first* — it dictates timelines, team assignments, and sequencing.
- **Single vs. multiple IDM (a hard scoping rule):** IDM does **not yet** support granular fund-level access controls within one environment, so any client with separate teams that must not see each other's data requires **multiple IDM environments**. Getting this wrong "leads to months of remapping and redesigning profiles."

## Connections
- Core source for the upgraded [[products/investor-data-management|IDM product page]] (What it does, three workflows, known limitations).
- Feeds [[concepts/investor-onboarding-workflow]] (centralize-once / reuse-forever) and the access-control limitation noted on the product page.
- Companion to the deeper module videos: [[sources/idm-funds-tab-training-video]], [[sources/idm-clients-tab-training-video]], [[sources/idm-contacts-training-video]], [[sources/idm-settings-training-video]], [[sources/idm-public-api-training-video]].

## Conflicts & Supersessions
- No conflicts. Corroborates and extends the existing thin IDM page. The "no granular fund-level access control in a single IDM" point is a **new, explicitly-stated limitation** not previously captured.

## Raw Notes
- Runtime 5:43, 8 sections. Date unknown (header reads "Unknown").
- Companion summary file (`1. Introduction to IDM.md`) ingested alongside the transcript; transcript is the authoritative artifact.
- Pre-scoping checklist named: client type · engagement scenario · CRM existence · sequencing priority.
- Pre-Anduin data path matters: data trapped in PDFs vs. clean spreadsheet = very different effort profiles.
