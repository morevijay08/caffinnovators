from fastapi import APIRouter, HTTPException
from app.schemas.recommendations import RecommendationSubmission, RecommendationResult
from app.services.career_recommendations import recommend_from_answers

router = APIRouter(prefix="/api/v1/recommendations", tags=["recommendations"])

@router.post("", response_model=RecommendationResult)
def recommend(payload: RecommendationSubmission):
    try:
        return recommend_from_answers([answer.model_dump() for answer in payload.answers], payload.limit)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
