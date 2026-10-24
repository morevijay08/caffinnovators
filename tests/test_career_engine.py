from services.career_engine import (
    calculate_career_match,
    get_match_explanation,
    recommend_careers,
)


def test_calculate_career_match():

    profile = {
        "technology": 100,
        "problem_solving": 80,
        "science": 60,
    }

    career = {
        "interest_areas": [
            "technology",
            "problem_solving",
            "science",
        ]
    }

    score = calculate_career_match(
        profile,
        career,
    )

    assert score == 80


def test_calculate_career_match_with_missing_interest():

    profile = {
        "technology": 100,
    }

    career = {
        "interest_areas": [
            "technology",
            "problem_solving",
        ]
    }

    score = calculate_career_match(
        profile,
        career,
    )

    assert score == 50


def test_match_explanation():

    profile = {
        "technology": 100,
        "problem_solving": 80,
        "science": 20,
    }

    career = {
        "interest_areas": [
            "technology",
            "problem_solving",
            "science",
        ]
    }

    explanation = get_match_explanation(
        profile,
        career,
    )

    assert "technology" in explanation
    assert "problem solving" in explanation


def test_recommend_careers():

    profile = {
        "technology": 100,
        "problem_solving": 100,
        "creative": 20,
        "business": 20,
        "social": 20,
        "science": 100,
        "communication": 20,
    }

    recommendations = recommend_careers(profile)

    assert len(recommendations) == 5

    assert recommendations[0]["match_score"] >= (
        recommendations[-1]["match_score"]
    )


def test_recommendation_contains_required_fields():

    profile = {
        "technology": 100,
        "problem_solving": 80,
        "science": 80,
    }

    recommendations = recommend_careers(profile, limit=3)

    for recommendation in recommendations:
        assert "career" in recommendation
        assert "match_score" in recommendation
        assert "explanation" in recommendation