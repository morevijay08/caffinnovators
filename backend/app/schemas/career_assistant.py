from typing import Literal
from pydantic import BaseModel, Field, field_validator

class HistoryMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=2000)

    @field_validator("content")
    @classmethod
    def nonblank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Message cannot be blank.")
        return value

class AssistantRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    conversation_history: list[HistoryMessage] = Field(default_factory=list, max_length=10)

    @field_validator("message")
    @classmethod
    def nonblank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Message cannot be blank.")
        return value

class AssistantResponse(BaseModel):
    answer: str
    model: str
    disclaimer: str
