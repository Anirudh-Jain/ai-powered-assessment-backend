from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import (
    JSON,
    CheckConstraint,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base

if TYPE_CHECKING:
    from src.models.exam import Exam
    from src.models.submission import SubmissionAnswer


class Question(Base):
    __tablename__ = "questions"
    __table_args__ = (
        CheckConstraint("question_order > 0", name="ck_questions_order_positive"),
        CheckConstraint("marks >= 0", name="ck_questions_marks_nonnegative"),
        UniqueConstraint("exam_id", "question_order", name="uq_questions_exam_order"),
    )

    id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4())
    )
    exam_id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), ForeignKey("exams.id", ondelete="CASCADE"), index=True
    )
    question_text: Mapped[str] = mapped_column(Text)
    question_type: Mapped[str] = mapped_column(String(40))
    options: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
    correct_answer: Mapped[str | None] = mapped_column(Text, nullable=True)
    marks: Mapped[int] = mapped_column(Integer)
    question_order: Mapped[int] = mapped_column(Integer)

    exam: Mapped["Exam"] = relationship(back_populates="questions")
    answers: Mapped[list["SubmissionAnswer"]] = relationship(back_populates="question")
