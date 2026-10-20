from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    Uuid,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base

if TYPE_CHECKING:
    from src.models.exam import Exam
    from src.models.question import Question
    from src.models.user import User


class Submission(Base):
    __tablename__ = "submissions"
    __table_args__ = (
        CheckConstraint(
            "final_score IS NULL OR final_score >= 0",
            name="ck_submissions_score_nonnegative",
        ),
    )

    id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4())
    )
    student_id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), ForeignKey("users.id", ondelete="RESTRICT"), index=True
    )
    exam_id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), ForeignKey("exams.id", ondelete="RESTRICT"), index=True
    )
    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    final_score: Mapped[float | None] = mapped_column(Numeric(7, 2), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="submitted")

    student: Mapped["User"] = relationship(back_populates="submissions")
    exam: Mapped["Exam"] = relationship(back_populates="submissions")
    answers: Mapped[list["SubmissionAnswer"]] = relationship(
        back_populates="submission",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class SubmissionAnswer(Base):
    __tablename__ = "submission_answers"
    __table_args__ = (
        CheckConstraint(
            "marks_obtained IS NULL OR marks_obtained >= 0",
            name="ck_answers_marks_nonnegative",
        ),
        UniqueConstraint(
            "submission_id", "question_id", name="uq_answers_submission_question"
        ),
    )

    id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4())
    )
    submission_id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False),
        ForeignKey("submissions.id", ondelete="CASCADE"),
        index=True,
    )
    question_id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), ForeignKey("questions.id", ondelete="RESTRICT"), index=True
    )
    answer: Mapped[str] = mapped_column(Text)
    marks_obtained: Mapped[float | None] = mapped_column(Numeric(7, 2), nullable=True)
    feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
    graded_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    submission: Mapped["Submission"] = relationship(back_populates="answers")
    question: Mapped["Question"] = relationship(back_populates="answers")
