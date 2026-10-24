import type { CareerList, CareerSummary } from "../types/careers";
const API_BASE = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");
async function request<T>(path: string, signal?: AbortSignal): Promise<T> {
  const response = await fetch(API_BASE + path, { signal });
  if (!response.ok) {
    let message = "Unable to load career information.";
    try { const data: unknown = await response.json(); if (data && typeof data === "object" && "detail" in data && typeof data.detail === "string") message = data.detail; } catch { /* generic fallback */ }
    throw new Error(message);
  }
  return await response.json() as T;
}
export function getCareers(search = "", cluster = "", signal?: AbortSignal): Promise<CareerList> {
  const params = new URLSearchParams();
  if (search.trim()) params.set("search", search.trim());
  if (cluster) params.set("cluster", cluster);
  const qs = params.toString();
  return request<CareerList>(`/api/v1/careers${qs ? "?" + qs : ""}`, signal);
}
export function getCareer(id: string, signal?: AbortSignal): Promise<CareerSummary> {
  return request<CareerSummary>(`/api/v1/careers/${encodeURIComponent(id)}`, signal);
}
