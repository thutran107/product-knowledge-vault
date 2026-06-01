---
type: product
title: "E-signature"
status: GA
source_count: 2
last_updated: 2026-05-26
tags: [e-signature, signature, qes, aes, schwab, docusign]
---

## What it does
Anduin's electronic signature product supporting standard e-signature as well as advanced (AES) and qualified (QES) signatures for regulated markets. Also enables custodian-based signing workflows (e.g., Schwab DocuSign) for RIA and advisor-driven subscription flows.

## Key capabilities
- Standard e-signature for subscription documents in FundSub.
- AES and QES for EU and regulated jurisdictions.
- Schwab DocuSign integration: advisor-initiated signing flow routing subscription docs through Schwab's custodian process (Alternative Investment Letter of Authorization).
- DocuSign used as the underlying provider for Schwab workflow; signers authenticate via phone number.
- Post-signing document delivery: automatically routes completed docs to Schwab after all parties sign.

## Implementation notes
Five setup components required per RIA firm onboarding (not sequential):
1. **RIA + Anduin setup**: Anduin creates a DocuSign sender email (`{ria-name}-docusign-sender@anduintransact.com`); RIA adds it to their Schwab Advisor Center (SAC) account.
2. **Schwab addendum**: RIA obtains Schwab approval for Anduin as third-party DocuSign provider via SAC → Account Management → Advisor-Owned DocuSign → "Anduin Transaction."
3. **Technical validation**: Anduin sends a test envelope to Schwab; Schwab approves before RIA can go live.
4. **Digitization setup**: Schwab form PDF must have `[Schwab form]` in filename to trigger the template. Logic gating question required to scope form to Schwab investors only.
5. **Fund app setup**: DocuSign must be enabled per fund. Form QA POC.

Setup effort: ~2–3 days; start 2–3 weeks before first live use. Internal testing backdoor: `+ceritypartners@anduin.fund` (Cerity). Email domain enforcement is hard-coded — only advisors with the registered RIA domain can initiate the Schwab flow.

Advisor Advantage (AAA product) is the GP-side interface where advisors manage investor subscriptions.

## Known limitations
- Schwab workflow deployed for Cerity Partners and Blue Arc; may have additional or varying requirements for other RIA firms.
- QES/AES compliance details require separate review of compliance sources.

## Features & sub-modules
- Schwab integration (sub-feature)
- QES/AES compliance

## Related customers
- [[wiki/customers/cerity-partners]] — Schwab workflow deployed for this RIA

## Sources
- [[wiki/sources/esignature-schwab-implementation-guide|Internal Guide: How to Set Up Schwab Signature Workflow]] — implementation guide (trust 2)
- [[wiki/sources/esignature-schwab-cerity-training|Schwab Integration — External Training Flow for Cerity Partners]] — client training (trust 7)

## Related
- [[wiki/products/fundsub|FundSub]] — context for e-signature workflows
- [[wiki/products/aaa|AAA]] — Advisor Advantage interface used in Schwab flow
