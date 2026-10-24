# LifePath India — Hackathon Demo Script (TASK-020)

**Every Interest Has a Future**

This script is for the **task12 branch** of the React + FastAPI application. It documents what exists on that branch; it does not imply that Member 2/3's other branches have been merged.

## Before the live demo
1. Check out task12 and verify the working tree is clean.
2. Run `python -m pytest -q` in backend and `npm run build` in frontend. Record actual output in the TASK_020_REVIEW checklist.
3. Start FastAPI on port 8000 and React/Vite on port 5173. Verify `http://localhost:8000/health` and `http://localhost:5173/`.
4. Open the app in a fresh browser tab, without old state, and choose a consistent, believable set of six interest answers for the walkthrough.
5. Have `/careers` and `/dashboard` ready as backup routes. **Do not claim persistence**; data is React memory and reload clears it.

## 4–6 minute live demonstration

### 0:00–0:40 — Problem & mission
**Speaker 1:**

> Students often feel pressured to decide their future from grades or a single expectation. LifePath India starts with curiosity. Our message is **Every Interest Has a Future.** We offer a welcoming place to explore different career possibilities, without labelling students or predicting what they can become.

**On screen:** `/` — landing page and main navigation.

### 0:40–1:20 — Student onboarding
**Speaker 1:**

> First, we ask students where they are in their learning journey and what interests them. There's no sign-in or sensitive profile required. Their responses stay temporarily in this browser session.

**On screen:** `/onboarding`; select an education stage, one or more interests, a goal. Finish and show the summary.

### 1:20–2:15 — Interest assessment
**Speaker 2:**

> Students then answer six short activity-preference questions. The FastAPI service validates the selected question and option IDs and computes explainable interest signals. The visible timer encourages focus, but this is a reflection activity—not a psychological assessment.

**On screen:** `/interest-assessment`; answer all six. Show the list of signals and supportive disclaimer.

### 2:15–3:05 — Explained career recommendations
**Speaker 2:**

> With one click we connect those signals to an illustrative career catalogue. Recommendations are deterministic: they compare interest tags and explain why each career is suggested. These overlap percentages are not success probabilities or eligibility scores. We deliberately show several possibilities rather than a single prescribed future.

**On screen:** Click **See career suggestions** and scroll to the five options. Open a career profile. Say that a detailed year-by-year roadmap is **not yet included on this branch**.

### 3:05–4:10 — Freedom to change paths
**Speaker 1:**

> Students should be allowed to reconsider. With Change My Path they can explore a different career and confirm their choice without throwing away onboarding or completed interest signals during the active session.

**On screen:** `/change-path`; choose one career, confirm, then choose a different one. Point out selected career and path history.

### 4:10–5:00 — Dashboard and comparison
**Speaker 1:**

> The dashboard brings their current journey together. Students can compare up to three fictional careers side by side—what each career explores, related interests, and skills to develop. There is no hard ranking of which future is best.

**On screen:** `/dashboard`; demonstrate the saved progress and select up to three careers. Try a fourth selection; it remains disabled until a selection is removed.

### 5:00–5:30 — Architecture & honest close
**Speaker 3:**

> Behind the interface is React, TypeScript, Vite and a Python FastAPI backend. Our sample catalogue and interest-scoring service run locally, with no database or third-party API requirement. We also have backend contract and cross-feature smoke tests. This branch does not yet integrate the math-readiness work or the Gemma 4 runtime assistant; those are separate roadmap tasks.

**On screen:** Quickly show `http://localhost:8000/docs` or the README, if time allows.

**Closing line:**

> LifePath India does not tell a student what they must become. It shows them paths worth exploring—because every interest has a future.

## Judge Q&A — accurate answers
- **Is this AI-generated career matching?** No. This branch computes deterministic heuristic interest-tag overlap. Runtime Gemma 4 is planned separately for TASK-014; do not demo or claim it until integrated and tested.
- **What does a 28% score mean?** A normalized overlap score for selected activity signals, not a 28% chance of success.
- **Are there real admission/salary/scholarship statistics?** No. Catalogue content is fictional/illustrative and is labelled as such.
- **Where does student data go?** Onboarding, assessment and selected path are held in React memory, not a database. A full refresh clears them.
- **Can students change direction?** Yes, while navigating the app in the same session.
- **Where is the math readiness feature?** Member 3 owns TASK-009/TASK-010. Those are not integrated into this branch; the dashboard makes that gap explicit.
- **Why React + FastAPI?** Clear separation of an accessible browser interface and validated, testable backend domain logic.

## Live-demo fallbacks
- **Backend unavailable:** Check terminal 1 and GET `/health`, restart Uvicorn; the frontend provides recoverable API errors. Do not pretend offline results are live.
- **Career catalogue temporarily fails:** Open `/careers` after backend restart and use **Try again**.
- **Refresh clears progress:** This is expected; repeat the short onboarding and assessment or use a separate prepared browser tab. Do not describe memory state as database persistence.
- **Unexpected recommendation percentages:** Explain they depend on the six answers and tag overlap; avoid a canned numeric claim.
- **Pressed for roadmap/maths/chatbot:** Point to roadmap and honestly state those are pending branch integration or future tasks.

## Important distinction
A complete hackathon MVP as defined by `.ai/roadmap/MASTER_ROADMAP.md` also requires integrated roadmaps, math readiness, topic improvements and Gemma 4 runtime assistant. Therefore **TASK-020 script readiness is not equivalent to complete product/release readiness**. Finish teammate review, PR merges and tests before claiming the full MVP is delivered.
