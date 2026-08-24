# Streamlit Resources — Notebooks and Working Apps

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**Three notebooks to read, three apps to run.**

The notebooks explain Streamlit concept by concept. The `.py` files are the working apps those concepts build up to — each one runs on its own.

---

## Learning path

Work through the notebooks in order, then run the apps.

| # | Notebook | What you learn |
| :-- | :-- | :-- |
| 1 | [`01_Introduction_to_Streamlit.ipynb`](./01_Introduction_to_Streamlit.ipynb) | What Streamlit is, installing it, and writing a first app |
| 2 | [`02_Streamlit_Components.ipynb`](./02_Streamlit_Components.ipynb) | The widget catalogue — text, inputs, buttons, feedback, charts |
| 3 | [`03_Build_a_Simple_Streamlit_App.ipynb`](./03_Build_a_Simple_Streamlit_App.ipynb) | Combining widgets into a complete BMI Calculator |

---

## Runnable apps

| App | What it does | Run with |
| :-- | :-- | :-- |
| [`app.py`](./app.py) | **BMI Calculator** — two inputs, a button, and a categorised result | `streamlit run app.py` |
| [`test.py`](./test.py) | **Widget tour** — selectbox, checkbox, and all four feedback message types | `streamlit run test.py` |
| [`calculator.py`](./calculator.py) | **Full calculator** — a styled keypad using session state | `streamlit run calculator.py` |

---

## Setup

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install streamlit
```

Then start any of the apps above. Each opens at `http://localhost:8501`. Press `Ctrl + C` to stop.

> [!IMPORTANT]
> The notebooks are for **reading and understanding**. Streamlit apps do not run inside a notebook cell — put the code in a `.py` file and start it with `streamlit run`.

---

## What each app demonstrates

### `app.py` — the shape of every Streamlit app

Title, inputs, a button, a result, and a message that changes with the outcome. Almost every small Streamlit tool is this pattern with different arithmetic in the middle.

```python
weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (meters):", min_value=0.1)

if st.button("Calculate BMI"):
    bmi = weight / (height * height)
    st.write("Your BMI is:", round(bmi, 2))
```

Note `min_value` — the widget itself prevents a zero height, so the division can never fail. Validating at the input is cheaper than handling the error afterwards.

### `test.py` — the feedback vocabulary

Four message types, each with its own meaning. Using the right one is how a user knows whether something worked.

| Call | Colour | Use it for |
| :-- | :-- | :-- |
| `st.success()` | Green | The action completed |
| `st.info()` | Blue | Neutral context |
| `st.warning()` | Yellow | Allowed, but check this |
| `st.error()` | Red | The action failed |

### `calculator.py` — session state

The keypad calculator has to remember the expression **between reruns**. Since Streamlit re-executes the whole script on every click, an ordinary variable would reset each time. `st.session_state` is what survives:

```python
if "expression" not in st.session_state:
    st.session_state.expression = ""
```

This is the single most important concept for building anything beyond a one-shot form.

> [!NOTE]
> `calculator.py` evaluates the typed expression with `eval()`. That is acceptable in a local learning demo where you are the only user. Never expose an `eval()` on user input in a deployed app — parse the expression instead.

---

## Requirements

- Python 3.9 or newer
- `streamlit`

📄 **The written guide for this folder:** [Introduction to Streamlit.md](../Introduction%20to%20Streamlit.md)

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
