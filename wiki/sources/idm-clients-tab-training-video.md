---
type: source
title: "IDM — Clients Tab: Profiles, Mapping & Import (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-data-management/4-clients-tab-introduction-and-demo/"
products: [IDM]
target_audience: CS
onboarding_required: Yes
tags: [idm, implementation, data-management, compliance]
---

## Summary
The longest module (34:29) — a deep walkthrough of the **Clients tab**, IDM's single source of truth for investor relationships. Covers the mandatory creation hierarchy (client → investment entity → profile → documents), back-end DG form-to-form mapping for historical funds, sequential bulk import, the cross-fund commitment dashboard, profile-design scoping technique, document AI-scanning rules, the new investor-chosen profile model, batch risk assessments, and custom exports.

## Key Takeaways
- **Client tab is the whole system.** "This is the most important tab of the IDM… where we store everything investor related." Everything downstream depends on it.
- **Creation order is mandatory:** client → investment entity → profile → documents. No single template collapses the steps.
- **DG mapping must precede import.** The back-end DG team completes form-to-form field mapping for each *historical* fund before data pulls in correctly; **all future funds map automatically** once IDM is live — so the pain is front-loaded by design.
- **Auto-sync has status limits.** After initial manual import, IDM auto-syncs back only for **submitted / countersigned / distributed** investors; pending/in-progress must be handled manually.
- **Scope profiles from the subscription agreement.** Don't ask clients "what data do you want to track?" — they don't know. Anchor to their existing subscription agreement, then layer CRM/risk fields.
- **Master profile** consolidates overlapping + unique fields across multiple funds; **build timeline is variable** (depends on complexity + client back-and-forth) — do not commit to a fixed timeline.
- **Cross-fund commitment view** (consolidated commitment across all funds per IE) is "something only IDM can provide at the moment." Client-merging feature cleans duplicate profiles without losing history.
- **Document name exact-match rule:** a slight name difference for the same requirement across funds creates **two separate document records**, polluting the investor record. AI scanning only activates for pre-configured document types. New **batch expiration-date alignment** feature added.
- **Investor-chosen profile at subscription:** investors now self-select their investment entity via a profile-selection banner at subscription, rather than the fund pre-assigning — because funds often don't know which entity a returning LP will use.
- **Batch risk assessments** across multiple IEs with proof docs + audit trail; **gap:** no automated anniversary reminders yet ("not yet" for the next-cycle prompt).
- **Custom exports** (e.g., per-investor tax reports) turn IDM into a reporting engine; custom IDs at client and IE levels.

## Connections
- Primary source for the new [[features/idm-clients-tab|IDM Clients Tab]] feature page.
- DG form-to-form mapping + document exact-match enrich [[concepts/data-mapping]].
- Compliance/document-tracking + risk assessments support [[products/investor-data-management]] (compliance workflow).
- Profile reuse / investor-chosen profile links to [[concepts/investor-onboarding-workflow]] and [[features/idm-contacts]].

## Conflicts & Supersessions
- No conflicts. The "all-contacts tab is largely a Portal feature, not core IDM" aside is a useful disambiguation, consistent with [[sources/investor-portal-contact-management]].

## Raw Notes
- 34:29 / 9 sections. Dated "Unknown".
- Example client "Axl": hybrid profile of subscription-derived fields + bespoke risk-assessment table mirroring their CRM; per-investor tax report for annual regulatory filing.
- Known gap explicitly stated: automated assessment reminders not built ("…not able to automatically generate another one for March 31st 2027. Not yet.").
