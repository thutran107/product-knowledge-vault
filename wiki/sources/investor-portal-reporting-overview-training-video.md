---
type: source
title: "Investor Portal — Reporting: Architecture & Investor Experience (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-portal/reporting/2-layers-architecture/ + 1-investor-experience/"
products: [Investor Portal]
target_audience: CS | Sales + RM
onboarding_required: No
tags: [investor-portal, implementation, integration]
---

## Summary
Two consolidated reporting videos — the **layers architecture** and the **investor-experience** view. Portal reporting is a three-layer system: **Datasets** (flexible, manager-defined structured data) → **Widgets** (visualizations) → **Pages** (landing-page compositions). Permissions are derived automatically from the contact matrix. The investor's experience is entirely a product of how the manager configures these layers.

## Key Takeaways
- **Three-layer architecture:** datasets store structured data; widgets visualize it; pages organize widgets — so **one data integration powers multiple presentation formats** ("integrate once, present everywhere").
- **Flexible schema, not fixed mapping:** unlike legacy tools that force data into a predefined schema, managers define their own data points (IRR, MOIC, transaction history). Flexibility is the foundational design principle.
- **Permissions that manage themselves:** tying each dataset record to an **investment object** connected to the **contact matrix** auto-enforces investor-level access — "the fund manager just needs to keep their contact matrices updated, and the permissioning will happen automatically." Page-level access control can serve different reporting experiences to different cohorts (LP tiers, co-investors, RPs).
- **Reporting is a native experience** alongside opportunities, onboarding, documents, profiles — one portal, not a siloed tool.
- **Real-time for RPs (Registered Placement Agents):** because managers refresh datasets via API or spreadsheet at any frequency, RPs pull fresh data immediately instead of manually parsing quarterly Excel/PDF packages.
- **Investor experience is manager-configured:** consolidated single-page vs. segmented multi-page layouts; **selective data exposure** (hide sensitive metrics); investor-level filtering by entity/capital account; investors can **always download** visible data.
- **Timeline:** "March ships tables" (the first widget); charts/metrics later.

## Connections
- Co-source (with [[sources/investor-portal-reporting-datasets-training-video]] and [[sources/investor-portal-reporting-pages-widgets-training-video]]) for [[features/investor-portal-reporting-dashboards]].
- Permission model rests on [[features/idm-contacts|the IDM communication matrix]] and the Portal-exclusive Financial Data permission ([[concepts/product-packaging-bundling]]).
- "Integrate once" model relates to [[concepts/integration-patterns]].

## Conflicts & Supersessions
- No conflict. Substantially deepens the "3-layer reporting framework" bullet on [[products/investor-portal]]. Reporting is **Portal-only** (explicitly *not* part of [[products/engagement-hub|Engagement Hub]]) — consistent with the EH page.

## Raw Notes
- Layers 8:20 / 8 sections; Investor-experience 1:52 / 5 sections. "Unknown" date.
- "March" / "Q3" cited; year inferred 2026.
