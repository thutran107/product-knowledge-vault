---
type: source
title: "Investor Portal — Settings Part 2 (Portal Plan) (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-portal/4-settings-portal-plan/"
products: [Investor Portal]
target_audience: CS
onboarding_required: No
tags: [investor-portal, implementation, compliance, security]
---

## Summary
Portal-plan settings that must exist before workflows run: **document types** (drive AI classification), **communication types** (drive recipient permissioning), **Terms of Access** (versioned consent), and **email settings** (design presets + content templates per email type). The "Part 2" companion to the IDM-plan settings video ([[sources/idm-settings-training-video]]).

## Key Takeaways
- **Document Types drive AI automation:** mapping each portal doc type to an Anduin category + loading keywords is what powers AI auto-suggestion at upload. "The more accurate and complete these two fields are, the better the automation works."
- **Communication Types control recipient permissioning:** assigned at the **fund-legal-entity level and the individual-contact level**, they become the filter that narrows distribution recipients. A **default toggle** auto-adds a type to every new FLE (saves setup per fund).
- **Terms of Access = built-in, auditable consent:** a **blocking modal with no decline option** on every portal route (including direct links). Editing the **body text** after ≥1 investor has accepted **creates a new version** and forces a **re-acceptance policy** choice (require all to re-accept, or exempt prior-version acceptors); cosmetic edits don't. Replaces error-prone external consent tracking.
- **Email settings:** each of the **four outbound email types** has its own **design preset** and **content template**, configured separately (branding ≠ copy). Mobile/desktop preview; **send-test email** renders the actual preset+template combo before it reaches investors; multiple content templates per type supported.

## Connections
- Resolves the forward references from [[sources/idm-settings-training-video]] and [[features/idm-firm-settings]] — same email-template/design-preset machinery, Portal-plan side.
- Document/communication types underpin [[features/investor-portal-document-distribution]] and [[features/idm-contacts|the communication matrix]].
- Settings detail folded into [[products/investor-portal]] Implementation notes.

## Conflicts & Supersessions
- No conflict. Deepens the Settings material already summarized in [[sources/investor-portal-customer-training-guide]]; consistent with Platform white-labeling/email infrastructure.

## Raw Notes
- 15:06 / 9 sections. "Unknown" date.
