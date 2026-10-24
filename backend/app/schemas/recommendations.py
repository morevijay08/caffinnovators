from pydantic import BaseModel, Field
from app.schemas.interest_assessment import Answer, InterestSignal

class RecommendationSubmission(BaseModel):
    answers: list[Answer] = Field(min_length=1, max_length=20)
    limit: int = Field(default=5, ge=1, le=12)

class RecommendationItem(BaseModel):
    career_id: str
    title: str
    cluster: str
    match_score: int = Field(ge=0, le=100)
    explanation: str
    matching_interests: list[str]
    suggested_steps: list[str]
    illustrative: bool

class RecommendationResult(BaseModel):
    recommendations: list[RecommendationItem]
    assessment_signals: list[InterestSignal]
    disclaimer: str
