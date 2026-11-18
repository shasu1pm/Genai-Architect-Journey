"""FastAPI wrapper so websites, Shopify stores or other apps can call the shopping agent.

POST /ask   sends a question (and optional chat history) to the CrewAI crew.
GET  /cart  returns the items in cart.xlsx and the grand total.
GET  /docs  interactive Swagger UI for trying both endpoints.

Run with: uvicorn api:app --reload
"""
import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent import crew

folder = os.path.dirname(os.path.abspath(__file__))
cart_file = os.path.join(folder, "cart.xlsx")

# Brand assets are used as they are from the repository's zz-Brand-Assets folder.
brand_folder = os.path.join(os.path.dirname(folder), "zz-Brand-Assets")
brand_files = {
    "logo.png": os.path.join(brand_folder, "Dragon-Motivation-Logo.png"),
    "negot.png": os.path.join(brand_folder, "NeGot-My-AI-Avatar.png"),
}
BRAND = "Shasu Vathanan - GEN AI - Product Manager"

app = FastAPI(
    title="ShopEasy Agent API | Shasu Vathanan",
    description=(
        '<img src="/brand/logo.png" alt="Dragon Motivation logo" height="56"> '
        '<img src="/brand/negot.png" alt="NeGot - my AI avatar" height="52">\n\n'
        f"**{BRAND}**\n\n"
        "A RAG agent for a sample online store: CrewAI agent + MCP tools + ChromaDB product search. "
        "Use **/ask** for questions and cart actions, and **/cart** to see the cart.\n\n"
        "[SHASUVATHANAN.COM](https://shasuvathanan.com) · "
        "[LinkedIn](https://www.linkedin.com/in/shasuvathanan) · "
        "[GitHub](https://github.com/shasu1pm/Genai-Architect-Journey)"
    ),
    contact={"name": BRAND, "url": "https://shasuvathanan.com"},
    docs_url=None,
)


class Question(BaseModel):
    question: str
    history: str = ""


@app.get("/")
def home():
    return {"message": "Shopping agent API is running. POST your question to /ask"}


@app.post("/ask")
def ask(body: Question):
    result = crew.kickoff(inputs={"history": body.history, "question": body.question})
    return {"question": body.question, "answer": result.raw}


@app.get("/cart")
def get_cart():
    cart = pd.read_excel(cart_file)
    return {"items": cart.to_dict(orient="records"), "grand_total": float(cart["total"].sum())}


@app.get("/docs", include_in_schema=False)
def docs():
    """Swagger UI with the brand logo as favicon."""
    return get_swagger_ui_html(openapi_url=app.openapi_url, title=app.title + " - Docs",
                               swagger_favicon_url="/brand/logo.png")


@app.get("/brand/{name}", include_in_schema=False)
def brand_image(name: str):
    """Serve only the two brand images used on the docs page."""
    if name not in brand_files or not os.path.exists(brand_files[name]):
        raise HTTPException(status_code=404)
    return FileResponse(brand_files[name], media_type="image/png")
