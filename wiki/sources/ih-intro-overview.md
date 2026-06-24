---
type: source
title: "[Internal use] Intro for Integration Hub"
date_ingested: 2026-05-11
as_of_date: 2025-09-29
source_type: note
trust_level: 10
original_file: notion://19e3f653-b1df-8041-83c2-f689f95df604
products: [Integration Hub]
target_audience: All teams
onboarding_required: Yes
tags: [integration-hub, onboarding]
---

## Summary
Internal overview document explaining what the Integration Hub is, how customers discover it, and how it works from a user's perspective. Intended to give all teams a foundational understanding before deeper research.

## Key Takeaways
- The Integration Hub is a feature within Anduin products (not a standalone product). Any customer with FundSub, IDM, or Data Room access can use it.
- Customers discover the Hub via: (a) in-app hooks from FundSub/DR/IDM, or (b) a public landing page.
- Access gating: users with email domain registered to an Anduin Entity see a "Find your solution" CTA; unregistered domains see "Request access."
- All users within the same Entity share one Hub. Users can modify/delete each other's integration instances.
- Three contact mechanisms for users: Contact Us (on enabled cards), Send Request (premium not purchased), and use-case text area (upcoming integrations).
- Integration Hub manages configuration; each Anduin app (FundSub, IDM, DR) enforces its own permissions separately.
- A new "Integration Platform" section in the admin portal lets Anduin manage premium integration quotas per Entity.
- Admin flow: grant access by adding customer's email domain to their Entity in the admin portal → set quota on premium integrations to unlock them.

## Connections
- [[products/integration-hub]] — this document is the primary introduction
- [[concepts/integration-patterns]] — describes the workflow patterns referenced
- [[products/fundsub]] — entry point for Hub discovery
- [[products/data-room]] — Anduin object type for Document Retrieval integrations
- [[products/investor-data-management]] — Anduin object type for IDM integrations

## Conflicts & Supersessions
- No conflicts found. Aligns with existing integration-hub product page on access model and URLs.

## Raw Notes
- MVP release date noted as Nov 19, 2024; US URL: integrations.anduin.app; UK: integrations.eu.anduin.app.
- Hooks from FundSub initially limited to pilot customers (Onex, Commonfund, Centerbridge, Bain Capital); from Nov 27 expanded to all customers.
- Integration versions: if a customer has deployed instances, the card shows that version; newer versions visible only in configuration. Future: backward compatibility focus.
- Slack channel for customer inquiries: integration-hub-user-request (C07V90JF19P).
