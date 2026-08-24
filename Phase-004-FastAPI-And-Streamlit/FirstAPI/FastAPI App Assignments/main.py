"""A small FastAPI application for the Basic FastAPI App assignment."""

from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="Basic FastAPI App",
    description=(
        "A beginner-friendly API with a welcome route, personalized greeting, "
        "and an in-memory list containing up to five items."
    ),
    version="1.1.0",
)


class ItemCreate(BaseModel):
    """Information accepted when a new item is created."""

    name: str = Field(min_length=1, max_length=100, examples=["Laptop"])
    description: Optional[str] = Field(
        default=None,
        max_length=300,
        examples=["Development computer"],
    )


class Item(ItemCreate):
    """An item stored by the application."""

    id: int


class ItemList(BaseModel):
    """The current item collection and its size."""

    total: int
    maximum: int
    items: list[Item]


MAX_ITEMS = 5
items: list[Item] = []


@app.get("/", summary="Show a welcome message")
def read_root() -> dict[str, str]:
    """Return a simple welcome message."""
    return {"message": "Hello, FastAPI"}


@app.get("/greet/{name}", summary="Greet someone by name")
def greet_user(name: str) -> dict[str, str]:
    """Return a greeting containing the name supplied in the URL path."""
    return {"message": f"Hello, {name}!"}


@app.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    summary="Create an item",
)
def create_item(item_data: ItemCreate) -> Item:
    """Add an item unless the list has already reached its five-item limit."""
    if len(items) >= MAX_ITEMS:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The item list already contains the maximum of 5 items.",
        )

    item = Item(id=len(items) + 1, **item_data.model_dump())
    items.append(item)
    return item


@app.get(
    "/items",
    response_model=ItemList,
    summary="List all items",
)
def list_items() -> ItemList:
    """Return every stored item together with the current and maximum totals."""
    return ItemList(total=len(items), maximum=MAX_ITEMS, items=items)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
