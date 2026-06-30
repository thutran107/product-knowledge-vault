---
type: source
title: "IDM — Settings Part 1: White-Labeling & SMTP (Training Video)"
date_ingested: 2026-06-30
as_of_date: undated
source_type: cs-training
trust_level: 6
original_file: "raw/product-training-videos/investor-data-management/6-settings-part-1-idm-plan/"
products: [IDM, Platform]
target_audience: CS
onboarding_required: No
tags: [idm, implementation, security, integration]
---

## Summary
Walkthrough of IDM firm-level **Settings** — white-labeling (logos, header colors, email header background) and **email sender configuration** (Anduin server vs. custom SMTP). Frames sender identity and branding as foundational firm-identity work done at onboarding, not optional polish. Closes on environment-level SMTP enforcement that locks firm-level controls.

## Key Takeaways
- **White Label page** controls: two logo variants (**square** for firm switcher, **long** for app header, with a height control), a four-value **header color** scheme with **real-time preview** and per-field reset, and an **email header background color**.
- **Two mutually exclusive email sender options:** (1) **Anduin server** — custom sender *name* + *prefix*, but the **domain is fixed to Anduin's** and cannot be changed; zero infrastructure overhead (the middle ground most firms want). (2) **Custom SMTP** — firm's own host/port/credentials/domain. Enabling one disables the other.
- **SMTP gotcha:** when the SMTP username is an email address, the **sender address field must match it exactly** — a silent misconfiguration risk. Always use the **test email** button before going live.
- **Email design precedence:** the White-Label email header background color only affects Anduin's **default preset**; any **advanced white-label templates per email type** (Email Settings tab) override it entirely. Hierarchy: advanced per-type > white-label header background > default preset.
- **Environment-level enforcement:** if SMTP is enforced at the environment level via **iTools**, the firm-level Email Server page is **locked** and can only be changed at the environment level. Critical for multi-firm deployments.

## Connections
- Primary source for the new [[features/idm-firm-settings|IDM Firm Settings — White-Labeling & Email/SMTP]] feature page.
- **Cross-product overlap:** white-labeling and SMTP are platform-level infrastructure shared with other products — links to [[features/platform-advanced-white-labeling]] and the environment/SMTP enforcement on [[concepts/environment-object]].
- Email design presets concept also appears Portal-side in [[sources/investor-portal-settings-portal-plan-training-video]] (Portal email settings) — same underlying email-template machinery.

## Conflicts & Supersessions
- No conflict. This is firm-level branding/email config; complements (does not contradict) the Platform Advanced White-Labeling FAQ and the Environment SSO/enforcement docs. Note the distinction: **firm-level** white-label/SMTP here vs. **environment-level** enforcement that overrides it.

## Raw Notes
- 8:19 / 8 sections. "Unknown" date. Titled "Settings - Part 1 (IDM plan)"; Part 2 is the Portal-plan settings video (see [[sources/investor-portal-settings-portal-plan-training-video]]).
- Presenter demos from a reset/blank sandbox to make configuration sequence legible.
