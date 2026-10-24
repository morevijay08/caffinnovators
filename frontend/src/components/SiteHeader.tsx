import { useState } from "react";
import { Link, NavLink } from "react-router-dom";

export default function SiteHeader() {
  const [open, setOpen] = useState(false);
  const close = () => setOpen(false);
  return <header className="site-header"><div className="container header-inner">
    <Link className="logo" to="/" onClick={close} aria-label="LifePath India home"><span className="logo-mark" aria-hidden="true">✦</span>LifePath <span>India</span></Link>
    <button className="menu-toggle" type="button" aria-expanded={open} aria-controls="site-nav" onClick={() => setOpen(!open)}>{open ? "Close" : "Menu"} <span aria-hidden="true">{open ? "×" : "☰"}</span></button>
    <nav id="site-nav" aria-label="Main navigation" className={open ? "site-nav is-open" : "site-nav"}>
      <NavLink to="/" end onClick={close}>Home</NavLink>
      <a href="/#how-it-works" onClick={close}>How it works</a>
      <Link to="/careers" onClick={close}>Explore careers</Link>
      <Link to="/interest-assessment" onClick={close}>Interest assessment</Link>
      <Link to="/discovery-lab" onClick={close}>Discovery Lab</Link>
      <Link to="/change-path" onClick={close}>Change my path</Link>
      <Link to="/dashboard" onClick={close}>Dashboard</Link>
      <Link className="nav-cta" to="/onboarding" onClick={close}>Get started <span aria-hidden="true">↗</span></Link>
    </nav>
  </div></header>;
}
