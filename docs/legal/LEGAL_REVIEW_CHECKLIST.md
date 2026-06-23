# FocusRSS Legal Review Checklist

Status: Draft for owner and qualified legal review  
Last updated: 2026-06-22

## Identity And Publication

- [ ] Confirm `崔华` is the correct public developer and legal entity name.
- [ ] Confirm the public address and phone may be published in Chinese and English.
- [ ] Select and verify the website domain.
- [ ] Confirm the English transliteration `Hua Cui` and address translation.
- [ ] Confirm the policy/terms update date and effective-date treatment.

## Privacy Policy

- [ ] Confirm all listed local data classes and the 90-day default retention behavior match the app.
- [ ] Confirm users can delete each listed local data class and Keychain credential as described.
- [ ] Confirm iCloud, analytics, crash reporting, accounts, and Sign in with Apple are disabled in the release binary.
- [ ] Confirm BYOK sends exactly the Focus question, user prompt, selected articles, and source URLs—and never the full subscription list.
- [ ] Confirm the BYOK provider disclosure is sufficient for every supported endpoint configuration.
- [ ] Confirm Hosted AI is disabled at launch.
- [ ] Before Hosted AI activation, identify every processor/subprocessor and confirm request/response non-storage and 14-day usage-log retention.
- [ ] Review cross-border transfer, personal-information, consent, and privacy-rights obligations for China and every distribution region.
- [ ] Confirm support-mailbox and website-host retention disclosures after providers are chosen.

## Terms And Purchases

- [ ] Confirm lifetime purchase availability and included functionality.
- [ ] Confirm the Hosted AI auto-renewable subscription, billing periods, prices, quotas, and cancellation language.
- [ ] Confirm Restore Purchases exists in the shipping app.
- [ ] Confirm Apple Standard EULA incorporation and priority language.
- [ ] Confirm acceptable-use, third-party content, AI output, availability, suspension, refund, warranty, liability, governing-law, and dispute terms are sufficient for target regions.
- [ ] Confirm Hosted AI limits never restrict access to locally stored RSS data.

## Support And Accessibility

- [ ] Send test messages to support, privacy, and business email addresses.
- [ ] Verify all public phone/address details.
- [ ] Check Chinese and English legal meaning for consistency.
- [ ] Keyboard-test every link and disclosure; verify focus visibility, contrast, zoom, screen-reader landmarks, and heading order.
- [ ] Test every route on narrow and wide viewports.

## App Store And Release

- [ ] Compare `APP_STORE_PRIVACY_DRAFT.md` with the exact production binary and live network traffic.
- [ ] Confirm App Store product metadata, privacy-policy URL, support URL, and marketing URL.
- [ ] Capture dated approval from the owner and qualified legal reviewer.
- [ ] Run `./scripts/validate-site.sh` with no blocking markers before deployment.
- [ ] Re-review all documents whenever accounts, iCloud, providers, retention, analytics, crash reporting, purchases, or Hosted AI change.

