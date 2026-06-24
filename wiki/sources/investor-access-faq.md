---
type: source
title: "Investor Access — Internal FAQ"
date_ingested: 2026-06-15
as_of_date: 2025-09-26
source_type: faq
trust_level: 4
original_file: Notion — Investor Access Internal FAQs (ae975bab40ae47d29510de4226b0fee2)
products: [Investor Access]
target_audience: Sales + RM | CS
onboarding_required: Yes
tags: [investor-access, lp, subscription-passport, aml-kyc, data-management, pricing]
---

## Summary
The comprehensive internal FAQ for Investor Access — Anduin's LP-side "subscription passport" that lets investors store data and AML/KYC documents once and reuse them to complete any fund subscription on Anduin. Covers what the product is, who it's for, the data model, AML/KYC handling, FundSub integration, collaboration, support, pricing, and objection handling. This is the first substantive source on Investor Access in the vault (previously only a one-line mention in the Neuberger Berman case study).

## Key Takeaways
- **What it is**: "A subscription passport that allows LPs to store and use data & AML/KYC documents to complete any fund subscription on Anduin." It is the **LP-side counterpart to IDM** (which is the fund/GP side, released Q3 2023).
- **Access**: directly at `investoraccess.anduin.app` or via the FundSub app sidebar.
- **Price**: **free of charge** — any investor with Anduin access can create an investment entity and use it in FundSub (if the GP enables the feature). The goal is to improve LP experience and increase platform stickiness. (A future paid model with basic price, add-on price, and PDF-update price is under discussion but not set.)
- **Data stored (MVP)**: investor type, generation info, contact info, wire instructions, bank wiring status, Form PF, CRS forms, AML questionnaire, plus AML/KYC documents with expiry tracking. The data set is **not customizable** and there is **one single profile template for all investors**.
- **Key concepts**: an *Investment Entity* is the legal entity an investor uses to subscribe; a *Profile* is the collection of static info attached to that entity. One subscription → one investment entity; one entity can be reused across many subscriptions; profile/KYC data **cannot be shared across entities**.
- **AML/KYC expiry**: documents can carry an expiration date with notifications at 14 days before, on the date, and 7 days after expiry.
- **FundSub integration**: prefill a subscription from profile data (system highlights the closest-matching entity and surfaces past entities), and update the profile from subscription data after signing. Conflicts are flagged when updating a profile from subscription data. Commitment-amount updates in FS auto-sync back to the IA Subscriptions tab.
- **Collaboration**: investors can invite teammates/service providers to an entity, but there are **no granular permissions** — all collaborators get full edit access. Inviting fund-side members to an entity is *not* recommended (share via export instead).
- **Opt-out**: investors can decline to use IA; GPs can turn it off entirely for a given FundSub.
- **Support**: Helpjuice support page, 8am–8pm ET, 24-hour response; a dedicated implementation manager only for the first 3 months of launch.

## Connections
- Primary source for [[products/investor-access|Investor Access]] (upgrades it from a stub to a documented product).
- Tightly coupled to [[products/fundsub|FundSub]] (the subscription flow IA prefills) and positioned as the LP-side mirror of [[products/investor-data-management|IDM]].
- AML/KYC handling connects to [[products/investor-data-management|IDM]]'s AML/KYC feature and the [[concepts/investor-onboarding-workflow|Investor Onboarding Workflow]].
- Import/export themes connect to [[concepts/import-export-templates|Import/Export Templates]].
- AAA advisors leverage the investor passport for subscription auto-fill — connects to [[products/aaa|AAA]].

## Conflicts & Supersessions
- **Terminology note (not a conflict)**: the objection-handling section refers to the fund-side product as "Fund Data Management (FDM)," whereas the vault and current materials use "Investor Data Management (IDM)." FDM appears to be an older internal name for IDM. Flag for CS so they don't treat FDM and IDM as separate products.
- No factual conflicts with existing pages. The Neuberger Berman case study's bare mention of "Investor Access" is now substantiated here.

## Raw Notes
- Content fetched from the linked "Investor Access Internal FAQs" Notion page (the Knowledge Library row itself is blank); last viewed 2025-09-26, used as the as-of date. The row has no explicit as-of date.
- Document Type = "FAQ" (trust 4); onboarding_required: Yes (Sales + RM, CS).
- Open roadmap item noted: CSV export of profile data ("working on") so investors can update their CRM or share with advisors/fund admins.
- A pricing discussion page and marketing one-pager are linked but not ingested.
