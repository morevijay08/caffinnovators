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
export interface JourneyState {
  profile: StudentProfile | null;
  setProfile(profile: StudentProfile): void;
  clearProfile(): void;
}
const JourneyContext = createContext<JourneyState | undefined>(undefined);

export function StudentJourneyProvider({ children }: { children: ReactNode }) {
  const [profile, updateProfile] = useState<StudentProfile | null>(null);
  const value = useMemo<JourneyState>(() => ({
    profile,
    setProfile: (next) => updateProfile({
      ...next,
      interests: [...next.interests],
      favoriteSubjects: [...next.favoriteSubjects],
    }),
    clearProfile: () => updateProfile(null),
  }), [profile]);
  return <JourneyContext.Provider value={value}>{children}</JourneyContext.Provider>;
}
export function useStudentJourney(): JourneyState {
  const context = useContext(JourneyContext);
  if (!context) throw new Error("useStudentJourney must be used within StudentJourneyProvider");
  return context;
}
