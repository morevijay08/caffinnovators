import type { InterestAnswer, InterestQuestionList, InterestResult } from "../types/interestAssessment";

const BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

async function parseJson<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let detail = "Could not complete your request.";
    try {
      const error: unknown = await response.json();
      if (error && typeof error === "object" && "detail" in error && typeof error.detail === "string") detail = error.detail;
    } catch { /* backend may be unavailable or response may not be JSON */ }
    throw new Error(detail);
  }
  return response.json() as Promise<T>;
}

export async function getInterestQuestions(signal?: AbortSignal, interests: string[] = []): Promise<InterestQuestionList> {
  return parseJson<InterestQuestionList>(await fetch(`${BASE_URL}/api/v1/interest-assessment${interests.length ? `?${new URLSearchParams(interests.map(value => ["interests", value])).toString()}` : ""}`, { signal }));
}

export async function submitInterestAnswers(answers: InterestAnswer[]): Promise<InterestResult> {
  return parseJson<InterestResult>(await fetch(`${BASE_URL}/api/v1/interest-assessment/submit`, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ answers })
  }));
}
