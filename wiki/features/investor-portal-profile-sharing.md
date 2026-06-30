---
type: feature
title: "Profile Sharing (LP Visibility into Their Records)"
parent_product: "Investor Portal"
status: GA
source_count: 1
last_updated: 2026-06-30
tags: [investor-portal, implementation, compliance]
---

## What it does
Gives LP contacts direct visibility into their own investment-entity records — identity, documents, contacts — that the GP holds in IDM, replacing the stale email-and-manual-entry loop. View-only today; an edit tier and two-way update workflow are roadmapped. Also a core [[products/engagement-hub|Engagement Hub]] feature (view live since Dec 2025); Portal inherits it.

## How it works
- **Two-gate access control:** (1) **firm-level section toggles** in Settings (Profile / Documents / Contacts — default on; turning a section off hides it entirely); (2) **per-contact permission** in the **communication matrix** (no access vs. view). Both gates must be open.
- The most intuitive entry point for granting access is the investment entity's own contacts view (access otherwise lives, less obviously, in the communication matrix).
- **Investor experience:** a **Profiles page** lists every accessible entity (card/list); the LP audits identity details, document expiry, and contacts without emailing anyone.
- **Subscription autofill:** "autofill using this profile" pre-populates a new subscription form (fields, documents, collaborator contacts) from a selected entity, with preview-before-select.

## Use cases
Let LPs self-verify what's on file and flag stale data; eliminate re-entry at subscription time via autofill — a continuous GP↔LP data-accuracy loop.

## Pricing & availability
Included in Investor Portal and Engagement Hub. Rests on IDM profiles ([[features/idm-clients-tab]]) and the contact matrix ([[features/idm-contacts]]).

## Known limitations
- **View-only today.** An **edit** permission tier will power the **LP Profile Update workflow** (GP-initiated review requests + LP-initiated change proposals). Cross-deck timeline nuance: EH page cites LP update requests Q3 2026; Portal page cites profile updates Q2 2026 — flagged for reconciliation, not overwritten.

## Sources
- [[sources/investor-portal-profile-sharing-training-video]] — profile sharing + roadmap (cs-training, trust 6)

## Related
- [[products/investor-portal]] — parent product
- [[products/engagement-hub]] — also an EH feature; Portal inherits it
- [[features/idm-contacts]] — communication-matrix gate
- [[features/idm-clients-tab]] — the IDM profiles being shared
- [[concepts/investor-onboarding-workflow]] — autofill / reuse
