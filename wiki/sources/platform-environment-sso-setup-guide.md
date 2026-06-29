---
type: source
title: "Setup Guide for Environment SSO (Environment-Based Authentication Policies)"
date_ingested: 2026-06-29
as_of_date: 2025-08-01
source_type: implementation-guide
trust_level: 2
original_file: "Notion — How to setup environment-based authentication policies (1ae3f653b1df80a1a4b6ca9f21905c74) → content page 827ae1b6e49441339de4b9bbfcde5bcf"
products: [Platform]
target_audience: CS
onboarding_required: No
tags: [platform, sso, security, implementation, authentication, environment]
---

## Summary
The authoritative CS-facing how-to for configuring **environment-based authentication policies** (SSO) on the Anduin platform. It walks through binding SSO configurations to a platform *Environment* and layering enforcement by email domain, by user role, and via a fallback policy, plus app-level SSO for Data Room and IDM. Replaces the older model where auth policies were bound to user accounts.

## Key Takeaways
- **Prerequisite**: SSO configs are created first in **Enterprise Login** (providers, protocols), then *scoped* to an environment ("in-scope" SSO configs).
- **Enforcement layers, in priority order**:
  1. **Per email domain** — n:1 (many domains → one SSO config). Always **highest priority**; if a user's domain is listed, it overrides everything else.
  2. **Per user role** — four FundSub roles: All GP members, All investors (primary contacts), Collaborators invited by GP, Collaborators invited by LP. Role-level enforcement is **FundSub-only**. Can bind Anduin credentials to a role or leave it unspecified (→ fallback).
  3. **Role priority** — when a user holds multiple roles across funds, drag-to-reorder sets which role's policy wins.
  4. **Fallback policy** — applies to users who hit no email/role rule: block entirely, allow Anduin credentials, allow any in-scope SSO, or allow a default in-scope SSO.
- **App-level SSO** is configured separately for **Data Room** (applies to all Data Room users) and **IDM** (applies to IDM, Portal, Landing Page). Mismatched SSO across layers forces a re-login. Process for Data Room and IDM is essentially identical.
- **Shareable links** (since 2025-04-16): a FundSub engagement added to an environment with auth policies can keep its shareable link by binding it to the **LP primary's SSO**; the link then ignores other SSO config. If the LP-primary role uses the fallback policy, the shareable link becomes unusable.
- **KKR stop-gap — "Global Enforcement"**: a specific SSO can be set as global enforcement so users always land on that SSO first when accessing the environment (built so KKR investors hit KKR's own login at kkr.subscribe.co). Anduin support retains access by logging into the default environment first.

## Connections
- Documents the [[features/platform-environment-sso|Environment-Based SSO & Authentication Policies]] feature of [[products/platform|Platform]].
- Conceptual background: [[sources/platform-environment-auth-enforcement|Environment Policy Enforcement & Authentication]] (the "why" doc this guide implements).
- Pairs with [[features/platform-advanced-white-labeling|Advanced White-Labeling]] — both are scoped to the platform [[concepts/environment-object|Environment object]].
- Role-based enforcement uses the same primary/collaborator role taxonomy as [[sources/fundsub-primary-vs-collaborator|Primary Investor vs Collaborator in FundSub]].
- Enriches [[customers/kkr|KKR]] (Global Enforcement stop-gap) and references **PGIM** (collaborator-role split rationale; PGIM not yet a tracked entity).

## Conflicts & Supersessions
- **Supersedes the user-account-bound auth model** described as the legacy approach in [[sources/platform-environment-auth-enforcement|the enforcement context doc]] — policies and authentication now bind to an environment and are checked on every API call.
- No conflicts with existing wiki pages (Platform was a 0-source stub before this batch).

## Raw Notes
- Notion master-view row is blank; content lives in the linked "Setup guide for Environment SSO" page (snapshot as of 2025-08-01).
- Document Type = "Implementation Guide" (trust 2); audience = CS.
- Eight numbered setup steps + an Appendix step (shareable/invitation links) + "User exposure" scenarios + an "Edge case" section (editing an in-scope SSO config warns and requires explicit activation in Enterprise Login, logging out only impacted users; editing env bindings shows an impact screen before applying).
- The doc is heavily screenshot-driven (images not captured here).
