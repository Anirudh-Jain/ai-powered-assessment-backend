from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import CheckConstraint, ForeignKey, Integer, Numeric, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base

if TYPE_CHECKING:
    from src.models.question import Question
    from src.models.submission import Submission
    from src.models.user import User


class Exam(Base):
    __tablename__ = "exams"
    __table_args__ = (
        CheckConstraint("duration_minutes > 0", name="ck_exams_duration_positive"),
        CheckConstraint("total_questions > 0", name="ck_exams_questions_positive"),
        CheckConstraint("pass_percentage BETWEEN 0 AND 100", name="ck_exams_pass_percentage"),
    )

    id: Mapped[str] = mapped_column(Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4()))
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    duration_minutes: Mapped[int] = mapped_column(Integer)
    total_questions: Mapped[int] = mapped_column(Integer)
    pass_percentage: Mapped[float] = mapped_column(Numeric(5, 2))
    created_by: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), ForeignKey("users.id", ondelete="RESTRICT"), index=True
    )

    creator: Mapped["User"] = relationship(back_populates="exams")
    questions: Mapped[list["Question"]] = relationship(
        back_populates="exam",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    submissions: Mapped[list["Submission"]] = relationship(back_populates="exam")