

"""
LifePath India - Career Recommendation Engine

TASK-007:
Ranks careers based on the student's interest profile.

The scoring is deterministic and explainable.
"""


from data.careers import get_all_careers


def calculate_career_match(
    interest_profile: dict,
    career: dict,
) -> int:
    """
    Calculate how well a career matches the student's interests.

    The score is based on the average interest score
    of the career's required interest areas.

    Returns a score from 0 to 100.
    """

    interest_areas = career.get("interest_areas", [])

    if not interest_areas:
        return 0

    scores = [
        interest_profile.get(interest, 0)
        for interest in interest_areas
    ]

    return round(sum(scores) / len(scores))


def get_match_explanation(
    interest_profile: dict,
    career: dict,
) -> str:
    """
    Create a simple explanation for why a career matches.
    """

    interest_areas = career.get("interest_areas", [])

    matched_interests = [
        interest
        for interest in interest_areas
        if interest_profile.get(interest, 0) >= 60
    ]

    if not matched_interests:
        return "This career has a weaker match with your current interests."

    formatted = ", ".join(
        interest.replace("_", " ")
        for interest in matched_interests
    )

    return (
        f"This career matches your interests in {formatted}."
    )


def recommend_careers(
    interest_profile: dict,
    limit: int = 5,
) -> list:
    """
    Return the best matching careers.

    Each result contains:
    - career information
    - match score
    - explanation
    """

    recommendations = []

    for career in get_all_careers():

        score = calculate_career_match(
            interest_profile,
            career,
        )

        explanation = get_match_explanation(
            interest_profile,
            career,
        )

        recommendations.append(
            {
                "career": career,
                "match_score": score,
                "explanation": explanation,
            }
        )

    recommendations.sort(
        key=lambda item: item["match_score"],
        reverse=True,
    )

    return recommendations[:limit]