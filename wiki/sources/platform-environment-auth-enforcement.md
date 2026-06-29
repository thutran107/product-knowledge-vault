---
type: source
title: "Environment Policy Enforcement and Authentication"
date_ingested: 2026-06-29
as_of_date: 2025-06-23
source_type: note
trust_level: 10
original_file: "Notion — Environment policy enforcement and authentication (1ae3f653b1df8049a093e51899281d51) → content page 75a5376e786549738be206f61b47685b"
products: [Platform]
target_audience: All teams
onboarding_required: No
tags: [platform, sso, security, authentication, environment]
---

## Summary
The conceptual "why" behind environment-based authentication. A short context/approach doc explaining the drawbacks of binding account policies and SSO to *user accounts*, and the shift to binding them to an *environment*, checked on every API call. This is the parent doc of the [[sources/platform-environment-sso-setup-guide|Environment SSO Setup Guide]].

## Key Takeaways
- **Legacy model (user-account-bound) drawbacks**:
  - A user in multiple funds inherits *all* funds' policies; only auto-resolvable policies (e.g. enforce MFA) were supportable because policies could conflict.
  - A user is always held to the *strictest* policy set, even when accessing a less strict fund or data room.
  - SSO is bound at fund/data-room level, so multi-fund users see *multiple SSO buttons* at login — confusing, and a button can break if the SSO provider already removed the account.
  - A user could log in via fund A's SSO and still access fund B, because the platform didn't track origin.
- **New approach (environment-bound)**:
  - Account policies + authentication method can be bound to an **environment**, not just a user account.
  - Policy enforcement and authentication are checked on **every API call**.
  - **Switching environments forces re-authentication** to satisfy the target environment's policies.
- Implementations referenced: "SSO-enabled environment" and "Cross-Environment Navigation updates."

## Connections
- Conceptual basis for the [[features/platform-environment-sso|Environment-Based SSO & Authentication Policies]] feature of [[products/platform|Platform]].
- The implementation steps live in [[sources/platform-environment-sso-setup-guide|the Environment SSO Setup Guide]].
- The environment as a boundary object is generalized in [[concepts/environment-object|Environment Object]].

## Conflicts & Supersessions
- Frames the legacy user-account-bound policy model as superseded by environment-bound enforcement. No conflict with existing wiki pages.

## Raw Notes
- Notion master-view row is blank; content lives in the linked content page (snapshot as of 2025-06-23). Created 2025-03-06.
- Document Type = "General Knowledge Page" → mapped to `note` (trust 10); audience = All teams. Functionally a how-it-works context doc, but the authoritative implementation reference is the trust-2 setup guide.
