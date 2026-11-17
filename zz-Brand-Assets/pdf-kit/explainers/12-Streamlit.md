---
out: Phase-004-FastAPI-And-Streamlit/Streamlit/Streamlit-Explainer.pdf
folder: Phase-004-FastAPI-And-Streamlit
title: Streamlit — Script to Interactive MVP
subtitle: Write Python, get a web app — no HTML, CSS or JavaScript
short: Streamlit
fact: Document | Sub-project explainer
fact: Level | Beginner
fact: Contents | Written guide · Streamlit Resources · Student Grade App
fact: Tools | Python 3.9+ · Streamlit
fact: Folder | Phase-004-FastAPI-And-Streamlit/Streamlit
keywords: Streamlit, MVP, web app, Python
---
# What it is
lead: Streamlit is a free, open-source Python framework that turns a script into an interactive web app.
Think of it as ready-made interface blocks: when you need a heading, input, button, table or chart, you call a function — `st.title()`, `st.number_input()`, `st.button()` — and Streamlit handles how it looks and responds in the browser.

# What is in this folder
| Item | What it is |
| :-- | :-- |
| `Introduction to Streamlit.md` + `.pdf` | The full written guide — basics, MVP thinking, a Calculator MVP step by step |
| `Streamlit_Basic.py` | The smallest possible Streamlit app |
| `Streamlit Resources/` | Three teaching notebooks and three runnable apps |
| `Streamlit Assignment Details/` | **Student Grade App** — the complete build with screenshots |

# The MVP idea
**MVP** means **Minimum Viable Product** — the smallest working version of an idea that still delivers its main value. A full calculator product might one day have scientific functions, history, accounts and themes; its MVP needs only two inputs, an operation, a button and a result.
> [!TIP] Product principle
> Build the smallest useful flow, test it with users, learn from the feedback, then add the next most valuable feature.

# How Streamlit runs your script
flow: Edit the .py file > Save > Browser reruns the script top to bottom > Widgets keep their values > Review and improve
Streamlit re-executes the whole script after every widget interaction, using the current widget values. There is no callback wiring — but expensive work runs every time unless it is cached.

# Get running in five commands
```powershell Terminal
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install streamlit
streamlit --version
streamlit run Streamlit_Basic.py
```
```python Streamlit_Basic.py
import streamlit as st

st.title("Streamlit Basic")
st.write("This is a basic Streamlit app")
```
> [!NOTE] Always use streamlit run
> Start apps with `streamlit run app.py`, never `python app.py` — only `streamlit run` starts the web server and the interactive reruns. The app opens at `http://localhost:8501`.

# Building blocks worth knowing
| Command | Purpose |
| :-- | :-- |
| `st.title("Text")` | Main page title |
| `st.write(value)` | Text, values and many Python objects |
| `st.text_input` / `st.number_input` | Text or numeric input |
| `st.selectbox("Label", options)` | Drop-down choice |
| `st.button("Label")` | Clickable action |
| `st.dataframe(data)` / `st.line_chart(data)` | Interactive table / quick chart |
| `st.success` / `st.warning` / `st.error` | Feedback messages |

# Common problems
| Problem | Fix |
| :-- | :-- |
| Streamlit not found | Activate the venv, or `python -m streamlit run app.py` |
| A change does not appear | Save the file, select **Rerun**, check the terminal for errors |
| Port 8501 in use | `Ctrl + C` the old server, or add `--server.port 8502` |

# Key takeaways
- Streamlit is the fastest path from a Python function to something a person can use.
- Design for reruns: the script runs top to bottom on every interaction.
- Start with an MVP, then iterate.
