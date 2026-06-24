---
type: product
title: "Integration Hub"
status: GA
source_count: 14
last_updated: 2026-05-11
tags: [integration-hub, anduin, platform]
---

## Overview
Anduin's centralized self-service platform for exploring, installing, and managing integrations between Anduin products (FundSub, Data Room, IDM) and third-party systems (DealCloud, Affinity, Salesforce, Box, etc.).

## Key Facts
- Each customer organization gets one dedicated Integration Hub, shared by all users with the same email domain.
- Access: authenticated Anduin GP user + email domain registered to an Anduin Entity.
- US URL: `https://integrations.anduin.app/` | UK: `https://integrations.eu.anduin.app/`
- Built around **Integration Cards** — prebuilt workflow templates customers can install and configure.
- Three integration patterns available: Order Creation, Data Retrieval, Document Retrieval.
- Premium integrations require a Quota to be set by Anduin in the Admin Tool.
- Has a Monitor → Execution tab for viewing run history and troubleshooting failures.
- Upcoming: automatic domain assignment to all existing customers (removing need for manual provisioning).
- **Underlying platform**: Prismatic powers the configuration wizards and monitoring tabs.
- **Two card types**: Operational cards (ready to install) and Dummy cards (logo-only, collect interest before integration is built).
- **Public landing page**: Hub is discoverable publicly, not just within Anduin apps.
- **Provisioning roadmap**: Jan 2025 — separate views per entity; Mar 2025 (tentative) — different orgs sharing one Hub.
- **Hooks**: entry points from FundSub, Data Room, and IDM drive discoverability within the platform.
- Positioning: "20+ app integrations available"; tagline "a single gateway to all your app integrations."

## Role in This Knowledge Base
The central product. Nearly every source document describes either the Hub's architecture or a specific integration available within it.

## Sources
- [[sources/mission-and-core-components|Mission and Core Components]]
- [[sources/configuration-vs-permission|Configuration vs Permission]]
- [[sources/user-role|User Role]]
- [[sources/ih-implementation-guide|IH Implementation Guide]]
- [[sources/ih-implementation-guide-pdf|IH Implementation Guide (PDF)]]
- [[sources/neuberger-berman-case-study|Neuberger Berman Case Study]]
- [[sources/ih-intro-overview|Intro for Integration Hub (Internal)]]
- [[sources/ih-sop|Integration SOP]]
- [[sources/ih-knowledge-hub|IH Knowledge Hub — All Available Implementations]]
- [[sources/ih-setup-guide|IH Setup Guide — Platform Setup]]
- [[sources/ih-smtp-gtm-training|Introduction to SMTP Integration]]
- [[sources/ih-salesforce-dataroom-release-notes|Automated Onboarding to Data Room from Salesforce (Release Notes)]]
- [[sources/ih-salesforce-dataroom-implementation-guide|Automated Onboarding to Data Room from Salesforce (Implementation Guide)]]

## Related
- [[products/fundsub|FundSub]], [[products/data-room|Data Room]], [[products/investor-data-management|IDM]]
- [[concepts/integration-patterns|Integration Patterns]]
- [[concepts/configuration-vs-permission|Configuration vs Permission]]
- [[concepts/user-roles|User Roles]]
