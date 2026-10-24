
"""FastAPI routes for math readiness and anonymous attempt history."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.math_readiness import (
    MathAssessmentPublic,
    MathAssessmentResult,
    MathAssessmentSubmitRequest,
)
from app.services.assessment_persistence import get_attempt, save_attempt
from app.services.math_readiness import (
    AssessmentSubmissionError,
    get_public_assessment,
    score_submission,
)

router = APIRouter(prefix="/api/v1/math-assessment", tags=["math-assessment"])


@router.get("", response_model=MathAssessmentPublic)
def read_math_assessment() -> MathAssessmentPublic:
    """Return public question text/options, never answer keys."""
    return get_public_assessment()


@router.post("/submit", response_model=MathAssessmentResult)
def submit_math_assessment(
    payload: MathAssessmentSubmitRequest,
    db: Session = Depends(get_db),
) -> MathAssessmentResult:
    """Score answers on the server and persist the result snapshot."""
    try:
        result = score_submission(payload)
    except AssessmentSubmissionError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    try:
        return save_attempt(db, result)
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=503,
            detail="Assessment result could not be saved. Please try again.",
        ) from exc


@router.get("/attempts/{attempt_id}", response_model=MathAssessmentResult)
def read_assessment_attempt(
    attempt_id: UUID,
    db: Session = Depends(get_db),
) -> MathAssessmentResult:
    """Return a previously saved anonymous result snapshot."""
    try:
        result = get_attempt(db, str(attempt_id))
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=503,
            detail="Assessment history is temporarily unavailable.",
        ) from exc

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Assessment attempt not found.",
        )

    return result
