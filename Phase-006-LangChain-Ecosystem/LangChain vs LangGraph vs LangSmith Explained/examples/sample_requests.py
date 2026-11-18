"""Send sample questions to a running AI Learning Assistant.

1. Start the server (from the project folder):   uvicorn app.main:app --reload
2. In a second terminal:                          python examples/sample_requests.py

Set BASE_URL to call another address, e.g.  set BASE_URL=http://127.0.0.1:9000
"""
import json
import os
import sys

import httpx

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

REQUESTS = [
    ("GET", "/health", None),
    ("POST", "/ask", {"question": "What is Agentic AI? Explain with a simple real-world example."}),
    ("POST", "/workflow", {"question": "LangChain vs LangGraph: what is the difference?"}),
    ("POST", "/workflow", {"question": "Hello!"}),
    ("POST", "/workflow", {"question": "   "}),      # invalid: shows the 422 error format
]


def main() -> None:
    try:
        with httpx.Client(base_url=BASE_URL, timeout=120) as client:
            for method, path, body in REQUESTS:
                response = client.request(method, path, json=body)
                print(f"\n{method} {path}  ->  HTTP {response.status_code}")
                if body is not None:
                    print("request :", json.dumps(body))
                print("response:", json.dumps(response.json(), indent=2, ensure_ascii=False))
    except httpx.ConnectError:
        sys.exit(f"Could not reach {BASE_URL}. Start the server first: uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()
