import pytest
from httpx import AsyncClient, ASGITransport
from main import app, items

@pytest.fixture(autouse=True)
def clear_items():
    items.clear()

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        response = await client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "FastAPI App"
        assert data["version"] == "0.1.0"
        assert "uptime" in data
        assert data["status"] == "OK"

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

@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        # First, create an item
        item_data = {"name": "Individual Item", "price": 30.0}
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 200

        # Get the item by id (assuming it's the first, id 0)
        response = await client.get("/items/0")
        assert response.status_code == 200
        assert response.json() == item_data

        # Test not found
        response = await client.get("/items/999")
        assert response.status_code == 404

@pytest.mark.asyncio
async def test_create_item_rejects_extra_fields():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        # Try to create item with extra fields
        item_data = {"name": "Test Item", "price": 10.5, "extra_field": "should be rejected"}
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 422  # Unprocessable Entity

@pytest.mark.asyncio
async def test_create_item_validates_name():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        # Test empty name
        item_data = {"name": "", "price": 10.5}
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 422

        # Test whitespace-only name
        item_data = {"name": "   ", "price": 10.5}
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_item_validates_price():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://testserver") as client:
        # Test zero price
        item_data = {"name": "Test Item", "price": 0}
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 422

        # Test negative price
        item_data = {"name": "Test Item", "price": -5.0}
        response = await client.post("/items/", json=item_data)
        assert response.status_code == 422

