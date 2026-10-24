import { Link, Route, Routes } from "react-router-dom";
import SiteHeader from "./components/SiteHeader";
import SiteFooter from "./components/SiteFooter";
import HomePage from "./pages/HomePage";
import OnboardingPage from "./pages/OnboardingPage";
import { StudentJourneyProvider } from "./state/StudentJourney";

export default function App() {
  return <StudentJourneyProvider><SiteHeader /><Routes>
    <Route path="/" element={<HomePage />} />
    <Route path="/onboarding" element={<OnboardingPage />} />
    <Route path="*" element={<main className="container not-found"><h1>That path isn't here yet.</h1><p>Let's get you back on track.</p><Link className="btn btn-primary" to="/">Return home ↗</Link></main>} />
  </Routes><SiteFooter /></StudentJourneyProvider>;
}
