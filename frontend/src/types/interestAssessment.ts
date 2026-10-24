export interface InterestOption { id: string; text: string }
export interface InterestQuestion { id: string; prompt: string; options: InterestOption[] }
export interface InterestQuestionList { questions: InterestQuestion[]; duration_seconds: number }
export interface InterestAnswer { question_id: string; option_id: string }
export interface InterestSignal { interest: string; score: number; evidence: string }
export interface InterestResult { signals: InterestSignal[]; top_interests: string[]; disclaimer: string }
