---
type: feature
title: "Communications (GP-to-Investor Messaging)"
parent_product: "Investor Portal"
status: GA
source_count: 1
last_updated: 2026-06-30
confidence: medium
tags: [investor-portal, implementation, sales-motion]
---

## What it does
A dedicated channel for GP-authored announcements and updates that are **separate from automated document/invitation notifications** — "a direct line for any message that does not necessarily come with a document attached." Also a core [[products/engagement-hub|Engagement Hub]] capability (centralized inbox/communication); Portal inherits it.

## How it works
- **Compose flow** with a firm-level **template library** (subject + body); create/edit/swap templates inline. Manual edits always win — the sent version reflects the fields at send time.
- **Dynamic placeholders** (receiver name, firm name, etc.) substitute per recipient; unsupported placeholders are flagged before delivery.
- **Individual vs. shared toggle:** individual (default — privacy, no reply-all) or one shared email to a group (e.g., an LP's internal team); CC/BCC via the contact picker.
- **Attachments auto-sync** to the Documents dashboard for GP and LP (no double upload); CTA button only links pages visible to all recipients.
- **Drafts** for collaborative async review.
- **Sent Items dashboard** logs every outbound email (message, share, invitation, request) with recipient counts, sender, date, and **email-type tags** for filtering — a durable compliance record.

## Use cases
Recurring investor updates (quarterly letters), announcements, and any non-document message — with personalization at scale and a built-in audit trail.

## Pricing & availability
Included in Investor Portal and Engagement Hub. Email design presets/content templates configured in Portal settings ([[sources/investor-portal-settings-portal-plan-training-video]]).

## Known limitations
- The investor-side **Inbox is read-only** today (a log); a two-way communication hub (inquiries, comments, replies) is roadmapped.

## Sources
- [[sources/investor-portal-communications-training-video]] — compose + Sent Items (cs-training, trust 6)

## Related
- [[products/investor-portal]] — parent product
- [[products/engagement-hub]] — also an EH feature; Portal inherits it
- [[features/investor-portal-document-distribution]] — sibling distribution channel
- [[features/idm-firm-settings]] / [[sources/investor-portal-settings-portal-plan-training-video]] — shared email-template machinery
