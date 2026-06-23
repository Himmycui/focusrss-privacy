# FocusRSS Data Flow Inventory

Status: Draft from `LEGAL_INPUTS.yaml`  
Last updated: 2026-06-22

This inventory documents every data flow represented by the current legal inputs. It does not activate a feature or broaden application behavior.

## Data Flow Matrix

| Flow | Trigger | Data | From | Recipient / destination | Storage and retention | User control |
|---|---|---|---|---|---|---|
| Local RSS subscription storage | User adds or imports a feed | RSS, Atom, or JSON Feed subscription details | User input | User's iOS device | On device; 90 days by default | Delete the subscription or app data |
| Feed article storage | User refreshes a feed | Feed-provided articles | Feed server | User's iOS device | On device; 90 days by default | Delete articles/source data or app data |
| Focus Card storage | User creates or edits a Focus Card | Focus Card content and configuration | User input | User's iOS device | On device; 90 days by default | Delete the Focus Card or app data |
| Reading-history storage | User reads content | Reading history | User interaction | User's iOS device | On device; 90 days by default | Delete reading history or app data |
| AI-summary storage | User generates or saves a summary | AI summary | Selected AI endpoint | User's iOS device | On device; 90 days by default | Delete summaries or app data |
| Feed retrieval | User adds or refreshes a feed | Feed request and normal network metadata | User's device | User-provided feed server | The legal inputs do not specify third-party server retention | Remove the source and stop refreshing it |
| BYOK AI request | User initiates an AI operation | Focus question, user prompt, selected articles, source URLs | User's device | User-provided AI endpoint | Provider-controlled; not specified by the legal inputs | Do not enable BYOK; choose articles; remove endpoint configuration |
| BYOK credential storage | User saves an endpoint credential | API key | User input | iOS Keychain | Until the endpoint credential is removed | Delete the endpoint configuration/credential |
| Full subscription list exclusion | BYOK AI request | Full RSS subscription list | User's device | Not sent | Not applicable | Enforced by product behavior represented in the legal inputs |
| Hosted AI request content | Hosted AI operation | Request content | User's device | Hosted AI | Disabled at launch; request content is not stored when enabled | Do not subscribe or initiate Hosted AI |
| Hosted AI response content | Hosted AI operation | Response content | Hosted AI | User's device | Disabled at launch; response content is not stored by Hosted AI when enabled | Delete the local AI summary |
| Hosted AI usage metadata | Hosted AI operation | Usage metadata | Hosted AI service | Hosted AI logs | Disabled at launch; 14 days when enabled | Contact privacy support; service-specific controls must be reviewed before launch |
| Purchase transaction | User buys lifetime access or subscribes | Purchase and entitlement information | User and App Store | Apple purchase infrastructure and FocusRSS entitlement logic | Not specified by the legal inputs | Manage purchases/subscriptions through Apple; restore purchases in the app |
| Support email | User voluntarily emails support | Email address and message content | User's email client | `himmy.cui@outlook.com` and email infrastructure | Not specified by the legal inputs | User chooses what to include; avoid API keys and unnecessary private content |
| Public website request | Visitor opens a page | Standard HTTP request metadata | Visitor's browser | Future website host | Domain and host are unresolved; host retention is not specified | Do not visit; browser/network controls |

## Explicitly Disabled Flows

- iCloud synchronization is disabled.
- Account creation is disabled.
- Sign in with Apple is disabled.
- Analytics is disabled and has no provider.
- Crash reporting is disabled and has no provider.
- Hosted AI is disabled at launch.
- The public site contains no cookies, analytics, tracking, advertising, external fonts, forms, or JavaScript.

## Processor And Retention Gaps

- The public website domain and hosting provider are unresolved.
- BYOK AI providers are selected by each user; their retention cannot be stated as a single FocusRSS period.
- Hosted AI processors, usage limits, and purchase pricing are not present in the legal inputs and require review before Hosted AI is enabled.
- Support mailbox and App Store retention are controlled partly by third parties and are not specified in the legal inputs.

