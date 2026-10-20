from datetime import datetime

from pydantic import BaseModel


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
