from __future__ import annotations

import html
import logging
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("openclaw.landing")

# Directory paths
BASE_DIR: Path = Path(__file__).resolve().parent
STATIC_DIR: Path = BASE_DIR / "static"
TEMPLATES_DIR: Path = BASE_DIR / "templates"

# Create FastAPI application
app = FastAPI(
    title="OpenClaw AI Engineering Team",
    description="Showcase landing page for the autonomous AI development team",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
)

# Ensure static & templates directory exist before mounting
STATIC_DIR.mkdir(parents=True, exist_ok=True)
(STATIC_DIR / "css").mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

# Mount static files and initialize templates
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


def get_landing_context() -> Dict[str, Any]:
    """Provide structured context data for the landing page template."""
    return {
        "app_name": "OpenClaw AI Dev Team",
        "app_tagline": "1 Lead Engineer + 5 Autonomous AI Bots = Studio-Grade Output",
        "version": "1.0.0",
        "metrics": {
            "velocity": "10x",
            "qa_pass_rate": "100%",
            "bad_commits": "0",
            "uptime_readiness": "24/7",
        },
        "team_roster": [
            {
                "id": "pm_bot",
                "name": "Paula",
                "role": "Project Manager & Orchestrator",
                "icon": "📋",
                "badge": "Orchestration",
                "description": (
                    "Deconstructs raw user ideas into rigorous specifications, defines acceptance "
                    "criteria, maps dependencies, and maintains immutable WORKLOG audit trails."
                ),
                "skills": [
                    "Task Decomposition (TASK-XX.md)",
                    "Dependency Analysis",
                    "Sprint Governance",
                    "WORKLOG Maintenance",
                ],
            },
            {
                "id": "dev_bot",
                "name": "Dev",
                "role": "Lead Golang Developer",
                "icon": "⚡",
                "badge": "High-Load Go",
                "description": (
                    "Engineers ultra-high-throughput Go backend services, concurrent pipelines, "
                    "gRPC microservices, and memory-safe systems with strict race condition testing."
                ),
                "skills": [
                    "Golang 1.22+ Concurrency",
                    "High-Throughput gRPC / REST",
                    "Memory Optimization",
                    "go test -race Verification",
                ],
            },
            {
                "id": "py_bot",
                "name": "Alex",
                "role": "Python Developer",
                "icon": "🐍",
                "badge": "FastAPI & DevOps",
                "description": (
                    "Builds production-grade FastAPI microservices, Telegram bot architectures, "
                    "Docker/SSH automation workflows, and comprehensive Pytest suites."
                ),
                "skills": [
                    "FastAPI & AsyncIO",
                    "Docker & SSH Orchestration",
                    "Telegram Bot Architecture",
                    "Pytest (≥80% Coverage)",
                ],
            },
            {
                "id": "qa_bot",
                "name": "QA",
                "role": "Quality Gatekeeper & Security Auditor",
                "icon": "🔍",
                "badge": "Quality & SAST",
                "description": (
                    "Enforces strict zero-defect policy: runs static analysis, coverage audits "
                    "(≥80% gate), SAST security scans, CVE dependency checks, and formal QA reports."
                ),
                "skills": [
                    "flake8 / golangci-lint",
                    "SAST & Vulnerability Auditing",
                    "≥80% Coverage Gatekeeping",
                    "QA_REPORT Formal Sign-Off",
                ],
            },
            {
                "id": "git_bot",
                "name": "Git",
                "role": "Release Manager & Git Guardian",
                "icon": "🌿",
                "badge": "Release Guardian",
                "description": (
                    "Guards repository integrity: creates isolated feat/* branches, enforces atomic "
                    "clean commits, generates pull requests, tags semantic releases, and prevents bad code on main."
                ),
                "skills": [
                    "Isolated Branching (feat/*)",
                    "Atomic Commit Integrity",
                    "Pull Request Generation",
                    "Zero Bad Commits on Main",
                ],
            },
        ],
        "capabilities": [
            {
                "title": "High-Load Go Backends",
                "icon": "⚡",
                "description": (
                    "Ultra-fast compiled Golang services designed for thousands of concurrent requests, "
                    "minimal memory footprints, and low-latency gRPC/HTTP interfaces."
                ),
            },
            {
                "title": "FastAPI Async Microservices",
                "icon": "🐍",
                "description": (
                    "Modern, typed, self-documenting asynchronous REST APIs powered by Pydantic v2 "
                    "and FastAPI with automated OpenAPI contracts."
                ),
            },
            {
                "title": "Telegram Bots & Automation",
                "icon": "🤖",
                "description": (
                    "Interactive, stateful, and asynchronous bot solutions for customer support, "
                    "team notifications, monitoring, and automated event triggers."
                ),
            },
            {
                "title": "Docker & SSH Server Orchestration",
                "icon": "🐳",
                "description": (
                    "Lightweight, multi-stage production container builds, secure sudo command management, "
                    "and automated remote host configuration."
                ),
            },
            {
                "title": "Automated CI/CD Quality Pipelines",
                "icon": "🛡️",
                "description": (
                    "Multi-tier quality gates combining linters, type checkers, race detectors, "
                    "vulnerability scanners, and test coverage mandates."
                ),
            },
            {
                "title": "Least Privilege Security Governance",
                "icon": "🔒",
                "description": (
                    "Sandboxed bot roles where developers write code, QA audits quality, and only "
                    "the release guardian merges to protected branches."
                ),
            },
        ],
    }


@app.get("/", response_class=HTMLResponse)
async def get_index_page(request: Request) -> HTMLResponse:
    """Serve the landing page."""
    logger.info(
        "Serving landing page request from %s",
        request.client.host if request.client else "unknown",
    )
    context = get_landing_context()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context,
    )


@app.get("/health", response_class=JSONResponse)
async def get_health_status(request: Request) -> JSONResponse:
    """Healthcheck endpoint verifying service status and telemetry."""
    logger.info(
        "Health check requested from %s",
        request.client.host if request.client else "unknown",
    )
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "service": "openclaw-ai-landing-page",
            "version": "1.0.0",
            "agents_active": 5,
            "security_model": "least_privilege",
        },
    )


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: Exception) -> HTMLResponse:
    """Custom 404 handler returning styled not-found page."""
    safe_path = html.escape(request.url.path)
    logger.warning("404 Not Found: %s", request.url.path)
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found | OpenClaw AI Dev Team</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body class="error-page">
    <div class="error-container">
        <div class="error-badge">404 ERROR</div>
        <h1>Endpoint Not Found</h1>
        <p>The requested route <code>{safe_path}</code> does not exist on this server.</p>
        <a href="/" class="btn-return">Return to Landing Page</a>
    </div>
</body>
</html>"""
    return HTMLResponse(content=content, status_code=404)
