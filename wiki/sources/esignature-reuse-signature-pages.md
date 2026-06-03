---
type: source
title: "User Guide — Allowing Post-Signing Changes Without New Signatures"
date_ingested: 2026-06-03
as_of_date: 2025-09-16
source_type: client-training
trust_level: 7
original_file: notion://2223f653b1df80dc988cdfdb4612c77b
products: [E-signature, FundSub]
target_audience: All teams
onboarding_required: No
tags: [e-signature, signature, fundsub, implementation]
---

## Summary
User guide for the "Reuse Signature Pages" feature, which allows post-signing modifications to subscription forms without requiring new investor signatures, provided specific conditions are met. SES-only feature requiring Anduin activation. Covers setup, end-to-end workflow, reuse conditions, and limitations.

## Key Takeaways
- **Feature must be activated by Anduin** before Fund Admins can enable it in Fund Settings.
- **7-step workflow**: investor signs (V1) → GP requests changes → LP edits → system evaluates reusability → LP consents → document review → auto-submit (V2).
- **Conditions for reuse** (ALL must be met):
  - Anduin Simple E-signature (SES) only — AES and DocuSign flows not supported.
  - Number of required signers unchanged.
  - Signature field type, location, and count unchanged.
  - Form field values within signature pages unchanged (e.g., commitment amount not edited).
- If conditions not met, investor must re-sign; only the e-sign option is shown.
- System **auto-submits** V2 subscription unless fund has manual submission configured.
- **No new signature certificate** generated for the updated version.
- Free-text changes are not auto-detected — reviewer must manually compare signature pages.
- Feature is for **online subscriptions only**.

## Connections
- [[wiki/products/e-signature]] — describes this feature and its constraints
- [[wiki/products/fundsub]] — feature applies within FundSub subscription workflow
- [[wiki/concepts/qes-aes-compliance]] — limitations tied to SES-only scope; AES/QES not compatible

## Conflicts & Supersessions
None. No prior wiki page covered this feature.

## Raw Notes
- Parent page in Notion: Fund Onboarding Home
- The guide includes confirmation that an optional email notification can be sent when a subscription is updated.
- Question at bottom of doc: "Can we ask QA to support with the above? It seems out of DS scope." — suggests feature was recently shipped at time of writing.
