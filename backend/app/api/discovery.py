from fastapi import APIRouter, Query
from app.data.discovery_activities import get_activities
from app.schemas.discovery import DiscoveryActivityList

router = APIRouter(prefix="/api/v1/discovery-activities", tags=["discovery"])

@router.get("", response_model=DiscoveryActivityList)
def list_discovery_activities(interest: str = Query(default="", max_length=40)):
    activities = get_activities(interest)
    return {"activities": activities, "total": len(activities)}
