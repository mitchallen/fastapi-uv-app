# FastAPI App

A simple FastAPI application demonstrating async endpoints, Pydantic models, testing with pytest, and code coverage.

## Features

- **FastAPI**: Modern web framework for building APIs with async support
- **Pydantic**: Data validation and serialization
- **pytest**: Testing framework with async support
- **pytest-cov**: Code coverage reporting
- **uv**: Fast Python package installer and resolver

## Installation

1. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/mitchallen/fastapi-uv-app.git
   cd fastapi-uv-app
   ```

3. Install dependencies:
   ```bash
   make install
   ```

## Usage

### Running the Application

Start the development server:
```bash
make run
```

The API will be available at `http://localhost:8000`

### API Endpoints

- `GET /` - Returns a hello world message
- `POST /items/` - Creates a new item

Example POST request:
```json
{
  "name": "Sample Item",
  "price": 19.99
}
```

### Testing

Run tests:
```bash
make test
```

### Code Coverage

Generate HTML coverage report:
```bash
make coverage
```

Open coverage report in browser:
```bash
make coverage-open
```

## Project Structure

```
.
├── main.py              # FastAPI application
├── tests/
│   └── test_main.py     # Test cases
├── pyproject.toml       # Project dependencies
├── Makefile             # Build and test commands
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Development

- Install dependencies: `make install`
- Run tests: `make test`
- View help: `make help`