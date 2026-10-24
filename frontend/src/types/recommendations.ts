import type { InterestAnswer, InterestSignal } from "./interestAssessment";
export type { InterestAnswer };
export interface CareerRecommendation {
  career_id: string; title: string; cluster: string; match_score: number;
  explanation: string; matching_interests: string[]; suggested_steps: string[]; illustrative: boolean;
}
export interface RecommendationResult {
  recommendations: CareerRecommendation[]; assessment_signals: InterestSignal[]; disclaimer: string;
}
