<!-- brand:header:start -->
<p align="center">
  <img src="../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# Advanced Model Integration — One Code Base, Many Models

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

📘 **Explainer:** [LangChain-Advanced-Model-Integration-Explainer.pdf](./LangChain-Advanced-Model-Integration-Explainer.pdf) — this folder in a short, branded guide.

**Connect LangChain to OpenAI, Ollama, Claude or Gemini — and talk to any of them with the same messages.**

A **Phase-006-LangChain-Ecosystem** track. Only the line that creates the model changes between providers; `invoke()`, `stream()` and messages work the same way for all of them.

---

## Notebooks

| # | Notebook | What you learn |
| :-- | :-- | :-- |
| 01 | [01_Model_Integration.ipynb](./01_Model_Integration.ipynb) | `ChatOpenAI`, `invoke()`, `temperature`, streaming; switching to Ollama, Claude or Gemini |
| 02 | [02_Messages.ipynb](./02_Messages.ipynb) | `SystemMessage`, `HumanMessage`, `AIMessage`; the message list is the conversation memory |

## Providers at a glance

| Provider | Install | Create the model | Key |
| :-- | :-- | :-- | :-- |
| OpenAI | `langchain-openai` | `ChatOpenAI(model="gpt-4o-mini")` | `OPENAI_API_KEY` |
| Ollama | `langchain-ollama` | `ChatOllama(model="llama3")` | None — runs locally |
| Claude | `langchain-anthropic` | `ChatAnthropic(model="claude-opus-4-8")` | `ANTHROPIC_API_KEY` |
| Gemini | `langchain-google-genai` | `ChatGoogleGenerativeAI(model="gemini-2.0-flash")` | `GOOGLE_API_KEY` |

Model names are as written in the notebook; providers update their model lists regularly.

## Run

```powershell
cd "Phase-006-LangChain-Ecosystem\Langchain_Advanced_Model_Integration"
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
copy .env.example .env      # then paste your own keys into .env
```

The optional providers are commented out in [requirements.txt](./requirements.txt) — uncomment the ones you use. Keys go in a local `.env` file (see [.env.example](./.env.example)), which is git-ignored.

## Navigation

| Previous track | Up · Index | Next track |
| :-- | :--: | --: |
| [← LangChain Components](../Langchain-Components/) | [Phase-006-LangChain-Ecosystem](../) · [Journey index](../../README.md) | [LangChain vs LangGraph vs LangSmith →](../LangChain%20vs%20LangGraph%20vs%20LangSmith%20Explained/) |

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
  <a href="https://shasuvathanan.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/website-personal-logo.png" alt="Website" title="Website" height="24"></a>
  &nbsp;
  <a href="mailto:shasu1pm@gmail.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Gmail_Logo.svg" alt="Email" title="Email" height="24"></a>
  &nbsp;
  <a href="https://linkedin.com/in/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/linkedin.png" alt="LinkedIn" title="LinkedIn" height="24"></a>
  &nbsp;
  <a href="https://github.com/shasu1pm"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/github-custom.png" alt="GitHub" title="GitHub" height="24"></a>
  &nbsp;
  <a href="https://huggingface.co/Shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/huggingface.png" alt="Hugging Face" title="Hugging Face" height="24"></a>
  &nbsp;
  <a href="https://www.youtube.com/@ShasuVathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/youtube.png" alt="YouTube" title="YouTube" height="24"></a>
  &nbsp;
  <a href="https://x.com/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/x.png" alt="X (Twitter)" title="X (Twitter)" height="24"></a>
  &nbsp;
  <a href="https://higgsfield.ai/@shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Higgsfield_AI.png" alt="Higgsfield AI" title="Higgsfield AI" height="24"></a>
  <br>
  <sub><b>Connect:</b> <a href="https://shasuvathanan.com">Website</a> &nbsp;&#8226;&nbsp; <a href="mailto:shasu1pm@gmail.com">Email</a> &nbsp;&#8226;&nbsp; <a href="https://linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm">GitHub</a> &nbsp;&#8226;&nbsp; <a href="https://huggingface.co/Shasuvathanan">Hugging Face</a> &nbsp;&#8226;&nbsp; <a href="https://www.youtube.com/@ShasuVathanan">YouTube</a> &nbsp;&#8226;&nbsp; <a href="https://x.com/shasuvathanan">X (Twitter)</a> &nbsp;&#8226;&nbsp; <a href="https://higgsfield.ai/@shasuvathanan">Higgsfield AI</a></sub>
</p>
<!-- brand:social:end -->
<p align="center">
  <img src="../../zz-Brand-Assets/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>Shasu Vathanan - GEN AI - Product Manager</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; <a href="../../README.md">Back to the journey index</a></sub>
</p>
<!-- brand:footer:end -->
