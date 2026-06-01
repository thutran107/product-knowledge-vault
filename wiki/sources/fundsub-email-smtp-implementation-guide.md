---
type: source
title: "FundSub Email Configuration & SMTP Integration — Mar 2025"
date_ingested: 2026-05-11
as_of_date: 2025-03-01
source_type: implementation-guide
trust_level: 2
original_file: notion://26f3f653-b1df-80f0-8961-c20fcad84352
products: [Fundsub]
target_audience: CS
onboarding_required: No
tags: [fundsub, smtp, email-configuration, #implementation]
---

## Summary
CS-facing internal training deck (March 2025) covering FundSub email configuration and SMTP integration. Explains the two-layer email customization model — Standard Email Customization and SMTP Integration — how they interact, and how to configure SMTP credentials for customers who want emails sent from their own domain.

## Key Takeaways
- **Two customization layers:** Standard Email Customization (content/template) + SMTP Integration (routing/sender). Both can be active simultaneously.
- **SMTP Integration purpose:** Routes outgoing FundSub emails through the customer's own SMTP server and domain instead of Anduin's servers. Benefits: better deliverability, brand trust, compliance tracking.
- **When both are enabled:** Emails route via SMTP server; Reply-To, CC, BCC still customizable via Standard layer; sender name/email locked to SMTP Integration settings.
- **Required SMTP fields:** host, port, credentials (generic email account — e.g., onboarding@company.com — NOT personal credentials).
- **Ports:** 25, 465 (SSL — outdated), 587 (TLS — recommended). Enable TLS for port 587; disable for 465 or 25.
- **Protocol clarity for CS:** TLS encrypts after initial handshake (port 587); SSL encrypts from start (port 465, now considered outdated).
- **Security note:** Customers should use a dedicated generic email account for SMTP, not a personal work email — only one account needed.
- **Configured in:** Admin tool (not self-serve for GPs).

## Connections
- [[wiki/products/fundsub|FundSub]] — email configuration is a FundSub admin capability
- [[wiki/sources/ih-smtp-gtm-training|IH SMTP GTM Training]] — covers IH-level SMTP integration (different scope)
- [[wiki/sources/fundsub-duplicate-fund-config]] — SMTP/email config is among items that can be duplicated to a new fund

## Conflicts & Supersessions
None. This is FundSub-specific; IH SMTP guide covers a different integration layer.

## Raw Notes
- Google Slides: https://docs.google.com/presentation/d/1hRW_dmStmePxV6EN5Y86SmiSpyomrQMC87GxL2El2LY
- Deck explicitly references an "Internal Guide Doc for Setup Guide" for full step-by-step setup (not fetched).
- Notion attached PDF ("LP_Experience_Revamp_-_February_2025.pdf") is a Notion artifact, not relevant content.
