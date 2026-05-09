"""API Gateway service for AI Assessment Platform."""
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="API Gateway", version="0.1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Service URLs (from environment variables or defaults)
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth:8001")
EXAM_SERVICE_URL = os.getenv("EXAM_SERVICE_URL", "http://exam:8002")
QUESTION_SERVICE_URL = os.getenv("QUESTION_SERVICE_URL", "http://question:8003")
GRADING_SERVICE_URL = os.getenv("GRADING_SERVICE_URL", "http://grading:8004")
SUBMISSION_SERVICE_URL = os.getenv("SUBMISSION_SERVICE_URL", "http://submission:8005")

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "api-gateway"}

# Routes to auth service
@app.post("/api/auth/register")
async def register(user_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/register", json=user_data)
        return response.json()

@app.post("/api/auth/login")
async def login(credentials: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/login", json=credentials)
        return response.json()

# Routes to exam service
@app.get("/api/exams")
async def list_exams():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EXAM_SERVICE_URL}/exams")
        return response.json()

@app.post("/api/exams")
async def create_exam(exam_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{EXAM_SERVICE_URL}/exams", json=exam_data)
        return response.json()

# Routes to question service
@app.get("/api/questions")
async def list_questions(exam_id: str = None):
    async with httpx.AsyncClient() as client:
        params = {"exam_id": exam_id} if exam_id else {}
        response = await client.get(f"{QUESTION_SERVICE_URL}/questions", params=params)
        return response.json()

@app.post("/api/questions/generate")
async def generate_questions(params: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{QUESTION_SERVICE_URL}/generate", json=params)
        return response.json()

# Routes to grading service
@app.post("/api/grade")
async def grade_submission(submission_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{GRADING_SERVICE_URL}/grade", json=submission_data)
        return response.json()

# Routes to submission service
@app.get("/api/submissions")
async def list_submissions(student_id: str = None):
    async with httpx.AsyncClient() as client:
        params = {"student_id": student_id} if student_id else {}
        response = await client.get(f"{SUBMISSION_SERVICE_URL}/submissions", params=params)
        return response.json()

@app.post("/api/submissions")
async def submit_exam(submission_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{SUBMISSION_SERVICE_URL}/submissions", json=submission_data)
        return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
