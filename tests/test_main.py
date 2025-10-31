import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        item_data = {"name": "Test Item", "price": 10.5}
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 200
        assert response.json() == item_data

@pytest.mark.asyncio
async def test_create_and_read_items():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        item_data = {"name": "New Item", "price": 25.0}
        # Post an item
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 200
        assert response.json() == item_data

        # Get all items
        response = await client.get("/items/")
        assert response.status_code == 200
        items = response.json()
        assert len(items) > 0
        assert item_data in items