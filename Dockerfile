FROM python:3.11-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.13.3 /uv /uvx /bin/

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
	UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

FROM python:3.11-slim

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH" \
	PYTHONUNBUFFERED=1

RUN apt-get update \
	&& apt-get install --no-install-recommends -y libpq5 \
	&& rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
COPY src/ /app/src/

RUN groupadd --system --gid 10001 app \
	&& useradd --system --uid 10001 --gid app --no-create-home app

USER 10001:10001

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
	CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"]

CMD ["fastapi", "run"]
