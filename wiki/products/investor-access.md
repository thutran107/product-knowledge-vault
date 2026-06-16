---
type: product
title: "Investor Access"
status: GA
source_count: 2
last_updated: 2026-06-15
tags: [investor-access, lp, subscription-passport, aml-kyc, data-management]
---

## What it does
Investor Access is Anduin's LP-side **subscription passport**: it lets investors store their data and AML/KYC documents once and reuse them to complete any fund subscription on Anduin. It is the investor-facing counterpart to [[wiki/products/investor-data-management|IDM]] (which serves the fund/GP side). The goal is to make subscriptions faster for LPs and increase their stickiness with the platform.

## Key capabilities
- **Investment-entity profiles**: investors create investment entities (the legal entity they subscribe through) and maintain a static profile of reusable data.
- **Prefill subscriptions**: when a GP enables Investor Access for a fund, the LP can prefill a FundSub subscription from a chosen entity's profile — the system highlights the closest-matching entity and surfaces previously used entities for reuse.
- **Profile sync from subscriptions**: after signing, investors can update their profile from the data they just entered; the system flags conflicts and auto-syncs commitment-amount updates back to the IA Subscriptions tab.
- **AML/KYC document vault with expiry tracking**: store documents (manually or saved from a subscription) with expiration dates and notifications at 14 days before, on the date, and 7 days after expiry.
- **Collaboration**: invite teammates or service providers to help manage an entity (note: full edit access only — no granular permissions).
- **Subscription tracking**: link and track all subscriptions made from a given investment entity.

## Pricing & packaging
**Free of charge.** Any investor with Anduin access can create an investment entity and use it in FundSub when the GP enables the feature. A future paid model (basic price + add-on price + PDF-update price) is under internal discussion but not set. Source: [[wiki/sources/investor-access-faq|Investor Access FAQ]].

## Implementation notes
- Accessed at `investoraccess.anduin.app` or via the FundSub app sidebar.
- GPs enable/disable Investor Access per FundSub; investors can also opt out individually.
- Available in the demo sandbox for US/Cayman funds (enable IA in demo settings).
- Support: Helpjuice page, 8am–8pm ET, 24-hour response; a dedicated implementation manager only for the first 3 months after a customer's launch.

## Known limitations
- **Single, non-customizable profile template** for all investors — no fund-specific data templates (GPs needing that are steered to IDM).
- **Profile/KYC data cannot be shared across investment entities** — each profile attaches to one entity only.
- **No granular collaboration permissions** — all invited collaborators get full edit access.
- One subscription maps to exactly one investment entity (an entity can serve many subscriptions, but not vice versa).
- Replacing the linked entity on a subscription re-links only; it does not update the subscription's data.
- CSV export of profile data is a roadmap item ("working on"), not yet available.

## Features & sub-modules
Capabilities documented inline above. Tightly integrated with [[wiki/products/fundsub|FundSub]] (the subscription flow it prefills).

## Related customers
- [[wiki/customers/neuberger-berman|Neuberger Berman]] — deployed Investor Access as part of a full Anduin rollout (alongside FundSub, Data Room, IDM, Integration Hub).

## Sources
- [[wiki/sources/investor-access-faq|Investor Access — Internal FAQ]] (2025) — comprehensive product FAQ, data model, pricing, objection handling.
- [[wiki/sources/neuberger-berman-case-study|Neuberger Berman Case Study]] — names Investor Access as a deployed product.

## Related
- [[wiki/products/investor-data-management|IDM]] — fund-side counterpart (Investor Access is the LP-side mirror).
- [[wiki/products/fundsub|FundSub]] — the subscription product Investor Access prefills.
- [[wiki/products/aaa|AAA (Advisor Advantage)]] — advisors leverage the investor passport for auto-fill.
- [[wiki/concepts/investor-onboarding-workflow|Investor Onboarding Workflow]]
- [[wiki/concepts/import-export-templates|Import/Export Templates]]
