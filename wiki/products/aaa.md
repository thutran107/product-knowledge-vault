---
type: product
title: "AAA (Advisor Advantage)"
status: GA
source_count: 7
last_updated: 2026-06-15
tags: [aaa, advisor, ria, wealth-management, subscription-management, permissions]
---

## What it does
AAA (Advisor Advantage) is Anduin's dedicated fund-onboarding experience for **RIAs (Registered Investment Advisors) and Wealth Management teams** — the LP-side service providers who fill out subscription documents on behalf of their clients. It lets advisor teams create and manage client subscriptions to invited funds at scale while preserving their own entity structure and permissions, and lets fund managers (GPs) collaborate with advisors without over-exposing confidential fund information. Internally the product is called "RIA"; "Advisor Advantage" is the go-to-market name.

## Key capabilities
- **Advisor invitation (GP side, in FundSub)**: GPs invite existing or new advisor entities to a fund; they can create an entity on the advisor's behalf or let the advisor self-create during onboarding.
- **Real-time visibility & control**: an "Advisor Group" column on the FundSub Master Dashboard shows which subscriptions each advisor created; GPs can filter by RIA, track activation and per-advisor permissions, and disable/enable a group's ability to create new subscriptions in one click.
- **Assign/unassign subscriptions**: GPs can assign or unassign any subscription — created directly in FundSub, via CRM, or via IDM — to/from advisor entities (released Oct 2025; see [[wiki/sources/aaa-advisor-subscription-assign|release note]]).
- **Advisor Tags**: GPs post custom statuses/notes (e.g., "Custodian approve," "pending custodian approval") on the FundSub dashboard; tags sync in real time to the advisor's Advisor Advantage dashboard, replacing offline email status chasing.
- **Dedicated advisor workspace (Advisor Advantage app)**: one-time entity creation, an Opportunities dashboard across all accessible funds, fund-specific subscription dashboards, fund-level advisor management, and entity user management.
- **Email-domain automation**: whitelisting the RIA firm's email domain auto-adds advisors invited by GPs and enables syncing of created subscriptions to the Advisor Advantage dashboard.
- **Auto-fill onboarding**: advisors prefill subscription docs from past subscriptions or from an [[wiki/products/investor-access|Investor Access]] passport, and reuse pre-saved AML/KYC documents.
- **Signature enhancements**: one-envelope signing and Schwab custodian-approved signature workflows for advisor-driven subscriptions.

## Permission model
Two tiers (see [[wiki/sources/aaa-sales-deck|Sales Deck]] and [[wiki/sources/aaa-cs-training|CS Training]]):
- **Entity permission**: Entity Admin > Entity Manager > Entity Member.
- **Fund-group permission**: Entity Admin (always retains access) / Fund Group Admin / Fund Group Member — members operate on their own subscriptions as the main LP.

## Data model (for CS)
- **Temporary Advisor Group** — placeholder group the GP creates in FundSub to invite advisors; becomes active once accepted.
- **Advisor Entity (RIA entity)** — created by the advisor on accepting an invitation; represents their firm.
- **(Active) Advisor Fund Group** — auto-generated on acceptance; links the fund and the advisor entity.
- **Advisor Fund Dashboard** — lists an advisor's subscriptions in a fund. **Advisor Home Dashboard** — lists all accessible opportunities.
- **Advisor Subscriptions** — subscriptions tagged to a specific advisor entity.

## Pricing & packaging
**Not charged at MVP** (Dec 2024 release). Per the GTM training, the strategy was to onboard as many customers as possible to gather insights, then "pursue RIAs as paying customers" in 2025 with pricing for premium features. No published price list yet — flag as a data gap. Source: [[wiki/sources/aaa-gtm-training|AAA GTM Training]].

## Implementation notes
- **Setup prerequisite**: enable the "Enable Advisor workflow" / Advisor Group feature switch in the **Admin Portal** to expose the "Advisor Group" tab in a FundSub environment.
- **CS setup flow**: enable the feature switch → join the fund as Anduin Support → invite the advisor group and add yourself → open the email invitation and create the advisor entity per request, **always inputting the email domain** so other entity members can be auto-added.
- For existing funds, toggling "Enable Advisor workflow" off and on activates the Advisor Tag column without data loss.
- Full how-to articles published on HelpJuice (`support.anduintransact.com/en_US/advisor-advantage`); see [[wiki/sources/aaa-user-guide|AAA User Guide]].

## Known limitations
- No published pricing for the productized/paid tier (free at MVP).
- Some HelpJuice user-guide articles (advisor entity creation, invitation acceptance) are flagged "Needs update" and may lag current UX.
- Q4 2025 enhancements targeted known fund-manager pain points: difficulty setting up an advisor entity on the advisor's behalf, inability to manage the advisor group from the FundSub dashboard, and inability to delete test advisor groups.
- Reporting-by-RIA and fund-level progress tracking were post-MVP/archived items — confirm current availability before promising them.

## Features & sub-modules
Capabilities are documented inline above. AAA is delivered through [[wiki/products/fundsub|FundSub]] (GP side) and the standalone Advisor Advantage app (advisor side); signature features overlap with [[wiki/products/e-signature|E-signature]].

## Related customers
- [[wiki/customers/cerity-partners|Cerity Partners]] — uses AAA + FundSub + E-signature (Schwab DocuSign workflow).

## Sources
- [[wiki/sources/aaa-product-brief|AAA Product Brief]] (RIA brief, 2024) — who RIAs are and the business case.
- [[wiki/sources/aaa-sales-deck|AAA Sales Deck (Demo Screens)]] (Jan 2026) — capabilities + permission model.
- [[wiki/sources/aaa-gtm-training|AAA GTM Training]] (Nov 2024) — GTM motion, roadmap, pricing posture.
- [[wiki/sources/aaa-cs-training|AAA CS Demo + Training]] (Jan 2026) — setup, data model, troubleshooting.
- [[wiki/sources/aaa-user-guide|AAA User Guide]] (HelpJuice index) — end-user how-to articles.
- [[wiki/sources/aaa-advisor-tags|AAA Advisor Tags]] (2025) — GP→advisor tag communication.
- [[wiki/sources/aaa-advisor-subscription-assign|Assign/Unassign Subscriptions to Advisor Entities]] (Oct 2025).

## Related
- [[wiki/products/fundsub|FundSub]] — AAA's GP-side workflow lives here.
- [[wiki/products/investor-access|Investor Access]] — LP passport advisors use for auto-fill.
- [[wiki/products/e-signature|E-signature]] — one-envelope & Schwab custodian signing.
- [[wiki/products/investor-data-management|IDM]] — fund-side data management (GP-side counterpart context).
