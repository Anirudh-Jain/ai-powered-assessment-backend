from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import CheckConstraint, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base

if TYPE_CHECKING:
    from src.models.exam import Exam
    from src.models.submission import Submission


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("role IN ('student', 'teacher')", name="ck_users_role"),
    )

    id: Mapped[str] = mapped_column(
        Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4())
    )
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(200))
    role: Mapped[str] = mapped_column(String(20))

    exams: Mapped[list["Exam"]] = relationship(back_populates="creator")
    submissions: Mapped[list["Submission"]] = relationship(back_populates="student")
