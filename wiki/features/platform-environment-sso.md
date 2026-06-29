---
type: feature
title: "Environment-Based SSO & Authentication Policies"
parent_product: "Platform"
status: GA
source_count: 2
last_updated: 2026-06-29
tags: [platform, sso, security, authentication, environment, implementation]
---

## What it does
Lets Anduin bind authentication methods and account-security policies to a platform **Environment** rather than to individual user accounts. SSO configurations are scoped to an environment and enforced — checked on every API call — so users authenticate according to the environment they're accessing, and re-authenticate when they switch environments.

## How it works
SSO configs are first created in **Enterprise Login** (providers, protocols), then made "in-scope" for an environment. Enforcement is layered, in priority order:
1. **Per email domain** — many domains can map to one SSO config (n:1). Highest priority; a listed domain overrides all other rules.
2. **Per user role** — four FundSub roles (All GP members; All investors / primary contacts; Collaborators invited by GP; Collaborators invited by LP). Role-level enforcement is **FundSub-only**. A role can be bound to Anduin credentials, an SSO config, or left unspecified.
3. **Role priority** — drag-to-reorder decides which role's policy wins when a user holds multiple roles across funds.
4. **Fallback policy** — for users hitting no email/role rule: block, allow Anduin credentials, allow any in-scope SSO, or allow a default in-scope SSO.

**App-level SSO** is configured separately for **Data Room** (all Data Room users) and **IDM** (IDM, Portal, Landing Page); the setup flow is essentially the same for both. Mismatched SSO across layers forces a re-login.

**Global Enforcement** (the KKR stop-gap): a chosen SSO can be set so users always land on it first when entering the environment.

## Use cases
- Enterprise clients (e.g. **KKR**) who want investors to always see *their* branded login first via a custom domain.
- Multi-fund investors who previously saw multiple confusing SSO buttons — now resolved by environment-scoped, origin-aware enforcement.
- Workflows like **PGIM**'s where GP-invited collaborators need SSO but LP-invited collaborators do not — handled by splitting the collaborator roles.

## Pricing & availability
GA. Configured by Anduin support / Admin Portal. Part of the platform layer; tied to (and required for) Advanced White-Labeling's universal security policies. No standalone pricing documented.

## Known limitations
- Role-level enforcement applies to **FundSub only**.
- Shareable links require binding to the **LP primary's SSO**; if that role uses the fallback policy, the shareable link becomes unusable (behavior since 2025-04-16).
- Editing an in-scope SSO config requires an explicit activation step in Enterprise Login and logs out impacted users.
- Layered enforcement (global + email + role) can be confusing; the docs themselves note the flow needs to be made more intuitive.

## Sources
- [[sources/platform-environment-sso-setup-guide|Setup Guide for Environment SSO]] (implementation-guide, trust 2)
- [[sources/platform-environment-auth-enforcement|Environment Policy Enforcement and Authentication]] (note, trust 10)

## Related
- Parent: [[products/platform|Platform]]
- [[features/platform-advanced-white-labeling|Advanced White-Labeling]] (universal security policies run on this)
- [[concepts/environment-object|Environment Object]]
- [[customers/kkr|KKR]] (Global Enforcement stop-gap)
- [[products/fundsub|FundSub]], [[products/data-room|Data Room]], [[products/investor-data-management|IDM]]
