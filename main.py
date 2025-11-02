"""
FastAPI application with item management endpoints.
"""

import os
import time
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, field_validator
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

limiter = Limiter(key_func=get_remote_address, default_limits=["10/minute"])
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

start_time = time.time()

class Item(BaseModel):
    """Model for an item with name and price."""
    model_config = {"extra": "forbid"}

    name: str
    price: float

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("name must not be empty")
        return v.strip()

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("price must be positive")
        return v

items = []

@app.get("/")
async def read_root():
    """Return application information including name, version, uptime, and status."""
    uptime = time.time() - start_time
    return {
        "name": "FastAPI App",
        "version": "0.1.0",
        "uptime": f"{uptime:.2f} seconds",
        "status": "OK",
        "docs_url": "/docs"
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