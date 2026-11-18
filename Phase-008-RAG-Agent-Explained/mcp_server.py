"""MCP server for the shopping agent: one RAG tool and four cart tools.

search_products wraps the ChromaDB collection built in rag.py (RAG as a tool);
add_to_cart, remove_from_cart, view_cart and clear_cart read and write cart.xlsx.
agent.py starts this file as a subprocess and talks to it over stdio.
Swap cart.xlsx for a real database to use the same agent in production.
"""
import os
import pandas as pd
from mcp.server.fastmcp import FastMCP
import rag

folder = os.path.dirname(os.path.abspath(__file__))
cart_file = os.path.join(folder, "cart.xlsx")

if not os.path.exists(cart_file):
    empty_cart = pd.DataFrame(columns=["product_name", "price", "quantity", "total"])
    empty_cart.to_excel(cart_file, index=False)

mcp = FastMCP("product-shop")



@mcp.tool()
def search_products(question: str) -> str:
    """Search the product catalogue PDF. Use this for any question about products,
    prices, features, categories, delivery or returns."""
    results = rag.collection.query(query_texts=[question], n_results=3)
    found_text = "\n\n".join(results["documents"][0])
    return found_text



@mcp.tool()
def add_to_cart(product_name: str, price: float, quantity: int = 1) -> str:
    """Add a product to the cart. Get the correct product name and price from
    search_products first."""
    cart = pd.read_excel(cart_file)

    if product_name in cart["product_name"].values:
        cart.loc[cart["product_name"] == product_name, "quantity"] += quantity
    else:
        new_row = pd.DataFrame([{"product_name": product_name, "price": price, "quantity": quantity}])
        cart = pd.concat([cart, new_row], ignore_index=True)

    cart["total"] = cart["price"] * cart["quantity"]
    cart.to_excel(cart_file, index=False)
    return "Added " + str(quantity) + " x " + product_name + " to the cart."


@mcp.tool()
def remove_from_cart(product_name: str) -> str:
    """Remove a product from the cart using its name."""
    cart = pd.read_excel(cart_file)
    if product_name not in cart["product_name"].values:
        return product_name + " is not in the cart."
    cart = cart[cart["product_name"] != product_name]
    cart.to_excel(cart_file, index=False)
    return "Removed " + product_name + " from the cart."


@mcp.tool()
def view_cart() -> str:
    """Show everything in the cart and the grand total."""
    cart = pd.read_excel(cart_file)
    if cart.empty:
        return "The cart is empty."
    return cart.to_string(index=False) + "\n\nGrand total: Rs. " + str(cart["total"].sum())


@mcp.tool()
def clear_cart() -> str:
    """Remove all products from the cart."""
    empty_cart = pd.DataFrame(columns=["product_name", "price", "quantity", "total"])
    empty_cart.to_excel(cart_file, index=False)
    return "The cart is now empty."


if __name__ == "__main__":
    mcp.run(transport="stdio")
