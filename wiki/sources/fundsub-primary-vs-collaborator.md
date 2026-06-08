---
type: source
title: "Distinction Between Primary Investor and Collaborator in FundSub"
date_ingested: 2026-06-08
as_of_date: 2025-11-10
source_type: gtm-training
trust_level: 5
original_file: raw/Notion page 2a73f653b1df80669250d0674242470c
products: [FundSub]
target_audience: CS
onboarding_required: No
tags: [fundsub, implementation]
---

## Summary
Concise internal guide clarifying the distinction between Primary Investor and Collaborator in FundSub orders. Useful for CS to explain to GPs how to structure investor access during onboarding.

## Key Takeaways
- Every order has exactly one Primary Investor (the first person invited).
- Collaborators are optional and have the same functional permissions as the Primary.
- Key differences are around removal and promotion rights, not day-to-day access.
- In practice, a placeholder Primary is often set during data entry, then replaced (via promotion) with the actual investor once the subscription is complete.

## Permissions (same for Primary and Collaborators)
- Fill out forms
- Upload documents
- Leave comments
- Send signature requests
- Invite additional collaborators
- Remove other collaborators from the order
- Perform all actions required to complete the subscription

## Key Differences

| | Primary Investor | Collaborator |
|--|-----------------|-------------|
| Remove themselves | ❌ Cannot | ✅ Can |
| Promote to Primary | N/A | ❌ Cannot self-promote |
| Promote others | ✅ Can promote a Collaborator to Primary | ❌ Cannot |

## Common Workflow Pattern
1. Initial data entry contact is set as Primary (often an admin or counsel).
2. They fill out forms or assist with documents.
3. Once subscription is complete, the actual investor (often a Collaborator) is promoted to Primary.
4. This ensures subscription form data accurately reflects the real investor while allowing multiple parties to assist.

## Connections
- [[wiki/products/fundsub]]
- [[wiki/sources/anduin-investor-guide-may-2025]] — LP-facing guide also covers collaborator invitation flow

## Conflicts & Supersessions
None found. First dedicated source on this distinction.

## Raw Notes
- This was labeled as a GTM Training Deck in Notion but contains spec-level precision on permission rules.
