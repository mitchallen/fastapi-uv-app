import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

start_time = time.time()

class Item(BaseModel):
    name: str
    price: float

items = []

@app.get("/")
async def read_root():
    uptime = time.time() - start_time
    return {
        "name": "FastAPI App",
        "version": "0.1.0",
        "uptime": f"{uptime:.2f} seconds",
        "status": "OK"
    }

@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item