export interface CareerSummary { id: string; title: string; cluster: string; summary: string; interest_tags: string[]; skill_tags: string[]; illustrative: boolean }
export interface CareerList { careers: CareerSummary[]; clusters: string[]; total: number }

export interface RoadmapYear { year: number; title: string; focus: string; activities: string[]; milestone: string }
export interface CareerRoadmap { career_id: string; career_title: string; illustrative: boolean; duration_years: number; years: RoadmapYear[]; disclaimer: string }
