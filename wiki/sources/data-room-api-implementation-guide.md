---
type: source
title: "Data Room - Customer Setup Guide for API Access to DR"
date_ingested: 2026-05-11
as_of_date: 2025-06-04
source_type: implementation-guide
trust_level: 2
original_file: raw/notion-fetch
products: [Data Room]
target_audience: CS | Sales + RM
onboarding_required: No
tags: [data-room, api, implementation, integration]
---

## Summary
Internal-only step-by-step guide for CS to set up API access for customers to the Data Room. Covers service account creation, authentication, webhook configuration, and an 8-question FAQ for common API support scenarios.

## Key Takeaways
- **Service account** is created by the Anduin team; API key is delivered to the client via Data Room
- Authentication: **Basic Auth** — API key used as Bearer Authentication, no password required
- All API requests **must** use HTTPS; plain HTTP requests will fail
- Setup flow: Admin Portal > Public API section > select service account > add Data Room > enter Data Room ID > toggle webhook on
- **Webhook is disabled by default** at the Data Room level; must be enabled per-data-room in Admin Portal
- Lost API keys **cannot be retrieved** — only regenerated via Anduin support
- **Multiple API keys** can be issued per customer on request (for different apps or teams)
- Salesforce limit: **5 active sessions per Connected App**
- Rotation of API keys is recommended periodically for security
- CS should ensure clients understand the API documentation and provide assistance as needed

## Connections
- [[products/data-room]] — API sub-feature, Known limitations

## Conflicts & Supersessions
None identified.

## Raw Notes
- API reference: https://developers.anduintransact.com/reference/list-data-rooms
- Webhook verification: https://developers.anduintransact.com/reference/get-all-webhook-endpoints
- FAQ Q1: Lost API key → contact Anduin support; only regenerated, not retrieved
- FAQ Q2: Multiple keys → yes, on request
- FAQ Q5: Access level → based on service agreement
- Internal only — do not share directly with customers
