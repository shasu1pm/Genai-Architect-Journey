"""Build the branded explainer PDFs for folders that did not have one.

Every document is written from the folder's real content (README, notebooks, scripts) —
nothing is invented. Run:  python build_docs.py [name-filter ...]
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand_pdf import (ASSETS, BLUE, CORAL, LM, LOGO, NAME, NEGOT, RM, S, STRIP, W, Spacer, _img, build,  # noqa: E402
                       bullets, callout, code, flow, h1, h2, lead, p, small, table)
from reportlab.platypus import Flowable, Paragraph, Table, TableStyle  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
P4 = "Phase-004-FastAPI-And-Streamlit"
P6 = "Phase-006-LangChain-Ecosystem"
P7 = "Phase-007-RAG-Introduction"


class _AssetImage(Flowable):
    """Draws an original brand asset (downscaled in memory by brand_pdf._img)."""

    def __init__(self, path, width):
        super().__init__()
        self.ir = _img(path)
        iw, ih = self.ir.getSize()
        self.width, self.height = width, width * ih / iw

    def draw(self):
        self.canv.drawImage(self.ir, 0, 0, width=self.width, height=self.height, mask="auto")


def _asset_image(path, width):
    return _AssetImage(path, width)


# ============================================================================ Phase-004 overview
def doc_phase004():
    s = []
    s += h1("Where scripts become products")
    s.append(lead("Phase-004-FastAPI-And-Streamlit adds the two interfaces that turn Python logic into "
                  "something other people — and other programs — can reach."))
    s.append(p("Phase-001-Programming-Foundations to Phase-003-Robotic-Process-Automation-(RPA) produced "
               "logic that runs in a terminal. Nobody else can use a terminal script. This phase adds "
               "**a web UI with Streamlit** and **a web API with FastAPI**."))
    s += flow(["Python logic", "Streamlit · for people", "FastAPI · for programs", "Shared by every client"])
    s += h1("What is in this phase")
    s += h2("Streamlit — the human interface")
    s += table(["Item", "What it is"], [
        ["`Streamlit/Introduction to Streamlit.md` + `.pdf`", "The full written guide — framework basics, MVP thinking and a Calculator MVP built step by step"],
        ["`Streamlit/Streamlit Resources/`", "Three teaching notebooks and three working apps — BMI calculator, widget tour, styled calculator"],
        ["`Streamlit/Streamlit Assignment Details/`", "**Student Grade App** — the complete build, with screenshots and a project brief PDF"],
        ["`Streamlit/Streamlit_Basic.py`", "The smallest possible Streamlit app"],
    ], [0.42, 0.58])
    s += h2("FastAPI — the machine interface")
    s += table(["Item", "What it is"], [
        ["`FirstAPI/FastAPI Calculator API.pdf`", "Complete build guide for the Calculator API — source, endpoints, testing, error handling"],
        ["`FirstAPI/calculator.py`", "The Calculator API — four operations, Pydantic models, guarded division"],
        ["`FirstAPI/FirstAPI.py`", "The first endpoint written in this repository"],
        ["`FirstAPI/FastAPI App Assignments/`", "**Basic FastAPI App** — the complete build, with a Postman collection and project brief PDF"],
    ], [0.42, 0.58])
    s += h1("Streamlit or FastAPI — which one, and when")
    s.append(p("Both take the same Python function and make it reachable. They differ in who is doing the reaching."))
    s += table(["", "Streamlit", "FastAPI"], [
        ["**Built for**", "A person, in a browser", "Another program, over HTTP"],
        ["**You write**", "Widgets and layout", "Endpoints and data models"],
        ["**Returns**", "A rendered page", "JSON"],
        ["**Run it with**", "`streamlit run app.py`", "`uvicorn main:app --reload`"],
        ["**Default address**", "`http://localhost:8501`", "`http://127.0.0.1:8000`"],
        ["**Documentation**", "The interface is the documentation", "Auto-generated at `/docs`"],
        ["**Best for**", "Demos, dashboards, internal tools, MVPs", "Services, integrations, automation, AI agents"],
    ], [0.22, 0.39, 0.39])
    s += callout("They are not competitors",
                 "A common production shape is a **FastAPI service holding the logic** with a **Streamlit app "
                 "calling it** — the API serves every client, and the UI is just one of them.")
    s += callout("Real-world illustration (hypothetical)",
                 "An online retailer could expose its price-check logic once through FastAPI, then let its "
                 "mobile app, its partners and an internal Streamlit dashboard all call the same endpoint. "
                 "This is an illustration, not a description of any company's system.", "tip")
    s += h1("What this phase demonstrates")
    s += bullets([
        "**Both interface models**, built from scratch rather than from a template.",
        "**Input validation as a first-class concern** — every app handles empty, non-numeric and out-of-range input without crashing.",
        "**Meaningful failure** — HTTP 400 for impossible operations, 422 for malformed data, friendly on-screen messages for people.",
        "**Evidence of working software** — screenshots for the UI and an importable Postman collection for the API.",
    ])
    s += h1("Running anything in this phase")
    s.append(p("Each project folder has its own README with exact commands. The general shape is always the same:"))
    s += code('cd "path\\to\\the\\project"\npython -m venv venv\nvenv\\Scripts\\Activate.ps1\n'
              'python -m pip install -r requirements.txt\n\n'
              'streamlit run <file>.py          # a Streamlit app\nuvicorn <file>:app --reload      # a FastAPI app',
              "PowerShell")
    s += callout("Keep environments local",
                 "Create a fresh virtual environment inside the project you want to run. Virtual environments are "
                 "machine-specific and never committed — `requirements.txt` is what makes a project reproducible.")
    s += h1("Key takeaways")
    s += bullets(["A script becomes a product when someone else can reach it.",
                  "Streamlit is the fastest path to a UI for people; FastAPI is the standard path to an API for programs.",
                  "Validate every input and fail with a clear, specific message.",
                  "Next: Phase-005-LLM-Foundations-and-Practical-Tools adds the model itself."])
    return dict(out=REPO / P4 / "FastAPI-And-Streamlit-Explainer.pdf", folder=P4, title="FastAPI and Streamlit",
                short="FastAPI and Streamlit", subtitle="Interfaces and APIs — turning Python scripts into products people and programs can use",
                facts=[("Document", "Phase explainer"), ("Level", "Beginner to intermediate"),
                       ("Tools", "Python 3.9+ · Streamlit · FastAPI · Pydantic · Uvicorn"),
                       ("Tracks", "Streamlit (human interface) · FirstAPI (machine interface)"),
                       ("Folder", P4)],
                story=s, keywords="Streamlit, FastAPI, API, UI, Python")


# ============================================================================ Streamlit Resources
def doc_streamlit_resources():
    s = []
    s += h1("Three notebooks to read, three apps to run")
    s.append(lead("The notebooks explain Streamlit concept by concept; the .py files are the working apps those concepts build up to."))
    s += table(["File", "What it is"], [
        ["`01_Introduction_to_Streamlit.ipynb`", "What Streamlit is, installing it, a first app, and running it with `streamlit run`"],
        ["`02_Streamlit_Components.ipynb`", "Text, input, button, slider, selectbox, checkbox and message components"],
        ["`03_Build_a_Simple_Streamlit_App.ipynb`", "Building a complete BMI Calculator, plus a Greeting App practice idea"],
        ["`app.py`", "The finished BMI Calculator from notebook 03"],
        ["`test.py`", "A short widget tour — title, selectbox, checkbox and the four message types"],
        ["`calculator.py`", "A styled calculator app using custom CSS in the brand's deep-blue palette"],
    ], [0.4, 0.6])
    s += callout("Streamlit apps do not run inside notebook cells",
                 "Save the code in a `.py` file and run it with `streamlit run filename.py`. It opens in the browser, "
                 "usually at `http://localhost:8501`. Press **Ctrl + C** in the terminal to stop it.")
    s += h1("1. Introduction to Streamlit")
    s.append(p("**Streamlit** is a free Python library for building web apps quickly — without HTML, CSS or JavaScript. "
               "It is easy (only Python), fast (an app in minutes), interactive (buttons, sliders, charts) and widely "
               "used for data-science and AI demos."))
    s += code("pip install streamlit", "Terminal")
    s += code('import streamlit as st\n\nst.title("My First Streamlit App")\nst.write("Hello! Welcome to Streamlit.")', "app.py — your first app")
    s += code("streamlit run app.py", "Run it")
    s += h1("2. Streamlit components")
    s += table(["Group", "Components", "What they do"], [
        ["Text", "`st.title` · `st.header` · `st.subheader` · `st.write` · `st.markdown`", "Show headings and text"],
        ["Input", "`st.text_input` · `st.number_input`", "Get typed values from the user"],
        ["Widgets", "`st.button` · `st.slider` · `st.selectbox` · `st.checkbox`", "Let the user click, slide, choose or tick"],
        ["Messages", "`st.success` · `st.info` · `st.warning` · `st.error`", "Coloured feedback boxes"],
    ], [0.15, 0.5, 0.35])
    s += code('city = st.selectbox("Choose your city", ["Chennai", "Delhi", "Mumbai"])\n'
              'st.write("You selected:", city)\n\n'
              'agree = st.checkbox("I agree to the terms")\nif agree:\n    st.write("Thank you for agreeing!")',
              "Widgets return the user's value")
    s += h1("3. Build a simple app — BMI Calculator")
    s += flow(["Title", "Weight (kg)", "Height (m)", "Calculate button", "BMI + message"])
    s += code('''import streamlit as st

st.title("BMI Calculator")
st.write("Enter your details to calculate your BMI.")

weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (meters):", min_value=0.1)

if st.button("Calculate BMI"):
    bmi = weight / (height * height)
    st.write("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.warning("You are underweight.")
    elif bmi < 25:
        st.success("You have a normal weight.")
    else:
        st.error("You are overweight.")''', "app.py")
    s += bullets(["`st.number_input()` asks for numbers; `min_value` blocks zero and negative input.",
                  "The code under `st.button(...)` runs only when the button is clicked.",
                  "`if / elif / else` picks a different coloured message for each BMI range."])
    s += h1("Run the apps")
    s += code('cd "Phase-004-FastAPI-And-Streamlit\\Streamlit\\Streamlit Resources"\n'
              'pip install streamlit\n\nstreamlit run app.py          # BMI Calculator\n'
              'streamlit run test.py         # widget tour\nstreamlit run calculator.py   # styled calculator',
              "PowerShell")
    s += h1("Key takeaways")
    s += bullets(["A real app combines **text + inputs + button + logic**.",
                  "Widgets return values you can store in variables.",
                  "Always run apps with `streamlit run <file>.py`.",
                  "Practise with small apps — a calculator, a greeting app — before larger builds."])
    return dict(out=REPO / P4 / "Streamlit" / "Streamlit Resources" / "Streamlit-Resources-Explainer.pdf", folder=P4,
                title="Streamlit Resources", short="Streamlit Resources",
                subtitle="Notebooks and working apps — from a first Streamlit page to a complete BMI calculator",
                facts=[("Document", "Folder explainer"), ("Level", "Beginner"),
                       ("Contents", "3 notebooks · app.py · test.py · calculator.py"),
                       ("Tools", "Python · Streamlit"), ("Folder", f"{P4}/Streamlit/Streamlit Resources")],
                story=s, keywords="Streamlit, widgets, BMI calculator")


# ============================================================================ Phase-006 overview
def doc_phase006():
    s = []
    s += h1("The parts every LLM application is built from")
    s.append(lead("LangChain gives each step of an AI application a standard component, so you can load, split, "
                  "embed, store, search and answer with a few lines of Python."))
    s.append(p("Phase-005-LLM-Foundations-and-Practical-Tools explained what a model is and how to run one. "
               "Phase-006-LangChain-Ecosystem puts a framework around the model: nine beginner-friendly notebooks "
               "in two tracks, written to be run from top to bottom, plus a third track — the AI Learning Assistant — that "
               "shows LangChain (build), LangGraph (orchestrate) and LangSmith (observe) working together behind a FastAPI service."))
    s += table(["Track", "Folder", "Notebooks"], [
        ["**LangChain Components**", "`Langchain-Components/`", "7 — the building blocks of a retrieval (RAG) app"],
        ["**Advanced Model Integration**", "`Langchain_Advanced_Model_Integration/`", "2 — connecting to OpenAI, Ollama, Claude and Gemini; messages"],
        ["**LangChain vs LangGraph vs LangSmith**", "`LangChain vs LangGraph vs LangSmith Explained/`", "AI Learning Assistant — LangChain chains, a LangGraph workflow, optional LangSmith tracing, FastAPI; mock, OpenAI or Ollama"],
    ], [0.3, 0.4, 0.3])
    s += h1("The LangChain ecosystem")
    s += table(["Layer", "Package / product", "Role"], [
        ["Protocol", "`langchain-core`", "Base interfaces and **LCEL** — the `|` operator that joins components into a chain"],
        ["Integrations", "`langchain-community`, `langchain-openai`, `langchain-huggingface`", "Loaders, vector stores, embedding models and chat models"],
        ["Application", "`langchain`", "Ready-made chains and agents built on the core"],
        ["Observability", "**LangSmith**", "Traces every call — inputs, outputs, latency and tokens"],
    ], [0.18, 0.4, 0.42])
    s.append(small("Three external reference diagrams of the ecosystem are kept in the folder for study; credit belongs to their original creators."))
    s += h1("How the components connect")
    s += flow(["01 Load", "02 Split", "03 Embed", "04 Store", "05 Retrieve", "06 Chain"])
    s.append(p("A **loader** reads your data into Documents; the **splitter** cuts them into chunks; an **embedding "
               "model** turns each chunk into a vector; the **vector store** saves the vectors; the **retriever** "
               "fetches the chunks closest in meaning to a question; and a **chain** sends the question plus those "
               "chunks to a model. **07 LangSmith** records each run so it can be inspected."))
    s += callout("A worked scenario (hypothetical)",
                 "An online retailer wants an assistant that answers customer questions from its own product "
                 "manuals. Load the manuals → split them into chunks → embed and store the chunks → retrieve the "
                 "best matches for each question → let the model answer from those matches. Phase-007-RAG-Introduction "
                 "turns this flow into running code.", "tip")
    s += h1("Track 1 — LangChain Components")
    s += table(["#", "Notebook", "What you learn"], [
        ["01", "Data Ingestion", "`TextLoader` turns a file into Documents; other loaders: `PyPDFLoader`, `CSVLoader`, `WebBaseLoader`"],
        ["02", "Text Splitter", "`RecursiveCharacterTextSplitter`; `chunk_size` and `chunk_overlap`"],
        ["03", "Embeddings", "Free local `all-MiniLM-L6-v2` or OpenAI `text-embedding-3-small`; cosine similarity"],
        ["04", "Vector Store", "FAISS — `from_texts`, `similarity_search`, `save_local` / `load_local`"],
        ["05", "Retriever", "`.as_retriever(search_kwargs={\"k\": 2})` and `retriever.invoke(question)`"],
        ["06", "Chains", "Prompt → Model → Output parser joined with `|`; `.invoke({...})`"],
        ["07", "LangSmith", "Tracing via 4 environment variables, `@traceable`, `wrap_openai`"],
    ], [0.06, 0.2, 0.74])
    s += h1("Track 2 — Advanced Model Integration")
    s += table(["#", "Notebook", "What you learn"], [
        ["01", "Model Integration", "`ChatOpenAI`, `invoke()`, `temperature`, streaming; swapping to Ollama, Claude or Gemini"],
        ["02", "Messages", "`SystemMessage`, `HumanMessage`, `AIMessage`; the message list is the memory"],
    ], [0.06, 0.24, 0.7])
    s += h1("Running the notebooks")
    s += code('cd "Phase-006-LangChain-Ecosystem\\Langchain-Components"\npython -m venv venv\n'
              'venv\\Scripts\\Activate.ps1\npython -m pip install -r requirements.txt\n'
              'copy .env.example .env      # then paste your own keys into .env', "PowerShell")
    s += callout("Keys stay local",
                 "Real keys go in a local `.env` file, which is git-ignored. Notebooks 01, 02, 04 and 05 need no "
                 "API key — they use the free Hugging Face embedding model (downloaded once on first run).")
    s += h1("Key takeaways")
    s += bullets(["LangChain does not replace the model — it standardises everything around it.",
                  "A retrieval app is six swappable steps: load → split → embed → store → retrieve → answer.",
                  "Changing provider is usually a one-line change of the chat-model class.",
                  "Tracing with LangSmith makes each step visible, so problems are debugged instead of guessed.",
                  "Next: Phase-007-RAG-Introduction."])
    return dict(out=REPO / P6 / "LangChain-Ecosystem-Explainer.pdf", folder=P6, title="LangChain Ecosystem",
                short="LangChain Ecosystem", subtitle="LangChain building blocks and model integration — the parts every LLM application is built from",
                facts=[("Document", "Phase explainer"), ("Level", "Beginner"),
                       ("Tools", "Python · LangChain · FAISS · Hugging Face · OpenAI · LangSmith"),
                       ("Contents", "9 notebooks in 2 tracks"), ("Folder", P6)],
                story=s, keywords="LangChain, RAG, embeddings, FAISS, LangSmith")


# ============================================================================ Langchain-Components
def doc_components():
    s = []
    s += h1("Seven building blocks of a RAG app")
    s += flow(["Load", "Split", "Embed", "Store", "Retrieve", "Chain", "Trace"])
    s.append(p("Each notebook covers one block. Notebooks 01–05 run without an API key; 06 and 07 call OpenAI."))
    s += h1("01 · Data Ingestion — Document Loaders")
    s.append(p("Data ingestion means **bringing your data into the program**. A model does not know your notes, PDFs "
               "or company files — so the first step of RAG is to load them."))
    s += code('from langchain_community.document_loaders import TextLoader\n\nloader = TextLoader("sample.txt")\n'
              'documents = loader.load()\nprint(documents[0].page_content)', "TextLoader")
    s += table(["Loader", "Loads from"], [["`TextLoader`", "A `.txt` file"], ["`PyPDFLoader`", "A PDF (needs `pypdf`)"],
                                          ["`CSVLoader`", "A CSV file"], ["`WebBaseLoader`", "A website URL"]], [0.35, 0.65])
    s += h1("02 · Text Splitter")
    s.append(p("Models read a limited amount of text at a time, and smaller chunks give more accurate search. "
               "`chunk_size` sets the size of each chunk (characters); `chunk_overlap` repeats a little text between "
               "chunks so meaning is not lost at the edges."))
    s += code('from langchain_text_splitters import RecursiveCharacterTextSplitter\n\n'
              'splitter = RecursiveCharacterTextSplitter(chunk_size=80, chunk_overlap=10)\n'
              'chunks = splitter.split_text(long_text)          # plain text\n'
              'chunks = splitter.split_documents(documents)     # loaded Documents', "Splitting")
    s.append(small("In the notebook, a 261-character text becomes 4 chunks with these settings."))
    s += h1("03 · Embeddings")
    s.append(p("Embeddings turn text into a **vector** — a list of numbers. Similar meanings get similar numbers, "
               "so the computer can compare meaning with maths (cosine similarity: closer to 1 = more similar)."))
    s += table(["", "Free / local", "OpenAI (paid)"], [
        ["Model", "Hugging Face `all-MiniLM-L6-v2`", "`text-embedding-3-small`"],
        ["Create", "`HuggingFaceEmbeddings(model_name=\"all-MiniLM-L6-v2\")`", "`OpenAIEmbeddings(model=\"text-embedding-3-small\")`"],
        ["Use", "`.embed_query(text)`", "`.embed_query(text)`"],
        ["API key", "No", "Yes — `OPENAI_API_KEY`"],
    ], [0.14, 0.43, 0.43])
    s += callout("Only one line changes", "Swap the import and the create line; everything after that stays the same.", "tip")
    s += h1("04 · Vector Store — FAISS")
    s.append(p("A vector store is a database for embeddings that searches by **meaning**, not exact words — a search "
               "for \"car\" can also find \"vehicle\"."))
    s += code('from langchain_community.vectorstores import FAISS\n\n'
              'vector_store = FAISS.from_texts(texts, embeddings)\n'
              'results = vector_store.similarity_search("Tell me about pets", k=2)\n\n'
              'vector_store.save_local("my_store")\n'
              'vector_store = FAISS.load_local("my_store", embeddings, allow_dangerous_deserialization=True)',
              "Store, search, save, load")
    s.append(small("Notebook result for \"Tell me about pets\": \"Dogs are friendly animals.\" and \"Cats like to sleep a lot.\" "
                   "The saved index is the `my_store/` folder."))
    s += h1("05 · Retriever")
    s.append(p("The vector store is the shelf; the **retriever** is the helper who brings back the right books for your "
               "question. It is the bridge between your data and the model."))
    s += code('retriever = vector_store.as_retriever(search_kwargs={"k": 2})\n'
              'results = retriever.invoke("What is used to build web apps?")', "Retriever")
    s += h1("06 · Chains")
    s.append(p("A chain joins steps so the output of one becomes the input of the next — like boiling water, adding "
               "tea, adding milk, pouring. The most common chain is **Prompt → Model → Output parser**, joined with `|`."))
    s += code('from langchain_openai import ChatOpenAI\nfrom langchain_core.prompts import ChatPromptTemplate\n'
              'from langchain_core.output_parsers import StrOutputParser\n\n'
              'prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")\n'
              'model = ChatOpenAI(model="gpt-4o-mini")\nchain = prompt | model | StrOutputParser()\n\n'
              'print(chain.invoke({"topic": "Python"}))', "Prompt | Model | Parser")
    s += h1("07 · LangSmith — tracing")
    s.append(p("LangSmith records every run — the input, the prompt, the reply, the time taken and the tokens used. "
               "Think of it as CCTV for your AI app: you can replay each step to see why an answer looks wrong."))
    s += table(["Variable", "Purpose"], [["`LANGSMITH_TRACING`", "`\"true\"` switches tracing on"],
                                         ["`LANGSMITH_API_KEY`", "Your LangSmith key"],
                                         ["`LANGSMITH_PROJECT`", "Groups runs under a project name"],
                                         ["`OPENAI_API_KEY`", "The model provider key"]], [0.35, 0.65])
    s += bullets(["LangChain chains are traced **automatically** once the variables are set.",
                  "`@traceable` traces your own Python functions.",
                  "`wrap_openai(OpenAI())` traces direct OpenAI client calls.",
                  "View runs at `https://smith.langchain.com`."])
    s += h1("Key takeaways")
    s += bullets(["Load → split → embed → store → retrieve is the retrieval half of every RAG app.",
                  "The embedding model can be free and local or paid — the rest of the code is unchanged.",
                  "Chains turn separate steps into one reusable pipeline; LangSmith shows what happened inside it."])
    return dict(out=REPO / P6 / "Langchain-Components" / "LangChain-Components-Explainer.pdf", folder=P6,
                title="LangChain Components", short="LangChain Components",
                subtitle="Loaders, splitters, embeddings, vector stores, retrievers, chains and LangSmith — one notebook each",
                facts=[("Document", "Sub-project explainer"), ("Level", "Beginner"),
                       ("Notebooks", "01 Data Ingestion → 07 LangSmith"),
                       ("Tools", "LangChain · Hugging Face · FAISS · OpenAI · LangSmith"),
                       ("Folder", f"{P6}/Langchain-Components")],
                story=s, keywords="LangChain, loaders, embeddings, FAISS, retriever, chains, LangSmith")


# ============================================================================ Advanced Model Integration
def doc_model_integration():
    s = []
    s += h1("01 · Model Integration")
    s.append(lead("Model integration means connecting LangChain to an AI model so you can send messages and get replies."))
    s += code('from langchain_openai import ChatOpenAI\nfrom dotenv import load_dotenv\n\nload_dotenv()\n'
              'llm = ChatOpenAI(model="gpt-4o-mini")\n\nresponse = llm.invoke("What is Python in one sentence?")\n'
              'print(response.content)', "Create the model and invoke it")
    s += table(["Setting", "Meaning"], [["`model`", "Which model to use, for example `gpt-4o-mini` or `gpt-4o`"],
                                        ["`temperature`", "0 = focused and predictable · 1 = more creative"]], [0.25, 0.75])
    s += code('for chunk in llm.stream("Count from 1 to 5 slowly."):\n    print(chunk.content, end="", flush=True)',
              "Streaming the reply word by word")
    s += h2("Swap providers by changing one line")
    s += table(["Provider", "Install", "Create the model", "Key"], [
        ["**OpenAI**", "`langchain-openai`", "`ChatOpenAI(model=\"gpt-4o-mini\")`", "`OPENAI_API_KEY`"],
        ["**Ollama**", "`langchain-ollama`", "`ChatOllama(model=\"llama3\")`", "None — runs locally"],
        ["**Claude**", "`langchain-anthropic`", "`ChatAnthropic(model=\"claude-opus-4-8\")`", "`ANTHROPIC_API_KEY`"],
        ["**Gemini**", "`langchain-google-genai`", "`ChatGoogleGenerativeAI(model=\"gemini-2.0-flash\")`", "`GOOGLE_API_KEY`"],
    ], [0.13, 0.22, 0.42, 0.23])
    s.append(small("Model names are as written in the notebook; providers update their model lists regularly, so check the current names before running."))
    s += callout("Everything after that line is the same",
                 "`invoke()`, `stream()`, messages and tools work identically for every provider. Ollama needs the app "
                 "from ollama.com and `ollama pull llama3`.", "tip")
    s += h1("02 · Messages")
    s.append(p("Every chat is a **list of messages**, and each message has a role."))
    s += table(["Message", "Who", "Used for"], [["`SystemMessage`", "You (setup)", "Instructions for how the AI should behave — the director's notes"],
                                                ["`HumanMessage`", "The user", "What the person says"],
                                                ["`AIMessage`", "The AI", "The model's reply (text in `.content`)"]], [0.22, 0.18, 0.6])
    s += code('from langchain_core.messages import SystemMessage, HumanMessage\n\nmessages = [\n'
              '    SystemMessage(content="You are a friendly teacher. Keep answers very short."),\n'
              '    HumanMessage(content="What is a variable in Python?"),\n]\nresponse = llm.invoke(messages)   # an AIMessage',
              "Send a list of messages")
    s += h2("Holding a conversation")
    s.append(p("The model has no memory of its own. To continue a chat, append each reply and each new question to "
               "the list and send the whole list again — **the message list is the memory**."))
    s += code('messages = [SystemMessage(content="You are a helpful assistant."),\n'
              '            HumanMessage(content="My name is Anjali.")]\nreply = llm.invoke(messages)\n\n'
              'messages.append(reply)\nmessages.append(HumanMessage(content="What is my name?"))\n'
              'reply = llm.invoke(messages)     # the model now answers from the history',
              "Conversation memory")
    s += h1("Run it")
    s += code('cd "Phase-006-LangChain-Ecosystem\\Langchain_Advanced_Model_Integration"\npython -m venv venv\n'
              'venv\\Scripts\\Activate.ps1\npython -m pip install -r requirements.txt\n'
              'copy .env.example .env      # paste OPENAI_API_KEY (and others if used)', "PowerShell")
    s += h1("Key takeaways")
    s += bullets(["Only the model-creation line changes between providers.",
                  "`invoke()` returns a message; read its text with `.content`.",
                  "System, human and AI messages give the conversation structure; resend the list to keep context."])
    return dict(out=REPO / P6 / "Langchain_Advanced_Model_Integration" / "LangChain-Advanced-Model-Integration-Explainer.pdf",
                folder=P6, title="Advanced Model Integration", short="Advanced Model Integration",
                subtitle="Connecting LangChain to OpenAI, Ollama, Claude and Gemini — and talking to them with messages",
                facts=[("Document", "Sub-project explainer"), ("Level", "Beginner"),
                       ("Notebooks", "01 Model Integration · 02 Messages"),
                       ("Tools", "LangChain · OpenAI · Ollama · Anthropic · Google Gemini"),
                       ("Folder", f"{P6}/Langchain_Advanced_Model_Integration")],
                story=s, keywords="LangChain, ChatOpenAI, Ollama, Claude, Gemini, messages")


# ============================================================================ Phase-007
def doc_phase007():
    s = []
    s += h1("What RAG is and why it is used")
    s.append(lead("Retrieval-Augmented Generation: find the right text first, then let the model answer from it."))
    s += table(["Word", "Meaning"], [["**Retrieval**", "Find the right data"], ["**Augmented**", "Add that data to the question"],
                                     ["**Generation**", "The model writes the answer"]], [0.25, 0.75])
    s.append(p("A plain model has two problems: it **does not know your private data**, and it can **hallucinate** — "
               "give answers that sound right but are wrong. RAG fixes both by giving the model real, relevant text "
               "before it answers. It is the difference between a closed-book and an open-book exam."))
    s += bullets(["Accurate answers grounded in real data.", "Works with your own PDFs, notes and documents.",
                  "Stays current — update the data instead of retraining the model.", "Fewer made-up answers, at lower cost than retraining."])
    s += h1("How RAG works")
    s += flow(["1 Load", "2 Split", "3 Embed", "4 Store (FAISS)", "5 Retrieve top-k", "6 Answer"])
    s.append(p("Steps 1–4 index the document once. For every question, step 5 retrieves the closest chunks and step 6 "
               "places them in the prompt so the model answers **using only that text**."))
    s += callout("Worked scenario (hypothetical)",
                 "An online retailer's assistant receives \"Can I wash this jacket?\". RAG retrieves the care-label "
                 "section of that product's manual and the model answers from it — instead of guessing. This is an "
                 "illustration, not a real deployment.", "tip")
    s += h1("RAG types")
    s += table(["Type", "Main idea", "Remember it as"], [
        ["**Basic (naive) RAG**", "Retrieve → Augment → Generate", "The starting point"],
        ["**Self RAG**", "The model decides whether to retrieve, grades document relevance and checks its answer is supported", "\"Let me double-check my own answer.\""],
        ["**Corrective RAG (CRAG)**", "A grader labels retrieved data correct, ambiguous or incorrect; weak data triggers a new search (for example, the web)", "\"This info is bad, let me search again.\""],
        ["**Fusion RAG**", "Ask the question several ways, search with each, merge rankings with Reciprocal Rank Fusion", "\"Let me ask in many ways.\""],
        ["**BM25 + Rerank**", "Keyword search, then a reranker re-orders results so the best is first", "\"Find by keywords, sort the best on top.\""],
    ], [0.22, 0.5, 0.28])
    s += h2("Self RAG vs Corrective RAG")
    s.append(p("Both add a check. **Self RAG** checks its own answer and reasoning; **Corrective RAG** checks the "
               "retrieved data and re-searches when it is weak."))
    s += h2("Reciprocal Rank Fusion in one function")
    s += code('''def reciprocal_rank_fusion(searches, k=60):
    scores = {}
    for result_list in searches:
        for rank, doc in enumerate(result_list):
            scores[doc] = scores.get(doc, 0) + 1 / (rank + 1 + k)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)''', "05_Fusion_RAG.ipynb")
    s.append(small("Documents found near the top of many searches get the highest combined score."))
    s += h2("BM25 vs embeddings")
    s += table(["", "BM25 (keyword)", "Embeddings (semantic)"], [
        ["Matches", "Exact words", "Meaning"], ["Good for", "Names, codes, exact terms", "Similar ideas, synonyms"],
        ["Example", "Finds \"iPhone 15\" exactly", "Knows \"phone\" ≈ \"mobile\""]], [0.2, 0.4, 0.4])
    s.append(p("Using both is **hybrid search**. A common pattern: search fast for the top 20, then **rerank** carefully to keep the best 3."))
    s += h1("The three runnable demos")
    s += table(["File", "What it does"], [
        ["`rag_demo.py`", "The six RAG steps over `llm_document.txt` with a local Hugging Face embedding model and FAISS. With `OPENAI_API_KEY` set it asks `gpt-4o-mini`; without a key it prints the retrieved text."],
        ["`rag_demo_langsmith.py`", "The same demo with one extra line — `wrap_openai(OpenAI())` — so the call is traced in LangSmith."],
        ["`rag_faiss_app.py`", "An interactive Q&A loop over `spotify_web_app_architecture.pdf`. Builds a FAISS index on first run, saves it to `faiss_index/`, and answers only from the document — otherwise \"I don't know from the provided document.\""],
    ], [0.27, 0.73])
    s += code('cd "Phase-007-RAG-Introduction"\npython -m venv venv\nvenv\\Scripts\\Activate.ps1\n'
              'python -m pip install -r requirements.txt\ncopy .env.example .env\n\n'
              'python rag_demo.py\npython rag_demo_langsmith.py\npython rag_faiss_app.py     # type exit to stop',
              "PowerShell")
    s += callout("Data files",
                 "`llm_document.txt` is a beginner's guide to LLMs used as the knowledge source. "
                 "`spotify_web_app_architecture.pdf` is a sample architecture document for a hypothetical "
                 "Spotify-like app, used only as RAG input.")
    s += h1("Key takeaways")
    s += bullets(["RAG keeps the model the same and changes what it reads before answering.",
                  "Retrieval quality decides answer quality — chunking, embeddings and top-k all matter.",
                  "Advanced types add checks (Self RAG, CRAG) or better search (Fusion RAG, BM25 + rerank).",
                  "\"Answer only from the context\" plus an honest \"I don't know\" is the simplest guard against made-up answers."])
    return dict(out=REPO / P7 / "RAG-Introduction-Explainer.pdf", folder=P7, title="RAG Introduction", short="RAG Introduction",
                subtitle="Retrieval-Augmented Generation — concepts, RAG types and three working demos",
                facts=[("Document", "Phase explainer"), ("Level", "Beginner to intermediate"),
                       ("Contents", "6 notebooks · 3 Python demos"),
                       ("Tools", "LangChain · Hugging Face · FAISS · rank-bm25 · OpenAI · LangSmith"),
                       ("Folder", P7)],
                story=s, keywords="RAG, retrieval, FAISS, Self RAG, CRAG, Fusion RAG, BM25")


# ============================================================================ Brand guidelines
def doc_brand():
    s = []
    s += h1("The brand in one line")
    s.append(lead("Shasu Vathanan - GEN AI - Product Manager — exactly this string, everywhere."))
    s += table(["Element", "Value"], [
        ["Brand display name", "**Shasu Vathanan - GEN AI - Product Manager**"],
        ["Website", "`SHASUVATHANAN.COM` → `https://shasuvathanan.com`"],
        ["LinkedIn", "`https://www.linkedin.com/in/shasuvathanan`"],
        ["GitHub", "`https://github.com/shasu1pm/Genai-Architect-Journey`"],
        ["AI avatar", "**NeGot** — a supporting guide, never a replacement for the author's identity"],
    ], [0.28, 0.72])
    s += h1("Official links and social profiles")
    from social import LINKS
    s += table(["Platform", "Link", "Logo in Social-Media-Logos/PNG"],
               [[l["label"], f"`{l['url'].replace('mailto:', '')}`", f"`{l['logo']}`" if l["logo"] else "— (text link)"]
                for l in LINKS], [0.2, 0.5, 0.3])
    from social import logo_path
    icons = [l for l in LINKS if logo_path(l)]
    grid = Table([[_asset_image(logo_path(l), 26) for l in icons],
                  [Paragraph(f"<font size=7.5>{l['label']}</font>", S["cell"]) for l in icons]],
                 colWidths=[(W - LM - RM) / len(icons)] * len(icons))
    grid.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    s += [grid, Spacer(1, 4)]
    s.append(small("Every README footer, notebook footer, PDF cover, the closing slide and the web page footer carry this Connect row; the list lives in pdf-kit/social.py and the files in Social-Media-Logos/ (see its README)."))
    s += h1("Brand assets in zz-Brand-Assets/")
    logo = _asset_image(LOGO, 62)
    negot = _asset_image(NEGOT, 70)
    name = _asset_image(NAME, 230)
    strip = _asset_image(STRIP, 300)
    t = Table([[logo, p("**Dragon-Motivation-Logo.png** — personal emblem (1019 × 1510). Covers, page headers, README headers.")],
               [negot, p("**NeGot-My-AI-Avatar.png** — NeGot, my AI avatar (1254 × 1254). Footers and friendly accents; never recoloured.")],
               [name, p("**SHASUVATHANAN-NAME.png** — name lockup (1863 × 199). Covers, root README, title slides.")],
               [strip, p("**ShasuVathanan-GEN AI-Product-Manager.png** — brand strip (2323 × 63). Every header.")]],
              colWidths=[310, 193])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))
    s += [t, Spacer(1, 6)]
    s += h2("Hero banner — SHASUVATHANAN-THE-ONE-NAME.png")
    s.append(_asset_image(ASSETS / "SHASUVATHANAN-THE-ONE-NAME.png", W - LM - RM))
    s.append(small("1280 × 320 · root README only, full width directly above the main title, linked to the website."))
    s += callout("Use the files as they are",
                 "Reference the originals in `zz-Brand-Assets/`. Do not copy them into phase folders, create renamed or "
                 "resized copies in the repository, redraw, recolour or crop them. PDF tools may downscale in memory "
                 "while embedding; the source files stay untouched.")
    s += h1("Colour")
    s += table(["Token", "Hex", "Use"], [["Coral Red", "`#FF4A62`", "Rules, highlights, gradient start"],
                                         ["Coral Red 2", "`#FF5A45`", "Gradient end (`#FF4A62 → #FF5A45`)"],
                                         ["Deep Blue", "`#031273`", "Headings, tables, body emphasis, footers"],
                                         ["Soft Blue tint", "`#F2F4FF`", "Callouts and table stripes"],
                                         ["Black", "—", "**Never** as a design colour"]], [0.25, 0.2, 0.55])
    s.append(p("The artwork is red on transparency — always place it on white or a light tint, never on a coral fill."))
    s += h1("Where the assets appear")
    s += table(["Artifact", "Brand use"], [
        ["README / Markdown", "Logo + brand strip header with website and LinkedIn; footer with the Connect row (eight logos and links) and NeGot. Root README also shows the hero banner"],
        ["Jupyter notebooks", "First cell: logo, brand line, badges, coral rule, kicker. Last cell: NeGot, Created and Maintained by, Connect row"],
        ["PDF", "Cover: logo, name lockup, brand strip, coral hero, facts, NeGot brand block, CONNECT row. Every page: header (logo, lockups, exact folder name, website) and footer (NeGot, brand line, links, PAGE n / N). ≤ 15 pages. One Explainer PDF per folder"],
        ["PowerPoint", "Title slide with the lockups and NeGot on a white badge; closing slide with NeGot and a white Connect panel of linked logos; author property = brand"],
        ["Word / Excel", "Title page or first sheet with the lockups and brand line; author property = brand"],
        ["Website and HTML pages", "Logo as favicon, lockups in the header, NeGot and the Connect row in the footer, branded title and author meta"],
    ], [0.27, 0.73])
    s += h1("Making a new branded PDF")
    s += code('import sys; sys.path.insert(0, "zz-Brand-Assets/pdf-kit")\nfrom brand_pdf import build, h1, p, bullets, table, code, callout, flow\n\n'
              'build("Phase-008-Example/Example.pdf",\n      folder="Phase-008-Example", title="Example",\n'
              '      subtitle="One-line purpose", facts=[("Document", "Phase explainer"), ("Folder", "Phase-008-Example")],\n'
              '      story=[h1("What it is"), p("..."), bullets(["...", "..."])])', "zz-Brand-Assets/pdf-kit")
    s.append(p("New folders use a short Markdown source in `pdf-kit/explainers/` and `build_explainers.py`. Existing PDFs keep their pages: `rebrand_existing.py` replaced only their header and footer bands and `apply_covers.py` gives them the brand cover. The full run order of all tools is in `pdf-kit/README.md`."))
    return dict(out=REPO / "zz-Brand-Assets" / "Brand-Guidelines.pdf", folder="zz-Brand-Assets", title="Brand Guidelines",
                short="Brand Guidelines", subtitle="How the brand assets, the official links, the palette and the exact brand name are used across the repository",
                facts=[("Document", "Brand guide"), ("Assets", "Logo · Name lockup · Brand strip · NeGot · Hero banner"),
                       ("Official links", "8 — Website, Email, LinkedIn, GitHub, Hugging Face, YouTube, X, Higgsfield AI"),
                       ("Palette", "#FF4A62 → #FF5A45 · #031273 · #F2F4FF · no black"),
                       ("Folder", "zz-Brand-Assets")],
                story=s, kicker="Shasu Vathanan  ·  Personal brand", keywords="brand, NeGot, palette, logo")


DOCS = [doc_phase004, doc_streamlit_resources, doc_phase006, doc_components, doc_model_integration, doc_phase007, doc_brand]

if __name__ == "__main__":
    import fitz
    only = sys.argv[1:]
    for fn in DOCS:
        if only and not any(o in fn.__name__ for o in only):
            continue
        spec = fn()
        out = spec.pop("out")
        keywords = spec.pop("keywords", "")
        build(out, keywords=keywords, **spec)
        n = fitz.open(out).page_count
        flag = "" if n <= 10 else ("  (over target 10)" if n <= 15 else "  ** OVER 15 **")
        print(f"{n:3d}p  {out.relative_to(REPO)}{flag}")
