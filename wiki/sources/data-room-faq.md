---
type: source
title: "Data Room - FAQ"
date_ingested: 2026-05-11
as_of_date: undated
source_type: faq
trust_level: 4
original_file: raw/notion-fetch
products: [Data Room]
target_audience: CS, Sales + RM
onboarding_required: No
tags: [data-room, faq]
---

## Summary
Comprehensive FAQ covering file upload behavior, notification settings, activity tracking, branding customization, and miscellaneous Data Room behavior. Authoritative on operational limits and edge cases for CS and Sales.

## Key Takeaways
- File upload limit: **1 GB per upload batch**; supported formats: Video (MP4, WebM, OGG), Image (APNG, AVIF, GIF, JPEG, PNG, SVG, WebP)
- Video upload limit: 1 GB; displayed at 16:9 ratio
- Excel file preview limit: **30 MB**
- Uploaders are **not** notified of their own uploads; admins cannot exclude specific documents from upload notifications
- Daily upload digest: **12:05 AM UTC**; Weekly digest: **Monday 1:00 AM UTC**
- "Recent files" section shows uploads for **30 days** since upload date
- Document inactivity: tab switch = stop tracking immediately; tab open but unfocused = stop after 10 minutes
- Data Room inactivity: user is asked to log in again after **24 hours** of inactivity
- Access % in Insights = files accessed since the data room was created
- Insights can be exported via Public API (available end of March 2025)
- Logo upload: square or long, JPG or PNG, 12–512px width/height
- Homepage banner: **1280×400 px**
- Email template variables: [DR Name], [Inviter Name], [Inviter Email], [Invitee Name], [Invitee Email], [Invitation Date], [Actor Name], [Actor Email]
- "/" character is **not allowed** in folder or file names (AWS S3 compatibility)
- Data room Organization cannot be changed after creation

## Connections
- [[products/data-room]] — operational limits, notification behavior, branding specs

## Conflicts & Supersessions
None identified.

## Raw Notes
- Upload notification toggle: if enabled, uploaders can choose to notify participants immediately at upload time
- "Can you export Participants and Content insights?" — Yes, via Public API available end of March 2025. This implies the API was in development as of the FAQ date (undated).
