import type {DiscoveryList} from "../types/discovery";
const BASE=(import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/,"");
export async function getDiscoveryActivities(interest="",signal?:AbortSignal):Promise<DiscoveryList>{
  const query=interest ? "?interest="+encodeURIComponent(interest):"";
  const response=await fetch(BASE+"/api/v1/discovery-activities"+query,{signal});
  if(!response.ok)throw new Error("Could not load discovery activities. Check that FastAPI is running.");
  return await response.json() as DiscoveryList;
}
