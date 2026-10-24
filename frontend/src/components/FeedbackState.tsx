import type { ReactNode } from "react";
import "../styles/feedback.css";
type Kind = "loading" | "error" | "empty" | "success";
export default function FeedbackState({ kind, title, message, onRetry, action }: {
  kind: Kind; title: string; message: string; onRetry?: () => void; action?: ReactNode;
}) {
  return <section className={`feedback-state feedback-${kind}`} role={kind === "error" ? "alert" : "status"} aria-live={kind === "error" ? "assertive" : "polite"} aria-busy={kind === "loading"}>
    <span className="feedback-symbol" aria-hidden="true">{kind === "loading" ? "◌" : kind === "error" ? "!" : kind === "success" ? "✓" : "◇"}</span>
    <div className="feedback-body"><h2>{title}</h2><p>{message}</p>
      {(onRetry || action) && <div className="feedback-actions">{onRetry && <button className="btn btn-secondary" type="button" onClick={onRetry}>Try again ↻</button>}{action}</div>}
    </div>
  </section>;
}
