---
type: product
title: "E-signature"
status: GA
source_count: 7
last_updated: 2026-06-03
tags: [e-signature, signature, qes, aes, schwab, docusign]
---

## What it does
Anduin's electronic signature product supporting three tiers of e-signature (SES, AES, QES) for fund subscription workflows. Enables EU-regulated qualified signatures via DocuSign + IDnow, custodian-based signing via the Schwab DocuSign integration, and a native SES flow with post-signing edit capabilities.

## Key capabilities
- **Standard e-signature (SES)**: Anduin native signature for most fund subscription flows. Low overhead, no ID verification.
- **Advanced e-signature (AES)**: Identity-linked signature via GlobalSign eSeal for elevated assurance.
- **Qualified e-signature (QES)**: Highest eIDAS tier — legally equivalent to handwritten signature. Delivered via DocuSign + IDnow face-to-face video verification. Valid for EU entities requiring strict eIDAS compliance.
- **DocuSign integration**: Funds can choose DocuSign as their signature provider (instead of Anduin native). Supports SES, AES, and QES within DocuSign; covers subscription docs, tax forms, GP countersign, and additional docs.
- **Schwab custodian signing**: Advisor-initiated DocuSign workflow routing subscription docs through Schwab's Advisor Center (SAC). Requires per-RIA setup and Schwab addendum. Phone authentication; auto-CC to Schwab on completion.
- **Reuse signature pages**: Post-signing form edits without re-signature, if conditions met (SES only; same signers, fields, and values in signature pages). Requires Anduin activation per fund.

## Pricing & packaging
- **DocuSign SES/QES**: Charged per signature credits (not DocuSign envelope pricing). QES, SES, and LexisNexis credits tracked in Salesforce. Customers can purchase QES-only credits; GP countersign can be done offline (free) or via SES credits.
- A fund can have both QES and SES within a DocuSign environment.
- No pricing docs in the vault for native SES or AES; DocuSign/QES pricing referenced in [[sources/esignature-docusign-qes-faq]].

## Implementation notes

### Choosing a signature provider
- A fund must choose **either** Anduin native signing OR DocuSign — cannot mix on the same fund.
- DocuSign is required for QES (Anduin cannot be a Qualified Trust Service Provider on the European Trust List).
- DocuSign SES batch countersigning is available; QES batch countersign is NOT (individual consent required).

### DocuSign/QES fund setup
1. In FundSub fund settings, choose DocuSign as signature provider (enables SES for all 4 processes).
2. To enable QES per-process, check the `QES (Qualified e-signature with IDnow)` checkbox.
3. GP countersign forced to match LP's signature type under QES (forced logic).
4. Available authentication: Email OTP (all funds), Access code (DocuSign funds only).

### Schwab custodian signing setup (5 components, not sequential)
1. **RIA + Anduin**: Anduin creates DocuSign sender email (`{ria-name}-docusign-sender@anduintransact.com`); RIA adds to Schwab Advisor Center.
2. **Schwab addendum**: RIA obtains Schwab approval for Anduin as third-party DocuSign provider via SAC.
3. **Technical validation**: Anduin sends test envelope to Schwab; Schwab approves before go-live.
4. **Digitization setup**: Schwab form PDF must have `[Schwab form]` in filename. Logic gating required.
5. **Fund app setup**: DocuSign must be enabled per fund. Start 2–3 weeks before first live use.

### Reuse signature pages
- Requires Anduin activation; then enabled by Fund Admin in Fund Settings.
- SES only — AES and DocuSign flows not compatible.
- Conditions: same number of signers, same signature field type/location/count, unchanged form field values within signature pages.
- No new signature certificate generated for updated version; free-text changes not auto-detected (manual review required).

## Known limitations
- A fund cannot use both Anduin native signing and DocuSign on the same fund.
- QES batch countersign not available (DocuSign constraint).
- Safari + date picker fields known to freeze — advise Chrome or Edge for DocuSign users.
- Schwab workflow deployed for Cerity Partners and Blue Arc; RIA-specific requirements may vary.
- Reuse signature pages: SES only; no AES or DocuSign support.
- AES (GlobalSign eSeal) implementation details not fully documented in the vault — no dedicated implementation guide.

## Features & sub-modules
- [[concepts/qes-aes-compliance|QES/AES/SES compliance]] — eIDAS signature tier framework
- Schwab integration (see [[sources/esignature-schwab-implementation-guide]])
- Reuse signature pages (see [[sources/esignature-reuse-signature-pages]])
- DocuSign integration (see [[entities/docusign]])

## Related customers
- [[customers/cerity-partners]] — Schwab workflow deployed for this RIA

## Sources
- [[sources/esignature-docusign-qes-faq|DocuSign and QES — Internal FAQ]] — faq (trust 4, Jan 2026)
- [[sources/esignature-schwab-implementation-guide|Internal Guide: Schwab Signature Workflow]] — implementation-guide (trust 2)
- [[sources/esignature-reuse-signature-pages|User Guide: Reuse Signature Pages]] — client-training (trust 7)
- [[sources/esignature-schwab-cerity-training|Schwab Training — Cerity Partners]] — client-training (trust 7)
- [[sources/esignature-whitepaper|Anduin e-Signature Guide Whitepaper]] — security-whitepaper (trust 8)
- [[sources/esignature-docusign-sales-deck|Anduin x DocuSign Sales Deck]] — sales-deck (trust 5)
- [[sources/esignature-sample-signed-documents|Sample SES/AES/QES Signed Documents]] — note (trust 10)

## Related
- [[products/fundsub|FundSub]] — subscription platform context for all e-signature workflows
- [[products/aaa|AAA]] — Advisor Advantage interface used in Schwab flow
- [[entities/docusign|DocuSign]] — integration partner for QES and Schwab workflows
