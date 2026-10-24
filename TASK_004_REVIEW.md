# TASK-004 — Student Onboarding (Member 1)

Branch: `task3`, created from the reviewed `task2` branch. No Member 2/3 backend files were modified.

## Implemented
- Accessible three-step React onboarding journey at `/onboarding`.
- Step 1: education level (Class 8–12, Diploma, College), required.
- Step 2: one or more interests (required) and favourite subjects (optional).
- Step 3: primary exploration goal (required), optional career idea text required only if that particular goal is chosen.
- Clear validation errors; previous/next navigation; editable completion summary; clear answers.
- Shared typed React context for temporary profile state, usable by later dashboard/path features.
- Landing and header Get Started links now lead to the onboarding route.
- Responsive layout, keyboard-friendly semantic form controls and focus styles.

## Boundaries and privacy
- No name, email, phone, marks, sensitive traits or account information collected.
- No backend profile route, database or persistence. Data exists only in React memory while app stays loaded; refresh clears it.
- No fake career recommendation or assessment functionality.
- This is TASK-004 only; Member 2 owns interest scoring and Member 3 owns maths scoring.

## Run locally on Windows
From the repository root:
```powershell
git fetch origin
git switch --track origin/task3
cd frontend
npm install
npm run build
npm run dev
```
If `task3` already exists locally, use `git switch task3`. Open http://localhost:5173/onboarding .

## Manual acceptance checklist
- [ ] The home/header CTAs open onboarding.
- [ ] Cannot continue without choosing education level.
- [ ] Can select multiple interests, and cannot continue with none.
- [ ] Subject selection is optional.
- [ ] Goal is required; career text is required only when goal is 'I have a career in mind'.
- [ ] Previous step preserves selected answers.
- [ ] Completing shows accurate summary and allows editing/clearing.
- [ ] Navigating to home and back during the same mounted app retains the profile.
- [ ] Refresh clears profile (explicit temporary-state behaviour).
- [ ] Mobile sizing, keyboard navigation and validation messages work.
- [ ] `npm run build` succeeds and API health status on the landing page still works.

## Verification status
GitHub files were committed and fetched for a basic inspection. Build/browser interaction tests were not run within this environment; do not mark the task done until locally verified.
