---
type: source
title: "Investor Portal — Document Distribution & Management (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-portal/1-document-distribution-and-management/"
products: [Investor Portal, Engagement Hub]
target_audience: CS
onboarding_required: No
tags: [investor-portal, implementation, sales-motion]
---

## Summary
Walkthrough of post-close LP document distribution. Three methods cover distinct file↔recipient shapes: **Group Share** (one file to many), **Private Share** (a unique file per recipient, AI-matched), and **Split & Share** (one bundled PDF cracked open and routed). Recipient targeting, AI matching, delivery controls, and the Package View audit trail are covered.

## Key Takeaways
- **Three methods, matched to distribution shape:** Group Share (same file → many), Private Share (different file → each, **AI matching** by file name/content), Split & Share (one bundled file → split → routed; hands off to Private Share matching). Split modes: ad-hoc, even, and **marker-based detection**.
- **Entity targeting beats contact targeting.** Targeting **Specific Investment Entities** is recommended because new contacts added to an entity later **automatically inherit access** to past distributions — no manual rework when investor teams change. Specific contacts / contact lists are static snapshots.
- **Communication Type = precision filter:** only contacts assigned to that communication type for the entity receive the document, preventing accidental disclosure at scale.
- **Fund-related vs. general documents** fork determines downstream recipient logic. AI auto-suggests document types on upload (review/confirm).
- **Delivery controls:** schedule future-dated access, delay or trigger email immediately, apply confidentiality **watermarks**, compose with dynamic placeholders or saved firm templates. Contact Review step is read-only by design (deliberate pause before send). Save-progress enables staged, multi-person workflows.
- **Package name is internal-only** (LPs never see it) — treat as an audit-trail artifact.
- **Package View** reconstructs full distribution context (method, recipients, template, settings) after the fact. **Remove** cuts access immediately for all recipients (no grace period). Manage Recipients swaps LP contacts post-share.
- **Roadmap:** AI confidence scores + duplicate detection not yet live.

## Connections
- Primary source for [[features/investor-portal-document-distribution]].
- Communication-type filtering is configured in [[sources/investor-portal-settings-portal-plan-training-video]] and rests on the [[features/idm-contacts|IDM communication matrix]].
- Document Distribution is also a core [[products/engagement-hub|Engagement Hub]] feature; Portal inherits it.

## Conflicts & Supersessions
- No conflict. Adds method-level + AI-matching + Package View detail to the Document distribution bullet already on [[products/investor-portal]].

## Raw Notes
- 15:45 / 9 sections. "Unknown" date.
- Use cases by method: quarterly updates (Group), capital calls (Private), K-1 packages (Split & Share).
