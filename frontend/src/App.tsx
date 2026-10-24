
import { Link, Route, Routes } from "react-router-dom";
import SiteHeader from "./components/SiteHeader";
import SiteFooter from "./components/SiteFooter";
import HomePage from "./pages/HomePage";
import OnboardingPage from "./pages/OnboardingPage";
import InterestAssessmentPage from "./pages/InterestAssessmentPage";
import CareerExplorerPage from "./pages/CareerExplorerPage";
import CareerDetailPage from "./pages/CareerDetailPage";
import ChangePathPage from "./pages/ChangePathPage";
import DashboardPage from "./pages/DashboardPage";
import DiscoveryLabPage from "./pages/DiscoveryLabPage";
import MathAssessmentPage from "./pages/MathAssessmentPage";
import ScholarshipsPage from "./pages/ScholarshipsPage";
import CareerAssistantPage from "./pages/CareerAssistantPage";
import AuthPage from "./pages/AuthPage";
import { useStudentJourney } from "./state/StudentJourney";
import { StudentJourneyProvider } from "./state/StudentJourney";

function Protected({children}:{children:React.ReactNode}){const {account,authLoading}=useStudentJourney();if(authLoading)return <main className="container"><p role="status">Restoring your saved journey…</p></main>;if(!account)return <main className="container"><h1>Sign in to continue</h1><p>Your career exploration and progress are saved to your account.</p><Link className="btn btn-primary" to="/auth">Create account or sign in</Link></main>;return <>{children}</>;}

export default function App() {
  return (
    <StudentJourneyProvider>
      <SiteHeader />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/auth" element={<AuthPage />} />
        <Route path="/onboarding" element={<Protected><OnboardingPage /></Protected>} />
        <Route path="/interest-assessment" element={<Protected><InterestAssessmentPage /></Protected>} />
        <Route path="/careers" element={<Protected><CareerExplorerPage /></Protected>} />
        <Route path="/careers/:careerId" element={<Protected><CareerDetailPage /></Protected>} />
        <Route path="/change-path" element={<Protected><ChangePathPage /></Protected>} />
        <Route path="/dashboard" element={<Protected><DashboardPage /></Protected>} />
        <Route path="/discovery-lab" element={<Protected><DiscoveryLabPage /></Protected>} />
        <Route path="/career-assistant" element={<Protected><CareerAssistantPage /></Protected>} />
        <Route path="/assessment" element={<Protected><MathAssessmentPage /></Protected>} />
        <Route path="/scholarships" element={<Protected><ScholarshipsPage /></Protected>} />
        <Route
          path="*"
          element={
            <main className="container not-found">
              <h1>That path isn't here yet.</h1>
              <p>Let's get you back on track.</p>
              <Link className="btn btn-primary" to="/">
                Return home ↗
              </Link>
            </main>
          }
        />
      </Routes>
      <SiteFooter />
    </StudentJourneyProvider>
  );
}
