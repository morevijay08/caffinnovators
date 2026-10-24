import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getCareers } from "../api/careers";
import type { CareerSummary } from "../types/careers";
import { useStudentJourney } from "../state/StudentJourney";
import "../styles/changePath.css";

export default function ChangePathPage() {
  const {profile,assessment,selectedCareerId,pathHistory,changePath} = useStudentJourney();
  const [careers,setCareers] = useState<CareerSummary[]>([]);
  const [loading,setLoading] = useState(true);
  const [error,setError] = useState("");
  const [choice,setChoice] = useState("");
  const [confirming,setConfirming] = useState(false);
  const [notice,setNotice] = useState("");
  const [retry,setRetry] = useState(0);
  useEffect(()=>{
    const controller=new AbortController();
    setLoading(true);setError("");
    getCareers("","",controller.signal).then(data=>setCareers(data.careers))
      .catch(cause=>{if(!controller.signal.aborted)setError(cause instanceof Error?cause.message:"Unable to load careers.");})
      .finally(()=>{if(!controller.signal.aborted)setLoading(false);});
    return ()=>controller.abort();
  },[retry]);
  const current=careers.find(c=>c.id===selectedCareerId);
  const next=careers.find(c=>c.id===choice);
  const choose=(id:string)=>{setChoice(id);setConfirming(false);setNotice("");};
  const apply=()=>{
    if (!next || next.id===selectedCareerId) return;
    changePath(next.id);setConfirming(false);setNotice("Your selected path has changed. Your onboarding answers and interest assessment are still here.");
  };
  return <main className="path-page"><div className="container path-content">
    <span className="eyebrow">YOUR JOURNEY CAN CHANGE</span>
    <h1>Change your path. Keep your progress.</h1>
    <p className="path-lead">Interests can grow and plans can change. Pick another direction whenever you like. All careers remain open to explore.</p>
    <section className="path-summary" aria-label="Saved progress">
      <div><strong>Onboarding</strong><span>{profile ? profile.educationLevel+" · "+profile.interests.length+" interests" : "Not completed yet"}</span></div>
      <div><strong>Interest assessment</strong><span>{assessment ? "Completed · "+assessment.signals.length+" interest signals" : "Not completed yet"}</span></div>
      <div><strong>Current career path</strong><span>{current?.title ?? (selectedCareerId ? "Previously selected career" : "Not selected yet")}</span></div>
    </section>
    <section className="path-picker"><h2>Choose a direction to explore</h2>
      {loading&&<p role="status">Loading career options…</p>}
      {error&&<div role="alert" className="path-error">{error}<button className="btn btn-secondary" type="button" onClick={()=>setRetry(x=>x+1)}>Try again</button></div>}
      {!loading&&!error&&<><div className="path-choices">{careers.map(c=><label key={c.id} className={choice===c.id?"path-choice chosen":"path-choice"}>
        <input type="radio" name="selected-path" value={c.id} checked={choice===c.id} onChange={()=>choose(c.id)}/>
        <span><strong>{c.title}</strong><small>{c.summary}</small></span>
      </label>)}</div>
      {choice&&choice===selectedCareerId&&<p role="status">This is already your selected path.</p>}
      {choice&&choice!==selectedCareerId&&!confirming&&<button type="button" className="btn btn-primary" onClick={()=>setConfirming(true)}>Review path change →</button>}
      {confirming&&next&&<div className="path-confirm" role="group" aria-label="Confirm change of career path">
        <h3>Switch to {next.title}?</h3><p>We’ll update only your selected career path. Your onboarding answers, completed assessment and previous path choices will remain saved to your student account.</p>
        <div className="path-actions"><button type="button" className="btn btn-primary" onClick={apply}>Yes, change my path</button><button type="button" className="btn btn-secondary" onClick={()=>setConfirming(false)}>Cancel</button></div>
      </div>}</>}
      {notice&&<p className="path-success" role="status">{notice}</p>}
    </section>
    {selectedCareerId&&<p><Link className="btn btn-secondary" to={`/careers/${selectedCareerId}`}>View my selected career ↗</Link></p>}
    {pathHistory.length>0&&<section className="path-history"><h2>Your path journey</h2><ol>{pathHistory.map((entry,index)=><li key={index}>{careers.find(c=>c.id===entry.careerId)?.title??entry.careerId} <small>({new Date(entry.changedAt).toLocaleString()})</small></li>)}</ol></section>}
    <p className="path-note">Your choices are saved to your student account and restored after refresh. Changing a path does not erase your progress during this session or guarantee a career outcome.</p>
    <div className="path-links"><Link to="/onboarding">Edit onboarding →</Link><Link to="/interest-assessment">Interest assessment →</Link><Link to="/careers">Browse all careers →</Link></div>
  </div></main>;
}
