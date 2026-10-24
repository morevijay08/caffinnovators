import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import FeatureHub from "../components/FeatureHub";
import { getHealth } from "../api/client";

type Status = "checking" | "connected" | "unavailable";
const paths = [
  { icon: "⌘", name: "Technology & Robotics", detail: "Create, code and solve problems", tone: "teal" },
  { icon: "◈", name: "Design & Creativity", detail: "Turn ideas into experiences", tone: "peach" },
  { icon: "✳", name: "Science & Discovery", detail: "Ask questions, find answers", tone: "lilac" },
  { icon: "✦", name: "Business & Leadership", detail: "Build ideas that make an impact", tone: "blue" }
];
const stages = [
  { number: "01", name: "Tell us what excites you", detail: "Start with your interests, activities and the things you enjoy." },
  { number: "02", name: "Discover possibilities", detail: "Explore multiple careers with explanations — never a single label." },
  { number: "03", name: "Build your path forward", detail: "Understand skills, learning steps and areas to improve." }
];

export default function HomePage() {
  const [status, setStatus] = useState<Status>("checking");
  useEffect(() => {
    const controller = new AbortController();
    getHealth(controller.signal).then(() => setStatus("connected")).catch(() => { if (!controller.signal.aborted) setStatus("unavailable"); });
    return () => controller.abort();
  }, []);

  return <main>
    <section className="hero-section"><div className="container hero-grid">
      <div className="hero-copy">
        <div className="pill"><span className="pill-dot" /> Career discovery made for Indian students</div>
        <h1>Don't just pick a career. <span className="gradient-text">Discover your path.</span></h1>
        <p className="hero-lead">Your future is bigger than a report card. Explore what you love, discover possibilities and take the next step with confidence.</p>
        <div className="hero-actions"><Link className="btn btn-secondary" to="/auth">Student Login / Register ↗</Link><Link className="btn btn-primary" to="/onboarding">Explore my future <span aria-hidden="true">↗</span></Link><Link className="btn btn-secondary" to="#all-features">See all features ↗</Link><Link className="btn btn-secondary" to="/assessment">Math Readiness Check ↗</Link><a className="btn btn-secondary" href="#how-it-works">See how it works <span aria-hidden="true">↓</span></a></div>
        <div className="hero-trust"><span className="avatar-cluster" aria-hidden="true"><i>✦</i><i>★</i><i>◆</i></span><span>Built for the curious, the dreamers, and the still-figuring-it-out.</span></div>
      </div>
      <div className="hero-visual" aria-label="Preview of possible career paths">
        <div className="orb orb-one" /><div className="orb orb-two" />
        <div className="preview-card"><div className="preview-top"><span className="preview-overline">YOUR JOURNEY</span><span className="preview-symbol">✦</span></div><div className="preview-title">The future looks <em>bright.</em></div><p>There's more than one way to follow your curiosity.</p><div className="preview-options"><div><span>⌘</span> Build something new</div><div><span>◈</span> Create something beautiful</div><div><span>✳</span> Discover how things work</div></div><div className="preview-bottom"><span>Made for your journey</span><span aria-hidden="true">↗</span></div></div>
        <div className="floating-note note-top">✦ Your interests matter</div><div className="floating-note note-bottom">↗ Every path starts somewhere</div>
      </div>
    </div></section>
    <section className="mission-strip"><div className="container mission-content"><strong>Not defined by marks.</strong><span className="strip-separator" aria-hidden="true">✳</span><strong>Driven by curiosity.</strong><span className="strip-separator" aria-hidden="true">✳</span><strong>Built around you.</strong></div></section>
    <section className="section section-intro" id="how-it-works"><div className="container"><div className="section-heading"><span className="eyebrow">YOUR JOURNEY, SIMPLIFIED</span><h2>Clarity comes <span>one step at a time.</span></h2><p>You don't need to have everything figured out. We're here to help you explore.</p></div><div className="steps-grid">{stages.map(step => <article className="step-card" key={step.number}><span className="step-number">{step.number}</span><h3>{step.name}</h3><p>{step.detail}</p><span className="card-arrow" aria-hidden="true">↗</span></article>)}</div></div></section>
    <section className="section section-paths" id="explore"><div className="container"><div className="paths-head"><div><span className="eyebrow">A WORLD OF POSSIBILITY</span><h2>There is more than <span>one kind of success.</span></h2></div><p>Here are just a few directions you might enjoy exploring.</p></div><div className="paths-grid">{paths.map(path => <article className={`path-card ${path.tone}`} key={path.name}><span className="path-icon" aria-hidden="true">{path.icon}</span><h3>{path.name}</h3><p>{path.detail}</p><span className="path-hint">Illustrative career cluster <span aria-hidden="true">↗</span></span></article>)}</div></div></section>
    <FeatureHub />
    <section className="section final-section" id="start"><div className="container"><div className="final-card"><span className="eyebrow">YOUR FUTURE IS YOURS</span><h2>Start curious.<br /><span>Go anywhere.</span></h2><p>Begin with a few simple questions about your interests. Explore careers, save your learning journey, and check your math readiness with a student account.</p><Link className="btn btn-light" to="/onboarding">Get started <span aria-hidden="true">↗</span></Link><div className="api-indicator" role="status" aria-live="polite">API connection: <strong>{status === "checking" ? "Checking…" : status === "connected" ? "Connected" : "Unavailable — start FastAPI"}</strong></div></div></div></section>
  </main>;
}
