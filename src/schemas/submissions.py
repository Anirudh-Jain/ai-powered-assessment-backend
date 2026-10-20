from datetime import datetime

from pydantic import BaseModel


class SubmissionResponse(BaseModel):
    question_id: str
    answer: str


class SubmissionCreate(BaseModel):
    student_id: str
    exam_id: str
    responses: list[SubmissionResponse]


class Submission(BaseModel):
    id: str
    student_id: str
    exam_id: str
    submitted_at: datetime
    final_score: float | None = None
    status: str
