# AI Career Compass

A student-first career exploration app. Interests and practice matter more than grades.

## Local setup
1. Install Node.js 20+ and MongoDB.
2. Run `npm install`.
3. Copy `.env.example` to `.env.local` and configure the MongoDB URI and a random SESSION_SECRET of at least 32 characters. Keep credentials private.
4. Run `npm run dev`, then visit http://localhost:3000.
5. Run `npm test` for scoring unit tests.

## Features
Registration/login, optional onboarding, career library, beginner roadmaps with saved progress, server-scored timed assessment, project ideas, and optional backend AI mentor.

## Limits and next steps
This is a functional starter MVP, not the complete specification. Career coverage, comparison, mentor chat history, advanced assessments, parent/teacher access, reliable distributed rate limiting, age assurance/consent, deletion/retention workflows, and Playwright end-to-end coverage still require implementation. Career qualification statements are exploratory, not verified legal/eligibility guidance. For production, configure MongoDB unique indexes (especially users.email and progress userId+careerId+phase), HTTPS, a shared rate limiter and appropriate privacy review for minors. Do not deploy to students before privacy and security review.
