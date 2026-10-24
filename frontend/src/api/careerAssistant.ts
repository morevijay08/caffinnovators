import type { AssistantMessage, AssistantReply } from "../types/careerAssistant";

const BASE = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

export async function askCareerAssistant(message: string, conversation_history: AssistantMessage[]): Promise<AssistantReply> {
  const response = await fetch(BASE + "/api/v1/career-assistant", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, conversation_history }),
  });
  if (!response.ok) {
    let detail = "Could not reach the career assistant. Please try again.";
    try {
      const data: unknown = await response.json();
      if (data && typeof data === "object" && "detail" in data && typeof data.detail === "string") {
        detail = data.detail;
      }
    } catch { /* keep a safe generic error */ }
    throw new Error(detail);
  }
  return await response.json() as AssistantReply;
}
