import { createContext, useContext, useMemo, useState, type ReactNode } from "react";

export const EDUCATION_LEVELS = ["Class 8", "Class 9", "Class 10", "Class 11", "Class 12", "Diploma", "College"] as const;
export const INTEREST_OPTIONS = ["Technology", "Science", "Design", "Writing", "Business", "Helping people", "Environment", "Arts", "Mathematics", "Sports"] as const;
export const SUBJECT_OPTIONS = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "Commerce", "Art", "Other"] as const;
export const GOAL_OPTIONS = ["Explore career options", "Discover what interests me", "I have a career in mind", "Improve my subject skills"] as const;
export type EducationLevel = (typeof EDUCATION_LEVELS)[number];
export type StudentGoal = (typeof GOAL_OPTIONS)[number];
export interface StudentProfile {
  educationLevel: EducationLevel;
  interests: string[];
  favoriteSubjects: string[];
  goal: StudentGoal;
  careerIdea: string;
}
export interface PathChange { careerId: string; changedAt: string }
export interface JourneyState {
  assessment: { answers: {question_id:string;option_id:string}[]; signals: {interest:string;score:number;evidence:string}[] } | null;
  saveAssessment(data: {answers:{question_id:string;option_id:string}[];signals:{interest:string;score:number;evidence:string}[]}): void;
  selectedCareerId: string | null;
  pathHistory: PathChange[];
  changePath(careerId: string): void;
  profile: StudentProfile | null;
  setProfile(profile: StudentProfile): void;
  clearProfile(): void;
}
const JourneyContext = createContext<JourneyState | undefined>(undefined);

export function StudentJourneyProvider({ children }: { children: ReactNode }) {
  const [profile, updateProfile] = useState<StudentProfile | null>(null);
  const [assessment, setAssessment] = useState<JourneyState["assessment"]>(null);
  const [selectedCareerId, setSelectedCareerId] = useState<string | null>(null);
  const [pathHistory, setPathHistory] = useState<PathChange[]>([]);
  const value = useMemo<JourneyState>(() => ({
    profile, assessment, selectedCareerId, pathHistory,
    saveAssessment: data => setAssessment({ answers: data.answers.map(a => ({...a})), signals: data.signals.map(x => ({...x})) }),
    changePath: careerId => { if (careerId !== selectedCareerId) { setSelectedCareerId(careerId); setPathHistory(old => [...old, {careerId, changedAt:new Date().toISOString()}]); } },
    setProfile: (next) => updateProfile({
      ...next,
      interests: [...next.interests],
      favoriteSubjects: [...next.favoriteSubjects],
    }),
    clearProfile: () => updateProfile(null),
  }), [profile, assessment, selectedCareerId, pathHistory]);
  return <JourneyContext.Provider value={value}>{children}</JourneyContext.Provider>;
}
export function useStudentJourney(): JourneyState {
  const context = useContext(JourneyContext);
  if (!context) throw new Error("useStudentJourney must be used within StudentJourneyProvider");
  return context;
}
