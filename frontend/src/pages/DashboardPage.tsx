import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { getCareers } from "../api/careers";
import type { CareerSummary } from "../types/careers";
import { useStudentJourney } from "../state/StudentJourney";
import "../styles/dashboard.css";

export default function DashboardPage() {
  const { profile, assessment, selectedCareerId, pathHistory } = useStudentJourney();
  const [careers, setCareers] = useState<CareerSummary[]>([]);
  const [comparison, setComparison] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [retry, setRetry] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    setLoading(true);
    setError("");
    getCareers("", "", controller.signal).then(data => setCareers(data.careers))
      .catch(cause => { if (!controller.signal.aborted) setError(cause instanceof Error ? cause.message : "Could not load careers."); })
      .finally(() => { if (!controller.signal.aborted) setLoading(false); });
    return () => controller.abort();
  }, [retry]);
  const selectedCareer = careers.find(c => c.id === selectedCareerId);
  const comparedCareers = useMemo(() => comparison.map(id => careers.find(c => c.id === id)).filter((c): c is CareerSummary => Boolean(c)), [careers, comparison]);
  function toggleComparison(id: string) {
    setComparison(current => current.includes(id) ? current.filter(key => key !== id) : current.length < 3 ? [...current, id] : current);
  }
  return <main className="dashboard-page"><div className="container dashboard-content">
    <span className="eyebrow">MY LIFEPath JOURNEY</span><h1>Your exploration dashboard</h1>
    <p className="dashboard-lead">A snapshot of what you've explored so far. Your interests and career direction can change anytime.</p>
    <div className="dashboard-overview">
      <article><span>Onboarding</span><strong>{profile ? "Completed" : "Not started"}</strong><p>{profile ? profile.educationLevel + " · " + profile.interests.length + " interests" : "Tell us a little about what you enjoy."}</p><Link to="/onboarding">{profile ? "Edit profile" : "Start onboarding"} ↗</Link></article>
      <article><span>Interest assessment</span><strong>{assessment ? "Completed" : "Not started"}</strong><p>{assessment ? assessment.signals.length + " interest signals recorded" : "Discover interests through six short questions."}</p><Link to="/interest-assessment">{assessment ? "Explore again" : "Take assessment"} ↗</Link></article>
      <article><span>Current career</span><strong>{selectedCareer?.title ?? (selectedCareerId ? "Saved career" : "Not selected")}</strong><p>{pathHistory.length} path {pathHistory.length === 1 ? "choice" : "choices"} in this session</p><Link to="/change-path">Change my path ↗</Link></article>
    </div>
    {assessment && <section className="dashboard-section"><h2>Your interest signals</h2><div className="dashboard-signals">{assessment.signals.slice(0, 6).map(s => <div key={s.interest}><span>{s.interest.replaceAll("_", " ")}</span><strong>{s.score}%</strong></div>)}</div><p className="dashboard-muted">These scores describe activities you selected, not your ability or likelihood of success.</p></section>}
    <section className="dashboard-section"><div className="dashboard-title-row"><div><h2>Compare career possibilities</h2><p>Select up to three illustrative careers to view them side by side.</p></div><strong>{comparison.length}/3 selected</strong></div>
      {loading && <p role="status">Loading career catalogue…</p>}
      {error && <div className="dashboard-error" role="alert">{error}<button type="button" className="btn btn-secondary" onClick={() => setRetry(n => n + 1)}>Try again</button></div>}
      {!loading && !error && <><div className="dashboard-career-list">{careers.map(career => <label className={comparison.includes(career.id) ? "dashboard-select selected" : "dashboard-select"} key={career.id}>
        <input type="checkbox" checked={comparison.includes(career.id)} disabled={!comparison.includes(career.id) && comparison.length >= 3} onChange={() => toggleComparison(career.id)} />
        <span><strong>{career.title}</strong><small>{career.cluster.replaceAll("-", " ")}</small></span>
      </label>)}</div>{comparedCareers.length > 0 ? <div className="dashboard-comparison" aria-label="Career comparison">{comparedCareers.map(career => <article key={career.id}><span className="eyebrow">{career.cluster.replaceAll("-", " ")}</span><h3>{career.title}</h3><p>{career.summary}</p><h4>Interests</h4><div className="dashboard-tags">{career.interest_tags.map(tag => <span key={tag}>{tag.replaceAll("_"," ")}</span>)}</div><h4>Skills to develop</h4><div className="dashboard-tags">{career.skill_tags.map(tag => <span key={tag}>{tag.replaceAll("-"," ")}</span>)}</div><Link to={`/careers/${career.id}`}>View career ↗</Link></article>)}</div> : <p className="dashboard-empty">Choose a career above to start comparing.</p>}</>}
    </section>
    <section className="dashboard-section dashboard-next"><h2>What's next?</h2><p>Math readiness and improvement-plan results will appear here after Member 3's TASK-009/TASK-010 APIs are integrated. No results are generated or assumed yet.</p><Link to="/careers">Browse career explorer ↗</Link></section>
    <p className="dashboard-muted">Progress and comparison choices are temporary for this open app session. Refreshing the page clears them. All career examples are illustrative.</p>
  </div></main>;
}
