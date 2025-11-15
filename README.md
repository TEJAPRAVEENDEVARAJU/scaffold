# AutoApply — Multi-Agent Job Application Assistant

## Overview
AutoApply automates job discovery, tailored resume & cover letter generation, and application tracking.
It’s a multi-agent system built with ADK-Python demonstrating sequential & parallel agents, tools, sessions & memory, observability, and agent evaluation.

## Features
- Job discovery (web search + scraping)
- Role scoring & filtering
- Tailored CV and cover letter generation (LLM)
- Form-filling automation stub (Playwright / Puppeteer)
- Application tracking (CSV / Google Sheet)
- Memory: session + long-term memory (Memory Bank)
- Observability: structured logging & basic metrics
- Optional: A/B evaluation for cover letter variants

## Tech stack
- Backend: Python + ADK-Python + FastAPI
- Frontend: React + Tailwind (starter)
- Browser automation: Playwright (recommended)
- DB / Storage: SQLite for demo, optional Postgres
- Deployment: Cloud Run (backend), Vercel (frontend) recommended

## Quickstart (local)
1. Clone repository
2. Create virtual env: `python -m venv venv && source venv/bin/activate`
3. Backend:

   - `cd backend`
   - `pip install -r requirements.txt`
   - `uvicorn app:app --reload --port 8000`
4. Frontend:
   - `cd frontend`
   - `npm install`
   - `npm run dev
5. Open `http://localhost:3000` for frontend; API at `http://localhost:8000`

## Repo structure

<img width="1024" height="1536" alt="ChatGPT Image Nov 15, 2025, 10_28_25 AM" src="https://github.com/user-attachments/assets/6462bd21-d9e8-48f0-b1fb-e219b318c161" />

<img width="1536" height="1024" alt="ChatGPT Image Nov 15, 2025, 10_32_32 AM" src="https://github.com/user-attachments/assets/d528463b-ac3d-402f-b112-c9dc5a940cc0" /> 
