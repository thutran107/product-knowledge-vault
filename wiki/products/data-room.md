---
type: product
title: "Data Room"
status: GA
source_count: 10
last_updated: 2026-05-11
tags: [data-room, anduin, investor-engagement, #integration]
---

## What it does
Anduin Data Room is a secure digital document sharing platform for fund managers to manage investor document access, track engagement, and control permissions throughout the due diligence process. It functions as a self-contained Anduin Object — a container for documents and participant management.

## Key capabilities
- **Document storage & sharing** — file and folder management with granular access control; supports versioning and bulk uploads
- **Participant management** — user and group-based access model; groups define inherited permissions; multi-group support
- **Activity tracking & insights** — tracks per-document engagement (viewed, downloaded), time spent, inactivity, and access percentage; exportable via Public API
- **Notification management** — configurable upload notification settings (immediate, daily digest at 12:05 AM UTC, weekly digest Monday 1:00 AM UTC)
- **Branding & customization** — custom logo, homepage banner, email templates, and drag-and-drop homepage editor per data room; custom URL with white-label domain option
- **Public API** — service account-based API with Basic Auth; webhook support per data room; managed via Admin Portal
- **Salesforce integration** — invite investors to Data Room directly from Salesforce via Integration Hub (paid, inbound CRM integration)
- **DealCloud integration** — sync real-time investor engagement data to DealCloud CRM
- **Demo sandbox** — Sales/CS can demo Data Room to prospects at https://demo.anduin.app/dataroom/#/public/demo

## Implementation notes
- Service account for API access is created by the Anduin team; API key delivered to customer via Data Room
- API authentication: Basic Auth, HTTPS required, no password
- Webhooks must be enabled per data room in Admin Portal (disabled by default)
- For Salesforce integration: customer must configure a Connected App, Screen Flow, and Custom Button in Salesforce; Anduin creates user groups in the target Data Room in advance
- Demo sandbox is maintained by the DR squad; updated when new features ship to production

## Known limitations
- **System limits:** max 3,000 participants + 50,000 files per data room (as of August 2025)
- **File upload:** 1 GB per upload batch
- Supported file formats: Video (MP4, WebM, OGG), Image (APNG, AVIF, GIF, JPEG, PNG, SVG, WebP)
- **Excel file preview limit:** 30 MB
- **Video display:** rendered at 16:9 ratio; 1GB upload limit; no specific dimension requirements
- Organization of an existing Data Room **cannot be changed** after creation
- "/" character not allowed in folder or file names (AWS S3 compatibility)
- Admin cannot exclude specific documents from upload notifications
- Insights export via Public API (available as of end of March 2025)
- Separate demo sandbox URLs for each product (DR, FS Normal, FS Flexible, FS Wire) — consolidation was under consideration as of October 2025
- Salesforce Connected App session limit: max 5 active sessions (customer must create a new Connected App if reached)

## Features & sub-modules
- User & Group management (multi-group internal training: [[wiki/sources/data-room-multi-group-training-video]])
- Public API & Webhooks ([[wiki/sources/data-room-api-implementation-guide]])

## Related customers
- [[wiki/customers/neuberger-berman]] — Data Room in use alongside FundSub and IDM

## Sources
- [[wiki/sources/data-room-faq]] — Data Room FAQ (operational limits, notifications, branding, misc)
- [[wiki/sources/data-room-brochure-v2]] — Data Room Brochure v2 (March 2024, Google Drive)
- [[wiki/sources/data-room-api-implementation-guide]] — API Access Setup Guide (June 2025)
- [[wiki/sources/data-room-multi-group-training-video]] — Multi-group training video (June 2025)
- [[wiki/sources/data-room-system-limits]] — Internal Slide on System Limits (August 2025)
- [[wiki/sources/data-room-demo-sandbox-guide]] — Demo Sandbox/Simulator Guide
- [[wiki/sources/fundsub-dataroom-theme-customization]] — Theme Customization (FundSub + Data Room)
- [[wiki/sources/automated-data-room-insights]] — Automated Data Room Insights (DealCloud integration)
- [[wiki/sources/configuration-vs-permission]] — Configuration vs Permission
- [[wiki/sources/neuberger-berman-case-study]] — Neuberger Berman Case Study

## Related
- [[wiki/products/integration-hub]] — Salesforce and DealCloud integrations
- [[wiki/products/fundsub]] — Often deployed alongside FundSub
- [[wiki/entities/dealcloud]] — DealCloud Data Room alert integration
- [[wiki/entities/salesforce]] — Salesforce → Data Room automated onboarding (IH paid integration)
- [[wiki/concepts/integration-patterns]] — Integration patterns
