import type { HealthResponse } from "../types/api";

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

export async function getHealth(signal?: AbortSignal): Promise<HealthResponse> {
  const response = await fetch(`${API_BASE_URL}/health`, { signal });
  if (!response.ok) throw new Error(`API returned HTTP ${response.status}`);
  const data: unknown = await response.json();
  if (!data || typeof data !== "object" || !("status" in data) || !("service" in data) || data.status !== "ok" || data.service !== "lifepath-api") throw new Error("Invalid API health response");
  return { status: "ok", service: "lifepath-api" };
}
