from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect


def test_migrations_upgrade_and_downgrade(tmp_path, monkeypatch):
    database_path = (tmp_path / "migration-test.db").as_posix()
    database_url = f"sqlite:///{database_path}"
    monkeypatch.setenv("DATABASE_URL", database_url)
    config = Config("alembic.ini")

    command.upgrade(config, "head")

    engine = create_engine(database_url)
    assert {
        "users",
        "exams",
        "questions",
        "submissions",
        "submission_answers",
        "alembic_version",
    } <= set(inspect(engine).get_table_names())

    command.downgrade(config, "base")

    assert inspect(engine).get_table_names() == ["alembic_version"]
    engine.dispose()
