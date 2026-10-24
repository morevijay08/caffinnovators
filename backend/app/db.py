"""SQLite database configuration and session lifecycle for anonymous attempts."""
import os
from pathlib import Path
from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""

_DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "data" / "lifepath.db"
_DEFAULT_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{_DEFAULT_DB_PATH.as_posix()}")
_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=_connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

def init_db() -> None:
    """Create tables for the current MVP schema."""
    from app.models.assessment_attempt import AssessmentAttempt
    from app.models.student import Student, StudentSession, StudentJourney
    Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, None, None]:
    """Yield one request-scoped database session and always close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
