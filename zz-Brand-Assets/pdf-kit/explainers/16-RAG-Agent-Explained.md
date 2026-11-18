---
out: Phase-008-RAG-Agent-Explained/RAG-Agent-Explained-Explainer.pdf
folder: Phase-008-RAG-Agent-Explained
title: RAG Agent Explained
subtitle: Turn RAG into a tool, serve it through MCP, and let a CrewAI agent use it — a shopping assistant for a sample online store
short: RAG Agent Explained
fact: Document | Phase explainer
fact: Level | Intermediate
fact: Pattern | AI agent + RAG + MCP
fact: Stack | CrewAI · MCP · ChromaDB · OpenAI · Streamlit · FastAPI
fact: Contents | 5 Python files · product catalogue PDF · cart workbook
fact: Folder | Phase-008-RAG-Agent-Explained
keywords: RAG agent, MCP, CrewAI, ChromaDB, tool calling, Streamlit, FastAPI, e-commerce
---
# What this phase is
lead: A plain RAG app only answers questions. An agent can also act. This phase joins the two.
Phase-007-RAG-Introduction built RAG as a standalone question-answering app. Here the same idea becomes **one tool among several**. The product search (RAG) and four cart actions are published by an **MCP server**, and a **CrewAI shopping agent** decides which tool to call for each customer message. A Streamlit chat UI and a FastAPI service put the agent in front of people and other applications.

# Why it matters
- **RAG alone is not enough for real workflows.** Customers do not only ask "what do you sell?" — they also say "add two of those to my cart". Answering and acting need different tools.
- **RAG as a tool** lets the agent choose: search the catalogue for facts, call a cart tool for actions.
- **MCP (Model Context Protocol)** gives every tool one standard interface. The agent loads whatever the server offers, so new capabilities — an email notifier, a database, a booking calendar — can be added as further MCP tools without rewriting the agent.
- **An API** makes the agent reusable: a website, an online shop or another service can call it over HTTP.

# The RAG workflow, in one line
flow: Documents (PDF) > Split into chunks > Embed as vectors > Store in vector DB > Embed the question > Retrieve closest chunks > LLM answers
Text becomes numbers (embeddings); the question is embedded the same way, the closest chunks are found in the vector database, and only those chunks reach the model. Phase-006 and Phase-007 built this with LangChain; this phase builds it directly with **pypdf** and **ChromaDB** in one short file (`rag.py`).

# The agent architecture
flow: Customer message > CrewAI agent (gpt-4o-mini) > MCP server (stdio) > search_products (RAG) or cart tools > Reply + updated cart
The agent never touches ChromaDB or the cart file directly. It only sees tool **names and descriptions** from the MCP server, and its backstory tells it when to use each one.
| Layer | File | Role |
| :-- | :-- | :-- |
| Knowledge | `products_catalog.pdf` | 12 sample products of ShopEasy, a hypothetical online store |
| RAG | `rag.py` | Reads the PDF, one chunk per product, OpenAI `text-embedding-3-small` embeddings, ChromaDB on disk |
| Tools | `mcp_server.py` | FastMCP server named `product-shop` with five tools |
| Agent | `agent.py` | CrewAI `Agent` + `Task` + `Crew`, tools loaded through `MCPServerAdapter` |
| UI | `app.py` | Streamlit chat with the cart in the sidebar — for demos |
| API | `api.py` | FastAPI: `POST /ask`, `GET /cart`, Swagger UI at `/docs` |
| Data | `cart.xlsx` | Empty cart template the tools fill — stands in for a real database |

# The five MCP tools
| Tool | What it does | Uses RAG? |
| :-- | :-- | :-- |
| `search_products(question)` | Queries ChromaDB and returns the 3 closest product chunks | Yes |
| `add_to_cart(product_name, price, quantity)` | Adds a product, or raises its quantity if already in the cart | No |
| `remove_from_cart(product_name)` | Removes one product by name | No |
| `view_cart()` | Lists the cart and the grand total | No |
| `clear_cart()` | Empties the cart | No |
> [!TIP] Grounding rules live in the agent's backstory
> Always use `search_products` for questions about products, prices or features, answer only from what it returns, never make up products or prices, and look up the exact name and price before adding to the cart. These rules are what keep the agent honest.

# How one conversation flows
- **"What wireless products are available?"** — the agent calls `search_products`; ChromaDB returns the three closest catalogue chunks (for example the Wireless Mouse, Rs. 499, and the Bluetooth Headphones, Rs. 2999); the agent answers from them.
- **"Add the wireless mouse to my cart."** — no RAG is needed. The agent calls `add_to_cart` with the exact name and price it found, the tool writes `cart.xlsx`, and the Streamlit sidebar shows the cart and its total.
- **Memory:** `app.py` sends the last six chat messages as `history` with every question, so follow-ups like "add it" make sense. `POST /ask` accepts the same `history` field.
_note: Exact wording of answers varies between runs because the reply is written by the model. cart.xlsx ships as an empty template; add_to_cart calculates each total as price × quantity.

# Run it
```powershell Setup and the two front ends
cd "Phase-008-RAG-Agent-Explained"
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
copy .env.example .env          # then add your own OPENAI_API_KEY

python agent.py                 # one-question smoke test in the terminal
streamlit run app.py            # chat UI at http://localhost:8501
uvicorn api:app --reload        # API at http://127.0.0.1:8000  ·  try it at /docs
```
> [!NOTE] First run and keys
> The first import of `rag.py` embeds the catalogue and creates `chroma_db/` (git-ignored). Delete that folder whenever `products_catalog.pdf` changes so the index is rebuilt. Both embeddings and the agent call OpenAI, so `OPENAI_API_KEY` is required.

# From demo to production
| In this demo | In a real shop |
| :-- | :-- |
| `cart.xlsx` on disk | A real database connected through its own MCP tool or credentials |
| Streamlit chat UI | Streamlit is for demos; production front ends call the FastAPI service |
| Price passed to `add_to_cart` by the agent | Recommended: look the price up again on the server before saving |
| Open API on localhost | Recommended: authentication, rate limits and one cart per customer |
| CrewAI | Other agent frameworks such as AutoGen or Google's agent SDK can follow the same pattern |

# Key takeaways
- **RAG becomes a tool**, so the agent can decide when to search and when to act.
- **MCP** is the connector: one server, many tools, and new tools without changing the agent.
- **Grounding rules** in the backstory, plus tools that return real data, prevent invented products and prices.
- **API first:** the same crew powers the chat UI and the HTTP service.
- Next: replace the Excel cart with a database and add more MCP tools.

# References & Credits
The e-commerce RAG-agent idea and the first version of this code follow a public video walkthrough by another educator, who shared the code openly. All documentation here is written in my own words; the code was reviewed and extended (brand on the UI and API docs, a safer intro chunk in rag.py, purpose notes, a rebuilt catalogue, an empty cart template). No licence was published with the original code, so all rights to the original remain with its author.
| Library | Licence |
| :-- | :-- |
| CrewAI and CrewAI Tools · MCP Python SDK · FastAPI · openpyxl | MIT |
| ChromaDB · OpenAI Python · Streamlit | Apache-2.0 |
| pypdf · Uvicorn · pandas · python-dotenv | BSD-3-Clause |
_note: Libraries are installed from requirements.txt, not copied into the repository. ShopEasy, its products and prices are sample data for a hypothetical store.
