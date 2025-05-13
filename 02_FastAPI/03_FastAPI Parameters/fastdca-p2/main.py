from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Home Route: Displays a welcome message
@app.get("/")
async def home():
    return {"message": "Welcome to the home page!"}

# Path Parameter: Get item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="Item ID", ge=1)):
    return {"item_id": item_id}

# Query Parameter: Search items with a query
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None)):
    if q:
        return {"message": f"Searching for: {q}"}
    return {"message": "No search query provided"}

# Path + Query Parameters: Get item details with an optional query
@app.get("/items/{item_id}/details")
async def read_item_details(item_id: int, detail: Optional[str] = Query(None)):
    if detail:
        return {"item_id": item_id, "detail": detail}
    return {"item_id": item_id, "detail": "No detail provided"}

# Pydantic Model: Defines structure for item data
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# POST Request: Create a new item
@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}
