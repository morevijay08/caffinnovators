"""Pure catalogue operations; no recommendations or roadmap claims."""
from app.data.careers import get_all_careers

def list_careers(search: str = "", cluster: str = "") -> list[dict]:
    records = get_all_careers()
    needle = search.strip().casefold()
    selected_cluster = cluster.strip().casefold()
    return [career for career in records
            if (not selected_cluster or career["cluster"] == selected_cluster)
            and (not needle or needle in " ".join([
                career["title"], career["summary"], *career["interest_tags"], *career["skill_tags"]
            ]).casefold())]

def get_career(career_id: str) -> dict | None:
    return next((career for career in get_all_careers() if career["id"] == career_id), None)

def get_clusters() -> list[str]:
    return sorted({career["cluster"] for career in get_all_careers()})
