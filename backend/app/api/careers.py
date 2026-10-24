from fastapi import APIRouter, HTTPException, Query
from app.schemas.careers import CareerList, CareerSummary
from app.schemas.roadmaps import CareerRoadmap
from app.services.career_roadmaps import get_career_roadmap
from app.services.career_catalogue import get_career, get_clusters, list_careers

router = APIRouter(prefix="/api/v1/careers", tags=["careers"])

@router.get("", response_model=CareerList)
def careers(search: str = Query(default="", max_length=100), cluster: str = Query(default="", max_length=60)):
    items = list_careers(search=search, cluster=cluster)
    return {"careers": items, "clusters": get_clusters(), "total": len(items)}

@router.get("/{career_id}", response_model=CareerSummary)
def career(career_id: str):
    item = get_career(career_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Career not found in the illustrative catalogue.")
    return item

@router.get("/{career_id}/roadmap", response_model=CareerRoadmap)
def career_roadmap(career_id: str):
    roadmap = get_career_roadmap(career_id)
    if roadmap is None:
        raise HTTPException(status_code=404, detail="Career roadmap not found in the illustrative catalogue.")
    return roadmap
