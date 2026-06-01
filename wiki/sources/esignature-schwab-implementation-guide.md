---
type: source
title: "Internal Guide: How to Set Up Schwab Signature Workflow on Anduin FundSub"
date_ingested: 2026-05-26
as_of_date: 2025-12-15
source_type: implementation-guide
trust_level: 2
original_file: notion://d374318469284220bb201efec79e71be
products: [E-signature, FundSub]
target_audience: CS
onboarding_required: No
tags: [e-signature, schwab, implementation, ria, docusign, fundsub]
---

## Summary
Internal CS implementation guide for setting up the Schwab custodian signing workflow on Anduin FundSub. Covers the full 5-component setup process for RIA firms, including Anduin/RIA DocuSign authorization, Schwab addendum, technical validation, digitization requirements, and fund-level app setup. Based on implementation experience with Cerity Partners and Blue Arc.

## Key Takeaways
- **Schwab workflow** automates 3 things: applying Schwab's DocuSign template requirements (phone auth, document visibility, disclosures); auto-CC'ing signed docs to Schwab; and logic-gating Schwab forms to only investors with Schwab-custodied assets.
- **5 setup components** (not sequential):
  1. **RIA + Anduin setup** (per RIA firm): Anduin creates a unique DocuSign sender email per RIA entity (`{ria-name}-docusign-sender@anduintransact.com`); RIA adds it as authorized user in their Schwab Advisor Center (SAC) account.
  2. **Schwab + RIA addendum** (per RIA firm): RIA obtains Schwab's approval for Anduin as third-party DocuSign provider via signed addendum through SAC → Account Management → Advisor-Owned DocuSign → "Anduin Transaction."
  3. **Technical validation with Schwab** (per RIA firm): Anduin sends a test envelope to Schwab on behalf of the RIA; Schwab test-signs and approves. Failures resolved by engineer + product team.
  4. **Digitization setup** (per FundSub engagement): Schwab form PDF must contain `[Schwab form]` in filename to trigger Schwab template. Logic gating question required: "Is this investment associated with Schwab?" to display form only to relevant investors.
  5. **Anduin app setup** (per fund/subscription agreement): DocuSign must be enabled as signature type on each fund using Schwab integration. POC: Form QA.
- **Email domain enforcement**: Only advisors with the registered RIA email domain can initiate Schwab flow. Anduin hard-codes this restriction.
- **Internal testing backdoor** for Cerity Partners flow: `+ceritypartners@anduin.fund` (alias for `@anduintransact.com` inbox).
- Setup effort: ~2–3 days; initiate 2–3 weeks before first live use.
- `@anduin.fund` is an alias for `@anduintransact.com` — email notifications arrive at the `@anduintransact.com` inbox.

## Connections
- [[wiki/products/e-signature]] — primary implementation guide for the Schwab signing sub-feature
- [[wiki/products/fundsub]] — subscription context; digitization setup is per-fund engagement
- [[wiki/customers/cerity-partners]] — named in guide as primary implementation reference alongside Blue Arc

## Conflicts & Supersessions
- More detailed and authoritative than [[wiki/sources/esignature-schwab-cerity-training]] (trust level 2 vs. 7). The Cerity training covers the advisor-facing UX flow; this guide covers the internal CS setup process. Complementary, no conflicts.

## Raw Notes
- Lives under: E-signature Home → DocuSign Integration → PRD: Schwab DocuSign - Custodian Signing
- Edit log: Published 2025-02-21; updated 2025-06-27 (POC change, component reorder); updated 2025-12-15 (Component 2 updated)
- RIA offerings deck: https://docs.google.com/presentation/d/17bd9Y7tpUreNGCb65MANYDbaHY3jbqKj-aew67yLta8/edit (not fetched)
- Schwab Advisor Services Center (SAC): provides support and custody services to independent RIAs
- Schwab template (DocuSign concept): envelope template carrying SMS requirement, Document Visibility requirement, Auto-CC Schwab setup
