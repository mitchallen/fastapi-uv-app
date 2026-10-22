FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set workdir
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies. --no-cache keeps uv's download cache (a second copy
# of every wheel) out of the image.
RUN uv sync --frozen --no-install-project --no-dev --no-cache

# The app runs from /app/.venv, so the base image's own pip (and the old
# urllib3/msgpack it vendors) and ensurepip's bundled pip wheel are dead
# weight that the scheduled Trivy scan flags. Remove them.
RUN python -m pip uninstall -y pip && \
    rm -rf /usr/local/lib/python3.12/ensurepip/_bundled

# Copy source code
COPY main.py ./

# Expose port
EXPOSE 8000

# Run the app. --no-sync: a plain `uv run` re-syncs the default groups at
# every start, which downloads the dev tooling --no-dev left out above.
CMD ["uv", "run", "--no-sync", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]