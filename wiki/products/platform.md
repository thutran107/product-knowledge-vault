---
type: product
title: "Platform"
status: GA
source_count: 3
last_updated: 2026-06-29
tags: [platform, anduin, sso, security, branding]
---

## What it does
Anduin's core platform layer that underpins all products — authentication, security-policy enforcement, brand/white-labeling, and the shared **Environment** object that other products (FundSub, Data Room, IDM, etc.) run on top of.

## Key capabilities
- **Environment-Based SSO & Authentication Policies** — SSO configs scoped to an environment and enforced on every API call, layered by email domain → user role → fallback, plus app-level SSO for Data Room and IDM. See [[features/platform-environment-sso|the feature page]].
- **Advanced White-Labeling** — custom domains, branded login/signup, branded FundSub app dashboard, and universal security policies, built on top of fund-level white-labeling. See [[features/platform-advanced-white-labeling|the feature page]].
- **Environment object** — the brand/auth boundary that owns engagements across offerings; see [[concepts/environment-object|the concept page]].
- Shared primitives also documented elsewhere: [[concepts/configuration-vs-permission|Configuration vs Permission]] and [[concepts/user-roles|User Roles]].

## Pricing & packaging
No standalone platform pricing doc ingested. Advanced White-Labeling pricing is referenced in an external sales deck (slide 15, not captured); SSO/auth is configured by Anduin support with no separate price documented.

## Implementation notes
- SSO configs are created in **Enterprise Login**, then scoped to an environment via the **Admin Portal** ("Authentication Policies" tab).
- Custom domains: Anduin subdomain (instant) or customer-provided domain via **InfoSec → Cloudflare** (1 TXT + 1 CNAME, added within 7 days).
- Both entity-level and fund-level white-labeling must be enabled for a seamless branded experience.

## Known limitations
- Role-level SSO enforcement is **FundSub-only**.
- Advanced White-Labeling is available for FundSub and Data Room but **not** Investor Access; favicon and custom loading screens unsupported.
- Layered SSO enforcement is acknowledged as not yet fully intuitive.

## Features & sub-modules
- [[features/platform-environment-sso|Environment-Based SSO & Authentication Policies]]
- [[features/platform-advanced-white-labeling|Advanced White-Labeling]]

## Related customers
- [[customers/kkr|KKR]] — environment + custom domain + Global Enforcement.

## Sources
- [[sources/platform-environment-sso-setup-guide|Setup Guide for Environment SSO]] (implementation-guide, trust 2)
- [[sources/platform-environment-auth-enforcement|Environment Policy Enforcement and Authentication]] (note, trust 10)
- [[sources/platform-advanced-white-labeling-faq|Advanced White-Labeling — Internal FAQ]] (faq, trust 4)

## Related
- [[concepts/environment-object|Environment Object]]
- [[concepts/anduin-object-model|Anduin Object Model]]
- [[products/fundsub|FundSub]]
- [[products/data-room|Data Room]]
- [[products/investor-data-management|IDM]]
- [[products/integration-hub|Integration Hub]]
