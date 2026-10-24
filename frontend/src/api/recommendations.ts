import type { InterestAnswer, RecommendationResult } from "../types/recommendations";
const BASE = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");
export async function getRecommendations(answers: InterestAnswer[], signal?: AbortSignal): Promise<RecommendationResult> {
  const response = await fetch(`${BASE}/api/v1/recommendations`, {
    method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answers, limit: 5 }), signal
  });
  if (!response.ok) {
    let message = "Could not load career recommendations.";
    try {
      const data: unknown = await response.json();
      if (data && typeof data === "object" && "detail" in data && typeof data.detail === "string") message = data.detail;
    } catch { /* fallback */ }
    throw new Error(message);
  }
  return await response.json() as RecommendationResult;
}
