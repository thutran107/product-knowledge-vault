---
type: source
title: "FundSub — Duplicate Fund Configuration (Nov 2025)"
date_ingested: 2026-05-11
as_of_date: 2025-11-01
source_type: implementation-guide
trust_level: 2
original_file: notion://26f3f653-b1df-807d-b5d0-d8c3b9f587d4
products: [Fundsub]
target_audience: CS
onboarding_required: No
tags: [fundsub, duplicate-fund, configuration, implementation]
---

## Summary
CS-facing demo/training deck covering the Duplicate Fund Configuration feature in FundSub. Allows GPs (via Anduin internal team) to clone an existing fund's settings as the baseline for a new fund, significantly reducing setup time. Originally presented Sep 2024; surfaced in Notion as Nov 2025.

## Key Takeaways
- **What gets duplicated:** White Labeling, Email Templates, Dashboard, Feature Switches, Basic Configs, GP Group names + permissions, GP members per group, LP Group names (only), and Doc Review workflows (unsigned sub doc, signed sub doc, AML/KYC).
- **What is NOT duplicated:** Data export templates (form-dependent, excluded by design).
- **Access:** Available in Internal Admin Portal only — not yet self-serve for GPs.
- **6-step flow:** Create New Fund → Select old fund to copy from → Copy Basic Configs → Copy Fund & Investor Groups → Copy Doc Review Workflows → Review & Save.
- **Can duplicate to an existing fund** (not just new), if: a form has been selected, no external FMs or LPs are invited (only Anduin Support), and you have access to that fund.
- **Email templates:** Both admin email config settings (custom sender, reply-to, CC) and app-level email templates are carried over.
- **GP members:** All GP members except Anduin Support are copied; invitation email sent immediately after applying.
- **Multi-currency:** Amount columns not transferred (form-based).
- **Edge case:** Funds with restricted LP flow or disabled permissions will not appear in fund selection.
- **Review workflow caveat:** Carry-over depends on old fund settings — feature switch must be enabled, GP members must be copied, workflow must not be configured by investor/document group.

## Connections
- [[products/fundsub|FundSub]] — Duplicate Fund is a core configuration capability
- [[sources/fundsub-email-smtp-implementation-guide]] — email templates are part of what gets duplicated

## Conflicts & Supersessions
None. Date on slides says "Sep 2024 demo" — Notion page surfaced as Nov 2025; content appears stable.

## Raw Notes
- Google Slides: https://docs.google.com/presentation/d/1Lkv51kGL7Hs-q7FXthBXWaL7GEXDi9Cu0yuozd00Gr0
- Slide deck header: "Duplicate Fund Configuration — Demo, Sep 2024"; Notion as-of date: Nov 2025.
- Notion page shares an attached PDF filename with the SMTP guide — likely a Notion artifact, not relevant.
