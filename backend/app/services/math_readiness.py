"""Deterministic math readiness assessment logic; no LLM or persistence required."""
from collections import defaultdict

from backend.app.data.math_questions import ASSESSMENT_ID, DURATION_SECONDS, QUESTION_BANK
from backend.app.schemas.math_readiness import (
    MathAssessmentPublic,
    MathAssessmentResult,
    MathOptionPublic,
    MathQuestionPublic,
    MathAssessmentSubmitRequest,
    TopicScore,
)


class AssessmentSubmissionError(ValueError):
    """Raised when submitted answers reference unknown or repeated items."""


def get_public_assessment() -> MathAssessmentPublic:
    """Return questions and options without exposing answer keys or explanations."""
    questions = [
        MathQuestionPublic(
            id=question.id,
            prompt=question.prompt,
            topic=question.topic,
            topic_label=question.topic_label,
            options=[MathOptionPublic(id=option_id, text=text) for option_id, text in question.options],
        )
        for question in QUESTION_BANK
    ]
    return MathAssessmentPublic(
        assessment_id=ASSESSMENT_ID,
        title="Math Readiness Check",
        duration_seconds=DURATION_SECONDS,
        question_count=len(questions),
        questions=questions,
    )


def score_submission(submission: MathAssessmentSubmitRequest) -> MathAssessmentResult:
    """Score server-side answer keys; omitted questions count as unanswered/incorrect."""
    question_by_id = {question.id: question for question in QUESTION_BANK}
    submitted: dict[str, str] = {}

    for answer in submission.answers:
        if answer.question_id not in question_by_id:
            raise AssessmentSubmissionError(f"Unknown question id: {answer.question_id}")
        if answer.question_id in submitted:
            raise AssessmentSubmissionError(f"Duplicate answer for question: {answer.question_id}")
        question = question_by_id[answer.question_id]
        valid_option_ids = {option_id for option_id, _ in question.options}
        if answer.option_id not in valid_option_ids:
            raise AssessmentSubmissionError(f"Invalid option for question: {answer.question_id}")
        submitted[answer.question_id] = answer.option_id

    topic_totals: dict[str, dict[str, object]] = defaultdict(
        lambda: {"label": "", "total": 0, "correct": 0}
    )
    correct_count = 0
    for question in QUESTION_BANK:
        bucket = topic_totals[question.topic]
        bucket["label"] = question.topic_label
        bucket["total"] = int(bucket["total"]) + 1
        is_correct = submitted.get(question.id) == question.correct_option_id
        if is_correct:
            correct_count += 1
            bucket["correct"] = int(bucket["correct"]) + 1

    total_questions = len(QUESTION_BANK)
    percentage = round(correct_count * 100 / total_questions) if total_questions else 0
    topic_breakdown = [
        TopicScore(
            topic=topic,
            topic_label=str(values["label"]),
            correct=int(values["correct"]),
            total=int(values["total"]),
            percentage=round(int(values["correct"]) * 100 / int(values["total"])),
        )
        for topic, values in sorted(topic_totals.items())
    ]
    encouragement = (
        "Great work—use your topic breakdown to choose what to explore next."
        if percentage >= 75
        else "Every skill can grow. Pick one topic to practise, then try again."
    )
    return MathAssessmentResult(
        assessment_id=ASSESSMENT_ID,
        total_questions=total_questions,
        answered_questions=len(submitted),
        correct_answers=correct_count,
        incorrect_or_unanswered=total_questions - correct_count,
        percentage=percentage,
        elapsed_seconds=submission.elapsed_seconds,
        time_limit_seconds=DURATION_SECONDS,
        time_limit_exceeded=submission.elapsed_seconds > DURATION_SECONDS,
        topic_breakdown=topic_breakdown,
        encouragement=encouragement,
    )
