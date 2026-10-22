# --- Stage 1: Build ---
# Build the venv on Chainguard/Wolfi's Python-dev image (uv is preinstalled).
# Building on the SAME base as the runtime keeps the venv's interpreter symlink
# valid at runtime. Wolfi carries none of the Debian OS packages (util-linux,
# perl, ncurses, tar, systemd libs) behind the ~160 unfixable findings the
# scheduled Trivy scan reported on python:3.12-slim.
FROM cgr.dev/chainguard/python:latest-dev AS builder
WORKDIR /app

# Compile bytecode, copy (don't link) into the venv, and build on the image's
# own Python rather than downloading one, so the runtime stage can host it.
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0

# Runtime dependencies only: --no-dev leaves out the test/scan tooling (and
# the pip that pip-audit pulls in), --no-cache keeps uv's wheel cache out.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev --no-cache

# --- Stage 2: Production ---
# Distroless Chainguard/Wolfi Python: no shell, no pip, no package manager,
# and it already runs as the non-root 'nonroot' user (uid 65532).
FROM cgr.dev/chainguard/python:latest AS prod
WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY main.py ./

# The venv's uvicorn runs directly; there is no uv in this stage.
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
