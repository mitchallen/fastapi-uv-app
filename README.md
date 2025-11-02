# FastAPI App

A simple FastAPI application demonstrating async endpoints, Pydantic models, testing with pytest, and code coverage.

## Features

- **FastAPI**: Modern web framework for building APIs with async support
- **Pydantic**: Data validation and serialization with strict input validation
- **pytest**: Testing framework with async support
- **pytest-cov**: Code coverage reporting
- **uv**: Fast Python package installer and resolver
- **Security**: Rate limiting, input validation, and vulnerability scanning
- **SlowAPI**: Rate limiting middleware for API protection

## Installation

### Local Development

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

### Docker

Build and run with Docker:
```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

## Usage

### Running the Application

Start the development server:
```bash
make run
```

The API will be available at `http://localhost:8000`

### API Endpoints

- `GET /` - Returns application information including a link to API documentation
- `GET /docs` - Interactive API documentation (Swagger UI)
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

## Security

### Vulnerability Scanning

The project includes automated security scanning to identify potential vulnerabilities in dependencies and source code.

Run all security scans:
```bash
make security
```

Check dependencies for known vulnerabilities:
```bash
make safety
```

Run security linting on source code:
```bash
make bandit
```

### Security Features

- **Rate Limiting**: 10 requests per minute per IP address using SlowAPI
- **Input Validation**: Pydantic models with strict validation and field sanitization
- **Dependency Scanning**: Automated checks for known security vulnerabilities in Python packages
- **Code Security Linting**: Static analysis for potential security issues in source code

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

## About

This project was originally created using [opencode](https://opencode.ai) v1.0.11 and the Grok LLM.

## Development

- Install dependencies: `make install`
- Run tests: `make test`
- View help: `make help`