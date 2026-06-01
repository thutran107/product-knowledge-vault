---
type: source
title: "User Role"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/User role.md
products: [Integration Hub]
target_audience: CS
onboarding_required: No
tags: [integration-hub, user-roles, access-control]
---

## Summary
Defines the two user roles in the Integration Hub: Admin (default for authenticated Anduin GP users within the same email domain) and Member (external collaborators like consultants invited by admins).

## Key Takeaways
- All authenticated Anduin GP users with the same email domain share one Hub and all are admins by default.
- Admins can: create, modify, remove integrations, and invite Members.
- Member role was introduced to accommodate external consultants/IT providers with different email domains.
- Members have near-identical access to admins, except they cannot invite other users.
- Members can be removed by admins at any time.

## Connections
- [[wiki/concepts/user-roles|User Roles]] — concept page expanding on this.
- [[wiki/products/integration-hub|Integration Hub]].

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- Typical Member use case: external consultant sets up integrations during implementation, then hands control back to the customer.
- Example given: Anduin org inviting Salesforce support as a Member.
