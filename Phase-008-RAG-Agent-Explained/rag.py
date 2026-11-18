"""RAG layer: turn products_catalog.pdf into a searchable ChromaDB collection.

On the first import the PDF is read with pypdf, split into one chunk per product
(the text is split on "Product Name:"; the catalogue intro becomes its own chunk),
embedded with OpenAI text-embedding-3-small and stored in the chroma_db folder
next to this file.
Later imports reuse the stored collection. mcp_server.py exposes it as the
search_products tool.
"""
import os
from dotenv import load_dotenv
from pypdf import PdfReader
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

load_dotenv()

folder = os.path.dirname(os.path.abspath(__file__))
pdf_file = os.path.join(folder, "products_catalog.pdf")
db_folder = os.path.join(folder, "chroma_db")

chroma_client = chromadb.PersistentClient(path=db_folder)

embedding_function = OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-small",
)

collection = chroma_client.get_or_create_collection(
    name="products",
    embedding_function=embedding_function,
)

if collection.count() == 0:
    reader = PdfReader(pdf_file)
    full_text = ""
    for page in reader.pages:
        full_text = full_text + page.extract_text() + "\n"

    parts = full_text.split("Product Name:")
    # parts[0] is the text before the first product (title, delivery and returns
    # note); it is kept as its own chunk without a "Product Name:" prefix.
    chunks = []
    if parts[0].strip() != "":
        chunks.append(parts[0].strip())
    for part in parts[1:]:
        if part.strip() != "":
            chunks.append("Product Name:" + part.strip())

    ids = []
    for i in range(len(chunks)):
        ids.append("chunk_" + str(i))

    collection.add(documents=chunks, ids=ids)
