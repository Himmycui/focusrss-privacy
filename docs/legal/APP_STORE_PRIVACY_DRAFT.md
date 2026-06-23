# App Store Connect Privacy Questionnaire Draft

Status: Draft — owner review required  
Source: `docs/legal/LEGAL_INPUTS.yaml`  
Bundle ID: `com.xingshi356.focusrss`

This is a working aid, not a submission. Answers must be checked against the exact binary and every enabled production service immediately before App Store submission.

## Current Launch Configuration

- Account creation: No.
- Sign in with Apple: No.
- iCloud sync: No.
- Analytics: No; provider is null.
- Crash reporting: No; provider is null.
- Hosted AI at launch: No.
- BYOK AI: Yes.
- Purchases represented in inputs: lifetime purchase and auto-renewable subscription for Hosted AI.

## Data Types To Review In App Store Connect

### User Content

Potential data: Focus questions, user prompts, selected feed articles, source URLs, and AI summaries.

- Stored locally: Yes, for RSS/feed content, Focus Cards, reading history, and AI summaries.
- Sent off device: Yes, only when the user invokes BYOK AI; sent to the user-selected endpoint.
- Full subscription list sent to BYOK: No.
- Linked to identity: No account exists in the supplied launch configuration. Confirm whether Apple purchase records or endpoint behavior changes Apple's classification.
- Used for tracking: No.
- Purpose candidate: App Functionality.

### Identifiers And Purchase Information

Potential data: App Store purchase/entitlement information for lifetime purchases and Hosted AI subscriptions.

- Exact StoreKit fields collected by the app: not supplied.
- Linked to identity: requires verification against the implementation and Apple's definitions.
- Used for tracking: No analytics or advertising is enabled.
- Purpose candidate: App Functionality.

### Usage Data

Potential data: Hosted AI usage metadata.

- Hosted AI enabled at launch: No.
- Request content stored by Hosted AI: No.
- Response content stored by Hosted AI: No.
- Usage metadata stored: Yes when Hosted AI is enabled.
- Retention: 14 days.
- App Store answer at launch: verify that disabled code paths and server configuration do not collect this data before answering “not collected.”

### Contact Information

- Account creation: No.
- Sign in with Apple: No.
- The support website exposes contact emails but contains no form.
- Support email content is user-initiated outside the app; confirm whether any in-app support composer or uploaded diagnostics changes the questionnaire answer.

### Diagnostics

- Crash reporting: Disabled.
- Provider: None.
- Confirm the production binary does not include an active crash-reporting SDK or custom diagnostic upload.

## Tracking

- Analytics provider: None.
- Advertising: None stated.
- Cross-app or cross-site tracking: No flow is identified in the legal inputs.
- Public site tracking: None.

## Submission Blockers

- Select the public website domain and verify the live privacy-policy URL.
- Inspect the production binary and network traffic against this draft.
- Confirm exact StoreKit transaction and entitlement fields.
- Re-run this questionnaire before enabling Hosted AI, analytics, crash reporting, accounts, or iCloud.

