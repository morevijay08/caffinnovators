import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getInterestQuestions, submitInterestAnswers } from "../api/interestAssessment";
import type { InterestQuestionList, InterestResult } from "../types/interestAssessment";
import { useStudentJourney } from "../state/StudentJourney";
import "../styles/interestAssessment.css";
import CareerRecommendations from "../components/CareerRecommendations";
import FeedbackState from "../components/FeedbackState";

type LoadState = "loading" | "ready" | "error";
export default function InterestAssessmentPage() {
  const { profile, assessment, saveAssessment } = useStudentJourney();
  const [loadState, setLoadState] = useState<LoadState>("loading");
  const [requestVersion, setRequestVersion] = useState(0);
  const [questions, setQuestions] = useState<InterestQuestionList | null>(null);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [index, setIndex] = useState(0);
  const [timeLeft, setTimeLeft] = useState(0);
  const [expired, setExpired] = useState(false);
  const [result, setResult] = useState<InterestResult | null>(null);
  const [submittedAnswers, setSubmittedAnswers] = useState<{question_id:string;option_id:string}[]>([]);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  useEffect(() => {
    const controller = new AbortController();
    getInterestQuestions(controller.signal).then(data => {
      if (!controller.signal.aborted) {
        setQuestions(data);
        setTimeLeft(data.duration_seconds);
        setLoadState("ready");
      }
    }).catch(() => { if (!controller.signal.aborted) setLoadState("error"); });
    return () => controller.abort();
  }, [requestVersion]);
  useEffect(() => {
    if (loadState !== "ready" || result || expired || submitting) return;
    const timer = window.setInterval(() => setTimeLeft(previous => {
      if (previous <= 1) { setExpired(true); return 0; }
      return previous - 1;
    }), 1000);
    return () => window.clearInterval(timer);
  }, [loadState, result, expired, submitting]);
  async function finish() {
    if (!questions || expired || submitting) return;
    if (Object.keys(answers).length !== questions.questions.length) { setError("Answer every question before submitting."); return; }
    setSubmitting(true); setError("");
    try {
      const selected = questions.questions.map(q => ({ question_id: q.id, option_id: answers[q.id] }));
      const next = await submitInterestAnswers(selected);
      saveAssessment({ answers: selected, signals: next.signals });
      setSubmittedAnswers(selected);
      setResult(next);
    } catch (cause) { setError(cause instanceof Error ? cause.message : "Unable to submit answers."); }
    finally { setSubmitting(false); }
  }
  function reset() { setAnswers({}); setIndex(0); setTimeLeft(questions?.duration_seconds ?? 0); setExpired(false); setError(""); setResult(null); setSubmittedAnswers([]); }
  const current = questions?.questions[index];
  return <main className="assessment-page"><div className="assessment-shell">
    <span className="eyebrow">INTEREST DISCOVERY</span><h1>What feels exciting to you?</h1>
    <p className="assessment-intro">Choose the activities you would enjoy most. There are no right or wrong answers.</p>
    {!profile && <p className="assessment-notice">You can try this assessment without onboarding. <Link to="/onboarding">Add your student profile</Link> whenever you're ready.</p>}
    {loadState === "loading" && <FeedbackState kind="loading" title="Preparing your questions" message="Your reflection activity is loading…" />}
    {loadState === "error" && <FeedbackState kind="error" title="Questions could not be loaded" message="Start the FastAPI backend, then try again. Your onboarding information is unaffected." onRetry={() => {setLoadState("loading");setRequestVersion(n=>n+1);}} />}
    {result && <section className="assessment-result" aria-live="polite"><h2>Your interest signals</h2><p>Based on the activities you selected, you may enjoy exploring:</p><div className="signal-list">{result.signals.slice(0, 6).map(signal => <div className="signal-item" key={signal.interest}><div><strong>{signal.interest.replaceAll("_"," ")}</strong><span>{signal.evidence}</span></div><span>{signal.score}%</span></div>)}</div><p className="assessment-notice">{result.disclaimer} Your interests are just the beginning. You can explore any career and change your path anytime.</p><button type="button" className="btn btn-secondary" onClick={reset}>Try again</button>{submittedAnswers.length > 0 && <CareerRecommendations answers={submittedAnswers} />}</section>}
    {expired && !result && <section className="assessment-result"><h2>Time is up</h2><p>Your answers weren't submitted. You can try again at your own pace.</p><button className="btn btn-primary" type="button" onClick={reset}>Restart assessment</button></section>}
    {loadState === "ready" && questions && !result && !expired && current && <section className="assessment-panel">
      <div className="assessment-meta"><span>Question {index + 1} of {questions.questions.length}</span><span className="assessment-timer" role="timer" aria-label="Time remaining">{String(Math.floor(timeLeft / 60)).padStart(2,"0")}:{String(timeLeft % 60).padStart(2,"0")}</span></div>
      <div className="assessment-progress"><div style={{ width: `${((index + 1) / questions.questions.length) * 100}%` }} /></div>
      <fieldset className="assessment-fieldset"><legend>{current.prompt}</legend><div className="assessment-options">{current.options.map(option => <label key={option.id} className={answers[current.id] === option.id ? "assessment-choice selected" : "assessment-choice"}><input type="radio" name={current.id} checked={answers[current.id] === option.id} onChange={() => {setAnswers(previous => ({...previous,[current.id]:option.id}));setError("");}} />{option.text}</label>)}</div></fieldset>
      {error && <p role="alert" className="assessment-error">{error}</p>}
      <div className="assessment-actions"><button type="button" className="btn btn-secondary" onClick={() => setIndex(i => Math.max(0,i-1))} disabled={index === 0}>← Previous</button>{index < questions.questions.length - 1 ? <button type="button" className="btn btn-primary" onClick={() => {if (!answers[current.id]) {setError("Choose an option to continue.");return;}setError("");setIndex(i=>i+1);}}>Next →</button> : <button type="button" className="btn btn-primary" disabled={submitting} onClick={finish}>{submitting ? "Submitting…" : "See my interest signals ↗"}</button>}</div>
    </section>}
    {assessment && !result && <p className="assessment-notice">Your previous completed assessment is still saved for this app session. <Link to="/change-path">Change my career path →</Link></p>}
    <p className="assessment-small">This is a short illustrative reflection activity, not a psychological test or a prediction of success.</p>
  </div></main>;
}
