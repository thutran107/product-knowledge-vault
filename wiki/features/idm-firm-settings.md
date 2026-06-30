---
type: feature
title: "IDM Firm Settings — White-Labeling & Email/SMTP"
parent_product: "IDM"
status: GA
source_count: 1
last_updated: 2026-06-30
confidence: medium
tags: [idm, implementation, security, integration]
---

## What it does
Firm-level settings that define how the app looks and how it communicates on behalf of the firm — white-labeling (logos and colors) and email sender configuration (Anduin server vs. the firm's own SMTP). Framed as foundational firm-identity work to complete at onboarding, so LPs never receive generic Anduin-branded emails or land in an app that looks like a third-party tool.

## How it works
**White-labeling (White Label settings page):**
- Two logo variants — **square** (firm switcher) and **long** (app header, with a height control).
- A four-value **header color** scheme with **real-time preview** and per-field reset.
- An **email header background color**.

**Email sender (two mutually exclusive options — enabling one disables the other):**
- **Anduin server** — custom sender *name* + *prefix*, but the **domain is fixed to Anduin's**; zero infrastructure overhead. The middle ground most firms want.
- **Custom SMTP** — the firm's own host, port, credentials, and domain. **Gotcha:** if the SMTP username is an email address, the sender-address field must match it exactly. Always send a **test email** before going live.

**Email design precedence:** advanced white-label templates per email type (Email Settings tab) > white-label email header background color > Anduin default preset.

## Use cases
- Brand the LP-facing experience (sender identity + app chrome) before launch.
- Route investor email through the firm's own infrastructure (deliverability/domain reputation) via custom SMTP, or get a branded sender with no setup via the Anduin-server option.

## Pricing & availability
Configured under the IDM plan; surfaced as standard firm settings. White-labeling and email infrastructure are platform-level capabilities shared across products.

## Known limitations
- **Anduin-server option:** only the prefix is editable — the **domain cannot be customized**.
- **Environment-level SMTP enforcement** (via **iTools**) **locks** the firm-level Email Server page; changes must then be made at the environment level. Know which layer owns a setting before troubleshooting.

## Sources
- [[sources/idm-settings-training-video]] — Settings Part 1: White-Labeling & SMTP (cs-training, trust 6)

## Related
- [[products/investor-data-management|IDM]] — parent product
- [[features/platform-advanced-white-labeling]] — platform-level white-labeling (domain/environment scope)
- [[concepts/environment-object]] — environment-level enforcement that overrides firm settings
- [[sources/investor-portal-settings-portal-plan-training-video]] — Portal-plan settings (Part 2) share the same email-template machinery
