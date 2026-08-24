# Basic FastAPI App

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**A small, beginner-friendly web API built with Python, FastAPI, and Uvicorn.**

A **Phase-004-FastAPI-And-Streamlit** build. The full [project brief](./GenAI_Architect_Basic_FastAPI_App_Assignment.pdf) — goal, requirements, setup, and deliverables — is included in this folder.

The API provides:

- A root endpoint that returns a welcome message.
- A greeting endpoint that reads a name from the URL path.
- A POST endpoint that creates items in an in-memory list.
- A GET endpoint that returns the list and its current total.
- A maximum-list-size rule that allows exactly five items.
- Automatically generated interactive API documentation.
- JSON responses that can be tested in a browser, Swagger UI, Postman, or another HTTP client.

---

## Quick Navigation

| Section | Contents |
| :-- | :-- |
| [Installation](#installation) | Virtual environment and dependencies |
| [Run the application](#run-the-application) | Starting the Uvicorn server |
| [API endpoints](#api-endpoints) | Every route, with request and response examples |
| [Interactive documentation](#interactive-api-documentation) | Swagger UI and ReDoc |
| [Testing](#test-with-a-browser-curl-or-postman) | Browser, curl, and the Postman collection |
| [Status codes](#expected-status-codes) | What each response code means |
| [Assignment checklist](#assignment-checklist) | Requirements met |

---

## Project structure

```text
.
├── main.py             # Complete FastAPI application
├── requirements.txt    # Python dependencies
├── Basic_FastAPI_App.postman_collection.json # Importable Postman tests
├── .gitignore          # Files Git should ignore
└── README.md            # Project documentation
```

All application code is kept in a single `main.py`, as the brief requires.

## Requirements

- Python 3.9 or newer
- `pip`

Python 3.10 or newer is recommended. No database, API key, or environment variable is required.

## Installation

### 1. Open the project directory

In a terminal, change into the directory containing `main.py`.

### 2. Create a virtual environment

```bash
python -m venv venv
```

On systems where Python is exposed as `python3`, run `python3 -m venv venv` instead.

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
venv\Scripts\activate.bat
```

macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the application

Start the development server with Uvicorn:

```bash
uvicorn main:app --reload
```

The command means:

- `main` is the Python file `main.py`.
- `app` is the FastAPI application created inside that file.
- `--reload` restarts the development server after a code change.

The server will normally be available at <http://127.0.0.1:8000>. Keep the terminal open while using the API. Press `Ctrl+C` to stop it.

The application can also be started with:

```bash
python main.py
```

## API endpoints

| Method | Path | Description | Example response |
| --- | --- | --- | --- |
| `GET` | `/` | Returns the welcome message. | `{"message":"Hello, FastAPI"}` |
| `GET` | `/greet/{name}` | Returns a greeting for the supplied path parameter. | `{"message":"Hello, Asha!"}` |
| `POST` | `/items` | Creates one item. The list can hold five items. | `{"name":"Laptop","description":"Development computer","id":1}` |
| `GET` | `/items` | Returns the items, current total, and maximum. | `{"total":1,"maximum":5,"items":[...]}` |

### Root endpoint

Request:

```http
GET http://127.0.0.1:8000/
```

Response (`200 OK`):

```json
{
  "message": "Hello, FastAPI"
}
```

### Greeting endpoint

Replace `{name}` with the person to greet.

Request:

```http
GET http://127.0.0.1:8000/greet/Asha
```

Response (`200 OK`):

```json
{
  "message": "Hello, Asha!"
}
```

The `name` value is required because it is a path parameter. A request to `/greet` does not match this endpoint and returns FastAPI's `404 Not Found` response. Spaces and other special URL characters should be URL-encoded by the client; browsers, Swagger UI, and Postman normally do this automatically.

### Create an item

Send a JSON request body to create one item:

```http
POST http://127.0.0.1:8000/items
Content-Type: application/json
```

```json
{
  "name": "Laptop",
  "description": "Development computer"
}
```

Response (`201 Created`):

```json
{
  "name": "Laptop",
  "description": "Development computer",
  "id": 1
}
```

`name` is required and must contain between 1 and 100 characters. `description` is optional and can contain up to 300 characters.

### List all items

Request:

```http
GET http://127.0.0.1:8000/items
```

After creating five items, the response is:

```json
{
  "total": 5,
  "maximum": 5,
  "items": [
    {"name": "Laptop", "description": "Development computer", "id": 1},
    {"name": "Keyboard", "description": null, "id": 2},
    {"name": "Mouse", "description": null, "id": 3},
    {"name": "Monitor", "description": null, "id": 4},
    {"name": "Headphones", "description": null, "id": 5}
  ]
}
```

The items are stored in memory. They are cleared whenever the application server restarts. A sixth `POST /items` request returns `409 Conflict` and does not change the list.

## Interactive API documentation

FastAPI builds OpenAPI documentation from the endpoint definitions in `main.py`.

After starting the server, open:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- Raw OpenAPI schema: <http://127.0.0.1:8000/openapi.json>

To test with Swagger UI:

1. Open `/docs` in a browser.
2. Expand an endpoint.
3. Select **Try it out**.
4. For `/greet/{name}`, enter a name.
5. Select **Execute** and inspect the JSON response and status code.

## Test with a browser, curl, or Postman

Browser URLs:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/greet/Asha
```

curl commands:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/greet/Asha
```

### Create five items with Postman

An importable collection is included in `Basic_FastAPI_App.postman_collection.json`. To run all tests automatically:

1. Restart the Uvicorn server so the in-memory item list is empty.
2. In Postman, select **Import** and choose `Basic_FastAPI_App.postman_collection.json`.
3. Open the imported **Basic FastAPI App** collection.
4. Select **Run collection** and run the requests in their numbered order.
5. Confirm all Postman tests pass. The run creates five items, verifies `total` is 5, and confirms a sixth item returns `409 Conflict`.

To test the POST request manually instead:

1. Start the FastAPI server and open Postman.
2. Create a new HTTP request and select the `POST` method.
3. Enter `http://127.0.0.1:8000/items` as the URL.
4. Select **Body**, choose **raw**, and select **JSON** from the content-type menu.
5. Enter `{"name":"Laptop","description":"Development computer"}`.
6. Select **Send**. Confirm the status is `201 Created` and the response has `"id": 1`.
7. Change the request body and send four more requests using the names `Keyboard`, `Mouse`, `Monitor`, and `Headphones`. Each successful response should have the next ID.
8. Create a new `GET` request for `http://127.0.0.1:8000/items`.
9. Select **Send** and confirm that the response contains `"total": 5`, `"maximum": 5`, and five objects inside `items`.
10. Optionally send the POST request a sixth time. Confirm the response is `409 Conflict` with a message explaining that the five-item maximum has been reached.

Postman automatically sets `Content-Type: application/json` when **raw JSON** is selected. No authorization is needed.

Equivalent curl commands:

```bash
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name":"Laptop","description":"Development computer"}'
curl http://127.0.0.1:8000/items
```

## Expected status codes

- `200 OK`: A defined endpoint was requested successfully.
- `201 Created`: An item was added successfully with `POST /items`.
- `409 Conflict`: The item list already contains five items.
- `422 Unprocessable Entity`: A POST body is missing, is not valid JSON, or contains invalid data.
- `404 Not Found`: The URL does not match an endpoint, such as `/greet` without a name.
- `405 Method Not Allowed`: A defined URL was called with an unsupported method, such as `POST /`.

## Implementation overview

`main.py` creates one `FastAPI` instance named `app`. The route decorators connect HTTP routes to regular Python functions. FastAPI validates POST data with Pydantic models, serializes Python data to JSON, and sends the appropriate status code and content type.

The item collection is a Python list held in application memory. Each successful POST adds an item with an automatically assigned numeric ID. Before adding it, the endpoint checks the collection size and rejects requests after the fifth item.

The functions include return type annotations, docstrings, and route summaries. FastAPI uses this metadata to make the generated OpenAPI schema and interactive documentation clear.

## Development notes

- `--reload` is intended for local development, not a production deployment.
- If port 8000 is already in use, choose another port with `uvicorn main:app --reload --port 8001` and use that port in the URLs.
- If `uvicorn` is not recognized, confirm that the virtual environment is active or run `python -m uvicorn main:app --reload`.
- In PowerShell, if script execution prevents activation, use Command Prompt with `venv\Scripts\activate.bat`, or review the local PowerShell execution policy before changing it.

## Stop the application

Press `Ctrl+C` in the terminal running Uvicorn. Then leave the virtual environment with:

```bash
deactivate
```

## Build checklist

- [x] Uses the FastAPI framework.
- [x] Provides `GET /` with a JSON welcome message.
- [x] Provides `GET /greet/{name}` with a URL path parameter.
- [x] Provides `POST /items` for creating items from JSON request data.
- [x] Provides `GET /items` for checking the list and total.
- [x] Enforces a maximum of five items.
- [x] Runs with the Uvicorn server.
- [x] Exposes automatic interactive documentation at `/docs`.
- [x] Keeps all application code in `main.py`.
- [x] Includes setup and usage documentation.

---

## Requirements

- Python 3.9 or newer (3.10+ recommended)
- `fastapi` and `uvicorn`

No database, API key, or environment variable is required.

📄 **Project brief:** [GenAI_Architect_Basic_FastAPI_App_Assignment.pdf](./GenAI_Architect_Basic_FastAPI_App_Assignment.pdf)

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank" rel="noopener">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank" rel="noopener">LinkedIn</a>
