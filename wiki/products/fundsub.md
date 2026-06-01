---
type: product
title: "FundSub (Fund Subscription)"
status: GA
source_count: 13
last_updated: 2026-05-12
tags: [fundsub, subscription, fund-management, workflows]
---

## What it does
FundSub is Anduin's fund subscription platform. Investors (LPs) complete subscription forms and sign documents through FundSub; GPs and their teams manage the onboarding, review, and approval process. It is the primary Anduin object for most integrations — order creation integrations write into FundSub, and data retrieval integrations read from it.

## Key capabilities
- **Multi-structure fund support**: handles closed-ended and open-ended/evergreen fund structures.
- **Multi-jurisdiction documents**: subscription documents can span Delaware, Cayman, Luxembourg feeders, and other legal jurisdictions.
- **Master Dashboard**: centralized view for GP review teams to track all subscriptions across a fund.
- **One envelope experience**: all documents presented to the LP in a single e-signature envelope, reducing friction (vs. multiple sequential envelopes).
- **Duplicate fund configuration**: GPs can clone an existing fund's configuration as a template for a new fund, reducing setup time.
- **Email configuration & SMTP integration**: per-fund or per-environment email sending can be customized, including custom SMTP sender settings.
- **Theme / brand color customization**: CS can configure a customer's brand color palette at the environment level via iTools > White Label > Theme Editor. Applies to FundSub and Data Room. IDM and Investor Portal not yet supported. Self-service not available — CS-managed only.
- **Self-service export templates**: customers can create their own export data templates via the FundSub UI without requiring Anduin involvement.
- **Integration Hub connections**: FundSub exposes Settings > Integrations for per-fund permission grants, enabling CRM and document automation workflows.
- **LP transfers and high data volumes**: supports bulk operations and large LP counts (e.g., Neuberger Berman onboarded ~3,000 LPs, raising $5.4B).
- **LP view (investor-facing UI)**: updated investor subscription view with improved UX (covered in New LP View one-pager, Dec 2025).

## Pricing & packaging
**Anduin Essentials** is the entry-level tier, designed for first-time and emerging fund managers.

| Tier | What's included |
|------|----------------|
| **Starter** | 18 months platform access, Marketing Data Room, digitization of 1 main sub doc |
| **Advanced** | Everything in Starter + additional workflows (MFN, SPV, Co-invest, etc.) |

Essentials supports: Domestic/Offshore, Open/Close-ended, Single or Multiple funds (single flow), Parallel/SPV/Hybrid structures. Max 2 investor groups; basic AML/KYC workflow.

**Enterprise** tier unlocks: multiple funds + multiple flows, more than 2 investor groups, customized flows, complex AML/KYC, and other Anduin modules (IDM, Investor Portal, Investor Access, Side Letter, Integration Hub).

*Source: [[wiki/sources/fundsub-essentials-sales-deck|Essentials Sales Deck]] (Jun 2025). No explicit pricing figures available — contact Sales for commercial terms.*

## Implementation notes
- A "fund" in FundSub is the core Anduin Object — the container for all subscription data for a given fund.
- Integration Hub: FundSub exposes Settings > Integrations for per-fund permission grants.
- Theme customization: configured in iTools at the environment level (see [[wiki/sources/fundsub-dataroom-theme-customization|Theme Customization Guide]]). Requires gathering brand color HEX values from the customer.
- Duplicate fund: allows GP to spin up a new fund from an existing fund's configuration (see [[wiki/sources/fundsub-duplicate-fund-config|Duplicate Fund Config Guide]]).
- Email/SMTP: custom email configuration available per CS setup (see [[wiki/sources/fundsub-email-smtp-implementation-guide|Email & SMTP Guide]]).

## Known limitations
- Theme customization: environment-level only — no per-fund color customization. IDM and Investor Portal not yet supported. Dark mode not supported. Customers cannot self-service.
- One envelope experience: documents must be configured appropriately; details in Google Slides deck.

## Features & sub-modules
- [[wiki/products/e-signature|E-signature]] — signing workflow embedded within FundSub
- Theme customization (see [[wiki/sources/fundsub-dataroom-theme-customization|Theme Customization Guide]])

## Related customers
- [[wiki/customers/neuberger-berman|Neuberger Berman]] — ~3,000 LPs, $5.4B raised via FundSub + IH
- [[wiki/customers/cerity-partners|Cerity Partners]] — FundSub + AAA + E-signature (Schwab DocuSign workflow)
- [[wiki/customers/nxstep|NXSTEP]] — Essentials tier; quote highlights 3x manual process efficiency gain

## Sources
- [[wiki/sources/fundsub-essentials-sales-deck|FundSub Anduin Essentials Sales Deck]] (Jun 2025, onboarding required)
- [[wiki/sources/fundsub-new-lp-view-one-pager|New LP View One-Pager]] (Dec 2025)
- [[wiki/sources/fundsub-email-smtp-implementation-guide|Email Configuration & SMTP Implementation Guide]] (Mar 2025)
- [[wiki/sources/fundsub-duplicate-fund-config|Duplicate Fund Configuration Guide]] (Nov 2025)
- [[wiki/sources/fundsub-one-envelope-experience|One Envelope Experience]] (Mar 2025)
- [[wiki/sources/fundsub-dataroom-theme-customization|Theme Customization — Internal Guide]] (Sep 2025)
- [[wiki/sources/automated-onboarding-fundsub-primary|DealCloud Order Creation]]
- [[wiki/sources/investor-onboarding-primary-collaborators|Affinity Order Creation]]
- [[wiki/sources/retrieve-subscription-data|DealCloud Data Retrieval]]
- [[wiki/sources/automated-document-repository|Box Document Retrieval]]
- [[wiki/sources/data-management|Data Management]]
- [[wiki/sources/configuration-vs-permission|Configuration vs Permission]]
- [[wiki/sources/neuberger-berman-case-study|Neuberger Berman Case Study]]

## Related
- [[wiki/products/integration-hub|Integration Hub]]
- [[wiki/products/investor-data-management|IDM]]
- [[wiki/products/data-room|Data Room]] — shares theme customization feature
- [[wiki/products/e-signature|E-signature]]
- [[wiki/concepts/investor-onboarding-workflow|Investor Onboarding Workflow]]
- [[wiki/concepts/import-export-templates|Import/Export Templates]]
