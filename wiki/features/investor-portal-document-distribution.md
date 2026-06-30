---
type: feature
title: "Document Distribution (Group / Private / Split & Share)"
parent_product: "Investor Portal"
status: GA
source_count: 2
last_updated: 2026-06-30
tags: [investor-portal, implementation, sales-motion]
---

## What it does
Post-close distribution of LP documents (K-1s, capital call notices, quarterly reports) through three methods matched to the file↔recipient shape, with AI-assisted matching, communication-type permissioning, and a full audit trail. Also a core [[products/engagement-hub|Engagement Hub]] capability — Portal inherits it.

## How it works
| Method | Shape | Notes |
|--------|-------|-------|
| **Group Share** | one file → many | quarterly updates; AI auto-suggests doc types on upload |
| **Private Share** | unique file → each | capital calls; **AI matching** pairs files to entities by name/content (review/correct exceptions) |
| **Split & Share** | one bundled PDF → split → routed | K-1 packages; split modes = ad-hoc, even, **marker-based**; hands off to Private Share matching |

- **Recipient targeting:** target **Specific Investment Entities** (recommended) so new contacts added later **auto-inherit access** to past distributions; or specific contacts / contact lists (static).
- **Communication Type filter** ensures only contacts assigned that type for the entity receive the document.
- **Delivery controls:** scheduled future-dated access, immediate or delayed email, confidentiality **watermarks**, dynamic placeholders / saved templates. Read-only Contact Review step; save-progress for staged workflows.
- **Package View** reconstructs full distribution context after the fact; **Remove** revokes access immediately (no grace period); Manage Recipients swaps contacts post-share. Package name is internal-only.

## Use cases
Quarterly report blasts, capital-call notice runs, and K-1 season — absorbing the manual "scissors and spreadsheets" splitting/matching work fund admins used to do by hand.

## Pricing & availability
Included in Investor Portal and Engagement Hub. Document/communication types and AI keywords are configured in Portal settings ([[sources/investor-portal-settings-portal-plan-training-video]]).

## Known limitations
- AI **confidence scores and duplicate detection** not yet live — every AI match should be human-reviewed before send (errors propagate to all recipients).

## Sources
- [[sources/investor-portal-document-distribution-training-video]] — methods + demo (cs-training, trust 6)
- [[sources/investor-portal-settings-portal-plan-training-video]] — document/communication type config (cs-training, trust 6)

## Related
- [[products/investor-portal]] — parent product
- [[products/engagement-hub]] — also an EH feature; Portal inherits it
- [[features/idm-contacts]] — communication matrix that drives recipient permissioning
- [[features/investor-portal-communications]] — sibling messaging channel
