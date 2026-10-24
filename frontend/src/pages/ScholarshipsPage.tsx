import { useMemo, useState } from "react";
import "../styles/scholarships.css";

const demoScholarships = [
  { name: "Curiosity Starter Award", amount: 15000, audience: "Students exploring their first post-school course", basis: "Illustrative merit + interest example" },
  { name: "Community Opportunity Grant", amount: 25000, audience: "Learners who need help meeting education costs", basis: "Illustrative need-based example" },
  { name: "Future Skills Support", amount: 10000, audience: "Students choosing a skills or vocational pathway", basis: "Illustrative skills-pathway example" },
];

const money = (value: number) => new Intl.NumberFormat("en-IN", {
  style: "currency", currency: "INR", maximumFractionDigits: 0,
}).format(value);

export default function ScholarshipsPage() {
  const [courseCost, setCourseCost] = useState("60000");
  const [familyContribution, setFamilyContribution] = useState("20000");
  const [otherSupport, setOtherSupport] = useState("5000");

  const estimate = useMemo(() => {
    const cost = Math.max(0, Number(courseCost) || 0);
    const contribution = Math.max(0, Number(familyContribution) || 0);
    const support = Math.max(0, Number(otherSupport) || 0);
    const gap = Math.max(0, cost - contribution - support);
    return { cost, contribution, support, gap, covered: cost === 0 ? 100 : Math.min(100, Math.round(((cost - gap) / cost) * 100)) };
  }, [courseCost, familyContribution, otherSupport]);

  return <main className="scholarship-page"><div className="container scholarship-content">
    <header className="scholarship-hero">
      <span className="eyebrow">SCHOLARSHIP & AFFORDABILITY</span>
      <h1>Make your next step feel more possible.</h1>
      <p>Explore example support options and estimate the gap between a course's cost and the money you may be able to put toward it.</p>
      <div className="scholarship-demo-note" role="note"><strong>Demo content only.</strong> Every scholarship and amount on this page is fictional and illustrative. These are not real offers, eligibility rules, or application links.</div>
    </header>

    <section className="scholarship-section" aria-labelledby="demo-scholarships-title">
      <div className="scholarship-section-heading"><div><span className="eyebrow">EXAMPLE SUPPORT</span><h2 id="demo-scholarships-title">Different ways support could work</h2></div><span className="demo-pill">Fictional examples</span></div>
      <div className="scholarship-cards">{demoScholarships.map(item => <article className="scholarship-card" key={item.name}>
        <span className="scholarship-card-icon" aria-hidden="true">✦</span>
        <p className="scholarship-card-basis">{item.basis}</p>
        <h3>{item.name}</h3>
        <strong className="scholarship-amount">{money(item.amount)}</strong>
        <p>{item.audience}</p>
        <span className="scholarship-card-foot">Sample amount · Not an actual scholarship</span>
      </article>)}</div>
    </section>

    <section className="scholarship-section affordability-panel" aria-labelledby="affordability-title">
      <div className="affordability-copy"><span className="eyebrow">QUICK ESTIMATOR</span><h2 id="affordability-title">Estimate an education-cost gap</h2><p>Use approximate figures to see how much of an example course cost may still need to be covered. You can change the numbers at any time.</p>
        <p className="estimator-disclaimer">This simple calculator is for planning practice, not financial advice or a prediction of aid eligibility.</p>
      </div>
      <div className="affordability-form">
        <label>Estimated course cost (₹)<input type="number" min="0" max="100000000" step="1000" value={courseCost} onChange={e => setCourseCost(e.target.value)} /></label>
        <label>Amount you could contribute (₹)<input type="number" min="0" max="100000000" step="1000" value={familyContribution} onChange={e => setFamilyContribution(e.target.value)} /></label>
        <label>Other confirmed support (₹)<input type="number" min="0" max="100000000" step="1000" value={otherSupport} onChange={e => setOtherSupport(e.target.value)} /></label>
        <div className="affordability-result" aria-live="polite">
          <span>Estimated remaining gap</span><strong>{money(estimate.gap)}</strong>
          <div className="coverage-track" role="progressbar" aria-label="Estimated course cost covered" aria-valuemin={0} aria-valuemax={100} aria-valuenow={estimate.covered}><span style={{ width: `${estimate.covered}%` }} /></div>
          <div className="coverage-caption"><span>{estimate.covered}% covered in this estimate</span><span>{money(estimate.cost)} total</span></div>
          <p>{estimate.gap === 0 ? "Your entered contribution and support cover the example cost." : "This is the amount still to plan for using your own research and trusted guidance."}</p>
        </div>
      </div>
    </section>
    <section className="scholarship-next"><div><span className="eyebrow">YOUR NEXT STEP</span><h2>Check real opportunities carefully.</h2><p>Before applying for any real scholarship, verify the provider, official eligibility criteria, deadlines, documents, and terms on the provider's official website or with your school counsellor.</p></div></section>
  </div></main>;
}
