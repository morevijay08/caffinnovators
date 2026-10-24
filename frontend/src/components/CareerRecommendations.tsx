import { useState } from "react";
import { Link } from "react-router-dom";
import { getRecommendations } from "../api/recommendations";
import type { InterestAnswer, RecommendationResult } from "../types/recommendations";
import "../styles/recommendations.css";

export default function CareerRecommendations({ answers }: { answers: InterestAnswer[] }) {
  const [result, setResult] = useState<RecommendationResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  async function load() {
    setLoading(true); setError("");
    try { setResult(await getRecommendations(answers)); }
    catch (cause) { setError(cause instanceof Error ? cause.message : "Could not load recommendations."); }
    finally { setLoading(false); }
  }
  return <section className="recommendations-panel" aria-labelledby="recommendations-heading">
    <div className="recommendations-heading"><span className="eyebrow">YOUR NEXT POSSIBILITIES</span><h2 id="recommendations-heading">Explore careers that connect with your interests</h2>
      <p>These are starting points based on your six answers. They are not limits or guarantees.</p></div>
    {!result && <button className="btn btn-primary" type="button" disabled={loading} onClick={load}>{loading ? "Finding possibilities…" : "See career suggestions ↗"}</button>}
    {error && <div role="alert" className="recommendation-error">{error}<button type="button" className="btn btn-secondary" disabled={loading} onClick={load}>Try again</button></div>}
    {result && <><div className="recommendation-grid">{result.recommendations.map((item, index) => <article className="recommendation-card" key={item.career_id}>
        <div className="recommendation-top"><span>OPTION {index + 1}</span><strong>{item.match_score}% signal overlap</strong></div>
        <h3>{item.title}</h3><p>{item.explanation}</p>
        <div className="recommendation-tags">{item.matching_interests.map(tag => <span key={tag}>{tag.replaceAll("_"," ")}</span>)}</div>
        <p className="recommendation-step">{item.suggested_steps[0]}</p>
        <Link to={`/careers/${item.career_id}`} className="career-link">Explore career profile ↗</Link>
      </article>)}</div><p className="assessment-notice">{result.disclaimer}</p><Link to="/careers" className="btn btn-secondary">Browse all career options →</Link> <Link to="/change-path" className="btn btn-primary">Change my path →</Link></>}
  </section>;
}
