from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items = []

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_items():
    return items

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item