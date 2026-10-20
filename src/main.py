"""FastAPI application setup."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers import auth, exams, grades, health, questions, submissions
from src.config import settings

app = FastAPI(title=settings.API_TITLE, version=settings.API_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(exams.router)
app.include_router(questions.router)
app.include_router(submissions.router)
app.include_router(grades.router)
