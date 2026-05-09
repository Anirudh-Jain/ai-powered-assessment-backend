FROM python:3.11-slim

# Install uv
RUN pip install uv

WORKDIR /app

# Copy pyproject.toml and lock file
COPY pyproject.toml .

# Create virtual environment and install dependencies
RUN uv venv && \
    uv pip install -r pyproject.toml

# Copy application code
COPY . .

EXPOSE 8002

CMD ["python", "main.py"]
