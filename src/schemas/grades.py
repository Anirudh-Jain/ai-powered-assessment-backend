from datetime import datetime

from pydantic import BaseModel


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
