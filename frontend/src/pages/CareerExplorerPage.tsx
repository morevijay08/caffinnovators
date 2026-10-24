import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getCareers } from "../api/careers";
import type { CareerList } from "../types/careers";
import "../styles/careers.css";
import FeedbackState from "../components/FeedbackState";
const names: Record<string,string> = {"social-impact":"Social impact", "technology":"Technology", "science":"Science", "creative":"Creative", "business":"Business", "communication":"Communication", "sports":"Sports"};
const label = (value: string) => names[value] ?? value.replaceAll("_", " ").replaceAll("-", " ");
export default function CareerExplorerPage() {
  const [search, setSearch] = useState("");
  const [cluster, setCluster] = useState("");
  const [catalogue, setCatalogue] = useState<CareerList | null>(null);
  const [clusters, setClusters] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [retry, setRetry] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    setLoading(true); setError("");
    getCareers(search, cluster, controller.signal).then(data => { setCatalogue(data); setClusters(data.clusters); })
      .catch(cause => { if (!controller.signal.aborted) setError(cause instanceof Error ? cause.message : "Could not load careers."); })
      .finally(() => { if (!controller.signal.aborted) setLoading(false); });
    return () => controller.abort();
  }, [search, cluster, retry]);
  return <main className="career-page"><div className="container">
    <div className="career-intro"><span className="eyebrow">CAREER EXPLORER</span><h1>A future full of possibilities.</h1><p>Explore different directions at your own pace. These are illustrative examples, not career rankings or guarantees.</p></div>
    <div className="career-filters"><label>Search careers<input type="search" value={search} maxLength={100} onChange={e=>setSearch(e.target.value)} placeholder="Try design, science, technology..." /></label><label>Career cluster<select value={cluster} onChange={e=>setCluster(e.target.value)}><option value="">All clusters</option>{clusters.map(c=><option key={c} value={c}>{label(c)}</option>)}</select></label></div>
    {loading && <FeedbackState kind="loading" title="Exploring the catalogue" message="Loading career possibilities…" />}
    {!loading && error && <FeedbackState kind="error" title="Careers are temporarily unavailable" message={error + " Check that the FastAPI backend is running."} onRetry={()=>setRetry(n=>n+1)} />}
    {!loading && !error && catalogue && <><p className="career-count" role="status">{catalogue.total} illustrative career{catalogue.total===1 ? "" : "s"} found</p>{catalogue.careers.length===0?<FeedbackState kind="empty" title="No careers match these filters" message="Try a different search term or cluster." action={<button type="button" className="btn btn-secondary" onClick={()=>{setSearch("");setCluster("");}}>Clear filters</button>} />:<div className="career-list">{catalogue.careers.map(c=><article className="career-tile" key={c.id}><span className="career-cluster">{label(c.cluster)}</span><h2>{c.title}</h2><p>{c.summary}</p><div className="career-tags">{c.interest_tags.map(tag=><span key={tag}>{label(tag)}</span>)}</div><Link className="career-link" to={`/careers/${c.id}`}>Explore career <span aria-hidden="true">↗</span></Link></article>)}</div>}</>}
  </div></main>;
}
