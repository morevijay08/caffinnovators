from pydantic import BaseModel, Field

class RoadmapYear(BaseModel):
    year: int = Field(ge=1)
    title: str
    focus: str
    activities: list[str] = Field(min_length=1)
    milestone: str

class CareerRoadmap(BaseModel):
    career_id: str
    career_title: str
    illustrative: bool = True
    duration_years: int = Field(ge=1)
    years: list[RoadmapYear] = Field(min_length=1)
    disclaimer: str
