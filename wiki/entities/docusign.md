---
type: entity
title: "DocuSign"
entity_kind: integration
source_count: 4
last_updated: 2026-06-03
tags: [e-signature, docusign, qes, integration, schwab]
---

## Overview
DocuSign is an electronic signature platform used by Anduin in two distinct integration contexts:
1. **QES/SES integration** — Anduin integrates with DocuSign to deliver Qualified (QES) and Standard (SES) electronic signatures for EU-regulated fund subscription workflows via DocuSign + IDnow.
2. **Schwab custodian signing** — Anduin uses DocuSign as the underlying provider for the Schwab Advisor Center signing workflow, routing subscription documents through Schwab's DocuSign template requirements.

## How it integrates with Anduin

### QES/SES signing path
- Fund admins choose DocuSign as the signature provider in FundSub fund settings (alternative to Anduin native signing).
- DocuSign provides the signing interface for subscription docs, tax forms, GP countersign, and additional docs.
- QES requires DocuSign + IDnow video identity verification (IDnow is a DocuSign partner).
- Pricing: Anduin charges per-signature credits (not DocuSign envelope pricing); QES, SES, and LexisNexis credits loaded into Salesforce.

### Schwab custodian signing path
- Anduin creates a DocuSign sender email per RIA firm (`{ria-name}-docusign-sender@anduintransact.com`).
- RIA adds that sender to their Schwab Advisor Center account.
- DocuSign template carries: SMS authentication requirement, Document Visibility, Auto-CC to Schwab.
- Signer authenticates via phone number; signed docs auto-delivered to Schwab after all parties sign.

## Key constraints
- A fund cannot have both Anduin native signature and DocuSign simultaneously — must choose one.
- Batch countersigning is NOT available for QES (individual consent required by DocuSign).
- DocuSign SES batch countersign IS available.
- Safari browser has a known issue with date picker fields — users should use Chrome or Edge.

## Sources
- [[wiki/sources/esignature-docusign-qes-faq]] — comprehensive FAQ (trust 4, Jan 2026)
- [[wiki/sources/esignature-docusign-sales-deck]] — sales positioning deck
- [[wiki/sources/esignature-schwab-implementation-guide]] — Schwab/DocuSign setup guide (trust 2)
- [[wiki/sources/esignature-schwab-cerity-training]] — Schwab/DocuSign client training

## Related
- [[wiki/products/e-signature]]
- [[wiki/concepts/qes-aes-compliance]]
- [[wiki/customers/cerity-partners]] — first RIA deployed on Schwab/DocuSign workflow
