---
type: source
title: "Investor Portal — Reporting: Datasets (Overview & Details) (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-portal/reporting/3-datasets-overview/ + 4-datasets-details/"
products: [Investor Portal]
target_audience: CS
onboarding_required: No
tags: [investor-portal, implementation, data-management]
---

## Summary
Two consolidated videos on **datasets** — the foundational reporting layer. A dataset is a structured table anchored to a **core object** (currently investment or transaction) that acts as primary key and permission anchor. Covers master vs. time-series record types, the draft/backup/published versioning model, auto-access permissions, and ingestion paths.

## Key Takeaways
- **Core object anchors everything:** every dataset is built around a core object (investment or transaction today; investment entities and fund vehicles on the roadmap) that serves as primary key — all other fields relate to it.
- **Master vs. time-series (a non-reversible choice):** **master** overwrites using the core object as a single key (latest snapshot); **time-series** uses a composite key of core object + date to preserve history ("to show progress over time, use a time-series dataset").
- **Permissioning baked into the data model:** a record is visible only if the user has access to the underlying **investment object** *and* holds the **Financial Data permission** in their contact matrix — no manual row-by-row ACLs. No-access mode is a hard override.
- **Flexible, user-defined schema:** the only mandatory field is the one tied to the core object; otherwise define key (machine-readable, for API/spreadsheet) + display name + data type + required flag.
- **Draft / Backup / Published versioning:** edits stay sandboxed in draft; publishing promotes to published and auto-preserves the prior state as backup — "if the fund manager realizes they made a mistake, they can revert to the backup version." Publishing is one click; structural field changes possible post-publish.
- **Decoupled record access vs. page access:** having access to a record does not guarantee seeing a given reporting page — controlled independently. Internal (admin) vs. external (investor) access tracks are separate.
- **Ingestion:** manual entry and **API are live; spreadsheet import is in progress** — at launch the manual path is the practical default for non-technical teams.

## Connections
- Co-source for [[features/investor-portal-reporting-dashboards]].
- Permission model is the concrete application of [[features/idm-contacts|the communication matrix]] + the Portal-exclusive Financial Data permission ([[concepts/product-packaging-bundling]]).
- Core object = investment/transaction ties to [[features/idm-funds-tab]] and [[concepts/anduin-object-model]].

## Conflicts & Supersessions
- No conflict. New spec-level detail beneath the Portal page's reporting bullet.

## Raw Notes
- Overview 4:17 / 6 sections; Details 3:51 / 6 sections. "Unknown" date.
- Note: video headers label this "IDM Datasets / IDM reporting architecture," but the capability is the **Investor Portal** Reporting feature (Reporting is Portal-only, built on the IDM data layer).
