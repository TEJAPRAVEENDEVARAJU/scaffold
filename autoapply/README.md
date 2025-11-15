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
   - `npm run dev`
5. Open `http://localhost:3000` for frontend; API at `http://localhost:8000`

## Repo structure

autoapply/
├─ README.md
├─ backend/
│  ├─ app.py
│  ├─ agents/
│  │  ├─ orchestrator.py
│  │  ├─ job_finder.py
│  │  ├─ role_scorer.py
│  │  ├─ personalization.py
│  │  ├─ form_filler.py
│  │  └─ tracker.py
│  ├─ tools/
│  │  ├─ search_tool.py
│  │  └─ browser_tool.py
│  ├─ memory/
│  │  ├─ memory_bank.py
│  │  └─ session_service.py
│  ├─ observability/
│  │  └─ logger.py
│  └─ requirements.txt
├─ frontend/
│  ├─ package.json
│  └─ src/App.jsx
└─ notebooks/
└─ demo_notebook.ipynb (Kaggle Notebook ready)

## Notes
- **No API keys** are included. Use environment variables for keys (e.g., `OPENAI_API_KEY`, `SEARCH_API_KEY`).
- See `docs/deploy.md` for Cloud Run deployment steps.

## How to submit to Kaggle
- Create writeup using the provided pitch & description.
- Link this GitHub repository in the writeup attachments.
- Add the demo YouTube video URL to the media gallery.
