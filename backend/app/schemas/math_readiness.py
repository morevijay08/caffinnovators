"""Pydantic request/response models for the math readiness API."""
from pydantic import BaseModel, Field


class MathOptionPublic(BaseModel):
    id: str
    text: str


class MathQuestionPublic(BaseModel):
    id: str
    prompt: str
    topic: str
    topic_label: str
    options: list[MathOptionPublic]


class MathAssessmentPublic(BaseModel):
    assessment_id: str
    title: str
    duration_seconds: int
    question_count: int
    questions: list[MathQuestionPublic]
    illustrative: bool = True


class MathAnswerSubmission(BaseModel):
    question_id: str = Field(min_length=1, max_length=80)
    option_id: str = Field(min_length=1, max_length=20)


class MathAssessmentSubmitRequest(BaseModel):
    answers: list[MathAnswerSubmission] = Field(min_length=1, max_length=50)
    # Client-reported duration is informational for the MVP, not a trusted clock.
    elapsed_seconds: int = Field(default=0, ge=0, le=3600)


class TopicScore(BaseModel):
    topic: str
    topic_label: str
    correct: int
    total: int
    percentage: int


class MathAssessmentResult(BaseModel):
    attempt_id: str | None = None
    assessment_id: str
    total_questions: int
    answered_questions: int
    correct_answers: int
    incorrect_or_unanswered: int
    percentage: int
    elapsed_seconds: int
    time_limit_seconds: int
    time_limit_exceeded: bool
    topic_breakdown: list[TopicScore]
    encouragement: str
    disclaimer: str = "This short practice quiz is for learning guidance, not a diagnosis or a measure of fixed ability."
