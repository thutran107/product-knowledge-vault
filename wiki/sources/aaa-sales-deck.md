---
type: source
title: "AAA (Advisor Advantage) — Sales Deck (Demo Screens)"
date_ingested: 2026-06-15
as_of_date: 2026-01-06
source_type: sales-deck
trust_level: 5
original_file: Google Slides — Anduin Advisor Advantage [Demo screens] (1REYNjJCmWf1uGMo5YXIv8ofIX2Y-Wgatbsh7hD8ua04)
products: [AAA]
target_audience: Sales + RM
onboarding_required: Yes
tags: [aaa, advisor, ria, sales-motion, permissions, signature]
---

## Summary
The canonical demo-screen walkthrough of Advisor Advantage, split into Fund Manager efficiency, Advisor experience, and the permission system. It shows how GPs invite advisor entities to a fund, track and control RIA activity from the FundSub dashboard, and how advisors operate in a dedicated workspace with fund-level access controls. Includes the full two-tier permission model and a Q4 2025 enhancement section addressing fund-manager pain points.

## Key Takeaways
- **What AAA is** (per the deck's framing): "A dedicated onboarding platform for RIAs and Wealth Management teams, streamlining the investor onboarding process to invited funds on Anduin," letting advisor teams create/manage client subscriptions while preserving their entity's structure and permissions — and protecting the fund's private information during fundraising.
- **Fund manager controls (in FundSub)**: invite existing or new advisor entities; create an entity on the advisor's behalf or let them self-create; track RIA activation and per-advisor permissions; restrict an advisor group from creating new subscriptions in one click; see an "Advisor Group" column on the Master Dashboard; filter the dashboard by RIA; assign/unassign any subscription (created on FS, via CRM, or via IDM) to/from advisor entities.
- **Advisor tags**: GPs communicate custom statuses ("Custodian approve," "pending custodian approval") or notes to advisors via the Advisor's tags column; tags sync to the advisor's dashboard in Advisor Advantage. (See [[sources/aaa-advisor-tags|AAA Advisor Tags release note]].)
- **Advisor experience (Advisor Advantage app)**: one-time entity creation; fund-specific dashboards; fund-level advisor management (give access to all or a subset); per-fund permission roles (Admin sees all subscriptions + analytics, Member sees only their own); Opportunities dashboard across all accessible funds; entity user management.
- **Email-domain automation**: whitelisting the RIA firm's email domain auto-invites advisors who already have subscriptions in the fund and enables syncing created subscriptions to the Advisor Advantage dashboard.
- **Permission system (two tiers)**:
  - *Entity permission*: Entity Admin > Entity Manager > Entity Member.
  - *Fund-group permission*: Entity Admin (always has access) / Fund Group Admin / Fund Group Member — where members operate on their own subscriptions as the main LP.
- **Q4 2025 enhancements**: address fund-manager pain points — difficulty setting up an advisor entity on the advisor's behalf, inability to manage the advisor group from the FundSub dashboard, and inability to delete test advisor groups.

## Connections
- Primary capability source for [[products/aaa|AAA (Advisor Advantage)]].
- Assign/unassign capability corroborates the existing [[sources/aaa-advisor-subscription-assign|Assign/Unassign Subscriptions to Advisor Entities]] release note.
- Signature/custodian elements connect to [[products/e-signature|E-signature]] and the Schwab workflow ([[sources/esignature-schwab-implementation-guide|Schwab Signature setup]]).
- Auto-fill via investor passport connects to [[products/investor-access|Investor Access]].

## Conflicts & Supersessions
- None. Most recent AAA artifact (as-of 2026-01-06); extends the product brief and GTM deck with current demo screens and the finalized permission model.

## Raw Notes
- Slide content extracted via the Google Drive connector (full text available; screenshots are visual only).
- "Archived (do not use)" slides flagged Reporting-by-RIA and fund-level progress tracking as post-MVP items — treat as forward-looking, not shipped.
- onboarding_required: Yes (Sales + RM).
