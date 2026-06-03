---
type: source
title: "DocuSign and Qualified E-Signature (QES) — Internal FAQ"
date_ingested: 2026-06-03
as_of_date: 2026-01-16
source_type: faq
trust_level: 4
original_file: notion://d0f6cb7c7a9d4400a3e78bb474d15f46
products: [E-signature]
target_audience: Sales + RM, CS
onboarding_required: No
tags: [e-signature, docusign, qes, aes, compliance, signature]
---

## Summary
Comprehensive internal FAQ covering Anduin's DocuSign integration for SES and QES electronic signatures. Addresses the eIDAS signature type hierarchy, why Anduin uses DocuSign for QES, pricing model, security controls, edge cases, and setup steps. Last updated January 2026.

## Key Takeaways

### Signature types (eIDAS)
- **SES** — Standard Electronic Signature: basic, no ID verification. Anduin provides this natively.
- **AES** — Advanced Electronic Signature: identity-linked, signer-verifiable. Anduin provides via GlobalSign eSeal.
- **QES** — Qualified Electronic Signature: highest level under eIDAS, legally equivalent to handwritten signature. Requires face-to-face video ID check via IDnow (DocuSign partner). Anduin provides via DocuSign + IDnow.

### Why DocuSign for QES
- Anduin cannot be listed as a Qualified Trust Service Provider on the European Trust List.
- DocuSign (via IDnow) provides the required QES certification process.
- DocuSign is also favored by some customers who have already onboarded their staff to it.

### Target customers for DocuSign/QES
- EU entities wanting eIDAS-compliant fund subscription signatures.
- Clients who already use or prefer DocuSign as a signing solution.

### Pricing
- Charged per **signature credits**, not DocuSign's envelope pricing structure.
- QES, SES, and LexisNexis pricing are loaded into Salesforce.
- Customers do NOT need to purchase DocuSign SES to use QES — purchase QES credits only.
- GP countersign can be done offline (no credits) or via SES credits.
- Pricing calculator available via Google Sheets link in FAQ.

### Fund configuration
- A fund **cannot** have both Anduin Sign and DocuSign — must choose one.
- A fund **can** have both QES and SES within DocuSign on the same environment.
- 4 signature processes can use DocuSign: subscription doc, tax form, GP countersign, additional docs.
- QES must be enabled per-process via a checkbox in fund settings.

### Batch countersign
- **Available** for DocuSign SES — multiple docs consolidated in one envelope.
- **NOT available** for QES — individual consent required; DocuSign would invalidate batch QES.

### QES signing logic
- **Type 1 — Suggestive**: defaults to prior signature type for LP workflows (sub doc, tax form, additional doc). Requesters can override.
- **Type 2 — Forced**: GP countersign is forced to match LP's signature type. If LP used QES, GP must QES.

### ID verification (IDnow VideoIdent)
- Process: face-to-face video call with IDnow professional after signing in DocuSign (state name + show ID + phone verification).
- Available 24/7; takes a few minutes.
- Valid for **12 months** — signer does not need to re-verify within that period.
- Multiple concurrent signers on one request may experience delays (one-at-a-time).

### Signature certificate
- Issued on every completed DocuSign signature request (regardless of SES or QES).
- QES includes a tamper-evident seal — any document modification breaks the seal.
- Accessible to investors via "download all signed copies" or email option; to fund managers via "view all documents."

### Authentication options
- **Email OTP**: available on all funds. Enabled via internal tool switch — no setup for requesters.
- **Access code**: DocuSign funds only. Requester sets per-signer code at time of preparation.
- **Access code lockout**: signer locked out after 3 failed attempts; requester can send reminder or update code.
- Reassignment: LP signature — both original assigner AND assignee can reassign. GP countersign — fund admin only.

### Known issues & edge cases
- **Safari browser**: date picker fields can freeze Safari + macOS. Use Chrome or Edge instead.
- Disabling DocuSign mid-raise: only affects new signature requests (existing envelopes unaffected).
- Enabling DocuSign mid-raise: only new signature requests affected.
- **Test bot suffix**: append `X-MANUALTEST-HAPPYPATH` to signer name when testing QES with a bot in DocuSign.

## Connections
- [[wiki/products/e-signature]] — primary product reference for DocuSign and QES capabilities
- [[wiki/concepts/qes-aes-compliance]] — eIDAS framework, SES/AES/QES definitions
- [[wiki/entities/docusign]] — DocuSign as the integration partner and QES certification path
- [[wiki/sources/esignature-docusign-sales-deck]] — referenced in FAQ as the enablement slide deck

## Conflicts & Supersessions
None. This is the most current and detailed source on QES/DocuSign (updated Jan 2026, trust level 4).

## Raw Notes
- QES pricing deck: https://docs.google.com/presentation/d/1a8VA6iIpCU93Ibcm03Rqd-sIodxw7N4p8vPT6fscTmQ/edit
- SES pricing deck (same as DocuSign sales deck): https://docs.google.com/presentation/d/1CUuYo4PWyp43e7arZAqAdWop1mxL3glgGxHSgZc52wc/edit
- Pricing calculator: https://docs.google.com/spreadsheets/d/1MznJ1XHlIHjgdwR2uR1UPcEyx9kRz-qqukR_GZQuJkg/edit
- Canary admin portal for demo fund setup: https://portal-canary.anduin.app/itools/#/fundsubs
