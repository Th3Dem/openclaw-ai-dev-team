from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from app import LOCALIZATION_DATA, app, get_landing_context


@pytest.fixture
def client() -> TestClient:
    """Create a FastAPI TestClient instance."""
    return TestClient(app)


class TestLandingPageApp:
    """Test suite for OpenClaw AI Dev Team Landing Page FastAPI application."""

    def test_localization_data_integrity(self) -> None:
        """Verify supported languages and essential keys in LOCALIZATION_DATA."""
        assert "en" in LOCALIZATION_DATA
        assert "ru" in LOCALIZATION_DATA
        assert LOCALIZATION_DATA["en"]["lang_code"] == "en"
        assert LOCALIZATION_DATA["ru"]["lang_code"] == "ru"

    def test_get_landing_context_default_en(self) -> None:
        """Verify the data structure returned by get_landing_context for English default."""
        context = get_landing_context("en")
        assert isinstance(context, dict)
        assert context["lang"] == "en"
        assert context["lang_code"] == "en"
        assert context["app_name"] == "OpenClaw AI Dev Team"
        assert "version" in context
        assert "metrics" in context
        assert "team_roster" in context
        assert "capabilities" in context
        assert "workflow" in context
        assert "roster" in context
        assert "trust" in context

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
        assert len(context["capabilities"]) >= 6

    def test_get_landing_context_russian(self) -> None:
        """Verify the data structure returned by get_landing_context for Russian."""
        context = get_landing_context("ru")
        assert isinstance(context, dict)
        assert context["lang"] == "ru"
        assert context["lang_code"] == "ru"
        assert "Инженерная команда OpenClaw AI" in context["html_title"]
        assert context["nav"]["overview"] == "Обзор"
        assert context["hero"]["metrics"]["velocity_label"] == "Скорость поставки"
        assert context["workflow"]["title"] == "Автономный процесс поставки"

        # Verify all 5 bots in Russian roster
        bot_ids = {agent["id"] for agent in context["team_roster"]}
        expected_bots = {"pm_bot", "dev_bot", "py_bot", "qa_bot", "git_bot"}
        assert expected_bots.issubset(bot_ids)

        # Verify 6 capabilities in Russian
        assert len(context["capabilities"]) == 6
        cap_titles = [item["title"] for item in context["capabilities"]]
        assert "Высоконагруженные Go-бэкенды" in cap_titles
        assert "Асинхронные микросервисы на FastAPI" in cap_titles

        # Verify trust matrix
        assert len(context["trust"]["rows"]) == 6
        assert context["trust"]["col_adv"] == "Преимущество"

    def test_get_landing_context_invalid_lang_fallback(self) -> None:
        """Verify invalid language code falls back safely to English."""
        context = get_landing_context("fr")
        assert context["lang"] == "en"
        assert context["lang_code"] == "en"

    def test_index_page_english_default(self, client: TestClient) -> None:
        """Verify the root index page returns 200 OK and valid English HTML content."""
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        html = response.text

        # Verify HTML document structure & lang
        assert "<!DOCTYPE html>" in html
        assert '<html lang="en">' in html
        assert "OpenClaw AI Engineering Team" in html

        # Verify Section 1: Hero Section (EN)
        assert 'id="hero"' in html
        assert "Human Ingenuity. Autonomous Precision." in html
        assert "Studio-Grade Output at 10x Velocity." in html
        assert "Delivery Velocity" in html
        assert "QA Gatekeeper Pass" in html

        # Verify Section 2: Workflow (EN)
        assert 'id="workflow"' in html
        assert "The Autonomous Delivery Flow" in html
        assert "Least Privilege Security Architecture" in html
        assert "TASK-XX.md" in html

        # Verify Section 3: Team Roster (EN)
        assert 'id="roster"' in html
        assert "Autonomous Team Roster" in html
        assert "Paula" in html
        assert "dev_bot" in html
        assert "py_bot" in html
        assert "qa_bot" in html
        assert "git_bot" in html

        # Verify Section 4: Capabilities (EN)
        assert 'id="capabilities"' in html
        assert "High-Load Go Backends" in html
        assert "FastAPI Async Microservices" in html

        # Verify Section 5: Analytics & Trust Matrix (EN)
        assert 'id="trust"' in html
        assert "AI Team vs Traditional Development" in html
        assert "10x Faster" in html
        assert "Zero-Trust" in html

        # Verify Language switcher presence
        assert 'id="langSwitcher"' in html
        assert 'href="/?lang=en"' in html
        assert 'href="/?lang=ru"' in html

    def test_index_page_english_explicit(self, client: TestClient) -> None:
        """Verify the index page with ?lang=en returns English content."""
        response = client.get("/?lang=en")
        assert response.status_code == 200
        assert '<html lang="en">' in response.text
        assert "Autonomous Multi-Agent Software Engineering" in response.text
        assert "The Autonomous Delivery Flow" in response.text

    def test_index_page_russian(self, client: TestClient) -> None:
        """Verify the index page with ?lang=ru returns valid Russian HTML content across all 5 sections."""
        response = client.get("/?lang=ru")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        html = response.text

        # Verify HTML document structure & lang
        assert "<!DOCTYPE html>" in html
        assert '<html lang="ru">' in html
        assert "Инженерная команда OpenClaw AI" in html

        # Verify Section 1: Hero Section (RU)
        assert 'id="hero"' in html
        assert "ПАРАДИГМА НОВОГО ПОКОЛЕНИЯ" in html
        assert "Человеческий замысел. Автономная точность." in html
        assert "Результат студийного уровня с 10-кратной скоростью." in html
        assert "Скорость поставки" in html
        assert "Прохождение QA-контроля" in html
        assert "Ошибочных коммитов в main" in html
        assert "Непрерывная готовность" in html

        # Verify Section 2: Workflow (RU)
        assert 'id="workflow"' in html
        assert "ДЕТЕРМИНИРОВАННЫЙ ПАЙПЛАЙН" in html
        assert "Автономный процесс поставки" in html
        assert "Архитектура безопасности на базе наименьших привилегий" in html
        assert "ИЗОЛЯЦИЯ РАЗРАБОТКИ" in html
        assert "НЕЗАВИСИМЫЙ АУДИТ" in html
        assert "НЕИЗМЕНЯЕМЫЙ АУДИТ" in html

        # Verify Section 3: Team Roster (RU)
        assert 'id="roster"' in html
        assert "Состав автономной команды" in html
        assert "Ведущий архитектор и Product Owner" in html
        assert "Пола" in html
        assert "Дев" in html
        assert "Алекс" in html
        assert "Хранитель релизов" in html

        # Verify Section 4: Capabilities (RU)
        assert 'id="capabilities"' in html
        assert "Возможности и инженерный стек" in html
        assert "Высоконагруженные Go-бэкенды" in html
        assert "Асинхронные микросервисы на FastAPI" in html
        assert "Telegram-боты и автоматизация" in html
        assert "Оркестрация серверов Docker и SSH" in html
        assert "Автоматизированные CI/CD пайплайны качества" in html

        # Verify Section 5: Analytics & Trust Matrix (RU)
        assert 'id="trust"' in html
        assert "ИИ-команда против традиционной разработки" in html
        assert "Критерий оценки" in html
        assert "В 10 раз быстрее" in html
        assert "0 Дефектов" in html

        # Verify cookie is set
        assert "openclaw_lang=ru" in response.headers.get("set-cookie", "")

    def test_index_page_cookie_persistence(self, client: TestClient) -> None:
        """Verify that openclaw_lang cookie dictates language when query param is absent."""
        response = client.get("/", cookies={"openclaw_lang": "ru"})
        assert response.status_code == 200
        assert '<html lang="ru">' in response.text
        assert "Автономный процесс поставки" in response.text

    def test_index_page_invalid_param_fallback(self, client: TestClient) -> None:
        """Verify that unsupported lang query param safely falls back to English."""
        response = client.get("/?lang=invalid_lang_code")
        assert response.status_code == 200
        assert '<html lang="en">' in response.text
        assert "Human Ingenuity. Autonomous Precision." in response.text

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
        assert "supported_languages" in data
        assert "en" in data["supported_languages"]
        assert "ru" in data["supported_languages"]

    def test_static_css_served(self, client: TestClient) -> None:
        """Verify that the CSS static asset is served properly."""
        response = client.get("/static/css/style.css")
        assert response.status_code == 200
        assert "text/css" in response.headers["content-type"]
        assert "--bg-primary" in response.text
        assert ".lang-switcher" in response.text

    def test_static_js_served(self, client: TestClient) -> None:
        """Verify that the JavaScript static asset is served properly."""
        response = client.get("/static/js/main.js")
        assert response.status_code == 200
        assert (
            "text/javascript" in response.headers["content-type"]
            or "application/javascript" in response.headers["content-type"]
        )
        assert "initLanguageSwitcher" in response.text

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
