"""Tests for TASK-009 math assessment data, privacy boundary and scoring."""
from app.data.math_questions import DURATION_SECONDS, QUESTION_BANK
from app.schemas.math_readiness import MathAssessmentSubmitRequest
from app.services.math_readiness import (
    AssessmentSubmissionError,
    get_public_assessment,
    score_submission,
)


def test_public_assessment_has_questions_and_no_answer_keys():
    public = get_public_assessment()
    assert public.question_count == len(QUESTION_BANK) == 12
    assert public.duration_seconds == DURATION_SECONDS
    assert len({question.id for question in public.questions}) == public.question_count
    assert {question.topic for question in public.questions} == {
        "arithmetic", "fractions-decimals", "algebra", "geometry", "ratios", "data-interpretation"
    }
    for question in public.questions:
        assert not hasattr(question, "correct_option_id")
        assert not hasattr(question, "explanation")
        assert len(question.options) == 4


def test_all_correct_answers_produce_full_score_and_topic_breakdown():
    submission = MathAssessmentSubmitRequest(
        answers=[
            {"question_id": question.id, "option_id": question.correct_option_id}
            for question in QUESTION_BANK
        ],
        elapsed_seconds=300,
    )
    result = score_submission(submission)
    assert result.correct_answers == 12
    assert result.percentage == 100
    assert result.answered_questions == 12
    assert result.incorrect_or_unanswered == 0
    assert len(result.topic_breakdown) == 6
    assert all(topic.correct == topic.total == 2 for topic in result.topic_breakdown)
    assert result.time_limit_exceeded is False


def test_wrong_and_unanswered_answers_count_as_not_correct():
    question = QUESTION_BANK[0]
    wrong_option = next(option_id for option_id, _ in question.options if option_id != question.correct_option_id)
    result = score_submission(MathAssessmentSubmitRequest(
        answers=[{"question_id": question.id, "option_id": wrong_option}],
        elapsed_seconds=700,
    ))
    assert result.answered_questions == 1
    assert result.correct_answers == 0
    assert result.incorrect_or_unanswered == 12
    assert result.percentage == 0
    assert result.time_limit_exceeded is True
    assert sum(topic.total for topic in result.topic_breakdown) == 12


def test_unknown_question_is_rejected():
    submission = MathAssessmentSubmitRequest(
        answers=[{"question_id": "not-a-real-question", "option_id": "a"}]
    )
    try:
        score_submission(submission)
    except AssessmentSubmissionError as exc:
        assert "Unknown question" in str(exc)
    else:
        raise AssertionError("Expected unknown question to be rejected")


def test_duplicate_question_is_rejected():
    question = QUESTION_BANK[0]
    submission = MathAssessmentSubmitRequest(answers=[
        {"question_id": question.id, "option_id": question.correct_option_id},
        {"question_id": question.id, "option_id": question.correct_option_id},
    ])
    try:
        score_submission(submission)
    except AssessmentSubmissionError as exc:
        assert "Duplicate answer" in str(exc)
    else:
        raise AssertionError("Expected duplicate answer to be rejected")


def test_invalid_option_is_rejected():
    submission = MathAssessmentSubmitRequest(
        answers=[{"question_id": QUESTION_BANK[0].id, "option_id": "not-valid"}]
    )
    try:
        score_submission(submission)
    except AssessmentSubmissionError as exc:
        assert "Invalid option" in str(exc)
    else:
        raise AssertionError("Expected invalid option to be rejected")
