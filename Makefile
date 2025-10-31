.PHONY: help install run test

help:  ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install:  ## Install dependencies
	uv sync

run:  ## Run the FastAPI app
	uv run uvicorn main:app --reload

test:  ## Run tests
	PYTHONPATH=. uv run pytest --cov=main --cov-report=term-missing