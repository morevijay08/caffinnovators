# TASK-014 Ollama timeout follow-up

Fix branch `fix/task15-ollama-timeout` based on `task15`.

## Code changes
- Increased the backend Ollama request timeout from 30 to 180 seconds (connect timeout 10 seconds) to accommodate slow local loading/generation.
- Reduced generation cap from 450 to 200 tokens and requested a ten-minute model keep-alive.
- Improved timeout feedback; no fake AI replies or fallback model.

## Important: Windows command not found is not fixed by repository code
If PowerShell says `ollama : The term 'ollama' is not recognized`, install Ollama from https://ollama.com/download/windows and fully restart VS Code, or run the installed binary directly:

```powershell
Test-Path "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" --version
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" list
```

If Test-Path returns False, Ollama may not be installed or may have been installed to another location. Check the installer rather than changing application code. The backend requires a running Ollama service and a verified installed Gemma 4 model tag to produce a real reply.

## Test this branch
```powershell
cd C:\Users\Admin\Desktop\caffinnovators
git status
git fetch origin
git switch --track origin/fix/task15-ollama-timeout
cd backend
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```

Use `git switch fix/task15-ollama-timeout` if it already exists locally. Test `http://localhost:5173/career-assistant` with the separately running frontend. The first answer can still be slow; an increased timeout does not resolve missing Ollama, model not installed or insufficient hardware.

**Verification:** Changes pushed to GitHub; local tests and actual model response not yet observed. No merge into task15/integration/main.
