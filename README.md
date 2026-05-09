# AI Assessment Backend Repository

This repository contains the single backend service for the AI Powered Assessment & Examination Platform.

The frontend is stored in a separate repository under `frontend/`.

## Repository Layout

```
backend/              # FastAPI backend service
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
cd c:\Users\Admin\Project
copy .env.example .env
```

Edit `.env` and add your OpenAI API key.

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

## Environment Variables

Use `.env.example` as a template.

```env
OPENAI_API_KEY=your-openai-api-key-here
POSTGRES_USER=assessmentuser
POSTGRES_PASSWORD=assessmentpass123
POSTGRES_DB=assessment_db
DATABASE_URL=postgresql://assessmentuser:assessmentpass123@postgres:5432/assessment_db
JWT_SECRET=your-secret-key-change-in-production
NEXT_PUBLIC_API_URL=http://localhost:8000
LOG_LEVEL=INFO
NODE_ENV=development
ENVIRONMENT=development
```

## Notes

- `backend/` is the main backend repository.
- `frontend/` is intentionally a separate Git repository.
- Root `.gitignore` excludes the nested `frontend/` repository.

## Next Steps

1. Implement backend database models and CRUD logic.
2. Add OpenAI integration in backend grading/question routes.
3. Connect frontend to the backend API.
4. Add authentication and authorization.
5. Write tests and deploy.
