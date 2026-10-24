# TASK-003 — Member 1 review checklist

Branch: `task2`, based on `task1`. This task extends the existing React/Vite starter. The FastAPI backend, health contract, approved dependencies and API client are preserved.

## Delivered
- Responsive sticky header and accessible mobile navigation.
- Shared visual design tokens expressed in plain CSS: navy, teal, amber accents, white/blue-gray backgrounds.
- Modern landing hero, informational journey section, illustrative career clusters, and final CTA.
- Consistent footer, 404 screen, keyboard focus styling, reduced-motion handling.
- Existing backend health indicator remains wired via `getHealth`.

## Scope boundaries
- No new dependencies.
- No onboarding forms, career assessment logic, career endpoints or user persistence.
- CTA buttons point to implemented on-page sections; they do **not** pretend student onboarding exists.
- Existing `.ai/` documents and other members' work are untouched.

## Review locally
From repository root:
```powershell
git fetch origin
git switch --track origin/task2
cd frontend
npm install
npm run build
npm run dev
```
If you already have `task2` locally, use `git switch task2` instead. Open `http://localhost:5173`.

1. View desktop and mobile widths (browser dev tools).
2. Verify Menu opens/closes on narrow screens.
3. Click Home, How it works, Explore paths and Get started — they must land on real page sections.
4. Use keyboard Tab to inspect visible focus indicators.
5. Start backend from `backend/` and verify the API indicator becomes Connected.
6. Run frontend build (`npm run build`) and backend tests (`python -m pytest -q` from backend).

## Verification
GitHub file writes and existence can be verified. Build, visual browser review, and local API connectivity are **not verified in this environment**. Do not mark TASK-003 complete until the teammate runs checks and reviews the UI.

## Next
After user approval and a reviewed merge, TASK-004 is the next Member 1 feature. It must follow shared student-state contracts.
