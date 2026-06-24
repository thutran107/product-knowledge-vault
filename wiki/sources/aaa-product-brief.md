---
type: source
title: "AAA (Advisor Advantage) — Product Brief / RIA Product Brief"
date_ingested: 2026-06-15
as_of_date: 2024-12-31
source_type: note
trust_level: 10
original_file: Notion — RIA product brief (dc9264629c454816a004ae5ce8582426)
products: [AAA]
target_audience: Sales + RM
onboarding_required: Yes
tags: [aaa, advisor, ria, wealth-management, product-strategy]
---

## Summary
The foundational product brief for Advisor Advantage (internally "RIA"), explaining who Registered Investment Advisors (RIAs) are, the problems they faced operating on Anduin as of 2024, and the goals of building a dedicated advisor experience. RIAs are LP-side service providers (wealth managers, advisors) who act on behalf of LPs to fill out subscription documents. The brief makes the business case: supporting RIA personas lets fund managers invite more advisors and onboard more investors.

## Key Takeaways
- **RIA definition**: A Registered Investment Advisor is an LP-side service provider role — representatives of the LP who fill out subscription documents and prepare supporting docs on the LP's behalf. Titles vary by region (wealth manager, advisor, etc.).
- **The 2024 problem**: Anduin historically focused on the GP side of fund onboarding. RIAs faced two problems: (1) inability to create subscriptions for their LP if none existed, and (2) an inefficient flat-list view to manage orders created for their LPs.
- **Risky workaround**: As a stopgap, many fund managers invited RIAs into the GP side as a custom group (restricting countersign, hiding reporting tabs). This is error-prone and risks GPs over-exposing confidential fund information to RIAs (which could leak to investors).
- **Market validation**: As of 2024, Anduin recorded 365 RIAs on the platform — a **222% growth** YoY (113 → 365 RIAs, May–Aug window), serving 804 LPs (79% growth) across 292 funds (68% growth).
- **Three personas**: Advisors (manage ~50 client profiles, no visibility into other advisors' work), Advisor Managers (oversee multiple RIA members for operational efficiency), Fund Managers (want to attract more RIAs without compromising fund confidentiality).
- **Three goals**: (1) let RIA advisors efficiently create/manage orders across multiple funds, (2) let RIA managers manage their advisors, (3) let GPs onboard more RIAs to their funds.

## Connections
- Primary source for [[products/aaa|AAA (Advisor Advantage)]] — establishes the "what" and "why."
- Closely related to [[products/fundsub|FundSub]] (the advisor workflow lives inside FundSub) and [[products/investor-access|Investor Access]] (the LP-side passport advisors leverage for auto-fill).
- The "do not over-expose fund info to RIA" concern connects to [[concepts/configuration-vs-permission|Configuration vs Permission Model]] and [[concepts/user-roles|User Roles]].

## Conflicts & Supersessions
- None. This is the earliest authoritative framing of AAA; later decks (sales, GTM, CS training) extend it with feature detail and updated stats (the Oct 2024 GTM deck cites 630 RIAs / 13,670 subscriptions, a more recent count than this brief's 365).

## Raw Notes
- Source row in the Knowledge Library has no as-of date; the linked Notion page ("RIA - product brief") was last viewed 2024-12-31 and its data covers May–Aug 2024 — dated here as 2024-12-31.
- Document Type in Notion = "General Knowledge Page" (mapped to `note`, trust 10).
- Internal terminology note: "RIA" is the engineering/internal name; "Advisor Advantage" (AAA) is the go-to-market name. The product home in Notion is "RIA home ✨."
- MVP estimation and Phase-1 Figma designs are linked from the brief (Google Sheets + Figma, not ingested).
