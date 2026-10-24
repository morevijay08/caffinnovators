from pydantic import BaseModel, Field

class Answer(BaseModel):
    question_id: str
    option_id: str

class Submission(BaseModel):
    answers: list[Answer] = Field(min_length=1, max_length=20)

class OptionOut(BaseModel):
    id: str
    text: str

class QuestionOut(BaseModel):
    id: str
    prompt: str
    options: list[OptionOut]

class QuestionList(BaseModel):
    questions: list[QuestionOut]
    duration_seconds: int

class InterestSignal(BaseModel):
    interest: str
    score: int
    evidence: str

class ResultOut(BaseModel):
    signals: list[InterestSignal]
    top_interests: list[str]
    disclaimer: str
