"""Scoring logic for the math readiness assessment."""
from collections import defaultdict
from app.data.math_questions import ASSESSMENT_ID, DURATION_SECONDS, QUESTION_BANK
from app.schemas.math_readiness import MathAssessmentPublic, MathAssessmentResult, MathOptionPublic, MathQuestionPublic, MathAssessmentSubmitRequest, TopicScore

class AssessmentSubmissionError(ValueError):
    """Raised when submitted answers reference unknown or repeated items."""

def get_public_assessment() -> MathAssessmentPublic:
    questions = [
        MathQuestionPublic(id=q.id, prompt=q.prompt, topic=q.topic, topic_label=q.topic_label,
            options=[MathOptionPublic(id=oid, text=text) for oid, text in q.options])
        for q in QUESTION_BANK
    ]
    return MathAssessmentPublic(assessment_id=ASSESSMENT_ID, title="Math Readiness Check",
        duration_seconds=DURATION_SECONDS, question_count=len(questions), questions=questions)

def score_submission(submission: MathAssessmentSubmitRequest) -> MathAssessmentResult:
    question_by_id = {q.id: q for q in QUESTION_BANK}
    submitted: dict[str, str] = {}
    for answer in submission.answers:
        if answer.question_id not in question_by_id:
            raise AssessmentSubmissionError(f"Unknown question id: {answer.question_id}")
        if answer.question_id in submitted:
            raise AssessmentSubmissionError(f"Duplicate answer for question: {answer.question_id}")
        q = question_by_id[answer.question_id]
        if answer.option_id not in {oid for oid, _ in q.options}:
            raise AssessmentSubmissionError(f"Invalid option for question: {answer.question_id}")
        submitted[answer.question_id] = answer.option_id
    totals: dict[str, dict[str, object]] = defaultdict(lambda: {"label": "", "total": 0, "correct": 0})
    correct = 0
    for q in QUESTION_BANK:
        bucket = totals[q.topic]
        bucket["label"] = q.topic_label
        bucket["total"] = int(bucket["total"]) + 1
        if submitted.get(q.id) == q.correct_option_id:
            correct += 1
            bucket["correct"] = int(bucket["correct"]) + 1
    total = len(QUESTION_BANK)
    breakdown = [TopicScore(topic=topic, topic_label=str(v["label"]), correct=int(v["correct"]), total=int(v["total"]), percentage=round(int(v["correct"])*100/int(v["total"]))) for topic,v in sorted(totals.items())]
    pct = round(correct*100/total) if total else 0
    return MathAssessmentResult(assessment_id=ASSESSMENT_ID, total_questions=total,
        answered_questions=len(submitted), correct_answers=correct, incorrect_or_unanswered=total-correct,
        percentage=pct, elapsed_seconds=submission.elapsed_seconds, time_limit_seconds=DURATION_SECONDS,
        time_limit_exceeded=submission.elapsed_seconds>DURATION_SECONDS, topic_breakdown=breakdown,
        encouragement="Great work—use your topic breakdown to choose what to explore next." if pct>=75 else "Every skill can grow. Pick one topic to practise, then try again.")
