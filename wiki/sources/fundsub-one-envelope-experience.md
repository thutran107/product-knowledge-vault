---
type: source
title: "FundSub — One Envelope Experience for Investors"
date_ingested: 2026-05-11
as_of_date: 2025-03-18
source_type: note
trust_level: 10
original_file: notion://1b53f653-b1df-806d-a3d4-d521b09348ac
products: [Fundsub]
target_audience: All teams
onboarding_required: No
tags: [fundsub, signature, e-signature, lp-experience]
---

## Summary
Feature overview deck (October 2024) covering FundSub's One Envelope experience — a workflow that bundles all subscription documents (sub agreement, PPM, investor questionnaire, tax forms) into a single e-signature package for the LP. Covers preparer flow, signer flow, DocuSign integration, and signing certificates. Targeted at all teams.

## Key Takeaways
- **Core concept:** All subscription and compliance documents sent to the LP in one envelope; LP signs once rather than across multiple sequential envelopes.
- **Designed for:** Private wealth customers (wealth managers + clients), RIAs, endowments — any fund where a preparer bundles docs before sending to a signer.
- **Preparer flow:** Collect digitized docs → Bundle into One Envelope → Add recipients (auto-populated from form-building; additional recipients can be added for uploaded files) → Add authentication method (AES if configured) → Tag fields (auto-tagged for digitized forms; manual tagging for uploaded files) → Final review → Send.
- **Signer flow:** Email notification → Secure link → Private signing view listing all pending documents → Option to reassign entire request → Review → Sign (highlighted fields).
- **Post-signature options:** Cancel request (if corrections needed before completion); "Mark as Complete" lets FMs close the envelope even if some recipients haven't signed.
- **DocuSign integration:** For funds with DocuSign enabled, signing occurs inside DocuSign interface. Signed documents stored securely upon completion.
- **Signature type choice:** For funds with both SES and QES enabled, the requester selects which method the signer must use.
- **Signing certificate:** Auto-generated and attached to each signed document; issued by DocuSign or AnduinSign depending on the signing method used.

## Connections
- [[wiki/products/fundsub|FundSub]] — One Envelope is a core FundSub signing capability
- [[wiki/products/e-signature|E-signature]] — QES/SES/AES methods and DocuSign integration
- [[wiki/concepts/investor-onboarding-workflow|Investor Onboarding Workflow]] — One Envelope is a key step in the LP-facing signing experience

## Conflicts & Supersessions
None. Slide deck dated October 2024; Notion page dated March 2025 — content appears stable across that period.

## Raw Notes
- Google Slides: https://docs.google.com/presentation/d/1f_JakC0S9kGTDNHHwHurQ3lb9ODjGNGpakC0ucmkfgI
- Slide header: "October 2024"; source page as_of_date set to 2025-03-18 (Notion metadata date).
