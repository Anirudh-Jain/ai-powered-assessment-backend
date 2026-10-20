from pydantic import BaseModel


class Question(BaseModel):
    id: str
    exam_id: str
    question_text: str
    question_type: str
    options: list[str] | None = None
    correct_answer: str | None = None
    marks: int


class QuestionGenerateRequest(BaseModel):
    exam_id: str
    topic: str
    num_questions: int
    question_type: str
    difficulty: str
