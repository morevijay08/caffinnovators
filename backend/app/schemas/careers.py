from pydantic import BaseModel, Field

class CareerSummary(BaseModel):
    id: str
    title: str
    cluster: str
    summary: str
    interest_tags: list[str]
    skill_tags: list[str]
    illustrative: bool = True

class CareerList(BaseModel):
    careers: list[CareerSummary]
    clusters: list[str]
    total: int = Field(ge=0)
