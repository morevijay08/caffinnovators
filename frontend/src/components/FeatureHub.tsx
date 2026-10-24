import {Link} from "react-router-dom";

const features=[
 {to:"/onboarding",title:"Student profile",description:"Save your grade, favourite subjects and interests."},
 {to:"/interest-assessment",title:"Interest assessment",description:"Find your interests through a short quiz."},
 {to:"/careers",title:"Career explorer",description:"Explore careers, matches and learning roadmaps."},
 {to:"/discovery-lab",title:"Discovery Lab",description:"Try activities and save your reflections."},
 {to:"/career-assistant",title:"AI Career Assistant",description:"Ask Gemma career questions using local Ollama."},
 {to:"/assessment",title:"Math assessment",description:"Test math readiness and save your results."},
 {to:"/scholarships",title:"Scholarships & costs",description:"Explore illustrative education funding options."},
 {to:"/change-path",title:"Change my path",description:"Update your preferred career without losing progress."},
 {to:"/dashboard",title:"My dashboard",description:"Review saved progress and compare careers."},
];
export default function FeatureHub(){
 return <section className="section" id="all-features" aria-labelledby="feature-hub-title">
  <div className="container">
   <div className="section-heading"><span className="eyebrow">ALL IN ONE PLACE</span><h2 id="feature-hub-title">Explore every LifePath feature</h2><p>Choose a feature below. Sign in once to keep your progress saved.</p></div>
   <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(min(100%,245px),1fr))",gap:16}}>
    {features.map(feature=><article key={feature.to} style={{background:"var(--surface,white)",border:"1px solid #d8e4e5",borderRadius:16,padding:22,display:"flex",flexDirection:"column",gap:12}}>
     <h3 style={{margin:0}}>{feature.title}</h3><p style={{margin:0,flex:1}}>{feature.description}</p>
     <Link className="btn btn-secondary" to={feature.to}>Open feature ↗</Link>
    </article>)}
   </div>
  </div>
 </section>;
}
