import { useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { askCareerAssistant } from "../api/careerAssistant";
import type { AssistantMessage } from "../types/careerAssistant";
import "../styles/careerAssistant.css";

export default function CareerAssistantPage() {
  const [messages, setMessages] = useState<AssistantMessage[]>([]);
  const [draft, setDraft] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [model, setModel] = useState("");
  const [disclaimer, setDisclaimer] = useState("AI-generated guidance for exploration, not official career or admissions advice.");
  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const message = draft.trim();
    if (!message || busy) return;
    setBusy(true);
    setError("");
    try {
      const reply = await askCareerAssistant(message, messages.slice(-10));
      setMessages(previous => [...previous, { role: "user", content: message }, { role: "assistant", content: reply.answer }]);
      setDraft("");
      setModel(reply.model);
      setDisclaimer(reply.disclaimer);
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "The assistant is unavailable.");
    } finally {
      setBusy(false);
    }
  }
  return <main className="assistant-page"><div className="assistant-shell">
    <span className="eyebrow">CAREER ASSISTANT</span>
    <h1>Ask about your possibilities.</h1>
    <p className="assistant-intro">Explore interests, activities and potential careers with Gemma 4 through a local Ollama model. This is guidance, not a decision about your future.</p>
    <div className="assistant-note">Please avoid sharing personal details such as your full name, contact information, school or marks. Chat messages are sent to the locally configured AI service; the application does not store a chat history in a database.</div>
    <section className="assistant-chat" aria-label="Career assistant conversation">
      {messages.length === 0 && <div className="assistant-empty">
        <h2>Not sure where to begin?</h2>
        <p>Try asking: “I like technology and drawing. What could I explore?”</p>
        <p>You can also <Link to="/careers">browse illustrative careers</Link> without using AI.</p>
      </div>}
      <div className="assistant-transcript" aria-live="polite" aria-relevant="additions text">
        {messages.map((item, index) => <div key={index} className={item.role === "user" ? "assistant-bubble from-user" : "assistant-bubble from-ai"}>
          <span>{item.role === "user" ? "You" : "Gemma career assistant"}</span>
          <p>{item.content}</p>
        </div>)}
      </div>
      {busy && <p className="assistant-status" role="status">Gemma is thinking about your question…</p>}
      {error && <div className="assistant-error" role="alert"><p>{error}</p><p>Your question is still in the text box. Check Ollama and try sending it again.</p></div>}
      <form className="assistant-form" onSubmit={submit}>
        <label htmlFor="assistant-message">Your career question</label>
        <textarea id="assistant-message" rows={3} maxLength={2000} value={draft} onChange={event => setDraft(event.target.value)} disabled={busy} placeholder="I like science and helping people. What could I explore?" />
        <div className="assistant-controls">
          <span>{draft.length}/2000</span>
          <button className="btn btn-primary" disabled={!draft.trim() || busy} type="submit">{busy ? "Sending…" : "Ask Gemma →"}</button>
        </div>
      </form>
    </section>
    {model && <p className="assistant-model">Reply provided by configured model: {model}</p>}
    <p className="assistant-disclaimer">{disclaimer} Verify educational requirements and other real-world details using official sources.</p>
    <button className="btn btn-secondary" type="button" onClick={() => { setMessages([]); setError(""); setDraft(""); setModel(""); }} disabled={busy || (messages.length === 0 && !draft && !error)}>Clear conversation</button>
  </div></main>;
}
