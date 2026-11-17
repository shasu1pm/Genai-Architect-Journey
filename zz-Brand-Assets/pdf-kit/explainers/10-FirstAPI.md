---
out: Phase-004-FastAPI-And-Streamlit/FirstAPI/FirstAPI-Explainer.pdf
folder: Phase-004-FastAPI-And-Streamlit
title: FirstAPI — Web APIs with FastAPI
subtitle: Three FastAPI builds, from a single endpoint to a validated, documented service
short: FirstAPI
fact: Document | Sub-project explainer
fact: Level | Beginner to intermediate
fact: Contents | FirstAPI.py · calculator.py · FastAPI App Assignments/
fact: Tools | Python 3.9+ · FastAPI · Pydantic · Uvicorn
fact: Folder | Phase-004-FastAPI-And-Streamlit/FirstAPI
keywords: FastAPI, API, Pydantic, Uvicorn
---
# What it is
lead: An API is how one program asks another program to do something.
This folder shows the progression: the first route written in this repository, a calculator that validates and guards every input, and the complete documented build with Postman tests.

# Why FastAPI
| What you write | What FastAPI does |
| :-- | :-- |
| A Python function | Exposes it at a URL and HTTP method |
| A Pydantic model | Validates the request body; returns `422` on bad input |
| A return value | Serialises it to JSON with the right content type |
| Type hints and docstrings | Builds the OpenAPI schema and interactive docs |
> [!TIP] Documentation that cannot drift
> The docs at `/docs` are generated from the code itself. Clear model names and honest type hints produce clear documentation for free.

# 1 · FirstAPI.py — the first endpoint
```python FirstAPI.py
import fastapi
from fastapi import FastAPI

app = FastAPI()

# Main endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
| URL | Response |
| :-- | :-- |
| `/` | `{"Hello":"World"}` |
| `/items/7` | `{"item_id":7,"q":null}` |
| `/items/7?q=laptop` | `{"item_id":7,"q":"laptop"}` |
| `/items/abc` | `422` — `item_id` is typed as `int` |
The last row is the lesson: nothing in the function checks the type, yet the bad request never reaches it. The annotation `item_id: int` **is** the validation.

# 2 · calculator.py — the Calculator API
flow: POST /calculate > Pydantic checks the shape > Function checks the meaning > JSON result or HTTP 400
| Method | Path | Purpose |
| :-- | :-- | :-- |
| `GET` | `/` | Landing page linking to the docs |
| `POST` | `/calculate` | One calculation: add, subtract, multiply or divide |
| `GET` | `/health` | Reports that the service is running |
| `GET` | `/docs` | Interactive Swagger UI |
```json Request → response
{"num1": 25, "num2": 5, "operation": "divide"}
{"num1": 25.0, "num2": 5.0, "operation": "divide", "result": 5.0, "message": "25.0 ÷ 5.0 = 5.0"}
```
| Status | When |
| :-- | :-- |
| `200 OK` | Valid calculation completed |
| `400 Bad Request` | Division by zero or an unknown operation (`HTTPException`) |
| `422 Unprocessable Entity` | Missing field, wrong type or malformed JSON (Pydantic) |
| `405 Method Not Allowed` | `GET /calculate` instead of `POST` |
> [!NOTE] Two layers of protection
> Pydantic guards the **shape** of the data; `HTTPException` guards its **meaning**. Failure is raised, never returned as an error dictionary — otherwise clients would see `200 OK` and treat it as success.

# 3 · FastAPI App Assignments — the complete build
The **Basic FastAPI App**: a welcome route, a greeting route with a path parameter, and an in-memory item list capped at five, with an importable Postman collection. See its own explainer.

# Run it
```powershell Run
pip install fastapi uvicorn
uvicorn FirstAPI:app --reload       # or: uvicorn calculator:app --reload
```
Open `http://127.0.0.1:8000/docs` to try every endpoint.

# Key takeaways
- Type hints are validation, documentation and editor help at once.
- Use the right status code: 400 for impossible requests, 422 for malformed ones.
- Full calculator walkthrough: FastAPI Calculator API.pdf in this folder.
