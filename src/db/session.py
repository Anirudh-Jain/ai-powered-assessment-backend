from collections.abc import Iterator
from functools import lru_cache

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.config import settings


@lru_cache(maxsize=1)
def get_engine() -> Engine:
    return create_engine(settings.DATABASE_URL, pool_pre_ping=True)


@lru_cache(maxsize=1)
def get_session_factory() -> sessionmaker[Session]:
    return sessionmaker(
        bind=get_engine(),
        autoflush=False,
        expire_on_commit=False,
    )


def get_db() -> Iterator[Session]:
    with get_session_factory() as session:
        yield session
