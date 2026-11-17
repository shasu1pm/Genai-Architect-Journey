---
out: Phase-004-FastAPI-And-Streamlit/FirstAPI/FastAPI App Assignments/Basic-FastAPI-App-Explainer.pdf
folder: Phase-004-FastAPI-And-Streamlit
title: Basic FastAPI App
subtitle: A beginner-friendly web API — welcome, greeting and a five-item list, tested with Postman
fact: Document | Sub-project explainer
fact: Level | Beginner
fact: Script | main.py (single file)
fact: Tools | Python 3.9+ · FastAPI · Uvicorn · Postman
fact: Tests | Basic_FastAPI_App.postman_collection.json
fact: Folder | …/FirstAPI/FastAPI App Assignments
keywords: FastAPI, Postman, REST, status codes
---
# What it is
lead: A complete small API: four endpoints, one business rule, automatic documentation and a test collection.
All application code lives in a single `main.py`, as the project brief requires. Items are stored in memory, so the list resets whenever the server restarts.

# The endpoints
| Method | Path | What it does | Example response |
| :-- | :-- | :-- | :-- |
| `GET` | `/` | Welcome message | `{"message":"Hello, FastAPI"}` |
| `GET` | `/greet/{name}` | Greets the name in the URL | `{"message":"Hello, Asha!"}` |
| `POST` | `/items` | Creates one item (max five) | `{"name":"Laptop","description":"Development computer","id":1}` |
| `GET` | `/items` | Lists items, total and maximum | `{"total":1,"maximum":5,"items":[...]}` |

# The business rule — exactly five items
flow: POST /items > Validate body (Pydantic) > List already has 5? > Yes → 409 Conflict > No → add with next id → 201 Created
`name` is required (1–100 characters); `description` is optional (up to 300). A sixth POST returns `409 Conflict` and leaves the list unchanged.
> [!TIP] A familiar way to picture it (hypothetical)
> Think of a small online shop's "compare products" tray that holds five items — the way large retailers such as Amazon let shoppers shortlist products. The sixth item is refused politely instead of silently replacing one. This is an illustration, not a description of any real system.

# Run it
```powershell Setup and run
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
`main` is the file, `app` is the FastAPI object inside it, and `--reload` restarts the server on code changes (development only). Documentation: `/docs` (Swagger UI), `/redoc`, `/openapi.json`.

# Test with Postman
1. Restart Uvicorn so the list is empty.
2. **Import** `Basic_FastAPI_App.postman_collection.json` and open the collection.
3. **Run collection** in numbered order.
4. All tests pass: five items created, `total` is 5, and the sixth item returns `409 Conflict`.

# Status codes
| Code | Meaning here |
| :-- | :-- |
| `200 OK` | A defined endpoint answered successfully |
| `201 Created` | An item was added |
| `409 Conflict` | The list already holds five items |
| `422 Unprocessable Entity` | Body missing, not JSON, or invalid |
| `404 Not Found` | No such URL — for example `/greet` without a name |
| `405 Method Not Allowed` | Wrong method — for example `POST /` |

# Key takeaways
- Pydantic models validate input before your code runs.
- Business rules belong in the endpoint and deserve their own status code (`409`).
- A test collection turns "it works on my machine" into repeatable evidence.
