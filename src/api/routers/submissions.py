from datetime import datetime

from fastapi import APIRouter

from src.schemas.submissions import Submission, SubmissionCreate

router = APIRouter()


@router.post("/submissions", response_model=Submission)
async def create_submission(submission: SubmissionCreate):
    return {
        "id": "mock-submission-id",
        "student_id": submission.student_id,
        "exam_id": submission.exam_id,
        "submitted_at": datetime.now(),
        "final_score": None,
        "status": "submitted",
    }


@router.get("/submissions", response_model=list[Submission])
async def list_submissions(student_id: str | None = None):
    return []


@router.get("/submissions/{submission_id}", response_model=Submission)
async def get_submission(submission_id: str):
    return {
        "id": submission_id,
        "student_id": "student-id",
        "exam_id": "exam-id",
        "submitted_at": datetime.now(),
        "final_score": None,
        "status": "submitted",
    }
