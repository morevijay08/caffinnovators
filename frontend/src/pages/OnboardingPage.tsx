import { useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import {
  EDUCATION_LEVELS, INTEREST_OPTIONS, SUBJECT_OPTIONS, GOAL_OPTIONS,
  useStudentJourney, type EducationLevel, type StudentGoal, type StudentProfile
} from "../state/StudentJourney";
import "../styles/onboarding.css";

const steps = ["Your stage", "Your interests", "Your direction"];
type Draft = { educationLevel: EducationLevel | ""; interests: string[]; favoriteSubjects: string[]; goal: StudentGoal | ""; careerIdea: string };
function createDraft(profile: StudentProfile | null): Draft {
  return profile ? { ...profile, interests: [...profile.interests], favoriteSubjects: [...profile.favoriteSubjects] }
    : { educationLevel: "", interests: [], favoriteSubjects: [], goal: "", careerIdea: "" };
}
function toggle(items: string[], item: string) {
  return items.includes(item) ? items.filter(value => value !== item) : [...items, item];
}
function validate(step: number, value: Draft): string | null {
  if (step === 0 && !value.educationLevel) return "Choose your current education level to continue.";
  if (step === 1 && value.interests.length === 0) return "Choose at least one interest to continue.";
  if (step === 2 && !value.goal) return "Choose what you want to explore.";
  if (step === 2 && value.goal === "I have a career in mind" && !value.careerIdea.trim()) return "Describe the career you have in mind.";
  return null;
}
export default function OnboardingPage() {
  const { profile, setProfile, clearProfile } = useStudentJourney();
  const [draft, setDraft] = useState<Draft>(() => createDraft(profile));
  const [step, setStep] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [finished, setFinished] = useState(profile !== null);
  function change(next: Draft) { setDraft(next); setError(null); }
  function next(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const validationError = validate(step, draft);
    if (validationError) { setError(validationError); return; }
    if (step < steps.length - 1) { setStep(step + 1); setError(null); return; }
    // Store in React memory only. The API does not yet have a student-profile contract.
    setProfile({
      educationLevel: draft.educationLevel as EducationLevel,
      interests: [...draft.interests],
      favoriteSubjects: [...draft.favoriteSubjects],
      goal: draft.goal as StudentGoal,
      careerIdea: draft.goal === "I have a career in mind" ? draft.careerIdea.trim() : ""
    });
    setFinished(true);
  }
  function back() { setStep(s => Math.max(0, s - 1)); setError(null); }
  function restart() { clearProfile(); setDraft(createDraft(null)); setStep(0); setError(null); setFinished(false); }
  if (finished) {
    // Saved profile can be edited; on first arrival show its summary instead of hiding it.
    return <main className="onboarding-page"><section className="onboarding-shell completed-panel">
      <span className="eyebrow">YOUR EXPLORATION STARTS HERE</span><h1>You're ready to explore.</h1><p>These choices help shape your experience. They never limit your future.</p>
      <dl className="profile-summary">
        <div><dt>Education</dt><dd>{profile?.educationLevel ?? draft.educationLevel}</dd></div>
        <div><dt>Interests</dt><dd>{(profile?.interests ?? draft.interests).join(", ")}</dd></div>
        <div><dt>Favourite subjects</dt><dd>{(profile?.favoriteSubjects ?? draft.favoriteSubjects).join(", ") || "Not selected"}</dd></div>
        <div><dt>Goal</dt><dd>{profile?.goal ?? draft.goal}</dd></div>
        {(profile?.careerIdea ?? draft.careerIdea) && <div><dt>Career idea</dt><dd>{profile?.careerIdea ?? draft.careerIdea}</dd></div>}
      </dl>
      <p className="privacy-message">Saved temporarily in this open app session only. Refreshing the page will clear your details. Interest assessment and recommendations are being built in upcoming tasks.</p>
      <div className="onboarding-actions">
        <button className="btn btn-secondary" type="button" onClick={() => { setDraft(createDraft(profile)); setStep(0); setFinished(false); }}>Edit answers</button>
        <button className="btn btn-outline-danger" type="button" onClick={restart}>Clear answers</button>
        <Link className="btn btn-primary" to="/interest-assessment">Start interest assessment ↗</Link>
      </div>
    </section></main>;
  }
  return <main className="onboarding-page"><section className="onboarding-shell" aria-labelledby="onboard-title">
    <div className="onboarding-heading"><div><span className="eyebrow">A LITTLE ABOUT YOU</span><h1 id="onboard-title">Your story, your future.</h1><p>We'll start with what you like—not your marks. No name or contact information needed.</p></div><span className="step-indicator">Step {step + 1} of {steps.length}</span></div>
    <ol className="onboarding-steps" aria-label="Onboarding progress">{steps.map((title, index) => <li className={index === step ? "is-current" : index < step ? "is-completed" : ""} aria-current={index === step ? "step" : undefined} key={title}><span>{index < step ? "✓" : index + 1}</span><small>{title}</small></li>)}</ol>
    <form onSubmit={next} noValidate>
      {step === 0 && <fieldset className="form-section"><legend>Where are you in your learning journey?</legend><p>There is no right or wrong starting point.</p><div className="choice-grid level-grid">{EDUCATION_LEVELS.map(value => <label key={value} className={draft.educationLevel === value ? "choice-card selected" : "choice-card"}><input type="radio" name="educationLevel" value={value} checked={draft.educationLevel === value} onChange={() => change({ ...draft, educationLevel: value })}/><span>{value}</span></label>)}</div></fieldset>}
      {step === 1 && <div className="form-section"><fieldset><legend>What sparks your curiosity?</legend><p>Select as many as you like. Interests can always change.</p><div className="choice-grid">{INTEREST_OPTIONS.map(value => <label key={value} className={draft.interests.includes(value) ? "choice-card selected" : "choice-card"}><input type="checkbox" checked={draft.interests.includes(value)} onChange={() => change({ ...draft, interests: toggle(draft.interests, value) })}/><span>{value}</span></label>)}</div></fieldset>
        <fieldset className="subjects-fieldset"><legend>Which subjects do you enjoy? <span className="optional">Optional</span></legend><p>Choose any number, or skip this section.</p><div className="choice-grid">{SUBJECT_OPTIONS.map(value => <label key={value} className={draft.favoriteSubjects.includes(value) ? "choice-card selected" : "choice-card"}><input type="checkbox" checked={draft.favoriteSubjects.includes(value)} onChange={() => change({ ...draft, favoriteSubjects: toggle(draft.favoriteSubjects, value) })}/><span>{value}</span></label>)}</div></fieldset></div>}
      {step === 2 && <fieldset className="form-section"><legend>What would you like help with?</legend><p>Pick the goal that feels most useful right now.</p><div className="choice-grid goal-grid">{GOAL_OPTIONS.map(value => <label key={value} className={draft.goal === value ? "choice-card selected" : "choice-card"}><input type="radio" name="goal" value={value} checked={draft.goal === value} onChange={() => change({ ...draft, goal: value })}/><span>{value}</span></label>)}</div>{draft.goal === "I have a career in mind" && <label className="career-label">Which career are you thinking about?<input type="text" maxLength={100} value={draft.careerIdea} onChange={event => change({ ...draft, careerIdea: event.target.value })} placeholder="e.g., Product designer, scientist, engineer..." /></label>}</fieldset>}
      {error && <p className="form-error" role="alert">{error}</p>}
      <div className="onboarding-actions">{step > 0 ? <button type="button" className="btn btn-secondary" onClick={back}>← Previous</button> : <Link className="btn btn-secondary" to="/">← Back home</Link>}<button className="btn btn-primary" type="submit">{step === steps.length - 1 ? "Save and continue ↗" : "Continue →"}</button></div>
    </form>
    <p className="privacy-message">Your answers stay in browser memory for this session only. No account, database, or backend profile is created.</p>
  </section></main>;
}
