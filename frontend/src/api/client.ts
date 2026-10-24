import type { HealthResponse } from "../types/api";

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

export async function getHealth(signal?: AbortSignal): Promise<HealthResponse> {
  const response = await fetch(`${API_BASE_URL}/health`, { signal });
  if (!response.ok) throw new Error(`API returned HTTP ${response.status}`);
  const data: unknown = await response.json();
  if (!data || typeof data !== "object" || !("status" in data) || !("service" in data) || data.status !== "ok" || data.service !== "lifepath-api") throw new Error("Invalid API health response");
  return { status: "ok", service: "lifepath-api" };
}


export type MathOption = { id: string; text: string };
export type MathQuestion = {
  id: string; prompt: string; topic: string; topic_label: string; options: MathOption[];
};
export type MathAssessment = {
  assessment_id: string; title: string; duration_seconds: number; question_count: number;
  questions: MathQuestion[]; illustrative: boolean;
};
export type TopicScore = {
  topic: string; topic_label: string; correct: number; total: number; percentage: number;
};
export type MathAssessmentResult = {
  attempt_id: string | null; assessment_id: string; total_questions: number;
  answered_questions: number; correct_answers: number; incorrect_or_unanswered: number;
  percentage: number; elapsed_seconds: number; time_limit_seconds: number;
  time_limit_exceeded: boolean; topic_breakdown: TopicScore[];
  encouragement: string; disclaimer: string;
};
export type MathAnswer = { question_id: string; option_id: string };

async function requestJson<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: { "Content-Type": "application/json", ...init?.headers },
  });
  if (!response.ok) {
    let message = `Request failed (HTTP ${response.status})`;
    try {
      const body: unknown = await response.json();
      if (body && typeof body === "object" && "detail" in body && typeof body.detail === "string") {
        message = body.detail;
      }
    } catch { /* Keep HTTP status message. */ }
    throw new Error(message);
  }
  return response.json() as Promise<T>;
}

export function getMathAssessment(signal?: AbortSignal): Promise<MathAssessment> {
  return requestJson<MathAssessment>("/api/v1/math-assessment", { signal });
}

export function submitMathAssessment(
  answers: MathAnswer[], elapsedSeconds: number
): Promise<MathAssessmentResult> {
  return requestJson<MathAssessmentResult>("/api/v1/math-assessment/submit", {
    method: "POST",
    body: JSON.stringify({ answers, elapsed_seconds: elapsedSeconds }),
  });
}

export function getMathAttempt(
  attemptId: string, signal?: AbortSignal
): Promise<MathAssessmentResult> {
  return requestJson<MathAssessmentResult>(
    `/api/v1/math-assessment/attempts/${encodeURIComponent(attemptId)}`, { signal }
  );
}
