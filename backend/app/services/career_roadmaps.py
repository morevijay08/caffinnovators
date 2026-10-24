"""Illustrative four-year exploration roadmaps, not formal credentials or guarantees.

Each career's plan is generated from its own catalogue skills and interests.
Year labels are fictional learning stages, not a mandatory age, degree, or timeline.
"""
from app.services.career_catalogue import get_career

PROJECT_IDEAS = {
    "software-developer": ("Make a simple interactive web page.", "Build a small useful app for a friend or community."),
    "robotics-technician": ("Explore a simple sensor or safe robotics simulation.", "Document a prototype that solves a small everyday problem."),
    "product-designer": ("Redesign an everyday object on paper.", "Test a clickable prototype with volunteers."),
    "illustrator": ("Draw a visual story in four scenes.", "Create a small portfolio of illustrated stories."),
    "research-scientist": ("Record observations and ask a testable question.", "Share a mini research poster with clear limitations."),
    "environmental-specialist": ("Map a local environmental question using observations.", "Present a small awareness or conservation idea."),
    "entrepreneur": ("Interview people about a problem they notice.", "Prototype a fictional product and get constructive feedback."),
    "community-organizer": ("Listen to different perspectives on a local issue.", "Plan a small voluntary community activity."),
    "science-writer": ("Explain a science concept in everyday words.", "Publish an illustrated explainer using checked sources."),
    "sports-coach": ("Design an enjoyable beginner practice activity.", "Reflect on a small inclusive practice session."),
    "data-analyst": ("Explore patterns in a public sample dataset.", "Make a clear chart with a short explanation of uncertainty."),
    "content-creator": ("Storyboard a short educational video.", "Create and review a small collection of helpful media."),
}

DISCLAIMER = (
    "This four-year pathway is an illustrative exploration example, not a required "
    "qualification, fixed timeline, admission rule, employment promise or career prediction. "
    "You can explore, learn and change direction at any stage."
)


def get_career_roadmap(career_id: str) -> dict | None:
    career = get_career(career_id)
    if career is None:
        return None
    first_project, second_project = PROJECT_IDEAS[career_id]
    interests = [tag.replace("_", " ") for tag in career["interest_tags"]]
    skills = [tag.replace("-", " ") for tag in career["skill_tags"]]
    steps = [
        {
            "year": 1,
            "title": "Discover the foundations",
            "focus": f"Explore {interests[0]} and what a {career['title'].lower()} might do.",
            "activities": [
                f"Try a beginner activity related to {interests[0]}.",
                f"Practise {skills[0]} with a small, low-pressure challenge.",
            ],
            "milestone": first_project,
        },
        {
            "year": 2,
            "title": "Build and experiment",
            "focus": f"Connect {interests[1]} with {skills[1]}.",
            "activities": [
                f"Practice {skills[1]} in a team or personal project.",
                "Ask for feedback and record what you enjoyed and found difficult.",
            ],
            "milestone": "Keep a short learning journal or portfolio of experiments.",
        },
        {
            "year": 3,
            "title": "Create and collaborate",
            "focus": f"Use {skills[2]} to share ideas and work with others.",
            "activities": [
                f"Explore how {interests[2]} connects to this career.",
                "Learn from a mentor, teacher, interview or accessible educational resource.",
            ],
            "milestone": second_project,
        },
        {
            "year": 4,
            "title": "Reflect and explore next options",
            "focus": "Review your interests, skills and possible next steps without locking into one path.",
            "activities": [
                "Choose one skill you would like to practise further.",
                "Compare different learning routes and verify real requirements with official sources when needed.",
            ],
            "milestone": "Make a flexible next-step plan with at least two options.",
        },
    ]
    return {
        "career_id": career_id,
        "career_title": career["title"],
        "illustrative": True,
        "duration_years": len(steps),
        "years": steps,
        "disclaimer": DISCLAIMER,
    }
