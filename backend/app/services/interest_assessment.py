"""Deterministic interest signals. No career ranking or psychological diagnosis."""
from collections import Counter
from app.data.interest_questions import QUESTIONS

def public_questions():
    return [{"id": q["id"], "prompt": q["prompt"],
             "options": [{"id": o["id"], "text": o["text"]} for o in q["options"]]}
            for q in QUESTIONS]

def score_answers(answers: list[dict]) -> dict:
    known = {q["id"]: q for q in QUESTIONS}
    if len(answers) != len(known) or len({a["question_id"] for a in answers}) != len(known):
        raise ValueError("Answer each question exactly once.")
    counts = Counter()
    for answer in answers:
        q = known.get(answer["question_id"])
        if q is None:
            raise ValueError("Unknown question.")
        option = next((o for o in q["options"] if o["id"] == answer["option_id"]), None)
        if option is None:
            raise ValueError("Invalid answer option.")
        counts.update(option["signals"])
    highest = max(counts.values(), default=0)
    signals = [{"interest": key, "score": round(value / len(known) * 100),
                "evidence": f"Selected in {value} of {len(known)} reflection questions"}
               for key, value in sorted(counts.items(), key=lambda item: (-item[1], item[0]))]
    return {"signals": signals, "top_interests": [s["interest"] for s in signals if counts[s["interest"]] == highest][:3],
            "disclaimer": "Interest signals are a starting point for exploration, not a diagnosis or career prediction."}
