"""Balanced rotating interest-question forms with deterministic server-side scoring."""
from collections import Counter
from itertools import count
from threading import Lock
from app.data.interest_questions import ALL_QUESTIONS, QUESTION_SETS

_counter = count()
_lock = Lock()
_SLOT_COUNT = len(QUESTION_SETS[0])
_QUESTION_MAP = {q["id"]: (slot, q) for group in QUESTION_SETS for slot, q in enumerate(group)}

def public_questions():
    # Advance to a different form for consecutive visits, including Try Again.
    with _lock:
        form = next(_counter) % len(QUESTION_SETS)
    return [{"id":q["id"],"prompt":q["prompt"],
             "options":[{"id":o["id"],"text":o["text"]} for o in q["options"]]}
            for q in QUESTION_SETS[form]]

def score_answers(answers: list[dict]) -> dict:
    # Each submission must contain exactly one question from each of the six slots;
    # this allows alternative forms without requiring a mutable server-side session.
    if len(answers) != _SLOT_COUNT:
        raise ValueError("Answer each question exactly once.")
    counts = Counter()
    slots = set()
    for answer in answers:
        item = _QUESTION_MAP.get(answer["question_id"])
        if item is None:
            raise ValueError("Unknown question.")
        slot, question = item
        if slot in slots:
            raise ValueError("Answer each question exactly once.")
        slots.add(slot)
        option = next((o for o in question["options"] if o["id"] == answer["option_id"]), None)
        if option is None:
            raise ValueError("Invalid answer option.")
        counts.update(option["signals"])
    if len(slots) != _SLOT_COUNT:
        raise ValueError("Answer each question exactly once.")
    highest = max(counts.values(), default=0)
    signals = [{"interest": key, "score": round(value / _SLOT_COUNT * 100),
                "evidence": f"Selected in {value} of {_SLOT_COUNT} reflection questions"}
               for key,value in sorted(counts.items(), key=lambda item: (-item[1],item[0]))]
    return {"signals":signals,
            "top_interests":[s["interest"] for s in signals if counts[s["interest"]] == highest][:3],
            "disclaimer":"Interest signals are a starting point for exploration, not a diagnosis or career prediction."}
