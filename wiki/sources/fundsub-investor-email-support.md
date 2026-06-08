---
type: source
title: "[Internal Guide] Investor Sends Email Support Directly from Platform"
date_ingested: 2026-06-08
as_of_date: 2025-09-18
source_type: implementation-guide
trust_level: 2
original_file: raw/Notion page 2713f653b1df80a5a4f9e7208b28a09f
products: [FundSub]
target_audience: CS
onboarding_required: No
tags: [fundsub, implementation]
---

## Summary
Internal implementation guide for FundSub's investor-initiated support email feature. Investors can contact the GP's support inbox directly from the platform via a "Contact Support" button — enabled by default for new funds, configurable in Itool for existing funds. Driven by whale customer requirement for controlled, traceable email routing.

## Key Takeaways
- Investor clicks "Contact Support" in the FundSub platform → fills in message → clicks Send → email delivered to configured support inbox with pre-filled context.
- Enabled by default for all newly created funds.
- For existing funds: Anduin team enables via Itool (fund settings toggle).
- Driven by whale customer requirement: they want control and traceability over every support email; standard email-to-support@anduintransact.com bypassed in favor of this controlled routing.
- Investor sees success confirmation in-app after sending.

## Setup

**Existing funds:** Anduin team opens fund settings in Itool → enables "Email Support option" toggle.

**New funds:** Enabled by default — no setup required.

## Investor Flow
1. Investor clicks **Contact Support** in the platform
2. Fills in message (detailed explanation; optional attachments)
3. Clicks **Send**
4. Email delivered to configured support inbox with pre-filled context (fund, investor info)
5. Investor sees success confirmation in-app

## Benefits
- **Transparent:** GP customers maintain oversight over every email sent from the platform
- **Default-ready:** All new funds configured automatically
- **Faster resolution:** Investors reach support without leaving the platform

## Connections
- [[wiki/products/fundsub]]

## Conflicts & Supersessions
None found. First source on this feature.

## Raw Notes
- This was filed under FundSub in Notion, not Investor Portal, though a similar mechanism may exist or be planned for Portal.
- The Notion entry was labeled "New Feature: Investor Email Support from Platform" — likely a relatively recent release as of Sep 2025.
