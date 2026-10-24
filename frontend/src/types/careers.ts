export interface CareerSummary { id: string; title: string; cluster: string; summary: string; interest_tags: string[]; skill_tags: string[]; illustrative: boolean }
export interface CareerList { careers: CareerSummary[]; clusters: string[]; total: number }
