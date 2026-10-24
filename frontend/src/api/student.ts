export interface StudentIdentity { id: string; username: string }
export interface SavedStudentJourney {
 profile: {educationLevel: "Class 8"|"Class 9"|"Class 10"|"Class 11"|"Class 12"|"Diploma"|"College";interests:string[];favoriteSubjects:string[];goal:"Explore career options"|"Discover what interests me"|"I have a career in mind"|"Improve my subject skills";careerIdea:string}|null;
 assessment: {answers:{question_id:string;option_id:string}[];signals:{interest:string;score:number;evidence:string}[]}|null;
 selectedCareerId:string|null; pathHistory:{careerId:string;changedAt:string}[];
 reflections:Record<string,string>; chatHistory:{role:"user"|"assistant";content:string}[];
 mathResult:import("./client").MathAssessmentResult|null; comparison:string[];
}
const BASE=(import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/,"");
async function call<T>(url:string,init?:RequestInit):Promise<T>{
 const response=await fetch(BASE+"/api/v1"+url,{credentials:"include",...init,headers:{"Content-Type":"application/json",...init?.headers}});
 if(!response.ok){let detail="Request could not be completed.";try{const json:unknown=await response.json();if(json&&typeof json==="object"&&"detail" in json&&typeof json.detail==="string")detail=json.detail;}catch{}throw new Error(detail);}
 return response.status===204?undefined as T:await response.json() as T;
}
export const getMe=()=>call<StudentIdentity>("/auth/me");
export const register=(username:string,password:string)=>call<StudentIdentity>("/auth/register",{method:"POST",body:JSON.stringify({username,password})});
export const login=(username:string,password:string)=>call<StudentIdentity>("/auth/login",{method:"POST",body:JSON.stringify({username,password})});
export const logout=()=>call<void>("/auth/logout",{method:"POST"});
export const getJourney=()=>call<SavedStudentJourney>("/journey");
export const patchJourney=(field:keyof SavedStudentJourney,value:unknown)=>call<SavedStudentJourney>("/journey",{method:"PATCH",body:JSON.stringify({field,value})});
