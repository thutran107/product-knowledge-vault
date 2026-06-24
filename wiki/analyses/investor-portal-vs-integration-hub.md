---
type: analysis
title: "Investor Portal vs. Integration Hub"
date: 2026-06-08
tags: [investor-portal, integration-hub, sales-motion, competitive]
---

## Question
What is the difference between Investor Portal and Integration Hub — what does each do, who buys it, how do they relate, and where does each fit in the Anduin product suite?

## Answer / Synthesis

These two products are not competitors — they serve fundamentally different layers of the Anduin platform.

**Investor Portal** is a GP-branded, LP-facing communication and relationship destination. Post-close, GPs use it to distribute K-1s, capital call notices, quarterly reports, and NAV data; LPs log in to view documents, complete tasks, and (Q2 2026) update their profiles. The GP side includes a drag-and-drop home page editor, three document distribution methods (Group Share, Private Share, AI-powered Split & Share), financial reporting widgets, and an investor inbox. It competes directly with standalone investor portals: InvestorFlow, AtomInvest, and Fundwave.

**Integration Hub** is platform infrastructure — no-code workflow templates ("Integration Cards") that move data between Anduin products and external systems (Salesforce, DealCloud, Affinity, Box). Three patterns: Order Creation (CRM → FundSub), Data Retrieval (FundSub → CRM), Document Retrieval (FundSub/Data Room → file storage). GPs configure it once; it runs in the background. It has no named category competitor in existing sources.

### How they relate

Investor Portal explicitly uses Integration Hub as its connectivity layer. The recommended bundle per the Portal pricing source is: **Portal + IDM + Landing Pages + Integration Hub**. Neither product stands alone — both require IDM as the data backbone.

### Anduin lifecycle map

| Stage | Product |
|---|---|
| Fund marketing | Landing Pages |
| Fundraising | Data Room + FundSub |
| Post-close relationship | **Investor Portal** |
| Data backbone + connectivity | IDM + **Integration Hub** |

### Side-by-side

| Dimension | Investor Portal | Integration Hub |
|---|---|---|
| Core purpose | GP → LP communication layer | Anduin ↔ third-party system connectivity |
| Primary user | Fund managers and their LPs | Ops/tech teams managing data flows |
| What it replaces | Standalone investor portals | Custom integrations, manual data entry |
| Pricing model | Annual fee per fund/SPV by AUM tier ($6K–$30K/fund/yr) | Not publicly priced; premium integrations require Anduin-set quota |
| Direct competitors | InvestorFlow, AtomInvest, Fundwave | None documented |
| Maturity | Newer (beta 2025, GA post-launch) | More established (SOP, full playbook, case study) |
| Source count | 9 | 14 |

### Buyer profile

**Portal** — buyer is the fund manager currently emailing documents or using a point-solution portal. Value prop: end-to-end platform (one system from onboarding to relationship management) plus branding. Pre-condition: IDM must be set up first. Reporting dashboards landed Q1 2026; investor self-service profiles Q2 2026.

**Integration Hub** — buyer is ops or technology team managing CRM/back-office data flows. Value prop: no-code self-service vs. custom API work. Setup: Access → Install (wizard) → Test → Deploy. Mature implementation playbook and Neuberger Berman case study available.

### Anduin differentiation

Portal wins against standalone portals on: end-to-end platform depth, UX/branding customization, and lower adoption friction for existing FundSub/IDM customers.

Integration Hub differentiates Anduin platform stickiness overall — it is a platform differentiator rather than a standalone sale.

## Evidence

- [[products/investor-portal]] — product page
- [[products/integration-hub]] — product page
- [[sources/investor-portal-pricing-faqs-boston]] — Portal pricing (trust 3) ⭐
- [[sources/investor-portal-gtm-primer]] — Portal market positioning and lifecycle map
- [[sources/investor-portal-sales-deck]] — Portal capabilities
- [[sources/ih-sales-deck-feb-2025]] — Integration Hub positioning and use cases
- [[sources/ih-sop]] — IH operational maturity
- [[sources/neuberger-berman-case-study]] — IH real-world deployment

## Caveats

- Integration Hub pricing is not documented in the wiki. The only note is that premium integrations require a quota set by Anduin. This is a gap if pricing comes up in a deal.
- Portal acquisition targets ($14M CFP by end of 2026) were set in Feb 2025 — verify whether these have been updated.
- Portal reporting roadmap (Q1–Q4 2026) is based on pre-launch planning; confirm current status with product team.
