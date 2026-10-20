import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.db.base import Base
from src.models import Exam, Question, Submission, SubmissionAnswer, User


@pytest.fixture
def db_session():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()


def test_assessment_entities_persist_and_load_relationships(db_session: Session):
    teacher = User(
        email="teacher@example.com",
        password_hash="hashed-password",
        full_name="Teacher One",
        role="teacher",
    )
    student = User(
        email="student@example.com",
        password_hash="hashed-password",
        full_name="Student One",
        role="student",
    )
    exam = Exam(
        title="Algebra",
        description="Linear equations",
        duration_minutes=45,
        total_questions=1,
        pass_percentage=60,
        creator=teacher,
    )
    question = Question(
        question_text="Solve 2x = 8",
        question_type="short_answer",
        options=None,
        correct_answer="4",
        marks=2,
        question_order=1,
    )
    exam.questions.append(question)
    submission = Submission(student=student, exam=exam)
    submission.answers.append(
        SubmissionAnswer(
            question=question, answer="4", marks_obtained=2, feedback="Correct"
        )
    )

    db_session.add_all([teacher, student, exam, submission])
    db_session.commit()

    saved_exam = db_session.scalar(select(Exam).where(Exam.title == "Algebra"))
    assert saved_exam is not None
    assert saved_exam.creator.email == "teacher@example.com"
    assert saved_exam.questions[0].question_text == "Solve 2x = 8"
    assert saved_exam.submissions[0].answers[0].marks_obtained == 2
