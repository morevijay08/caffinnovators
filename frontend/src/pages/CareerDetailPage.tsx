import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { getCareer } from "../api/careers";
import type { CareerSummary } from "../types/careers";
import "../styles/careers.css";
export default function CareerDetailPage() {
  const { careerId = "" } = useParams();
  const [career, setCareer] = useState<CareerSummary | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  useEffect(() => { const controller = new AbortController(); setLoading(true);setError("");setCareer(null);
    getCareer(careerId, controller.signal).then(setCareer).catch(e=>{if(!controller.signal.aborted)setError(e instanceof Error?e.message:"Career unavailable.");}).finally(()=>{if(!controller.signal.aborted)setLoading(false);});
    return ()=>controller.abort();
  },[careerId]);
  return <main className="career-page"><div className="container career-detail"><Link to="/careers" className="career-back">← Back to Career Explorer</Link>
    {loading&&<p role="status">Loading career details…</p>}
    {error&&<div role="alert" className="career-notice error">{error}. <Link to="/careers">Browse other careers</Link></div>}
    {career&&<article className="career-detail-card"><span className="eyebrow">ILLUSTRATIVE CAREER PROFILE</span><h1>{career.title}</h1><p className="career-lead">{career.summary}</p><div className="career-detail-grid"><section><h2>Interests you might enjoy</h2><div className="career-tags">{career.interest_tags.map(tag=><span key={tag}>{tag.replaceAll("_"," ")}</span>)}</div></section><section><h2>Skills to explore</h2><div className="career-tags">{career.skill_tags.map(tag=><span key={tag}>{tag.replaceAll("-"," ")}</span>)}</div></section></div><p className="career-notice">This profile is fictional/illustrative. The detailed year-by-year roadmap arrives in TASK-008; no qualifications, salaries or admissions claims are presented here.</p></article>}
  </div></main>;
}
