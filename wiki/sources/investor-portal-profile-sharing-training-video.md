---
type: source
title: "Investor Portal — Profile Sharing (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-portal/3-profile-sharing/"
products: [Investor Portal, Engagement Hub, IDM]
target_audience: CS
onboarding_required: No
tags: [investor-portal, implementation, compliance]
---

## Summary
Profile Sharing gives LP contacts direct visibility into their own investment-entity records (identity, documents, contacts) that the GP holds in IDM — replacing the stale email-and-manual-entry loop. Access is gated at two layers; view-only today, with an edit tier and a two-way update workflow on the roadmap. Profile data also powers subscription autofill.

## Key Takeaways
- **Two-gate access control:** (1) **firm-level section toggles** in Settings (Profile / Documents / Contacts — default on; turning a section off hides it entirely regardless of other settings); (2) **per-contact permission** in the **communication matrix** (no access vs. view). Both gates must be open.
- **Access lives in the communication matrix** — a discoverability risk; the most intuitive entry point is the investment entity's own contacts view.
- **Investor experience:** a dedicated **Profiles page** lists every accessible entity (card/list view); the LP can audit identity details, document expiry, and associated contacts without emailing anyone.
- **Visibility is itself a workflow** — it surfaces stale data and prompts LP-initiated outreach before any formal request mechanism exists.
- **Subscription autofill:** selecting an entity and clicking "autofill using this profile" pre-populates a new subscription form (fields, documents, collaborator contacts); preview-before-select is a trust mechanism.
- **Roadmap:** an **edit** permission tier will power a full **LP Profile Update workflow** — GP-initiated review requests + investor-initiated change proposals (the "real destination"; visibility shipped first by design).

## Connections
- Primary source for [[features/investor-portal-profile-sharing]].
- Profile Sharing is also an [[products/engagement-hub|Engagement Hub]] feature (view live since Dec 2025); Portal inherits it.
- Rests on [[features/idm-contacts|IDM contacts/communication matrix]] and IDM profiles ([[features/idm-clients-tab]]); autofill ties to [[concepts/investor-onboarding-workflow]].

## Conflicts & Supersessions
- No conflict. Consistent with the EH page's "Profile Sharing" (view live Dec 2025; LP update requests roadmapped Q3 2026) and the Portal page's "Profile updates Q2 2026" note. **Minor timeline nuance** to reconcile across decks — flagged, not overwritten.

## Raw Notes
- 8:27 / 8 sections. "Unknown" date.
