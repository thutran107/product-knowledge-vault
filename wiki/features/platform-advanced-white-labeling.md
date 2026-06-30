---
type: feature
title: "Advanced White-Labeling"
parent_product: "Platform"
status: GA
source_count: 1
last_updated: 2026-06-29
confidence: medium
tags: [platform, branding, white-labeling, custom-domain, sales-motion]
---

## What it does
Platform-level branding that lets an entity or service provider run Anduin FundSub (and Data Room) under their own brand. Built on top of the older fund-level **Fund White-labeling**, it adds custom domains, branded login/signup, a branded FundSub home dashboard spanning all of an entity's funds, and universal (environment-level) security policies.

## How it works
Branding and settings are stored on a platform **Environment** object (a brand = an environment; an engagement belongs to exactly one environment). Both **entity white-labeling** (offering level) and **fund white-labeling** (fund level) must be enabled for a seamless experience.

**Custom domains** come in two flavors:
- **Anduin subdomain** (e.g. `lpcommit.anduin.app`) — available instantly.
- **Customer-provided domain** (e.g. `lpcommit.com`) — customer must already own it; routed through **InfoSec** → **Cloudflare**, which returns 1 TXT + 1 CNAME record for the customer's eng to add (within 7 days); live in ~15–30 min.

Domains have **levels** (Offering / Fallback / Platform — only **Offering** is currently surfaced) and **categories**: **primary** (used in generated links/emails), **secondary** (access alias, not in links), **tertiary** (redirects to primary). To change a primary domain, demote the old one to tertiary/secondary and add a new primary — **never delete** old domains or past email links break.

## Use cases
- Enterprise entities wanting one branded space across many funds, with strict security policies.
- Service providers reselling FundSub under their own brand to preserve brand loyalty.

## Pricing & availability
GA. Available for **FundSub** and **Data Room**; **not** planned for **Investor Access**. Pricing referenced in an external sales deck (not captured). Customers request setup via an external template; no demo sandbox (use a Deals server).

## Known limitations
- **Favicon** customization and **custom loading screens** are not supported (page-load-time risk).
- Only **Offering-level** domains are surfaced (fallback/platform levels deprecated).
- A customer-provided domain can't be edited in place — you create a new domain and re-point primary.
- Not available for Investor Access.

## Sources
- [[sources/platform-advanced-white-labeling-faq|Advanced White-Labeling — Internal FAQ]] (faq, trust 4)

## Related
- Parent: [[products/platform|Platform]]
- [[features/platform-environment-sso|Environment-Based SSO & Authentication Policies]] (provides the universal security policies)
- [[concepts/environment-object|Environment Object]]
- [[sources/fundsub-dataroom-theme-customization|Theme Customization for FundSub and Data Room]] (fund-level theming)
- [[products/fundsub|FundSub]], [[products/data-room|Data Room]]
