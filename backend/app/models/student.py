"""Pseudonymous student accounts, opaque sessions and saved journey state."""
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Student(Base):
    __tablename__ = "students"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    username: Mapped[str] = mapped_column(String(40), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[str] = mapped_column(String(40), nullable=False)

class StudentSession(Base):
    __tablename__ = "student_sessions"
    token_hash: Mapped[str] = mapped_column(String(64), primary_key=True)
    student_id: Mapped[str] = mapped_column(String(36), ForeignKey("students.id"), nullable=False, index=True)
    expires_at: Mapped[int] = mapped_column(Integer, nullable=False)

class StudentJourney(Base):
    __tablename__ = "student_journeys"
    student_id: Mapped[str] = mapped_column(String(36), ForeignKey("students.id"), primary_key=True)
    profile_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    assessment_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    selected_career_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    path_history_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    reflections_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    chat_history_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    math_result_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    comparison_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
