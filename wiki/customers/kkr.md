---
type: customer
title: "KKR"
source_count: 1
last_updated: 2026-06-29
tags: [customer, pe, kkr, platform, sso]
---

## Overview
KKR & Co. Inc. — global investment firm managing PE, infrastructure, real estate, and credit.

## Products & features in use
- [[products/platform|Platform]] — runs FundSub through a white-labeled environment with a custom domain (kkr.subscribe.co) and [[features/platform-environment-sso|Environment-Based SSO]].

## Key facts
- **Custom-login requirement**: KKR routes users through its own login page (managed on KKR's end) to direct them to the appropriate authentication method. Their domain `kkr.subscribe.co` is treated as a white-labeled artifact, so investors must see KKR's login first.
- **Problem**: via the invitation route this worked, but investors re-entering the URL directly hit the Anduin login page instead of KKR's.
- **Solution — "Global Enforcement"**: Anduin shipped a stop-gap where a specific SSO is set as global enforcement, so users always land on that SSO first when accessing the environment. Investors now reliably land on KKR's login.
- **Support access preserved**: Anduin support logs into the default Anduin environment first, then accesses kkr.subscribe.co as an authenticated user; direct access without credentials gets stuck at KKR's login page.

## Open questions & considerations
- Global Enforcement layered with email-domain and role-based enforcement adds complexity; the platform team flagged the combined flow as needing to be made more intuitive.

## Sources
- [[sources/platform-environment-sso-setup-guide|Setup Guide for Environment SSO]] (KKR stop-gap documented as a worked example).

## Related
- [[products/platform|Platform]]
- [[features/platform-environment-sso|Environment-Based SSO & Authentication Policies]]
- [[concepts/environment-object|Environment Object]]
- [[customers/neuberger-berman|Neuberger Berman]]
