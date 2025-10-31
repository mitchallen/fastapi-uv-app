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