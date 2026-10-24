from pydantic import BaseModel, Field

class DiscoveryActivity(BaseModel):
    id: str
    title: str
    interest_tags: list[str]
    duration_minutes: int = Field(ge=1)
    materials: str
    instructions: list[str] = Field(min_length=1)
    reflection_prompt: str
    illustrative: bool = True

class DiscoveryActivityList(BaseModel):
    activities: list[DiscoveryActivity]
    total: int = Field(ge=0)
