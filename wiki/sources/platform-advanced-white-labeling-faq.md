---
type: source
title: "Advanced White-Labeling — Internal FAQ"
date_ingested: 2026-06-29
as_of_date: 2026-05-03
source_type: faq
trust_level: 4
original_file: "Notion — Advanced White Labeling - FAQ (19f3f653b1df80a2a252c1ecbf280113) → content page de8c3c7ab3914c1098fb69cb30cfcc33"
products: [Platform]
target_audience: Sales + RM | CS
onboarding_required: No
tags: [platform, branding, white-labeling, custom-domain, sales-motion, implementation]
---

## Summary
Internal FAQ for **Advanced White-Labeling**, the platform-level branding solution built on top of the older Fund White-labeling. It lets entities and service providers run FundSub (and Data Room) under their own brand — custom domain, branded login/signup, a branded FundSub home dashboard spanning all of an entity's funds, and universal (environment-level) security policies. The FAQ spans general info, GP/LP UX, sales/demo guidance, custom-domain mechanics, the Environment object, change management, and unsupported items.

## Key Takeaways
- **Advanced vs Fund White-label** (what's NEW in Advanced): custom domain, universal security policies, full white-label authentication (email invite + shareable link + custom domain, not just shareable links), and a white-labeled FundSub *app dashboard*. Both tiers support white-labeled email header, fund dashboard, and investor subscription dashboard.
- **Target customers**: enterprise entities wanting one branded space across many funds (and strict security policies), and service providers reselling FundSub under their own brand.
- **Custom domain**: two options — an instant **Anduin subdomain** (e.g. `lpcommit.anduin.app`) or a **customer-provided domain** (e.g. `lpcommit.com`, takes a few days). Customer must already own the domain (Anduin won't register one); each domain is single-use across offerings.
  - Setup of a customer-provided domain goes through **InfoSec** (#security) → added to **Cloudflare** → InfoSec returns 1 TXT + 1 CNAME record → customer's eng adds them (within 7 days; underscore prefix on `_cf.custom-hostname`) → ready in ~15–30 min.
- **Domain levels**: Offering / Fallback / Platform — only **Offering-level** is currently surfaced. **Primary / secondary / tertiary** domains: primary is used in generated links (emails, shareable links); secondary is an access alias not used in links; tertiary redirects to primary (used when changing a primary domain). **Never delete old domains** — past email links would break.
- **Environment object**: a platform-level container for all white-labeling/settings; equivalent to a brand. An engagement (fund, data room) belongs to **exactly one** environment. Both *entity* white-labeling (offering level) and *fund* white-labeling (fund level) must be enabled for a seamless experience.
- **Fund transfer between environments**: removing a fund moves it to the Anduin dashboard and strips that environment's security enforcements; adding it to a new environment imposes the destination's policies.
- **Availability/limits**: available for **Data Room**; **not** planned for **Investor Access**. Favicon and custom loading screens are **not** supported (page-load-time risk).
- **Requests/demos**: customers request via an external setup template; no demo sandbox — use a Deals server (demo envs: Anduin Capital custom domain, XY Ventures Anduin subdomain).

## Connections
- Documents the [[features/platform-advanced-white-labeling|Advanced White-Labeling]] feature of [[products/platform|Platform]].
- The **universal/environment-level security policies** it references are implemented via [[features/platform-environment-sso|Environment-Based SSO & Authentication Policies]] (see [[sources/platform-environment-sso-setup-guide|the SSO setup guide]]).
- The Environment object is generalized in [[concepts/environment-object|Environment Object]].
- Primarily a FundSub + Data Room branding capability: [[products/fundsub|FundSub]], [[products/data-room|Data Room]].
- Theme/branding overlaps with [[sources/fundsub-dataroom-theme-customization|Theme Customization for FundSub and Data Room]] (fund-level theming vs platform-level white-labeling).

## Conflicts & Supersessions
- No conflicts with existing pages. Advanced White-Labeling is positioned as the superset of (and built on) the older Fund White-labeling.

## Raw Notes
- Notion master-view row is blank; content lives in the linked "Advanced White-labeling Internal FAQ" page (snapshot as of 2026-05-03; created 2025-03-06).
- Document Type = "FAQ" (trust 4); audience = Sales + RM, CS; Related Customer = All.
- **Legacy/stale references**: the FAQ still says custom domain "will be available … in April 2023" and lists fallback/platform domain levels as "no longer surfaced" — treat the April 2023 dates as historical, not current availability.
- Pricing answer points to "slide 15" of an external Google Slides deck (not captured). Several UX answers are video walkthroughs (GP experience, LP experience, switching environments).
- Support: #fund-onboarding-support (urgent), #fund-onboarding (feedback). References a Tango workflow for environment setup and an external "Requesting Advanced White-labeling Setup Template."
