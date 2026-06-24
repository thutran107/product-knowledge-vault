---
type: customer
title: "Cerity Partners"
source_count: 2
last_updated: 2026-05-26
tags: [ria, e-signature, schwab, fundsub]
---

## Overview
Cerity Partners is an RIA (Registered Investment Advisor) using Anduin's FundSub with Advisor Advantage (AAA) and the Schwab DocuSign custodian signing workflow for fund subscriptions.

## Products & features in use
- [[products/fundsub|FundSub]] — subscription management
- [[products/aaa|AAA]] — Advisor Advantage interface for the advisor/GP side
- E-signature: Schwab DocuSign custodian workflow (Alternative Investment Letter of Authorization)

## Key facts
- Advisors access investor subscriptions from Advisor Advantage's fund dashboard.
- Schwab is selected as custodian, triggering a specialized signing workflow via DocuSign.
- Both advisor and investor complete DocuSign signatures with phone-number-based authentication.
- After signing, documents are automatically forwarded to Schwab.

## Open questions & considerations
- Whether Cerity Partners has other Anduin products beyond FundSub/AAA is unknown.
- Schwab workflow may expand to other advisor-model customers.

## Sources
- [[sources/esignature-schwab-implementation-guide|Internal Guide: How to Set Up Schwab Signature Workflow]] — internal CS setup guide (trust 2)
- [[sources/esignature-schwab-cerity-training|Schwab Integration — External Training Flow for Cerity Partners]] — external training (trust 7)

## Related
- [[products/e-signature|E-signature]]
- [[products/fundsub|FundSub]]
