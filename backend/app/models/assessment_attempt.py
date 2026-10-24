"""Database model for non-identifying math assessment result snapshots."""
from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class AssessmentAttempt(Base):
    """Persist a server-calculated result without storing submitted answer choices."""

    __tablename__ = "assessment_attempts"

    attempt_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    assessment_id: Mapped[str] = mapped_column(String(80), nullable=False, index=True)
    total_questions: Mapped[int] = mapped_column(Integer, nullable=False)
    answered_questions: Mapped[int] = mapped_column(Integer, nullable=False)
    correct_answers: Mapped[int] = mapped_column(Integer, nullable=False)
    incorrect_or_unanswered: Mapped[int] = mapped_column(Integer, nullable=False)
    percentage: Mapped[int] = mapped_column(Integer, nullable=False)
    elapsed_seconds: Mapped[int] = mapped_column(Integer, nullable=False)
    time_limit_seconds: Mapped[int] = mapped_column(Integer, nullable=False)
    time_limit_exceeded: Mapped[bool] = mapped_column(Boolean, nullable=False)
    topic_breakdown_json: Mapped[str] = mapped_column(Text, nullable=False)
    encouragement: Mapped[str] = mapped_column(Text, nullable=False)
    disclaimer: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[str] = mapped_column(String(40), nullable=False, index=True)
