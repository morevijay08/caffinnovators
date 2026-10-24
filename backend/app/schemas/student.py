"""Strict, bounded input contracts for pseudonymous student profiles."""
from typing import Literal
from pydantic import BaseModel, Field, field_validator

class Credentials(BaseModel):
    username: str = Field(min_length=3, max_length=40, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(min_length=10, max_length=128)

    @field_validator("username")
    @classmethod
    def normalize(cls, value: str) -> str:
        return value.strip().lower()

class StudentIdentity(BaseModel):
    id: str
    username: str

class Profile(BaseModel):
    educationLevel: Literal["Class 8","Class 9","Class 10","Class 11","Class 12","Diploma","College"]
    interests: list[str] = Field(max_length=12)
    favoriteSubjects: list[str] = Field(max_length=12)
    goal: Literal["Explore career options","Discover what interests me","I have a career in mind","Improve my subject skills"]
    careerIdea: str = Field(max_length=100)

class Answer(BaseModel):
    question_id: str = Field(max_length=80)
    option_id: str = Field(max_length=80)

class Signal(BaseModel):
    interest: str = Field(max_length=80)
    score: float = Field(ge=0, le=100)
    evidence: str = Field(max_length=500)

class Assessment(BaseModel):
    answers: list[Answer] = Field(max_length=30)
    signals: list[Signal] = Field(max_length=30)

class PathChange(BaseModel):
    careerId: str = Field(max_length=100)
    changedAt: str = Field(max_length=50)

class ChatMessage(BaseModel):
    role: Literal["user","assistant"]
    content: str = Field(min_length=1, max_length=2000)

class JourneyData(BaseModel):
    profile: Profile | None = None
    assessment: Assessment | None = None
    selectedCareerId: str | None = Field(default=None, max_length=100)
    pathHistory: list[PathChange] = Field(default_factory=list, max_length=100)
    reflections: dict[str, str] = Field(default_factory=dict)
    chatHistory: list[ChatMessage] = Field(default_factory=list, max_length=20)

    @field_validator("reflections")
    @classmethod
    def bounded_reflections(cls, data: dict[str,str]) -> dict[str,str]:
        if len(data) > 50 or any(len(k)>100 or len(v)>800 for k,v in data.items()):
            raise ValueError("Too many or oversized reflections.")
        return data

class JourneyPatch(BaseModel):
    # One change per call prevents accidentally clearing concurrently updated fields.
    field: Literal["profile","assessment","selectedCareerId","pathHistory","reflections","chatHistory"]
    value: object
