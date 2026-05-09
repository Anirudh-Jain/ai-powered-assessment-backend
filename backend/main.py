"""Single backend service for the AI Assessment Platform."""
import os
from datetime import datetime
from typing import List, Optional

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.config import settings

app = FastAPI(title=settings.API_TITLE, version=settings.API_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class UserRegister(BaseModel):
    email: str
    password: str
    full_name: str
    role: str  # "student" or "teacher"


class UserLogin(BaseModel):
    email: str
    password: str


class ExamCreate(BaseModel):
    title: str
    description: str
    duration_minutes: int
    total_questions: int
    pass_percentage: float
    created_by: str


class Exam(BaseModel):
    id: str
    title: str
    description: str
    duration_minutes: int
    total_questions: int
    pass_percentage: float
    created_by: str
    created_at: datetime


class Question(BaseModel):
    id: str
    exam_id: str
    question_text: str
    question_type: str
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    marks: int


class QuestionGenerateRequest(BaseModel):
    exam_id: str
    topic: str
    num_questions: int
    question_type: str
    difficulty: str


class SubmissionResponse(BaseModel):
    question_id: str
    answer: str


class SubmissionCreate(BaseModel):
    student_id: str
    exam_id: str
    responses: List[SubmissionResponse]


class Submission(BaseModel):
    id: str
    student_id: str
    exam_id: str
    submitted_at: datetime
    final_score: Optional[float] = None
    status: str


class GradeRequest(BaseModel):
    submission_id: str
    question_id: str
    student_answer: str
    correct_answer: str
    question_type: str


class Grade(BaseModel):
    submission_id: str
    question_id: str
    marks_obtained: int
    marks_total: int
    feedback: str
    graded_at: datetime


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "backend"}


@app.post("/register")
async def register(user: UserRegister):
    return {
        "access_token": "mock-token",
        "token_type": "bearer",
        "user_id": "mock-user-id",
    }


@app.post("/login")
async def login(credentials: UserLogin):
    return {
        "access_token": "mock-token",
        "token_type": "bearer",
        "user_id": "mock-user-id",
    }


@app.get("/validate")
async def validate_token(token: str):
    return {"valid": True, "user_id": "mock-user-id"}


@app.get("/exams", response_model=List[Exam])
async def list_exams():
    return []


@app.post("/exams", response_model=Exam)
async def create_exam(exam: ExamCreate):
    return {
        "id": "mock-exam-id",
        "title": exam.title,
        "description": exam.description,
        "duration_minutes": exam.duration_minutes,
        "total_questions": exam.total_questions,
        "pass_percentage": exam.pass_percentage,
        "created_by": exam.created_by,
        "created_at": datetime.now(),
    }


@app.get("/exams/{exam_id}", response_model=Exam)
async def get_exam(exam_id: str):
    return {
        "id": exam_id,
        "title": "Sample Exam",
        "description": "Example exam description",
        "duration_minutes": 60,
        "total_questions": 10,
        "pass_percentage": 60.0,
        "created_by": "teacher-id",
        "created_at": datetime.now(),
    }


@app.get("/questions", response_model=List[Question])
async def list_questions(exam_id: Optional[str] = None):
    return []


@app.post("/questions", response_model=Question)
async def create_question(question: Question):
    return question


@app.post("/questions/generate", response_model=List[Question])
async def generate_questions(params: QuestionGenerateRequest):
    return []


@app.post("/submissions", response_model=Submission)
async def create_submission(submission: SubmissionCreate):
    return {
        "id": "mock-submission-id",
        "student_id": submission.student_id,
        "exam_id": submission.exam_id,
        "submitted_at": datetime.now(),
        "final_score": None,
        "status": "submitted",
    }


@app.get("/submissions", response_model=List[Submission])
async def list_submissions(student_id: Optional[str] = None):
    return []


@app.get("/submissions/{submission_id}", response_model=Submission)
async def get_submission(submission_id: str):
    return {
        "id": submission_id,
        "student_id": "student-id",
        "exam_id": "exam-id",
        "submitted_at": datetime.now(),
        "final_score": None,
        "status": "submitted",
    }


@app.post("/grade", response_model=Grade)
async def grade_submission(request: GradeRequest):
    return {
        "submission_id": request.submission_id,
        "question_id": request.question_id,
        "marks_obtained": 0,
        "marks_total": 1,
        "feedback": "Feedback generated by AI",
        "graded_at": datetime.now(),
    }


@app.get("/grades/{submission_id}")
async def get_submission_grades(submission_id: str):
    return {"submission_id": submission_id, "grades": []}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
