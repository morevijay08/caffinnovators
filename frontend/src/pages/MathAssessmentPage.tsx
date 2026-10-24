import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { getMathAssessment, getMathAttempt, submitMathAssessment, type MathAssessment, type MathAssessmentResult } from "../api/client";
import "../styles/math-assessment.css";
import {useStudentJourney} from "../state/StudentJourney";

type Phase = "loading" | "intro" | "quiz" | "submitting" | "result" | "error";

export default function MathAssessmentPage() {
  const {saveMathResult}=useStudentJourney();
  const [params] = useSearchParams();
  const attemptParam = params.get("attempt");
  const [phase, setPhase] = useState<Phase>("loading");
  const [assessment, setAssessment] = useState<MathAssessment | null>(null);
  const [result, setResult] = useState<MathAssessmentResult | null>(null);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [current, setCurrent] = useState(0);
  const [remaining, setRemaining] = useState(600);
  const [startedAt, setStartedAt] = useState<number | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    const load = async () => {
      try {
        if (attemptParam) {
          setResult(await getMathAttempt(attemptParam, controller.signal));
          setPhase("result");
        } else {
          const data = await getMathAssessment(controller.signal);
          setAssessment(data);
          setRemaining(data.duration_seconds);
          setPhase("intro");
        }
      } catch (e) {
        if (!controller.signal.aborted) {
          setError(e instanceof Error ? e.message : "Unable to load assessment.");
          setPhase("error");
        }
      }
    };
    void load();
    return () => controller.abort();
  }, [attemptParam]);

  useEffect(() => {
    if (phase !== "quiz" || remaining <= 0) return;
    const id = window.setInterval(() => setRemaining(v => Math.max(0, v - 1)), 1000);
    return () => window.clearInterval(id);
  }, [phase, remaining > 0]);

  const questions = assessment?.questions ?? [];
  const question = questions[current];
  const answered = Object.keys(answers).length;

  function start() {
    setStartedAt(Date.now());
    setRemaining(assessment?.duration_seconds ?? 600);
    setPhase("quiz");
    setError("");
  }

  async function submit() {
    if (phase !== "quiz" || answered === 0) {
      setError("Choose at least one answer before submitting.");
      return;
    }
    setPhase("submitting");
    setError("");
    const elapsed = startedAt === null ? 0 : Math.min(3600, Math.floor((Date.now() - startedAt) / 1000));
    try {
      const next=await submitMathAssessment(Object.entries(answers).map(([question_id, option_id]) => ({ question_id, option_id })), elapsed);
      setResult(next);saveMathResult(next);
      setPhase("result");
    } catch (e) {
      setError(e instanceof Error ? e.message : "Submission failed.");
      setPhase("quiz");
    }
  }

  const clock = `${String(Math.floor(remaining / 60)).padStart(2, "0")}:${String(remaining % 60).padStart(2, "0")}`;

  if (phase === "loading") return <main className="container math-page"><p>Loading assessment…</p></main>;
  if (phase === "error") return <main className="container math-page"><h1>Assessment unavailable</h1><p role="alert">{error}</p><Link className="btn btn-primary" to="/assessment">Try again</Link></main>;
  if (phase === "intro") return <main className="container math-page"><Link to="/" className="math-back">← LifePath India</Link><section className="math-card"><span className="eyebrow">YOUR LEARNING JOURNEY</span><h1>{assessment?.title}</h1><p>Explore your current math readiness. This practice assessment is guidance, not a measure of fixed ability.</p><div className="math-stats"><div><strong>{assessment?.question_count}</strong><span>Questions</span></div><div><strong>{Math.round((assessment?.duration_seconds ?? 600)/60)} min</strong><span>Time limit</span></div><div><strong>Account</strong><span>Signed in</span></div></div>{assessment?.illustrative && <p className="math-note">Illustrative practice assessment</p>}<ul><li>Choose one option for each question you answer.</li><li>Use Previous and Next to review your answers.</li><li>Unanswered questions count as not correct.</li></ul><button className="btn btn-primary" onClick={start}>Start assessment ↗</button></section></main>;

  if (phase === "result" && result) return <main className="container math-page"><Link to="/" className="math-back">← LifePath India</Link><section className="math-card"><span className="eyebrow">YOUR RESULTS</span><h1>Your effort is a starting point.</h1><div className="math-score">{result.percentage}%</div><p>{result.encouragement}</p><div className="math-stats"><div><strong>{result.correct_answers}/{result.total_questions}</strong><span>Correct</span></div><div><strong>{result.incorrect_or_unanswered}</strong><span>Incorrect or unanswered</span></div><div><strong>{Math.floor(result.elapsed_seconds/60)} min</strong><span>Elapsed</span></div></div><h2>Topic breakdown</h2>{result.topic_breakdown.map(t => <div className="math-topic" key={t.topic}><div><span>{t.topic_label}</span><strong>{t.correct}/{t.total} · {t.percentage}%</strong></div><div className="math-track"><div style={{width:`${t.percentage}%`}} /></div></div>)}{result.attempt_id && <p className="math-note">Saved attempt: <code>{result.attempt_id}</code></p>}<p className="math-disclaimer">{result.disclaimer}</p><div className="math-actions"><Link className="btn btn-primary" to="/assessment">Try again</Link><Link className="btn btn-secondary" to="/">Back home</Link></div></section></main>;

  if (!question) return <main className="container math-page"><p>No questions are available.</p></main>;
  return <main className="container math-page"><div className="math-top"><Link to="/" className="math-back">← LifePath India</Link><div className={remaining < 60 ? "math-clock urgent" : "math-clock"}>⏱ {clock}</div></div><section className="math-card"><div className="math-progress-label"><span>Question {current+1} of {questions.length}</span><span>{answered} answered</span></div><div className="math-track"><div style={{width:`${((current+1)/questions.length)*100}%`}} /></div><span className="eyebrow">{question.topic_label}</span><h1>{question.prompt}</h1><div className="math-options">{question.options.map((option,i)=><label className={answers[question.id]===option.id?"math-option selected":"math-option"} key={option.id}><input type="radio" name={question.id} checked={answers[question.id]===option.id} onChange={()=>setAnswers(prev=>({...prev,[question.id]:option.id}))}/><span className="math-letter">{String.fromCharCode(65+i)}</span><span>{option.text}</span></label>)}</div>{error && <p className="math-error" role="alert">{error}</p>}{remaining===0 && <p className="math-error">Time is up. Submit your answers now.</p>}<div className="math-actions"><button className="btn btn-secondary" disabled={current===0} onClick={()=>setCurrent(v=>v-1)}>Previous</button>{current<questions.length-1?<button className="btn btn-primary" onClick={()=>setCurrent(v=>v+1)}>Next question ↗</button>:<button className="btn btn-primary" disabled={phase==="submitting"} onClick={()=>void submit()}>Submit assessment</button>}</div>{remaining===0 && <button className="btn btn-secondary math-submit-full" disabled={phase==="submitting"} onClick={()=>void submit()}>Submit now</button>}</section></main>;
}
