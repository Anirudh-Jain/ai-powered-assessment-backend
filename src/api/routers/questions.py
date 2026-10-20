from fastapi import APIRouter

from src.schemas.questions import Question, QuestionGenerateRequest

router = APIRouter()


@router.get("/questions", response_model=list[Question])
async def list_questions(exam_id: str | None = None):
    return []


@router.post("/questions", response_model=Question)
async def create_question(question: Question):
    return question


@router.post("/questions/generate", response_model=list[Question])
async def generate_questions(params: QuestionGenerateRequest):
    return []
