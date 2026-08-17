# OpenClaw AI Dev Team Landing Page (TASK-01)

A high-converting, studio-grade static informational landing page served by FastAPI, showcasing the OpenClaw AI Engineering Team (1 Lead Engineer + 5 Autonomous AI Bots), their synergy, workflows, roles, capabilities, and trust metrics.

---

## Architecture & Technical Stack

- **Backend:** FastAPI (Python 3.12+), Uvicorn, Jinja2 Templates, StaticFiles
- **Frontend:** Semantic HTML5, Studio-Grade Cyber-Engineering Dark Theme CSS (pure CSS, responsive, glassmorphism, no external JS/framework bloat)
- **Quality & Standards:** Pytest, pytest-cov (100% test coverage), black, flake8, mypy
- **Containerization:** Production Dockerfile (python:3.12-slim, non-root user, healthcheck)

---

## Core Sections

1. **Hero Section:** Human + AI engineering synergy (1 dev + 5 autonomous bots = studio-grade output, 10x velocity, 100% QA pass rate, 0 bad commits on main).
2. **Workflow (Automated Flow):** Visual, deterministic delivery pipeline (`User/Idea -> pm_bot -> dev_bot / py_bot -> qa_bot -> git_bot`) with the Least Privilege security model.
3. **Team Roster:** Full profiles & skills for `pm_bot` (Paula), `dev_bot` (Dev), `py_bot` (Alex), `qa_bot` (QA), `git_bot` (Git), and Lead Human Architect.
4. **Capabilities:** High-load Go backends, FastAPI microservices, Telegram bots, Docker/SSH automation, automated CI/CD pipelines.
5. **Analytics & Trust:** Comprehensive comparison matrix comparing AI-driven dev team vs classic outsourced/in-house development.

---

## Running Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

### 3. Run Tests and Linters
```bash
# Run pytest with coverage report
pytest -v --cov=. --cov-report=term-missing

# Code formatting check
black --check .

# Linting check
flake8 .

# Type checking
mypy .
```

---

## Docker Deployment

### Build Container
```bash
docker build -t openclaw-landing-page:latest .
```

### Run Container
```bash
docker run -d -p 8000:8000 --name openclaw-landing openclaw-landing-page:latest
```
Check health:
```bash
curl http://localhost:8000/health
```
