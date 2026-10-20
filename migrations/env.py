import os
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from dotenv import dotenv_values
from sqlalchemy import engine_from_config, pool

from src.db.base import Base
from src.db.url import normalize_database_url
from src.models import Exam, Question, Submission, SubmissionAnswer, User  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

dotenv_path = Path(".env")
file_database_url = (
    dotenv_values(dotenv_path).get("DATABASE_URL") if dotenv_path.exists() else None
)
database_url = (
    os.environ.get("DATABASE_URL")
    or file_database_url
    or config.get_main_option("sqlalchemy.url")
)
if not database_url:
    raise RuntimeError(
        "Set DATABASE_URL in the environment or .env before running migrations"
    )

config.set_main_option(
    "sqlalchemy.url", normalize_database_url(database_url).replace("%", "%%")
)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
