# Task Assignment: Landing Page Presenting AI Dev Team & Services

## Metadata
- **Task ID:** TASK-01
- **Project:** AI Dev Team Landing Page (`projects/task-01-landing-page`)
- **Assigned to:** py_bot (Alex 🐍)
- **Assigned by:** pm_bot (Paula 📋)
- **Date:** 2026-08-17
- **Priority:** HIGH
- **Status:** COMPLETED
- **Reviewer:** qa_bot (QA 🔍)
- **Release Owner:** git_bot (Git 🌿)

---

## 1. Objective
Develop a high-converting, static informational landing page presented as a single-page app served via FastAPI, showcasing the AI Engineering Team (Human + 5 AI Bots), their synergy, workflows, roles, capabilities, and trust metrics.

---

## 2. Requirements & Scope

### 🛑 Hard Constraints
- **Static Informational Page Only:** NO interactive buttons, submit forms, or clickable CTA popups/links that lead to unfinished handlers.
- **Design & Presentation:** Modern, clean, studio-grade aesthetic, balanced typography, responsive layout, clear information hierarchy.
- **All 5 Core Sections Must Be Included:**
  1. **Hero Section:** Human + AI engineering synergy. Core concept: 1 lead dev + 5 autonomous AI bots = studio-grade output. Key metrics: 10x velocity, 100% QA pass rate, 0 bad commits.
  2. **Workflow (Automated Flow):** Step-by-step visual diagram/description: `User/Idea -> pm_bot (Task Decomposition) -> dev_bot / py_bot (Code & Tests) -> qa_bot (Security & Audit) -> git_bot (PR & Release)`. Explanation of the Least Privilege security model.
  3. **Team Roster:** Full profiles for the 5 agents:
     - `pm_bot` (Paula) — Project Manager & Orchestrator
     - `dev_bot` (Dev) — Lead Golang Developer (High-load, Concurrency)
     - `py_bot` (Alex) — Python Developer (FastAPI, Docker/SSH Automation, Telegram)
     - `qa_bot` (QA) — Quality Gatekeeper & Security Auditor (Linters, SAST, Bug Hunter)
     - `git_bot` (Git) — Release Manager & GitHub Operations Guardian
  4. **Capabilities & Services:** High-load Go backends, FastAPI microservices, Telegram bots, Docker/SSH automation, automated CI/CD pipelines.
  5. **Analytics & Trust (AI vs Classic Dev Matrix):** Comparative matrix comparing AI-driven dev team vs classic outsourced/in-house dev across Speed/Velocity, Test Coverage, Security, Cost Efficiency, and Predictability.

---

## 3. Architecture & Technical Stack (py_bot)

- **Backend:** FastAPI, Uvicorn, Jinja2 / StaticFiles.
- **Frontend:** Clean semantic HTML5, Vanilla CSS (responsive, modern dark/light balanced theme, no bloated external dependencies), minimal UI enhancement JS.
- **Testing:** Comprehensive `pytest` test suite covering routes, template rendering, and error handling with target **coverage ≥ 80%**.
- **Containerization:** Production-ready `Dockerfile` to build and run the landing page container.
- **Documentation:** Produce `DEV_HANDOVER.md` with test output, lint results, and deployment instructions.

---

## 4. Definition of Done (Done-Done)
1. FastAPI application runs cleanly and serves the landing page with all 5 sections.
2. Code follows `shared/PYTHON_STANDARDS.md` (`black`, `flake8`, `mypy`).
3. `pytest` passes with $\ge 80\%$ test coverage.
4. `Dockerfile` builds and runs successfully in Docker.
5. `DEV_HANDOVER.md` is generated and handed over to `qa_bot` for security/quality audit.
6. Upon `qa_bot` APPROVAL, `git_bot` creates branch `feat/task-01-landing-page`, commits, pushes, and opens PR.

---

## 5. Required Reading for py_bot
- `shared/PYTHON_STANDARDS.md`
- `shared/HANDOVER_PROTOCOL.md`
