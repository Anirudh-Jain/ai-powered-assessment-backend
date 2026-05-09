FROM python:3.11-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml .
RUN uv venv && \
    uv pip install -r pyproject.toml

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
