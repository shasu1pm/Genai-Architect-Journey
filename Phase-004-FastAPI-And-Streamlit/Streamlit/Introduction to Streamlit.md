# Streamlit

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

## Contents

| # | Section | What it covers |
| :-- | :-- | :-- |
| 1 | [What is Streamlit?](#1-what-is-streamlit) | The framework and what it replaces |
| 2 | [What is an MVP?](#2-what-is-an-mvp) | Minimum Viable Product thinking |
| 3 | [Basic Streamlit App](#3-basic-streamlit-app---additional-instructions) | The fastest path to a running app |
| 4 | [Prepare the project](#4-prepare-the-project) | Python, folders, and virtual environments |
| 5 | [Create and run the first application](#5-create-and-run-the-first-application) | `app.py` and the development loop |
| 6 | [Build a simple Calculator MVP](#6-build-a-simple-calculator-mvp) | The complete example |
| 7 | [Understand the Calculator MVP](#7-understand-the-calculator-mvp) | Why each line is there |
| 8 | [Useful Streamlit building blocks](#8-useful-streamlit-building-blocks) | The widget reference |
| 9 | [Streamlit files and notebooks](#9-streamlit-files-and-notebooks) | Project layout |
| 10 | [Common problems](#10-common-problems) | Fixes for what usually breaks |
| 11 | [Final workflow](#11-final-workflow) | The whole loop, start to finish |

> [!NOTE]
> Every command in this guide is written for **Windows Command Prompt**, including the
> terminal inside Visual Studio Code when its profile is set to Command Prompt. Where
> macOS and Linux differ, the alternative is shown directly beneath.

📄 Also available as a branded, printable document: [Introduction to Streamlit.pdf](./Introduction%20to%20Streamlit.pdf)

---

## 1. What is Streamlit?

Streamlit is a free, open-source Python framework for building interactive web applications. It is commonly used for:

- quick product prototypes and Minimum Viable Products (MVPs);
- data dashboards and charts;
- calculators and small business tools; and
- machine-learning or Generative AI demonstrations.

You write Python, and Streamlit creates the web interface. For a basic application, you do not need to write separate HTML, CSS, or JavaScript.

### A simple way to understand a framework

Think of Streamlit as a set of ready-made interface blocks. When you need a heading, input, button, table, or chart, you call a Streamlit function such as `st.title()`, `st.number_input()`, or `st.button()`. The framework handles how those elements appear and respond in the browser. This lets you focus on the application's purpose and logic.

## 2. What is an MVP?

**MVP** means **Minimum Viable Product**. It is the smallest working version of an idea that gives users its main value and helps you collect feedback before building the full product.

For example, imagine a complete calculator product may eventually include scientific operations, calculation history, user accounts, themes, and cloud storage. Its MVP can contain only:

1. two number inputs;
2. one choice of operation;
3. a **Calculate** button; and
4. the result.

This small version is enough to test whether the main calculation flow works and whether users understand it. Streamlit is useful for MVPs because the interface can be built, shown, tested, and improved quickly.

> **Product principle:** Build the smallest useful flow, test it with users, learn from the feedback, and then add the next most valuable feature.

## 3. Basic Streamlit App - Additional Instructions

Use the following beginner-friendly sequence in **Windows Command Prompt**. Open Command Prompt in the folder where you want to create the application before starting.

| Step | Command | Purpose |
|---|---|---|
| 1. Create an environment | `python -m venv venv` | Creates an isolated Python environment named `venv`. |
| 2. Activate the environment | `venv\Scripts\activate` | Activates the environment in Windows Command Prompt. The prompt should show `(venv)`. |
| 3. Install Streamlit | `python -m pip install streamlit` | Installs Streamlit inside the active environment. Run this once for the environment. |
| 4. Check Streamlit | `streamlit --version` | Confirms that Streamlit is installed and displays its version. |
| 5. Run a standard app | `streamlit run app.py` | Starts a Streamlit file named `app.py`. |

### Required commands

```bat
python -m venv venv
venv\Scripts\activate
streamlit --version
streamlit run app.py
```

```bat
# Activate
venv\Scripts\activate

# Deactivate / exit venv
deactivate
```

### Basic application file

| Item | Details |
|---|---|
| File name | `Streamlit_Basic.py` |
| Command to run | `streamlit run Streamlit_Basic.py` |
| To Run | `Streamlit run Streamlit_Basic.py` |
| Expected browser address | `http://localhost:8501` |
| Stop the application | Press `Ctrl+C` in Command Prompt |

Create or open `Streamlit_Basic.py`, then use this basic code:

**Basic Code:**

```python
#Streamlit Basic
import streamlit as st

st.title("Streamlit Basic")
st.write("This is a basic Streamlit app")
```

### Basic code explanation

| Code | What it does |
|---|---|
| `#Streamlit Basic` | Adds a Python comment that identifies the example. |
| `import streamlit as st` | Imports Streamlit and gives it the short name `st`. |
| `st.title("Streamlit Basic")` | Displays the main heading in the browser. |
| `st.write("This is a basic Streamlit app")` | Displays the supporting text under the heading. |

### Run the basic application

Make sure the environment is active and Command Prompt is in the folder containing `Streamlit_Basic.py`. Then run:

```bat
streamlit run Streamlit_Basic.py
```

Streamlit opens the application in the default browser. If it does not open automatically, copy the Local URL shown in Command Prompt and open it manually. Press `Ctrl+C` to stop the server. When finished, run `deactivate` to leave the virtual environment.

## 4. Prepare the project

### Step 1 - Check Python

This guide uses **Windows Command Prompt**, including the terminal inside Visual Studio Code when its profile is set to **Command Prompt**.

```bat
py --version
py -m pip --version
```

If `py` is unavailable but `python` works, replace `py` with `python` in every command.

### Step 2 - Create and open a project folder

```bat
mkdir streamlit_mvp
cd streamlit_mvp
```

### Step 3 - Create a virtual environment

```bat
py -m venv .venv
```

A virtual environment keeps this project's packages separate from other Python projects.

### Step 4 - Activate it correctly

In **Windows Command Prompt**, run:

```bat
.venv\Scripts\activate.bat
```

The prompt should begin with `(.venv)`. Keep the terminal profile set to **Command Prompt** throughout this workflow.

For macOS or Linux, the equivalent command is:

```bash
source .venv/bin/activate
```

### Step 5 - Install and verify Streamlit

```bat
python -m pip install streamlit
python -m streamlit --version
```

After activation, using `python -m pip` ensures that Streamlit is installed into the active virtual environment.

### Step 6 - Confirm Streamlit with its built-in demo

```bat
python -m streamlit hello
```

A browser should open with Streamlit's example application. Return to the terminal and press `Ctrl+C` to stop it.

## 5. Create and run the first application

Create a file named `app.py` and add:

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello! Welcome to Streamlit.")
```

- `import streamlit as st` imports Streamlit using its standard short name.
- `st.title()` creates the main page heading.
- `st.write()` displays text or other Python values.

### Run and update the application

Save `app.py`. In the activated Command Prompt, run:

```bat
python -m streamlit run app.py
```

The general command is:

```text
python -m streamlit run <file-name>.py
```

Streamlit starts a local web server and normally opens the app in a browser. If it does not open automatically, use the **Local URL** shown in the terminal, usually `http://localhost:8501`.

Do not start a Streamlit interface with `python app.py`. The `streamlit run` command is needed to manage the web server and interactive reruns.

### The development loop

1. Edit the Python file.
2. Save it with `Ctrl+S`.
3. Return to the browser.
4. Select **Rerun** if Streamlit asks, or enable **Always rerun**.
5. Review the result and continue improving it.

Streamlit executes the script from top to bottom after a widget interaction. The current widget values are used during the new run.

## 6. Build a simple Calculator MVP

Replace the code in `app.py` with the following complete example:

```python
import streamlit as st

st.set_page_config(page_title="Calculator MVP", page_icon="🧮")

st.title("Calculator MVP")
st.write("Enter two numbers, select an operation, and calculate the result.")

number_1 = st.number_input("First number", value=0.0)
number_2 = st.number_input("Second number", value=0.0)
operation = st.selectbox(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"],
)

if st.button("Calculate", type="primary"):
    if operation == "Add":
        result = number_1 + number_2
    elif operation == "Subtract":
        result = number_1 - number_2
    elif operation == "Multiply":
        result = number_1 * number_2
    elif number_2 == 0:
        result = None
        st.error("Division by zero is not allowed.")
    else:
        result = number_1 / number_2

    if result is not None:
        st.success(f"Result: {result:g}")
```

Save the file. The running application reruns automatically or after you select **Rerun**.

## 7. Understand the Calculator MVP

### Page setup and content

`st.set_page_config()` sets browser-page information. It must be the first Streamlit command in the file. `st.title()` and `st.write()` explain the page's purpose.

### Inputs

`st.number_input()` returns a numeric value. Each call has a different label so users know which value to enter. `st.selectbox()` limits the operation to four valid choices.

### Action and decision logic

`st.button()` returns `True` when clicked. The `if` and `elif` statements then apply the selected operation. This logic is ordinary Python; Streamlit supplies the interface around it.

### Validation and output

Division by zero is checked before division takes place. `st.error()` explains invalid input, while `st.success()` presents a valid result. Good MVPs cover the main success path and an important failure path.

### What to test

Use this small test checklist before sharing the MVP:

| Test | Input | Expected result |
|---|---|---|
| Addition | `10`, `5`, Add | `15` |
| Subtraction | `10`, `5`, Subtract | `5` |
| Multiplication | `10`, `5`, Multiply | `50` |
| Division | `10`, `5`, Divide | `2` |
| Invalid division | `10`, `0`, Divide | Clear error message |

Ask a test user to complete a calculation without instructions. Observe whether the labels, operation choice, button, and result are easy to understand. That feedback determines what should be improved next.

## 8. Useful Streamlit building blocks

| Command | Purpose |
|---|---|
| `st.title("Text")` | Main page title |
| `st.write(value)` | Text, values, and many Python objects |
| `st.text_input("Label")` | Single-line text input |
| `st.number_input("Label")` | Numeric input |
| `st.selectbox("Label", options)` | Drop-down choice |
| `st.button("Label")` | Clickable action |
| `st.dataframe(data)` | Interactive data table |
| `st.line_chart(data)` | Quick line chart |
| `st.success("Text")` | Success feedback |
| `st.warning("Text")` | Warning feedback |
| `st.error("Text")` | Error feedback |

These building blocks can later support dashboards, chart applications, and AI model demonstrations mentioned in the lesson.

## 9. Streamlit files and notebooks

For this beginner workflow, place the application in a normal Python `.py` file and run it from a terminal. Do not paste the app into a normal Jupyter `.ipynb` cell and expect the same browser-app workflow.

```text
streamlit_mvp/
├── .venv/
├── app.py
└── requirements.txt
```

Create a small dependency file manually:

```text
streamlit
```

Install it on another computer with:

```bat
python -m pip install -r requirements.txt
```

Do not share the `.venv` directory. Recreate it and install the listed dependencies instead.

## 10. Common problems

### Streamlit is not found

Make sure `(.venv)` appears in Command Prompt, then use:

```bat
python -m streamlit run app.py
```

### The module is missing

Install Streamlit into the active environment:

```bat
python -m pip install streamlit
```

### The application file is not found

Run `dir`, confirm that `app.py` is listed, and use `cd` to enter the correct folder.

### The browser does not open

Copy the Local URL printed in the terminal and open it manually.

### A code change does not appear

Save the file, select **Rerun**, and check the terminal for a Python error.

### Port 8501 is already in use

Stop the previous server with `Ctrl+C`, or use another port:

```bat
python -m streamlit run app.py --server.port 8502
```

## 11. Final workflow

1. Open Command Prompt in the project folder.
2. Activate with `.venv\Scripts\activate.bat`.
3. Install Streamlit with `python -m pip install streamlit`.
4. Write the interface in `app.py`.
5. Run it with `python -m streamlit run app.py`.
6. Test the main user flow and important errors.
7. Collect user feedback before expanding the MVP.
8. Stop the server with `Ctrl+C`.
9. Deactivate the environment with `deactivate` when finished.

### Possible next improvements

After the MVP is validated, add one valuable feature at a time—for example calculation history, more operations, or a downloadable result. Avoid adding features until the main flow is clear and useful.

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
