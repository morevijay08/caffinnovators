import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { getCareer, getCareerRoadmap } from "../api/careers";
import type { CareerSummary, CareerRoadmap } from "../types/careers";
import "../styles/careers.css";
import "../styles/roadmap.css";
export default function CareerDetailPage() {
  const { careerId = "" } = useParams();
  const [career, setCareer] = useState<CareerSummary | null>(null);
  const [roadmap, setRoadmap] = useState<CareerRoadmap | null>(null);
  const [error, setError] = useState("");
  const [roadmapError, setRoadmapError] = useState("");
  const [loading, setLoading] = useState(true);
  const [roadmapLoading, setRoadmapLoading] = useState(true);
  const [retry, setRetry] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    setLoading(true); setRoadmapLoading(true);
    setError(""); setRoadmapError(""); setCareer(null); setRoadmap(null);
    getCareer(careerId, controller.signal)
      .then(value => { if (!controller.signal.aborted) setCareer(value); })
      .catch(cause => { if (!controller.signal.aborted) setError(cause instanceof Error ? cause.message : "Career unavailable."); })
      .finally(() => { if (!controller.signal.aborted) setLoading(false); });
    getCareerRoadmap(careerId, controller.signal)
      .then(value => { if (!controller.signal.aborted) setRoadmap(value); })
      .catch(cause => { if (!controller.signal.aborted) setRoadmapError(cause instanceof Error ? cause.message : "Roadmap unavailable."); })
      .finally(() => { if (!controller.signal.aborted) setRoadmapLoading(false); });
    return () => controller.abort();
  }, [careerId, retry]);
  return <main className="career-page"><div className="container career-detail">
    <Link to="/careers" className="career-back">← Back to Career Explorer</Link>
    {loading && <p role="status">Loading career details…</p>}
    {error && <div role="alert" className="career-notice error">{error}. <Link to="/careers">Browse other careers</Link></div>}
    {career && <article className="career-detail-card">
      <span className="eyebrow">ILLUSTRATIVE CAREER PROFILE</span>
      <h1>{career.title}</h1><p className="career-lead">{career.summary}</p>
      <div className="career-detail-grid">
        <section><h2>Interests you might enjoy</h2><div className="career-tags">{career.interest_tags.map(tag => <span key={tag}>{tag.replaceAll("_", " ")}</span>)}</div></section>
        <section><h2>Skills to explore</h2><div className="career-tags">{career.skill_tags.map(tag => <span key={tag}>{tag.replaceAll("-", " ")}</span>)}</div></section>
      </div>
      <section className="roadmap-panel" aria-labelledby="roadmap-heading">
        <span className="eyebrow">EXPLORE AT YOUR OWN PACE</span>
        <h2 id="roadmap-heading">An illustrative year-by-year roadmap</h2>
        <p className="roadmap-intro">These four learning stages are suggestions for exploration, not required qualifications. You can take a different route or change your mind anytime.</p>
        {roadmapLoading && <p role="status">Loading learning roadmap…</p>}
        {!roadmapLoading && roadmapError && <div className="career-notice error" role="alert">
          <p>{roadmapError}</p><button type="button" className="btn btn-secondary" onClick={() => setRetry(n => n + 1)}>Try again</button>
        </div>}
        {roadmap && <><ol className="roadmap-years">
          {roadmap.years.map(stage => <li key={stage.year} className="roadmap-year">
            <div className="roadmap-year-header"><span className="roadmap-year-number">Year {stage.year}</span><h3>{stage.title}</h3></div>
            <p>{stage.focus}</p>
            <ul>{stage.activities.map(activity => <li key={activity}>{activity}</li>)}</ul>
            <p className="roadmap-milestone"><strong>Example milestone:</strong> {stage.milestone}</p>
          </li>)}
        </ol><p className="career-notice">{roadmap.disclaimer}</p></>}
      </section>
      <p className="career-notice">This career profile is fictional/illustrative. Verify any real admissions, qualification or employment requirements from official sources.</p>
      <div className="roadmap-actions"><Link className="btn btn-secondary" to="/change-path">Change my path →</Link><Link className="btn btn-secondary" to="/dashboard">Open my dashboard →</Link></div>
    </article>}
  </div></main>;
}
