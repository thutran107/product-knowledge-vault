---
type: source
title: "Guide to Data Room Demo Sandbox/Simulator Environment"
date_ingested: 2026-05-11
as_of_date: undated
source_type: implementation-guide
trust_level: 2
original_file: raw/notion-fetch
products: [Data Room]
target_audience: All teams
onboarding_required: No
tags: [data-room, demo, sandbox, sales-motion]
---

## Summary
Internal guide for Sales and CS on how to access and use the Data Room demo sandbox environment for prospecting demos. Covers access steps, update/maintenance process, and testing server details.

## Key Takeaways
- Demo sandbox URL: **https://demo.anduin.app/dataroom/#/public/demo**
- Access: open link, enter Anduin email (or client email), access from email inbox
- Used by Sales/CS to demonstrate Data Room to prospective customers
- When new features ship to production (Deals), they are merged to demo sandbox; BD team must be trained on changes before they appear in demo scripts
- Two release scenarios: (1) new feature needs sample data — must be loaded; (2) no sample data needed — check if it breaks current demo script
- Testing server (QA): **https://simulator-test.anduin.app/**
- Implementation squad: DR squad (Product) or Slack @team_fundsub on #fund-onboarding or #fund-onboarding-support
- Known limitation: separate URLs for each demo sandbox (DR, FS Normal, FS Flexible, FS Wire) — consolidation was being considered

## Connections
- [[products/data-room]] — demo and sales motion
- [[products/fundsub]] — FS demo sandbox also maintained

## Conflicts & Supersessions
None identified.

## Raw Notes
- Sample data: https://drive.google.com/drive/folders/1aWwGhQmEV38XGb7DHnChuQXGbzGtnSm2
- Notion note about consolidating demo sandbox URLs into one — not yet done as of the page's last update (2025-10-08)
