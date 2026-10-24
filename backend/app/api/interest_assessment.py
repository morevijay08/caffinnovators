from fastapi import APIRouter, HTTPException
from app.schemas.interest_assessment import Submission, QuestionList, ResultOut
from app.services.interest_assessment import public_questions, score_answers

router = APIRouter(prefix="/api/v1/interest-assessment", tags=["interest-assessment"])

@router.get("", response_model=QuestionList)
def get_questions():
    return {"questions": public_questions(), "duration_seconds": 360}

@router.post("/submit", response_model=ResultOut)
def submit_answers(submission: Submission):
    try:
        return score_answers([answer.model_dump() for answer in submission.answers])
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
