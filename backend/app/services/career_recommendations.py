"""TASK-007: deterministic, explainable career ranking from server-scored answers."""
from app.services.career_catalogue import list_careers
from app.services.interest_assessment import score_answers

def recommend_from_answers(answers: list[dict], limit: int = 5) -> dict:
    assessment = score_answers(answers)  # Do not trust client-supplied scores.
    strengths = {signal["interest"]: signal["score"] for signal in assessment["signals"]}
    ranked = []
    for career in list_careers():
        tags = career["interest_tags"]
        contributions = [(tag, strengths.get(tag, 0)) for tag in tags]
        score = round(sum(value for _, value in contributions) / len(tags)) if tags else 0
        matched = sorted(((tag, value) for tag, value in contributions if value > 0), key=lambda x: (-x[1], x[0]))
        if matched:
            friendly = ", ".join(tag.replace("_", " ") for tag, _ in matched[:3])
            explanation = f"Your selected activities suggested interest in {friendly}, which connects with this career."
        else:
            explanation = "Your answers did not directly highlight this career's interest areas; you can still explore it."
        ranked.append({
            "career_id": career["id"], "title": career["title"], "cluster": career["cluster"],
            "match_score": score, "explanation": explanation,
            "matching_interests": [tag for tag, _ in matched],
            "suggested_steps": [
                f"Explore the illustrative {career['title']} profile.",
                "Try a beginner activity related to one of its skills.",
            ],
            "illustrative": True,
        })
    ranked.sort(key=lambda item: (-item["match_score"], item["career_id"]))
    return {"recommendations": ranked[:limit],
            "assessment_signals": assessment["signals"],
            "disclaimer": "These heuristic scores describe overlap with a short interest activity, not aptitude, probability, or career suitability. Every path remains open."}
