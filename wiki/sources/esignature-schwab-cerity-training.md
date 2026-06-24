---
type: source
title: "Schwab Integration — External Training Flow for Cerity Partners"
date_ingested: 2026-05-11
as_of_date: 2025-06-25
source_type: client-training
trust_level: 7
original_file: notion://21d3f653-b1df-8037-ac5b-cb8f161283a1
products: [E-signature, FundSub]
target_audience: Sales + RM
onboarding_required: No
tags: [e-signature, schwab, implementation, case-study]
---

## Summary
A 16-step visual walkthrough of the Schwab DocuSign signature workflow in FundSub, created as external training material for Cerity Partners. Covers the advisor journey from accessing a subscription through completing DocuSign signing with phone-based authentication.

## Key Takeaways
- **Flow**: Advisor accesses investor subscription from Advisor Advantage fund dashboard → selects Schwab as custodian → completes electronic documents → initiates DocuSign e-signature workflow.
- **Schwab custodian trigger**: selecting "Schwab" as custodian enables Schwab's "Alternative Investment Letter of Authorization" form.
- **DocuSign integration**: both advisor and investor complete signing in DocuSign (not Anduin's native e-signature). Requires phone number authentication.
- **Workflow steps**: fill e-docs → "Add e-signature" → confirm DocuSign routing → add documents → add signers (name, email, phone) → confirm Schwab template → prepare signature fields → review/send → advisor signs → investor signs → completion shown in both LP and AAA views.
- Customer: **Cerity Partners** (RIA using Advisor Advantage / AAA product).

## Connections
- [[products/e-signature]] — Schwab DocuSign is a sub-workflow of the e-signature product
- [[products/fundsub]] — FundSub is the context for the subscription workflow
- [[customers/cerity-partners]] — this doc was created specifically for Cerity Partners

## Conflicts & Supersessions
- No conflicts. First Schwab-specific workflow document ingested.

## Raw Notes
- "Advisor Advantage" = the product name for Cerity Partners' GP-side interface (likely AAA product).
- Phone authentication required for both advisor and investor in DocuSign step.
- After all signers complete: status visible in both LP view and AAA view.
- Parent Notion page: PRD: Schwab DocuSign - Custodian Signing (product spec exists separately).
