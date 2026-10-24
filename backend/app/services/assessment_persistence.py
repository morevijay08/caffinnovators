"""Persistence helpers for anonymous math assessment result snapshots."""
import json
from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.assessment_attempt import AssessmentAttempt
from app.schemas.math_readiness import MathAssessmentResult


def save_attempt(db: Session, result: MathAssessmentResult) -> MathAssessmentResult:
    """Persist a calculated result and return it with its generated attempt ID."""
    attempt_id = str(uuid4())
    created_at = datetime.now(timezone.utc).isoformat()
    record = AssessmentAttempt(
        attempt_id=attempt_id,
        assessment_id=result.assessment_id,
        total_questions=result.total_questions,
        answered_questions=result.answered_questions,
        correct_answers=result.correct_answers,
        incorrect_or_unanswered=result.incorrect_or_unanswered,
        percentage=result.percentage,
        elapsed_seconds=result.elapsed_seconds,
        time_limit_seconds=result.time_limit_seconds,
        time_limit_exceeded=result.time_limit_exceeded,
        topic_breakdown_json=json.dumps(
            [topic.model_dump() for topic in result.topic_breakdown],
            separators=(",", ":"),
        ),
        encouragement=result.encouragement,
        disclaimer=result.disclaimer,
        created_at=created_at,
    )
    try:
        db.add(record)
        db.commit()
    except Exception:
        db.rollback()
        raise
    return result.model_copy(update={"attempt_id": attempt_id})


def get_attempt(db: Session, attempt_id: str) -> MathAssessmentResult | None:
    """Load a saved result snapshot without answer-by-answer data."""
    record = db.get(AssessmentAttempt, attempt_id)
    if record is None:
        return None
    return MathAssessmentResult(
        attempt_id=record.attempt_id,
        assessment_id=record.assessment_id,
        total_questions=record.total_questions,
        answered_questions=record.answered_questions,
        correct_answers=record.correct_answers,
        incorrect_or_unanswered=record.incorrect_or_unanswered,
        percentage=record.percentage,
        elapsed_seconds=record.elapsed_seconds,
        time_limit_seconds=record.time_limit_seconds,
        time_limit_exceeded=record.time_limit_exceeded,
        topic_breakdown=json.loads(record.topic_breakdown_json),
        encouragement=record.encouragement,
        disclaimer=record.disclaimer,
    )
