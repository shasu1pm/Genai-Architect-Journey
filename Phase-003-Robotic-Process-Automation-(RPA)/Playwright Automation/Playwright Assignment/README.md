# WhatsApp Automation Bot

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

A Python and Playwright bot that uses Microsoft Edge to send personalized, consent-based WhatsApp Web messages, monitor replies, send a conditional follow-up, capture incoming messages, and generate dated JSON and Excel reports.

📄 **Project document:** [WhatsApp Automation Bot.pdf](./WhatsApp%20Automation%20Bot.pdf)

> Use this project only with people who have explicitly agreed to receive the messages. Automated or bulk messaging may violate WhatsApp's terms and can result in account restrictions.

## Features

- Opens WhatsApp Web in Edge with a reusable local browser profile.
- Supports manual QR login and manual **Use here** confirmation.
- Reads `Name`, `Phone`, and optional `Message` values from `contacts.xlsx`.
- Searches each international phone number and continues when a contact fails.
- Reads the displayed chat name and personalizes `{name}` placeholders.
- Waits for a new incoming `Hi` for up to five minutes.
- Sends one follow-up at 180 seconds only when a matching reply has not arrived.
- Sends a confirmation immediately after a valid reply.
- Extracts the latest three incoming messages and saves a final screenshot.
- Masks phone numbers in logs and generated reports.

## Message flow

The built-in initial message is:

```text
Hi {name}! This is a test message from my Playwright WhatsApp Automation project. Please reply "Hi". Thank you!
```

If no new `Hi` has arrived after 180 seconds, the bot sends exactly one follow-up:

```text
Hi {name}, just checking in. Please reply "Hi" when available.
```

When a new `Hi` is detected, it sends:

```text
Thank you {name}! Your reply has been received successfully.
```

The full timing window is fixed at 300 seconds per successfully messaged contact. The bot monitors immediately, sends the follow-up at 180 seconds if needed, and records `no_reply` at 300 seconds.

## Requirements

- Python 3.10+
- Microsoft Edge
- A WhatsApp account that can use WhatsApp Web
- Internet access
- Contacts who have consented to the test

## Setup

```powershell
cd "Playwright Automation\Playwright Assignment"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install playwright openpyxl
```

The script launches the installed Microsoft Edge channel, so a separate Chromium download is normally unnecessary. If Playwright reports missing browser support, run:

```powershell
python -m playwright install msedge
```

## Prepare `contacts.xlsx`

The included workbook is the runtime input. Back it up, review it for private data, and use the following first-row headers:

| Name | Phone | Message |
| --- | --- | --- |
| Sample Contact | +91XXXXXXXXXX | Hi {name}! This is a test message. Please reply "Hi". |

`Name` and `Phone` are required. `Message` is optional; the built-in initial message is used when it is empty or absent. Use international phone format with a country code. Do not publish a workbook containing real contact details.

## Run

Close any other Edge window using this project's `.whatsapp_profile`, then run:

```powershell
python Playwright-WhatsApp-Automation-Bot.py
```

On the first run, scan the WhatsApp Web QR code manually. If WhatsApp says it is active elsewhere, click **Use here** yourself. The visible browser then processes contacts one at a time.

Press `Ctrl+C` to stop safely. The bot still attempts to save results for contacts that have already been processed.

## Configuration

| Environment variable | Default | Purpose |
| --- | --- | --- |
| `CONTACTS_FILE` | `contacts.xlsx` | Input workbook path |
| `WHATSAPP_PROFILE_DIR` | `.whatsapp_profile` | Persistent Edge login profile |
| `OUTPUT_DIR` | `output` | Reports and screenshot directory |
| `LOGIN_TIMEOUT_SECONDS` | `300` | Maximum time for manual login/readiness |

Example:

```powershell
$env:CONTACTS_FILE = "C:\private\contacts.xlsx"
$env:OUTPUT_DIR = "C:\private\whatsapp-output"
python Playwright-WhatsApp-Automation-Bot.py
```

Reply timing is intentionally fixed in the source and cannot be shortened through environment variables.

## Output

```text
output/
├── screenshots/
│   └── Contact_Name_YYYYMMDD_HHMMSS.png
├── whatsapp_report_YYYY-MM-DD.json
└── whatsapp_report_YYYY-MM-DD.xlsx
```

Possible result statuses include:

- `reply_received` — the initial message was sent and a new expected reply was detected.
- `no_reply` — no valid new reply arrived during the 300-second window.
- `failed` — the contact could not be processed; the error is recorded and processing continues.

If a report is open or locked, the script attempts to use a timestamped fallback filename. Existing sample output may contain conversation metadata and should be reviewed before sharing.

## Reliability and privacy

WhatsApp Web is dynamic and its page structure can change. The bot uses selector fallbacks, explicit waits, outgoing-message confirmation, and exception handling, but future UI updates may require locator changes. Test with one consenting contact before processing more rows.

The `.whatsapp_profile` directory contains reusable login information. `contacts.xlsx`, generated reports, and screenshots can contain personal data. Keep all of them private and out of source control. The provided `.gitignore` excludes the profile, input workbook, and generated output when this folder is used in a Git repository.

The companion [`Playwright-WhatsApp Automation Bot.md`](./Playwright-WhatsApp%20Automation%20Bot.md) holds the project brief. The two `Error Fix` PNG files document browser dialogs encountered during development and how they were resolved.

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
