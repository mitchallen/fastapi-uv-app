"""
FastAPI application with item management endpoints.
"""

import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

start_time = time.time()

class Item(BaseModel):
    """Model for an item with name and price."""
    name: str
    price: float

items = []

@app.get("/")
async def read_root():
    """Return application information including name, version, uptime, and status."""
    uptime = time.time() - start_time
    return {
        "name": "FastAPI App",
        "version": "0.1.0",
        "uptime": f"{uptime:.2f} seconds",
        "status": "OK"
    }

@app.get("/items/")
async def read_items():
    """Return a list of all items."""
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Return a specific item by its ID (index)."""
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/")
async def create_item(item: Item):
    """Create a new item and add it to the list."""
    items.append(item)
    return item