import {useEffect,useState} from "react";
import {Link} from "react-router-dom";
import {getDiscoveryActivities} from "../api/discovery";
import type {DiscoveryActivity} from "../types/discovery";
import {useStudentJourney} from "../state/StudentJourney";
import "../styles/discovery.css";
const OPTIONS=["","technology","science","design","writing","business","helping_people","environment","arts","mathematics","sports","problem_solving"];
export default function DiscoveryLabPage(){
 const {assessment}=useStudentJourney();
 const [interest,setInterest]=useState("");const [activities,setActivities]=useState<DiscoveryActivity[]>([]);
 const [busy,setBusy]=useState(true);const [error,setError]=useState("");const [retry,setRetry]=useState(0);
 const [active,setActive]=useState<string|null>(null);
 const [drafts,setDrafts]=useState<Record<string,string>>({});
 const [reflections,setReflections]=useState<Record<string,string>>({});
 useEffect(()=>{const controller=new AbortController();setBusy(true);setError("");getDiscoveryActivities(interest,controller.signal).then(result=>{if(!controller.signal.aborted)setActivities(result.activities);}).catch(err=>{if(!controller.signal.aborted)setError(err instanceof Error?err.message:"Activities are unavailable.");}).finally(()=>{if(!controller.signal.aborted)setBusy(false);});return ()=>controller.abort();},[interest,retry]);
 const related=assessment?.signals.slice(0,3).map(s=>s.interest)??[];
 const chosen=activities.find(a=>a.id===active);
 return <main className="discovery-page"><div className="container discovery-content"><span className="eyebrow">INTEREST DISCOVERY LAB</span><h1>Explore by doing.</h1><p className="discovery-lead">Try a small creative challenge and reflect on what you enjoyed. There are no scores, grades or wrong answers.</p>
 {related.length>0&&<p className="discovery-hint">Your recent interest signals: {related.map(s=>s.replaceAll("_"," ")).join(", ")}. You can try any activity.</p>}
 <label className="discovery-filter">Find activities by interest <select value={interest} onChange={e=>{setInterest(e.target.value);setActive(null);}}>{OPTIONS.map(value=><option key={value} value={value}>{value?value.replaceAll("_"," "):"All interests"}</option>)}</select></label>
 {busy&&<p role="status">Loading activities…</p>}
 {error&&<div role="alert" className="discovery-error"><p>{error}</p><button className="btn btn-secondary" type="button" onClick={()=>setRetry(n=>n+1)}>Try again</button></div>}
 {!busy&&!error&&activities.length===0&&<p role="status">No activities match this interest yet. Choose another interest or all interests.</p>}
 {!busy&&!error&&<div className="discovery-grid">{activities.map(item=><article key={item.id} className="discovery-card"><span className="eyebrow">{item.duration_minutes} MIN · ILLUSTRATIVE</span><h2>{item.title}</h2><p>{item.interest_tags.map(x=>x.replaceAll("_"," ")).join(" · ")}</p><p><strong>Materials:</strong> {item.materials}</p><button type="button" className="btn btn-primary" onClick={()=>setActive(item.id)}>{reflections[item.id]?"Review activity":"Try this activity"} →</button>{reflections[item.id]&&<p className="discovery-complete">Reflection saved in this session ✓</p>}</article>)}</div>}
 {chosen&&<section className="discovery-detail" aria-labelledby="activity-title"><span className="eyebrow">ACTIVITY INSTRUCTIONS</span><h2 id="activity-title">{chosen.title}</h2><ol>{chosen.instructions.map(step=><li key={step}>{step}</li>)}</ol><label htmlFor="discovery-reflection"><strong>Reflect:</strong> {chosen.reflection_prompt}</label><textarea id="discovery-reflection" rows={4} maxLength={800} placeholder="What surprised you? What would you explore next?" value={drafts[chosen.id]??reflections[chosen.id]??""} onChange={e=>setDrafts(prev=>({...prev,[chosen.id]:e.target.value}))}/><div className="discovery-actions"><button className="btn btn-primary" type="button" disabled={!(drafts[chosen.id]??reflections[chosen.id]??"").trim()} onClick={()=>{setReflections(prev=>({...prev,[chosen.id]:(drafts[chosen.id]??reflections[chosen.id]??"").trim()}));}}>Save reflection</button><button type="button" className="btn btn-secondary" onClick={()=>setActive(null)}>Close</button></div>{reflections[chosen.id]&&<p role="status" className="discovery-complete">Saved reflection: {reflections[chosen.id]}</p>}</section>}
 <p className="discovery-hint">Reflections are temporary and disappear when you refresh. Activities are illustrative, not measures of talent or future success.</p><Link to="/careers">Explore careers →</Link></div></main>;
}
