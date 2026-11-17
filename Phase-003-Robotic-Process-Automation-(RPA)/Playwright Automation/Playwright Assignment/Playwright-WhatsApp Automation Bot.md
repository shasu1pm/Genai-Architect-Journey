<!-- brand:header:start -->
<p align="center">
  <img src="../../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# WhatsApp Automation Bot — Project Brief

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

## Project in Short

This project is a **Python + Playwright WhatsApp Web Automation Bot**
that runs through **Microsoft Edge**. It accesses WhatsApp Web using an
existing logged-in session when available, searches for a specific phone
number, sends a personalized test message, waits for a reply, sends a
follow-up when required, confirms successful replies, and takes a
screenshot.

## Automation Details

-   **Browser:** Microsoft Edge
-   **WhatsApp Web:** Access WhatsApp Web if the user is already logged in. Otherwise, wait and allow the user to 
	manually click the "Use Here" button. Once the user clicks the button, continue the entire workflow.
	Alternatively, if the phone number can already be searched successfully, proceed with the entire workflow.
-   **Search Phone Number:** `+91 80984 16430`
-   **Send Message:**
    `Hi {name}! This is a test message from my Playwright WhatsApp Automation project. Please reply "Hi". Thank you!`
-   **Expected Reply:** `Hi`
-   **Reply Waiting Time:** 60 to 300 seconds.
-   **Follow-up:** If no reply is received during the initial 60 to 180
    seconds, send:
    `Hi {name}, just checking in. Please reply "Hi" when available.`
-   **Reply Message:**
    `Thank you {name}! Your reply has been received successfully.`
-   **Screenshot:** Take a screenshot of the conversation/status.

## Workflow

``` text
START
  ↓
Launch Microsoft Edge
  ↓
Open WhatsApp Web
  ↓
Check Existing Login Session
  ↓
Search Phone Number: +91 80984 16430
  ↓
Open Chat
  ↓
Send Initial Message
  ↓
Wait for Reply (60–300 Seconds)
  ↓
Is "Hi" Received?
     /       \
   YES        NO
    ↓          ↓
Send Thank   If no reply during
You Message  initial 60–180 sec
    ↓          ↓
    │       Send Follow-up Message
    │          ↓
    │       Continue Waiting
    │          ↓
    └──────────┤
               ↓
        Take Screenshot
               ↓
              END
```

## Message Flow

### Initial Message

``` text
Hi {name}! This is a test message from my Playwright WhatsApp Automation project. Please reply "Hi". Thank you!
```

### Expected User Reply

``` text
Hi
```

### Follow-up Message

``` text
Hi {name}, just checking in. Please reply "Hi" when available.
```

### Successful Reply Confirmation

``` text
Thank you {name}! Your reply has been received successfully.
```

## Timing Logic

-   Start monitoring for a reply after sending the initial message.
-   Allow an overall reply waiting window of up to **300 seconds**.
-   If no expected reply is received during the initial **60--180
    second** period, send the follow-up message.
-   Continue monitoring for the expected `"Hi"` reply.
-   When `"Hi"` is received, send the confirmation message.
-   Take a screenshot of the resulting conversation/status.

## Expected Result

The automation demonstrates Microsoft Edge browser automation, existing
WhatsApp Web session access, contact search by phone number, automated
message sending, dynamic waiting, conditional follow-up messaging, reply
detection, automated confirmation messaging, screenshot capture, and
safe browser completion.

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>

<!-- brand:footer:start -->
<!-- brand:social:start -->
<p align="center">
  <a href="https://shasuvathanan.com"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/website-personal-logo.png" alt="Website" title="Website" height="24"></a>
  &nbsp;
  <a href="mailto:shasu1pm@gmail.com"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/Gmail_Logo.svg" alt="Email" title="Email" height="24"></a>
  &nbsp;
  <a href="https://linkedin.com/in/shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/linkedin.png" alt="LinkedIn" title="LinkedIn" height="24"></a>
  &nbsp;
  <a href="https://github.com/shasu1pm"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/github-custom.png" alt="GitHub" title="GitHub" height="24"></a>
  &nbsp;
  <a href="https://huggingface.co/Shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/huggingface.png" alt="Hugging Face" title="Hugging Face" height="24"></a>
  &nbsp;
  <a href="https://www.youtube.com/@ShasuVathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/youtube.png" alt="YouTube" title="YouTube" height="24"></a>
  &nbsp;
  <a href="https://x.com/shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/x.png" alt="X (Twitter)" title="X (Twitter)" height="24"></a>
  &nbsp;
  <a href="https://higgsfield.ai/@shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/Higgsfield_AI.png" alt="Higgsfield AI" title="Higgsfield AI" height="24"></a>
  <br>
  <sub><b>Connect:</b> <a href="https://shasuvathanan.com">Website</a> &nbsp;&#8226;&nbsp; <a href="mailto:shasu1pm@gmail.com">Email</a> &nbsp;&#8226;&nbsp; <a href="https://linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm">GitHub</a> &nbsp;&#8226;&nbsp; <a href="https://huggingface.co/Shasuvathanan">Hugging Face</a> &nbsp;&#8226;&nbsp; <a href="https://www.youtube.com/@ShasuVathanan">YouTube</a> &nbsp;&#8226;&nbsp; <a href="https://x.com/shasuvathanan">X (Twitter)</a> &nbsp;&#8226;&nbsp; <a href="https://higgsfield.ai/@shasuvathanan">Higgsfield AI</a></sub>
</p>
<!-- brand:social:end -->
<p align="center">
  <img src="../../../zz-Brand-Assets/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>Shasu Vathanan - GEN AI - Product Manager</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; <a href="../../../README.md">Back to the journey index</a></sub>
</p>
<!-- brand:footer:end -->
