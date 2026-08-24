# Streamlit — From Python Script to Interactive MVP

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**Write Python. Get a web app. No HTML, CSS, or JavaScript.**

Streamlit is a free, open-source Python framework for building interactive web applications. This folder holds the written guide, the teaching notebooks, the small working apps, and the complete Student Grade App build.

---

## Quick Navigation

| # | Item | What it is |
| :-- | :-- | :-- |
| 1 | [Introduction to Streamlit](./Introduction%20to%20Streamlit.md) | The complete written guide — read this first |
| 2 | [Streamlit Resources](./Streamlit%20Resources/) | Notebooks and small working apps to run and edit |
| 3 | [Streamlit Assignment Details](./Streamlit%20Assignment%20Details/) | **Student Grade App** — the complete build |

---

## Contents

| File | Description |
| :-- | :-- |
| [`Introduction to Streamlit.md`](./Introduction%20to%20Streamlit.md) | Framework basics, MVP thinking, and a Calculator MVP built step by step |
| [`Introduction to Streamlit.pdf`](./Introduction%20to%20Streamlit.pdf) | The same guide as a branded, printable document |
| [`Streamlit_Basic.py`](./Streamlit_Basic.py) | The smallest possible Streamlit app — four lines |
| [`Streamlit Resources/`](./Streamlit%20Resources/) | Three teaching notebooks and three runnable apps |
| [`Streamlit Assignment Details/`](./Streamlit%20Assignment%20Details/) | Student Grade App — the complete build, with screenshots |

---

## Why Streamlit

Think of Streamlit as a set of ready-made interface blocks. When you need a heading, input, button, table, or chart, you call a function — `st.title()`, `st.number_input()`, `st.button()` — and the framework handles how it appears and responds in the browser.

That leaves you free to work on what the application is actually *for*.

| Common use | Example |
| :-- | :-- |
| Prototypes and MVPs | A calculator that proves the flow before the real product is built |
| Data dashboards | Charts and tables over a live dataset |
| Small business tools | A grade calculator, a quote estimator, an internal lookup |
| AI demonstrations | A prompt box in front of a model, shown to non-technical stakeholders |

---

## Get running in five commands

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install streamlit
streamlit --version
streamlit run Streamlit_Basic.py
```

The app opens at `http://localhost:8501`. Press `Ctrl + C` to stop it, and `deactivate` to leave the environment.

### The smallest app there is

```python
# Streamlit Basic
import streamlit as st

st.title("Streamlit Basic")
st.write("This is a basic Streamlit app")
```

> [!IMPORTANT]
> Start Streamlit apps with `streamlit run app.py` — never `python app.py`. The `streamlit run` command is what manages the web server and the interactive reruns. Without it you get plain script output and no interface.

---

## The MVP idea, in one paragraph

**MVP** means **Minimum Viable Product** — the smallest working version of an idea that still delivers its main value. A complete calculator product might eventually have scientific operations, history, accounts, themes, and cloud sync. Its MVP needs only two inputs, one operation choice, a button, and a result. That is enough to find out whether the flow works and whether people understand it.

> **Product principle:** build the smallest useful flow, test it with users, learn from the feedback, and then add the next most valuable feature.

---

## Building blocks worth knowing

| Command | Purpose |
| :-- | :-- |
| `st.title("Text")` | Main page title |
| `st.write(value)` | Text, values, and many Python objects |
| `st.text_input("Label")` | Single-line text input |
| `st.number_input("Label")` | Numeric input |
| `st.selectbox("Label", options)` | Drop-down choice |
| `st.button("Label")` | Clickable action |
| `st.dataframe(data)` | Interactive data table |
| `st.line_chart(data)` | Quick line chart |
| `st.success` / `st.warning` / `st.error` | Feedback messages |

---

## How Streamlit reruns

Streamlit executes the script **top to bottom after every widget interaction**, using the current widget values. There is no callback wiring and no event loop to manage — but it does mean expensive work runs on every interaction unless you cache it.

The development loop:

1. Edit the Python file.
2. Save it with `Ctrl + S`.
3. Return to the browser.
4. Select **Rerun**, or enable **Always rerun**.
5. Review the result and keep improving it.

---

## Common problems

| Problem | Cause | Fix |
| :-- | :-- | :-- |
| Streamlit is not found | The environment is not active | Confirm `(venv)` in the prompt, then run `python -m streamlit run app.py` |
| The module is missing | Installed into a different environment | `python -m pip install streamlit` inside the active venv |
| The file is not found | Wrong working folder | Run `dir`, confirm the file is listed, then `cd` into the right folder |
| The browser does not open | No default browser handoff | Copy the **Local URL** from the terminal and open it manually |
| A change does not appear | File not saved, or the script errored | Save, select **Rerun**, and check the terminal for a Python error |
| Port 8501 already in use | A previous server is still running | `Ctrl + C`, or add `--server.port 8502` |

---

## Requirements

- Python 3.9 or newer
- `streamlit`

📄 **Full written guide:** [Introduction to Streamlit.md](./Introduction%20to%20Streamlit.md) · [PDF](./Introduction%20to%20Streamlit.pdf)

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
