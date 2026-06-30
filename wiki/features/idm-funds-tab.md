---
type: feature
title: "IDM Funds Tab (Fund Structure & Capital Flow)"
parent_product: "IDM"
status: GA
source_count: 1
last_updated: 2026-06-30
confidence: medium
tags: [idm, implementation, data-management]
---

## What it does
The Funds tab is IDM's fund/capital-side data model — a commitment-tracking and cash-flow ledger that answers "where did the money go, and who committed what?" It models the post-close world of capital calls, distributions, and reporting, distinct from the onboarding/intake world of fund subscriptions.

## How it works
A four-object chain, each object with exactly one job — **"subscriptions onboard, FLEs hold, investments relate, transactions move":**

| Object | Role |
|--------|------|
| **Fund subscription** | Onboarding/intake container (paperwork + investor experience). One subscription can feed multiple FLEs. |
| **Fund legal entity (FLE)** | The legal boundary that holds capital and positions. Day-to-day operations live here. |
| **Investment** | Links exactly **one investor to one FLE**. The linchpin — transactions cannot exist without it. |
| **Transaction** | Records actual money movement; always a child of an investment. |
| **Fund family** | *Optional* umbrella grouping related FLEs for aggregated commitment/cash-flow views. |

- **Six transaction types:** capital call, distribution, investment, transfer in, transfer out, redemption (+ "other").
- **Five investment-creation methods:** manual UI, batch, API, fund-suborder sync, pass-sub-import.
- **Automatch rules** govern fund-suborder sync — they decide whether incoming data spawns a new investment or attaches to an existing one. Misconfiguration silently duplicates/misroutes records.
- **Awaiting Sync** is a holding zone; data converts into IDM investments/transactions only once orders reach a firm-configured **status threshold (defaults to "submitted")**, so only GP-reviewed data lands.
- **Investment active/inactive status** gates inclusion in document distribution and communications while preserving exited investors' historical access.
- **Locked amounts:** fund-sub-sink transaction amounts are locked from edits after import (audit trail); corrections happen upstream.

## Use cases
- Track total commitment and cash flows per FLE and aggregated per fund family.
- Power post-close operations: capital calls, distributions, document delivery, investor reporting.
- Support funds run partly **outside Anduin** via a manual FLE/fund-family creation path (the digitization team auto-creates FLEs on the clean, Anduin-onboarded path).
- Surface fund participation in the client dashboard's fund column; create investments directly from that view.

## Pricing & availability
Part of IDM. No tier gating specific to the Funds tab documented in the training video. (Financial Data permission — which gates LP report access — is Portal-exclusive; see [[features/idm-contacts]].)

## Known limitations
- **Communication types are firm-level only** — they cannot be created/edited at the FLE level (a deliberate governance choice to prevent per-fund drift).
- Metadata not passed through subscription (total commitment, fees, balance, tax data) must be **manually populated**; data quality depends on operator discipline.

## Sources
- [[sources/idm-funds-tab-training-video]] — Funds tab structure + demo (cs-training, trust 6)

## Related
- [[products/investor-data-management|IDM]] — parent product
- [[features/idm-clients-tab]] — the investor/client side that the investment object bridges to
- [[features/idm-contacts]] — communication types/matrix referenced here
- [[concepts/anduin-object-model]] — IDM fund-side object model
- [[concepts/investor-onboarding-workflow]]
