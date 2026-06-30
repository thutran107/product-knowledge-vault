---
type: source
title: "IDM — Funds Tab: Structure & Demo (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-data-management/2-funds-tab-introduction/ + 3-funds-tab-demo/"
products: [IDM]
target_audience: CS
onboarding_required: Yes
tags: [idm, implementation, data-management]
---

## Summary
Two consolidated videos — the **Funds tab conceptual introduction** and the **hands-on demo** — covering how IDM models the fund/capital side of investor data. The Funds tab is a commitment-tracking and cash-flow ledger built on a four-object chain: **fund subscription → fund legal entity (FLE) → investment → transaction**. The demo walks fund-family/FLE creation, manual vs. auto creation, investment status, the Awaiting Sync holding zone, and how fund data surfaces in the client dashboard.

## Key Takeaways
- **Subscription ≠ FLE.** A fund subscription is an onboarding/intake container (paperwork + investor experience); a fund legal entity is the legal boundary that holds capital and positions. Conflating them "breaks reporting." One subscription can feed multiple FLEs.
- **Investment is the linchpin.** An investment record links exactly **one investor to one FLE**; transactions cannot exist without a parent investment. "Subscriptions onboard, FLEs hold, investments relate, transactions move."
- **Fund family = optional umbrella** grouping related FLEs for aggregated commitment/cash-flow views; day-to-day work happens at the FLE level.
- **Six transaction types:** capital call, distribution, investment, transfer in, transfer out, redemption (plus "other").
- **Five investment-creation methods:** manual UI, batch, API, fund-suborder sync, pass-sub-import.
- **Automatch rules govern sync integrity** — on fund-suborder sync they decide whether to spawn a new investment or attach to an existing one; misconfiguration silently duplicates/misroutes records.
- **Locked amounts = audit trail.** Fund-sub-sink transaction amounts are locked from edits after import; corrections must happen upstream.
- **Awaiting Sync is a policy decision, not a default** — data converts into IDM investments/transactions only once orders hit a firm-configured status threshold; **defaults to "submitted"** so only GP-reviewed data lands.
- **Investment active/inactive status** gates inclusion in document distribution and communications while retaining historical access for exited investors.
- **Manual creation path exists** because GPs run funds outside Anduin; the digitization team auto-creates FLEs on the clean path. Fund managers must manually populate metadata (total commitment, fees, balance, tax data) when not passed through subscription.

## Connections
- Primary source for the new [[features/idm-funds-tab|IDM Funds Tab]] feature page.
- Enriches [[concepts/anduin-object-model]] with the IDM fund-side object model (subscription / FLE / investment / transaction).
- Communication-types-at-firm-level detail links to [[features/idm-contacts]] (communication matrix) and [[sources/idm-contacts-training-video]].
- Supports [[products/investor-data-management]] Key capabilities + Implementation notes.

## Conflicts & Supersessions
- No conflicts. Net-new structural detail; consistent with FundSub onboarding material.

## Raw Notes
- Intro 3:06 / 8 sections; demo 9:57 / 8 sections. Both dated "Unknown".
- Worked example: Magma Property Fund 3 — a family trust subscribing onshore creates a Delaware investment; a capital call becomes a child transaction.
- "One real-world fund, one entity" design principle.
