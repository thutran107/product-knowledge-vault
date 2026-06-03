---
type: concept
title: "QES/AES/SES Compliance (eIDAS Signature Types)"
source_count: 2
last_updated: 2026-06-03
tags: [compliance, e-signature, qes, aes, signature, docusign]
---

## Definition
The eIDAS regulation (EU 2014/910) governs electronic signatures in the European Union and defines three tiers of electronic signature, each with increasing legal assurance and identity verification requirements. Anduin supports all three types through different technical implementations.

## Key dynamics

| Type | Full Name | Identity Verification | Legal Weight | Anduin Implementation |
|------|-----------|-----------------------|--------------|----------------------|
| SES | Standard Electronic Signature | None required | Basic | Anduin native signature |
| AES | Advanced Electronic Signature | Signer-linked, verifiable | Medium — burden of proof on signer | GlobalSign eSeal |
| QES | Qualified Electronic Signature | Face-to-face video ID check (IDnow) | Highest — legally equivalent to handwritten signature; burden of proof on challenger | DocuSign + IDnow |

### SES
- Most basic form; does not guarantee signer identity.
- Anduin's default signature type for most fund subscription flows.
- Required for the "Reuse Signature Pages" feature — AES and DocuSign flows are not compatible with that feature.

### AES
- Uniquely linked to the signer, capable of identifying them.
- Anduin provides AES through GlobalSign eSeal.
- In disputes, burden of proof lies with the signer and the requester.

### QES
- Strictest form; same legal value as a handwritten signature under eIDAS.
- Requires face-to-face video identity verification via IDnow (a DocuSign partner).
- IDnow VideoIdent: available 24/7, takes a few minutes, valid for 12 months per verification.
- Anduin cannot be listed as a Qualified Trust Service Provider on the European Trust List directly, so QES is delivered via Anduin's DocuSign integration.
- A tamper-evident seal is applied to QES-signed documents; any modification breaks the seal.
- Batch countersigning is NOT available for QES (individual consent required by DocuSign).
- GP countersign is forced to match LP's signature type — if LP signs QES, GP must countersign QES.

### Choosing between types
- **SES**: standard fund subscription flows, non-EU investors, advisor-driven flows (Schwab).
- **AES**: EU investors who need higher assurance but not full QES.
- **QES**: EU entities requiring highest eIDAS compliance, or clients who already use/prefer DocuSign.

## Evidence & examples
- Anduin offers a Google Drive folder of sample SES, AES, and QES signed documents for CS demonstrations: [[wiki/sources/esignature-sample-signed-documents]].
- DocuSign SES and QES pricing are loaded into Salesforce (per-credit model, not DocuSign envelope pricing). A fund can have both QES and SES within DocuSign on the same fund environment.
- A fund cannot simultaneously use Anduin native signature (SES) and DocuSign on the same fund — must choose one signature provider.

## Tensions & open questions
- QES pricing was described as "in discussion as of July 2023" in older FAQ content; current pricing appears to be in Salesforce as of Jan 2026 update but exact pricing tiers not documented in the wiki.
- AES via GlobalSign eSeal is mentioned but not deeply documented — no dedicated implementation guide in the vault.

## Related
- [[wiki/products/e-signature]] — parent product
- [[wiki/sources/esignature-docusign-qes-faq]] — most authoritative source (trust 4, Jan 2026)
- [[wiki/sources/esignature-reuse-signature-pages]] — SES-only constraint documented here
- [[wiki/entities/docusign]] — QES delivery mechanism
