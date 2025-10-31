# Agent Instructions for FastAPI App

## Build/Lint/Test Commands
- **Install dependencies**: `uv sync` or `make install`
- **Run app**: `uv run uvicorn main:app --reload` or `make run`
- **Run all tests**: `PYTHONPATH=. uv run pytest --cov=main --cov-report=term-missing` or `make test`
- **Run single test**: `PYTHONPATH=. uv run pytest tests/test_main.py::test_function_name -v`
- **Generate coverage**: `PYTHONPATH=. uv run pytest --cov=main --cov-report=html` or `make coverage`

## Code Style Guidelines
- **Language**: Python 3.12+ with FastAPI framework
- **Imports**: Standard library first, then third-party (fastapi, pydantic, slowapi, etc.)
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Types**: Use type hints for all function parameters and return values
- **Async**: Use async/await for all API endpoints
- **Models**: Use Pydantic BaseModel for data validation with `model_config = {"extra": "forbid"}`
- **Validation**: Use Pydantic field validators for business logic validation
- **Docstrings**: Required for all functions, classes, and modules
- **Error handling**: Use FastAPI's HTTPException for API errors
- **Rate limiting**: Implemented with slowapi middleware (10 requests/minute per IP)
- **Testing**: pytest with @pytest.mark.asyncio, httpx AsyncClient for integration tests
- **Formatting**: Follow PEP 8, use double quotes for strings