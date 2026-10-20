# AI Assessment Backend Repository

This repository contains the single backend service for the AI Powered Assessment & Examination Platform.

The frontend is stored in a separate repository under `frontend/`.

## Repository Layout

```
src/
  config.py
  main.py
Dockerfile
pyproject.toml
uv.lock
.python-version
frontend/             # Separate Next.js frontend repository
docker-compose.yml    # Local full-stack orchestration
Makefile              # Development helpers
.env.example          # Environment variable template
README.md             # Backend repository documentation
```

## Technology Stack

- **Backend**: FastAPI 0.115+, Python 3.11+, uv package manager
- **Database**: PostgreSQL 16
- **AI**: OpenAI API
- **Frontend**: Next.js 16+ (separate repository)
- **Containers**: Docker, Docker Compose

## Quick Start

### 1. Prepare Environment

```powershell
Copy-Item .env.example .env
```

Set a unique `JWT_SECRET` with at least 32 characters, configure `CORS_ORIGINS`, and add your OpenAI API key to `.env` before starting the services.

### 2. Start Services

```powershell
make up
```

### 3. Verify Health

```powershell
curl http://localhost:8000/health
```

### 4. Open Frontend

Open http://localhost:3000 in your browser.

## Running Locally

### Backend

Standard psycopg requires the PostgreSQL `libpq` client library. Docker installs it automatically; local development machines must have it installed and available on `PATH`.

```powershell
uv sync --group dev
uv run fastapi dev
```

Or use the Make target from the repository root:

```powershell
make backend-dev
```

### Frontend

```powershell
make frontend-dev
```

### Run Tests

```powershell
make test
```

## Docker Compose

The compose stack includes:

- `postgres` database
- `backend` FastAPI service
- `frontend` optional Next.js container

SQLAlchemy models and the request-scoped session dependency live under `src/models/` and `src/db/`. The API handlers remain mock-backed until persistence is wired into the routes. PostgreSQL URLs use the `postgresql+psycopg://` dialect.

Run `uv run alembic upgrade head` to apply migrations. In Docker Compose, use `docker compose run --rm backend alembic upgrade head` before deploying the backend. Create new revisions with `uv run alembic revision --autogenerate -m "describe schema change"`, review the generated file, and commit it with the model changes.

## Environment Variables

Use `.env.example` as a template.
Do not use sample database credentials or reuse secrets in production; provide deployment-specific values through the environment.

```env
OPENAI_API_KEY=your-openai-api-key-here
POSTGRES_USER=assessmentuser
POSTGRES_PASSWORD=assessmentpass123
POSTGRES_DB=assessment_db
DATABASE_URL=postgresql+psycopg://assessmentuser:assessmentpass123@postgres:5432/assessment_db
JWT_SECRET=your-secret-key-change-in-production
NEXT_PUBLIC_API_URL=http://localhost:8000
LOG_LEVEL=INFO
NODE_ENV=development
ENVIRONMENT=development
```

## Notes

- The backend project and source code live at the repository root.
- `frontend/` is intentionally a separate Git repository.
- Root `.gitignore` excludes the nested `frontend/` repository.

## Next Steps

1. Add Alembic migrations and wire API routes to database sessions.
2. Add OpenAI integration in grading and question-generation services.
3. Connect the frontend to persisted API endpoints.
4. Implement authentication and authorization.
5. Expand tests and prepare deployment.
