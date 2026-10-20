from datetime import datetime

from fastapi import APIRouter

from src.schemas.exams import Exam, ExamCreate

router = APIRouter()


@router.get("/exams", response_model=list[Exam])
async def list_exams():
    return []


@router.post("/exams", response_model=Exam)
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


@router.get("/exams/{exam_id}", response_model=Exam)
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
