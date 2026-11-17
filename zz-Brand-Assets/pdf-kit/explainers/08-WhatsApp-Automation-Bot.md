---
out: Phase-003-Robotic-Process-Automation-(RPA)/Playwright Automation/Playwright Assignment/WhatsApp-Automation-Bot-Explainer.pdf
folder: Phase-003-Robotic-Process-Automation-(RPA)
title: WhatsApp Automation Bot
subtitle: Consent-based WhatsApp Web messaging with reply monitoring, a timed follow-up and dated reports
fact: Document | Sub-project explainer
fact: Level | Intermediate
fact: Script | Playwright-WhatsApp-Automation-Bot.py
fact: Tools | Python · Playwright · Microsoft Edge · openpyxl
fact: Output | JSON + Excel reports, screenshots
fact: Folder | …/Playwright Automation/Playwright Assignment
keywords: Playwright, WhatsApp Web, Edge, automation, reports
---
# What it does
lead: Message each consenting contact, wait for a reply, follow up once if needed, and record the result.
The bot opens WhatsApp Web in Microsoft Edge with a reusable local profile, reads contacts from `contacts.xlsx`, sends a personalised message, monitors for a reply, sends at most one follow-up, captures the latest incoming messages and writes dated JSON and Excel reports.
> [!NOTE] Consent and terms
> Use this project only with people who have explicitly agreed to receive the messages. Automated or bulk messaging may violate WhatsApp's terms and can lead to account restrictions.

# The timing window — 300 seconds per contact
flow: Send initial message > Monitor for "Hi" > At 180 s: one follow-up if no reply > Reply → send confirmation > At 300 s: record no_reply
| Message | Text |
| :-- | :-- |
| Initial | Hi {name}! This is a test message from my Playwright WhatsApp Automation project. Please reply "Hi". Thank you! |
| Follow-up (once, at 180 s) | Hi {name}, just checking in. Please reply "Hi" when available. |
| Confirmation | Thank you {name}! Your reply has been received successfully. |

# Key features
- Manual QR login and manual **Use here** confirmation — the bot never bypasses security steps.
- Reads `Name`, `Phone` and optional `Message` columns; `{name}` placeholders are personalised.
- Continues to the next contact when one fails.
- Masks phone numbers in logs and reports; saves a final screenshot per contact.

# Run it
```powershell Setup and run
cd "Playwright Automation\Playwright Assignment"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install playwright openpyxl
python Playwright-WhatsApp-Automation-Bot.py
```
On the first run, scan the QR code yourself. `Ctrl+C` stops safely and still saves results for contacts already processed.

| Environment variable | Default | Purpose |
| :-- | :-- | :-- |
| `CONTACTS_FILE` | `contacts.xlsx` | Input workbook |
| `WHATSAPP_PROFILE_DIR` | `.whatsapp_profile` | Persistent Edge login profile |
| `OUTPUT_DIR` | `output` | Reports and screenshots |
| `LOGIN_TIMEOUT_SECONDS` | `300` | Time allowed for manual login |

# Output and statuses
```text Output
output/
├── screenshots/Contact_Name_YYYYMMDD_HHMMSS.png
├── whatsapp_report_YYYY-MM-DD.json
└── whatsapp_report_YYYY-MM-DD.xlsx
```
| Status | Meaning |
| :-- | :-- |
| `reply_received` | Message sent and a new expected reply detected |
| `no_reply` | No valid reply within the 300-second window |
| `failed` | Contact could not be processed; error recorded, run continues |

# Reliability and privacy
WhatsApp Web changes often, so the bot uses selector fallbacks, explicit waits and outgoing-message confirmation. The browser profile, `contacts.xlsx`, reports and screenshots can contain personal data — keep them private and out of source control (the folder's `.gitignore` excludes them).

# Key takeaways
- Fixed, honest timing rules beat aggressive retries.
- Keep humans in the loop for login and consent.
- Protect personal data: mask it in logs and never commit it.
