---
type: source
title: "IDM — Contacts: Concepts & Demo (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-data-management/5.1-contacts-concepts/ + 5.2-contacts-demo/"
products: [IDM, Investor Portal]
target_audience: CS | Sales + RM
onboarding_required: Yes
tags: [idm, implementation, data-management, pricing]
---

## Summary
Two consolidated videos — **Contacts concepts** and the **create/edit demo** — covering IDM's contact model. A contact is a single firm-wide record (keyed by email) linked many-to-many to clients and investment entities; the **communication matrix** is a per-investment, per-communication-type permission grid. The demo walks contact creation, matrix setup, client-level preference propagation, bulk management, and contact lists. Includes a key packaging signal: the **Financial Data permission is Investor Portal–exclusive**.

## Key Takeaways
- **Single source of truth.** A contact exists once and links to many clients/entities; updating a detail propagates everywhere — eliminating redundant list maintenance ("one Adam connected to everything he's part of").
- **Communication matrix is the heart of contact management** — granular per-investment, per-communication-type control (capital calls, K-1s, distribution notices, etc.); communication types are fully customizable at firm level.
- **Financial Data permission = package boundary, not a settings toggle.** The Financial Data column sits inside the communication matrix but governs access to **dynamic reports on the Investor Portal** and is **exclusively available in the Investor Portal package**. "If a client on a lower tier package asks about this, treat it as an upgrade conversation." → see [[concepts/product-packaging-bundling]].
- **Four ingestion methods:** manual creation, bulk spreadsheet import, automatic FundSub sync (**requires digitization-team involvement — loop them in early**), and public API (e.g., Salesforce). Match method to volume/context.
- **Three views, one record:** firm-wide All Contacts dashboard, client-level view, IE contact tab — three lenses on the same record.
- **Email is the immutable unique identifier** — no two contacts share an email; changing it requires a brand-new record.
- **Matrix auto-creates an investment** only if none exists between an IE and a fund; once one exists you can only pick from existing investments — new ones must be made in the Fund tab first.
- **Client-level preferences propagate and lock** all current and future child entities (e.g., Profile Access, Auto Assign) unless switched to **Custom**. **Auto Assign** makes new entities inherit contacts by default.
- **Removal is non-destructive** — affects future access only, never deletes the investment or prior assignments.
- **Bulk management from parent views** — client-view *Access Controls* and IE-view *Edit Communication Matrix* update many contacts at once.
- **Contact lists** are reusable mailing groups (a contact can be in many); target a list to avoid selecting recipients one by one. Engagements/Pages tabs are **read-only** (edits happen upstream).

## Connections
- Primary source for the new [[features/idm-contacts|IDM Contacts & Communication Matrix]] feature page.
- Financial Data permission gate is a cross-product packaging fact → [[products/investor-portal]] and [[concepts/product-packaging-bundling]].
- Communication-types-at-firm-level connects to [[sources/idm-funds-tab-training-video]] and [[features/idm-funds-tab]].
- Overlaps and complements [[sources/investor-portal-contact-management]] (Portal-side contact management deep-dive).

## Conflicts & Supersessions
- No conflict. The Financial Data permission being Portal-exclusive is consistent with the Portal-only-features packaging model on [[products/investor-portal]] and [[products/engagement-hub]].

## Raw Notes
- Concepts 12:13 / 6 sections; demo 12:53 / 9 sections. Both "Unknown" date.
- Narrative example "Adam Emmerich" (going on leave cascades manual edits without a single-record model). Demo example contact "Anna".
