import {createContext,useContext,useEffect,useMemo,useRef,useState,type ReactNode} from "react";
import {getMe,getJourney,patchJourney,register as registerAccount,login as loginAccount,logout as logoutAccount,type StudentIdentity,type SavedStudentJourney} from "../api/student";
export const EDUCATION_LEVELS = ["Class 8", "Class 9", "Class 10", "Class 11", "Class 12", "Diploma", "College"] as const;
export const INTEREST_OPTIONS = ["Technology", "Science", "Design", "Writing", "Business", "Helping people", "Environment", "Arts", "Mathematics", "Sports"] as const;
export const SUBJECT_OPTIONS = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "Commerce", "Art", "Other"] as const;
export const GOAL_OPTIONS = ["Explore career options", "Discover what interests me", "I have a career in mind", "Improve my subject skills"] as const;
export type EducationLevel=(typeof EDUCATION_LEVELS)[number];
export type StudentGoal=(typeof GOAL_OPTIONS)[number];
export type StudentProfile=NonNullable<SavedStudentJourney["profile"]>;
export type PathChange={careerId:string;changedAt:string};
export type Assessment=SavedStudentJourney["assessment"];
export interface JourneyState {
 account:StudentIdentity|null; authLoading:boolean; saveError:string;
 signIn(username:string,password:string):Promise<void>;
 signUp(username:string,password:string):Promise<void>;
 signOut():Promise<void>;
 profile:StudentProfile|null;setProfile(profile:StudentProfile):void;clearProfile():void;
 assessment:Assessment;saveAssessment(data:NonNullable<Assessment>):void;
 selectedCareerId:string|null;pathHistory:PathChange[];changePath(id:string):void;
 reflections:Record<string,string>;saveReflection(id:string,text:string):void;
 chatHistory:{role:"user"|"assistant";content:string}[];setChatHistory(messages:{role:"user"|"assistant";content:string}[]):void;
}
const Context=createContext<JourneyState|undefined>(undefined);
const empty:SavedStudentJourney={profile:null,assessment:null,selectedCareerId:null,pathHistory:[],reflections:{},chatHistory:[]};
export function StudentJourneyProvider({children}:{children:ReactNode}){
 const [account,setAccount]=useState<StudentIdentity|null>(null);
 const [authLoading,setAuthLoading]=useState(true);
 const [data,setData]=useState<SavedStudentJourney>(empty);
 const [saveError,setSaveError]=useState("");
 const live=useRef(data);live.current=data;
 const queue=useRef<Promise<unknown>>(Promise.resolve());
 useEffect(()=>{let active=true;async function restore(){try{const who=await getMe();const saved=await getJourney();if(active){setAccount(who);setData(saved);}}catch{if(active){setAccount(null);setData(empty);}}finally{if(active)setAuthLoading(false);}}void restore();return()=>{active=false;};},[]);
 const save=(field:keyof SavedStudentJourney,value:unknown)=>{
   if(!account){setSaveError("Sign in to save your progress.");return;}
   setSaveError("");
   queue.current=queue.current.catch(()=>{}).then(()=>patchJourney(field,value)).catch(err=>setSaveError(err instanceof Error?err.message:"Couldn't save changes. Please try again."));
 };
 const update=(field:keyof SavedStudentJourney,value:SavedStudentJourney[typeof field])=>{setData(old=>({...old,[field]:value}));save(field,value);};
 const authenticated=async(action:()=>Promise<StudentIdentity>)=>{setAuthLoading(true);try{const who=await action();const saved=await getJourney();setAccount(who);setData(saved);setSaveError("");queue.current=Promise.resolve();}finally{setAuthLoading(false);}};
 const signOut=async()=>{await queue.current.catch(()=>{});await logoutAccount();setAccount(null);setData(empty);setSaveError("");};
 const value=useMemo<JourneyState>(()=>({
 account,authLoading,saveError,
 signIn:(u,p)=>authenticated(()=>loginAccount(u,p)),
 signUp:(u,p)=>authenticated(()=>registerAccount(u,p)),signOut,
 profile:data.profile,assessment:data.assessment,selectedCareerId:data.selectedCareerId,pathHistory:data.pathHistory,
 reflections:data.reflections,chatHistory:data.chatHistory,
 setProfile:p=>update("profile",{...p,interests:[...p.interests],favoriteSubjects:[...p.favoriteSubjects]}),
 clearProfile:()=>update("profile",null),
 saveAssessment:a=>update("assessment",{answers:a.answers.map(x=>({...x})),signals:a.signals.map(x=>({...x}))}),
 changePath:id=>{if(id===live.current.selectedCareerId)return;const history=[...live.current.pathHistory,{careerId:id,changedAt:new Date().toISOString()}];setData(old=>({...old,selectedCareerId:id,pathHistory:history}));save("selectedCareerId",id);save("pathHistory",history);},
 saveReflection:(id,text)=>{const next={...live.current.reflections,[id]:text};update("reflections",next);},
 setChatHistory:messages=>update("chatHistory",messages.slice(-20))
 }),[account,authLoading,saveError,data]);
 return <Context.Provider value={value}>{children}{saveError&&<div role="alert" style={{position:"fixed",bottom:12,right:12,padding:14,background:"#fff1f1",color:"#831b1b",border:"1px solid #d88",zIndex:1000,maxWidth:340}}>Progress not saved: {saveError}</div>}</Context.Provider>;
}
export function useStudentJourney():JourneyState{const state=useContext(Context);if(!state)throw new Error("StudentJourneyProvider is missing");return state;}
