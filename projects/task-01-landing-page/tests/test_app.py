from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from app import app, get_landing_context


@pytest.fixture
def client() -> TestClient:
    """Create a FastAPI TestClient instance."""
    return TestClient(app)


class TestLandingPageApp:
    """Test suite for OpenClaw AI Dev Team Landing Page FastAPI application."""

    def test_get_landing_context_structure(self) -> None:
        """Verify the data structure returned by get_landing_context."""
        context = get_landing_context()
        assert isinstance(context, dict)
        assert context["app_name"] == "OpenClaw AI Dev Team"
        assert "version" in context
        assert "metrics" in context
        assert "team_roster" in context
        assert "capabilities" in context

        # Check metrics
        metrics = context["metrics"]
        assert metrics["velocity"] == "10x"
        assert metrics["qa_pass_rate"] == "100%"
        assert metrics["bad_commits"] == "0"
        assert metrics["uptime_readiness"] == "24/7"

        # Check all 5 bots are in team roster
        bot_ids = {agent["id"] for agent in context["team_roster"]}
        expected_bots = {"pm_bot", "dev_bot", "py_bot", "qa_bot", "git_bot"}
        assert expected_bots.issubset(bot_ids)

        # Check capabilities count
        assert len(context["capabilities"]) >= 5

    def test_index_page_success(self, client: TestClient) -> None:
        """Verify the root index page returns 200 OK and valid HTML content."""
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        html = response.text

        # Verify HTML document structure
        assert "<!DOCTYPE html>" in html
        assert "OpenClaw AI Engineering Team" in html

        # Verify Section 1: Hero Section
        assert 'id="hero"' in html
        assert "10x Velocity" in html or "10x" in html
        assert "100%" in html
        assert "Bad Commits" in html

        # Verify Section 2: Workflow (Automated Flow)
        assert 'id="workflow"' in html
        assert "The Autonomous Delivery Flow" in html
        assert "Least Privilege Security Architecture" in html
        assert "TASK-XX.md" in html

        # Verify Section 3: Team Roster
        assert 'id="roster"' in html
        assert "Autonomous Team Roster" in html
        assert "Paula" in html
        assert "dev_bot" in html
        assert "py_bot" in html
        assert "qa_bot" in html
        assert "git_bot" in html

        # Verify Section 4: Capabilities
        assert 'id="capabilities"' in html
        assert (
            "Capabilities &amp; Engineering Stack" in html
            or "Capabilities & Engineering Stack" in html
        )
        assert "High-Load Go Backends" in html
        assert "FastAPI Async Microservices" in html

        # Verify Section 5: Analytics & Trust Matrix
        assert 'id="trust"' in html
        assert "AI Team vs Traditional Development" in html
        assert "Delivery Velocity" in html
        assert "Test Coverage &amp; Rigor" in html or "Test Coverage & Rigor" in html

    def test_health_check_endpoint(self, client: TestClient) -> None:
        """Verify the healthcheck endpoint returns 200 and expected telemetry JSON."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["service"] == "openclaw-ai-landing-page"
        assert data["version"] == "1.0.0"
        assert data["agents_active"] == 5
        assert data["security_model"] == "least_privilege"

    def test_static_css_served(self, client: TestClient) -> None:
        """Verify that the CSS static asset is served properly."""
        response = client.get("/static/css/style.css")
        assert response.status_code == 200
        assert "text/css" in response.headers["content-type"]
        assert "--bg-primary" in response.text
        assert ".hero-title" in response.text

    def test_custom_404_handler(self, client: TestClient) -> None:
        """Verify the custom 404 handler returns a styled not-found page with 404 status."""
        response = client.get("/non-existent-route-endpoint")
        assert response.status_code == 404
        assert "text/html" in response.headers["content-type"]
        assert "404 ERROR" in response.text
        assert "Endpoint Not Found" in response.text
        assert "/non-existent-route-endpoint" in response.text

    def test_custom_404_handler_xss_protection(self, client: TestClient) -> None:
        """Verify that malicious XSS payload in 404 URL is safely escaped."""
        response = client.get("/<script>alert(1)</script>")
        assert response.status_code == 404
        assert "<script>" not in response.text
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in response.text

