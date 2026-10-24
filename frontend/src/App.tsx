import { useEffect, useState } from "react";
import { Link, Route, Routes } from "react-router-dom";
import { getHealth } from "./api/client";

type Status = "checking" | "connected" | "unavailable";
function Home() {
  const [status, setStatus] = useState<Status>("checking");
  useEffect(() => {
    const controller = new AbortController();
    getHealth(controller.signal).then(() => setStatus("connected")).catch(() => {
      if (!controller.signal.aborted) setStatus("unavailable");
    });
    return () => controller.abort();
  }, []);
  return <main className="container"><section className="hero"><span className="eyebrow">Every Interest Has a Future</span><h1>Discover your path with confidence.</h1><p>LifePath India helps students explore interests, understand career options, and make progress one step at a time.</p><div className="status" role="status" aria-live="polite">API connection: <strong>{status === "checking" ? "Checking…" : status === "connected" ? "Connected" : "Unavailable — start the backend"}</strong></div><p className="note">Application foundation only. Assessments, recommendations and dashboards arrive in later tasks.</p></section></main>;
}
export default function App() {
  return <><header className="topbar"><div className="container nav"><Link className="brand" to="/">LifePath <span>India</span></Link><span className="nav-label">Career discovery for students</span></div></header><Routes><Route path="/" element={<Home />} /><Route path="*" element={<main className="container"><h1>Page not found</h1><Link to="/">Return home</Link></main>} /></Routes><footer className="container footer">LifePath India · Hackathon prototype</footer></>;
}
