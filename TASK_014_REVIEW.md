# TASK-014 — Gemma 4 Career Assistant (Member 2)

Branch: `task15`, based on `task14`. Approved runtime architecture: React → FastAPI → local Ollama → configured Gemma model. No database, external hosted provider or additional Python/npm dependencies.

## Implementation
- `POST /api/v1/career-assistant`, request `{message, conversation_history?}`, response `{answer, model, disclaimer}`.
- Pydantic validation: trim and reject empty/overlong messages (max 2000); at most 10 history messages, user/assistant roles only. Client cannot inject a system-role message.
- Fixed backend system prompt discourages invented admissions/fees/salaries, sensitive student details and career determinism; model output remains fallible AI guidance.
- Async `httpx` Ollama `/api/chat` with `stream:false`, 30-second bounded timeout (5-second connect), bounded output tokens, configurable `GEMMA_MODEL` and `OLLAMA_BASE_URL`.
- Safe API error mapping: 503 unavailable, 504 timeout, 502 empty or malformed model reply. No fake responses when Ollama is down.
- New `/career-assistant` React route and navigation, typed Fetch client, accessible conversation, disabled controls while loading, retry by preserving text after errors, temporary in-page history and clear action.
- Mocked API tests cover input validation, safe failure paths, and forwarding only validated conversational roles to Ollama.
- No changes to deterministic recommendation scoring or Member 3 features.

## Ollama setup (required only for assistant chat)

1. Install Ollama on your machine via its official installer.
2. Confirm `ollama --version` and `ollama list` in a terminal.
3. Obtain an **available official Gemma 4 model tag** supported by the installed Ollama version and your hardware. The .ai contract proposes `gemma4:e2b` as an initial configuration; this tag **must be verified locally**, not assumed to exist. Run `ollama pull <your-verified-tag>` and confirm `ollama list`.
4. Start Ollama (or confirm its background service is running) and configure the backend before starting Uvicorn:

```powershell
$env:OLLAMA_BASE_URL="http://localhost:11434"
$env:GEMMA_MODEL="<your-verified-tag>"
```

If `gemma4:e2b` exists in your installed Ollama and fits your hardware, it can be used directly. Do not silently substitute Gemma 3 or an unrelated model and label it Gemma 4.

## Windows testing

```powershell
cd C:\Users\Admin\Desktop\caffinnovators
git status
git fetch origin
git switch --track origin/task15
```
Use `git switch task15` if it already exists locally; save changes before switching.

**Backend terminal:**

```powershell
cd C:\Users\Admin\Desktop\caffinnovators\backend
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```

**Frontend terminal:**

```powershell
cd C:\Users\Admin\Desktop\caffinnovators\frontend
npm install
npm run build
npm run dev
```

Open `http://localhost:5173/career-assistant` and ask about two interests. The `/docs` endpoint at `http://localhost:8000/docs` shows the chat contract.

## Acceptance checks

- [ ] Existing backend tests pass; new mocked assistant tests pass without needing Ollama.
- [ ] Frontend TypeScript `npm run build` passes.
- [ ] API returns HTTP 422 for blank, oversized or system-role history messages.
- [ ] When Ollama is stopped, an unavailable-model error appears (not an invented response).
- [ ] Start Ollama with a verified **Gemma 4** model; send a question and verify real model answer.
- [ ] Continue conversation, verifying short history is provided and answers remain cautious.
- [ ] Clear conversation and check no old messages remain.
- [ ] Narrow viewport, keyboard navigation and polite loading/error feedback work.
- [ ] No personal details, prompts or API keys are logged/stored by the app as a database.
- [ ] Career Explorer/recommendations still work without Ollama.

## Limitations
- A prompt can reduce hallucinations but cannot guarantee factual accuracy; always check official sources for real-world requirements.
- No server-persisted session: chat is React memory and clears on refresh.
- Local inference depends on Ollama, a compatible **Gemma 4** tag, available hardware, and model download. Mock tests do not prove live inference.
- Neither live Ollama availability nor frontend build/pytest execution was verified by this assistant. Full acceptance requires user review and team failure-path test coordination; no integration/main merge occurred.
