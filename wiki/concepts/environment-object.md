---
type: concept
title: "Environment Object"
source_count: 3
last_updated: 2026-06-29
tags: [platform, environment, branding, sso, security, architecture]
---

## Definition
A platform-level container on Anduin that represents a **brand** and owns engagements across product offerings (funds in FundSub, data rooms in Data Room, etc.). An environment stores white-labeling settings and binds authentication/security policies. An engagement belongs to **exactly one** environment.

## Key dynamics
- **One brand = one environment.** It can reflect a fund's own brand (e.g. 8VC, Sequoia) or a partner white-labeling the platform (e.g. LP Commit, Gen II). If a fund wants to sit under a partner's environment, it can't also have its own — it must choose.
- **Two things attach to an environment:**
  1. **Branding** (Advanced White-Labeling) — custom domains, branded login/dashboard, white-labeled app surfaces.
  2. **Authentication & security policies** (Environment-Based SSO) — SSO configs scoped to the environment, enforced on every API call, with re-authentication on environment switch.
- **Custom domains** are owned at the environment/offering level (primary/secondary/tertiary categories; only Offering-level surfaced).
- **Moving an engagement between environments** re-applies the destination's branding and security policies and strips the source's. Removing a fund returns it to the default Anduin dashboard/domain and removes environment-level enforcement.
- **Layering**: entity white-labeling (offering level) + fund white-labeling (fund level) both need to be enabled for a seamless experience.

## Evidence & examples
- **KKR**: uses environment + custom domain (kkr.subscribe.co) plus "Global Enforcement" so investors always hit KKR's login first — see [[features/platform-environment-sso|Environment-Based SSO]].
- Demo environments: Anduin Capital (custom domain) and XY Ventures (Anduin subdomain) per the [[sources/platform-advanced-white-labeling-faq|Advanced White-Labeling FAQ]].
- Available for FundSub and Data Room; **not** Investor Access (investors would lose cross-environment access to their own profile data).

## Tensions & open questions
- Relationship to the [[concepts/anduin-object-model|Anduin Object Model]]: an *Anduin Object* (Fund/Firm/Data Room) is the integration/permission unit; an *Environment* is the branding + auth boundary that owns those engagements. The two abstractions are complementary but not formally reconciled in the sources.
- Only Offering-level domains are live; Fallback/Platform levels are deprecated/"no longer surfaced."
- Layered SSO enforcement (global → email domain → role → fallback) is acknowledged as not yet intuitive.

## Related
- [[products/platform|Platform]]
- [[features/platform-environment-sso|Environment-Based SSO & Authentication Policies]]
- [[features/platform-advanced-white-labeling|Advanced White-Labeling]]
- [[concepts/anduin-object-model|Anduin Object Model]]
- [[customers/kkr|KKR]]
- [[products/fundsub|FundSub]], [[products/data-room|Data Room]]
