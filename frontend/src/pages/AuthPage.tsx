import {useState,type FormEvent} from "react";
import {Navigate,useNavigate} from "react-router-dom";
import {useStudentJourney} from "../state/StudentJourney";
import "../styles/auth.css";
export default function AuthPage(){
 const {account,authLoading,signIn,signUp}=useStudentJourney();
 const navigate=useNavigate();
 const [mode,setMode]=useState<"login"|"register">("register");
 const [username,setUsername]=useState("");const [password,setPassword]=useState("");
 const [working,setWorking]=useState(false);const [error,setError]=useState("");
 async function submit(e:FormEvent){e.preventDefault();setError("");setWorking(true);try{if(mode==="register")await signUp(username,password);else await signIn(username,password);navigate("/onboarding",{replace:true});}catch(err){setError(err instanceof Error?err.message:"Account request failed.");}finally{setWorking(false);}}
 if(authLoading)return <main className="auth-page"><p role="status">Checking account…</p></main>;
 if(account)return <Navigate to="/dashboard" replace/>;
 return <main className="auth-page"><section className="auth-panel"><span className="eyebrow">PRIVATE STUDENT JOURNEY</span><h1>{mode==="register"?"Create your account":"Welcome back"}</h1><p>Choose a nickname, not your full name. Your interests and progress are saved privately to this local app's database.</p>
 <form onSubmit={submit}><label>Username<input autoComplete="username" required minLength={3} maxLength={40} pattern="[a-zA-Z0-9_]+" value={username} onChange={e=>setUsername(e.target.value)} placeholder="e.g. future_explorer"/></label><label>Password<input type="password" autoComplete={mode==="register"?"new-password":"current-password"} required minLength={10} maxLength={128} value={password} onChange={e=>setPassword(e.target.value)}/></label>
 {error&&<p role="alert" className="auth-error">{error}</p>}<button className="btn btn-primary" type="submit" disabled={working}>{working?"Please wait…":mode==="register"?"Create account":"Sign in"}</button></form>
 <button type="button" className="auth-switch" onClick={()=>{setError("");setMode(mode==="register"?"login":"register");}}>{mode==="register"?"Already registered? Sign in":"New here? Create an account"}</button>
 <p className="auth-privacy">Do not use your real name or share personal contact information. Data stays in the project's local SQLite database; there is no hosted account recovery or email reset.</p>
 </section></main>;
}
