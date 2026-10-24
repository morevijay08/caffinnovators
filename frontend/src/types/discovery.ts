export interface DiscoveryActivity { id:string; title:string; interest_tags:string[]; duration_minutes:number; materials:string; instructions:string[]; reflection_prompt:string; illustrative:boolean }
export interface DiscoveryList { activities:DiscoveryActivity[]; total:number }
