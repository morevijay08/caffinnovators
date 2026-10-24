"""FastAPI router for the math readiness assessment (TASK-009)."""
from fastapi import APIRouter, HTTPException

from backend.app.schemas.math_readiness import (
    MathAssessmentPublic,
    MathAssessmentResult,
    MathAssessmentSubmitRequest,
)
from backend.app.services.math_readiness import (
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
def submit_math_assessment(payload: MathAssessmentSubmitRequest) -> MathAssessmentResult:
    """Score submitted answers using the server-side question bank."""
    try:
        return score_submission(payload)
    except AssessmentSubmissionError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
