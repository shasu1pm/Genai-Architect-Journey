# FirstAPI — Building Web APIs with FastAPI

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**Three FastAPI builds, from a single endpoint to a validated, documented service.**

An API is how one program asks another program to do something. This folder contains the progression: the first route ever written here, a calculator that validates and guards every input, and the complete documented build.

---

## Quick Navigation

| # | Project | What it demonstrates |
| :-- | :-- | :-- |
| 1 | [FirstAPI.py](#1--firstapipy--the-first-endpoint) | Routes, path parameters, query parameters |
| 2 | [calculator.py](#2--calculatorpy--the-calculator-api) | Pydantic models, POST bodies, guarded errors, health checks |
| 3 | [FastAPI App Assignments](#3--fastapi-app-assignments--the-complete-build) | The full documented build with Postman tests |

---

## Contents

| File | Description |
| :-- | :-- |
| [`FirstAPI.py`](./FirstAPI.py) | The starting point — a root route and one path parameter |
| [`calculator.py`](./calculator.py) | Calculator API — four operations with typed request and response models |
| [`FastAPI Calculator API.pdf`](./FastAPI%20Calculator%20API.pdf) | Complete build guide for `calculator.py` — source, endpoints, testing, error handling |
| [`FastAPI App Assignments/`](./FastAPI%20App%20Assignments/) | **Basic FastAPI App** — the complete build, with a Postman collection |

---

## Why FastAPI

You write an ordinary Python function and add a decorator above it. The framework does the rest.

| What you write | What FastAPI does |
| :-- | :-- |
| A Python function | Exposes it at a URL and an HTTP method |
| A Pydantic model | Validates the request body, returns `422` on bad input |
| A return value | Serializes it to JSON with the correct content type |
| Type hints and docstrings | Builds the OpenAPI schema and interactive documentation |

> [!NOTE]
> The documentation is generated **from the code**, not written beside it. Clear model names and honest type hints produce clear documentation for free — and they cannot drift out of date.

---

## 1 · `FirstAPI.py` — the first endpoint

The smallest useful API: one root route, and one route that reads a value out of the URL.

```python
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

### Run it

```powershell
uvicorn FirstAPI:app --reload
```

### Try it

| URL | Response |
| :-- | :-- |
| `http://127.0.0.1:8000/` | `{"Hello":"World"}` |
| `http://127.0.0.1:8000/items/7` | `{"item_id":7,"q":null}` |
| `http://127.0.0.1:8000/items/7?q=laptop` | `{"item_id":7,"q":"laptop"}` |
| `http://127.0.0.1:8000/items/abc` | `422` — `item_id` is typed as `int` |

The last row is the point of the exercise. Nothing in the function body checks the type, yet the bad request never reaches it. The annotation `item_id: int` *is* the validation.

---

## 2 · `calculator.py` — the Calculator API

A calculator exposed over HTTP: four operations, typed in and typed out, with division by zero and unknown operations rejected properly.

### Endpoints

| Method | Path | Purpose | Returns |
| :-- | :-- | :-- | :-- |
| `GET` | `/` | Landing page with a link to the docs | HTML |
| `POST` | `/calculate` | Performs one calculation | JSON |
| `GET` | `/health` | Reports that the service is running | JSON |
| `GET` | `/docs` | Interactive Swagger UI | HTML |

### Run it

```powershell
pip install fastapi uvicorn
uvicorn calculator:app --reload
```

Then open <http://127.0.0.1:8000/docs>.

### A complete request

```json
{
  "num1": 25,
  "num2": 5,
  "operation": "divide"
}
```

```json
{
  "num1": 25.0,
  "num2": 5.0,
  "operation": "divide",
  "result": 5.0,
  "message": "25.0 ÷ 5.0 = 5.0"
}
```

`25` returns as `25.0` because the model declares `float`. The model is the contract; the response is coerced to match it.

### Status codes

| Status | When | Produced by |
| :-- | :-- | :-- |
| `200 OK` | A valid calculation completed | Your function |
| `400 Bad Request` | Division by zero, or an unknown operation | Your `HTTPException` |
| `422 Unprocessable Entity` | Missing field, wrong type, malformed JSON | Pydantic, before your code runs |
| `405 Method Not Allowed` | `GET /calculate` instead of `POST` | FastAPI |

> [!IMPORTANT]
> Failure is signalled with `raise HTTPException(...)`, never by returning an error dictionary. Returning one would send `200 OK` with a failure inside it, and every client would treat the call as successful.

### Two layers of protection

Pydantic guards the **shape** of the data — the right fields with the right types. The `HTTPException` checks guard the **meaning** of the data — values that are well formed but impossible to compute, such as dividing by zero. A robust API needs both.

📄 **Full build guide:** [FastAPI Calculator API.pdf](./FastAPI%20Calculator%20API.pdf)

---

## 3 · `FastAPI App Assignments` — the complete build

The completed **Basic FastAPI App** build: a welcome route, a greeting route with a path parameter, and an in-memory item list capped at five entries.

It ships with an importable Postman collection that creates five items, verifies the total, and confirms a sixth request is rejected with `409 Conflict`.

➡️ [Open the project](./FastAPI%20App%20Assignments/)

---

## Common problems

| Problem | Cause | Fix |
| :-- | :-- | :-- |
| `uvicorn` is not recognized | Environment not active | Activate the venv, or run `python -m uvicorn <file>:app --reload` |
| Address already in use | Port 8000 is taken | Add `--port 8001` and use the new port in your URLs |
| `Error loading ASGI app` | Wrong file or variable name | The command is `file:variable` — check both halves |
| `405` on a POST route | Opened in a browser address bar, which sends `GET` | Use Swagger UI, curl, or Postman |
| `422` on every request | Body is not raw JSON, or a field name is misspelt | Send raw JSON with exactly the declared field names |

---

## Requirements

- Python 3.9 or newer (3.10+ recommended)
- `fastapi` and `uvicorn`

No database, API key, or environment variable is required by any project in this folder.

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank" rel="noopener">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank" rel="noopener">LinkedIn</a>
