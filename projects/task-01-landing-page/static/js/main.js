/**
 * OpenClaw AI Dev Studio - Interactive JavaScript
 * Handles language switching, state persistence, and responsive UI behaviors.
 */

document.addEventListener("DOMContentLoaded", () => {
    initLanguageSwitcher();
    initSmoothScrolling();
});

/**
 * Initialize Language Switcher with localStorage and cookie persistence.
 */
function initLanguageSwitcher() {
    const langButtons = document.querySelectorAll(".lang-btn");
    const currentLang = document.documentElement.lang || "en";
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get("lang");

    // If query param is explicitly set, update localStorage to match
    if (urlLang && (urlLang === "en" || urlLang === "ru")) {
        try {
            localStorage.setItem("openclaw_lang", urlLang);
            document.cookie = `openclaw_lang=${urlLang};path=/;max-age=2592000;SameSite=Lax`;
        } catch (e) {
            console.warn("Could not save language preference to storage", e);
        }
    } else {
        // If no query param in URL, check if user had a saved preference different from server render
        try {
            const savedLang = localStorage.getItem("openclaw_lang");
            if (savedLang && (savedLang === "en" || savedLang === "ru") && savedLang !== currentLang) {
                const targetUrl = new URL(window.location.href);
                targetUrl.searchParams.set("lang", savedLang);
                window.location.replace(targetUrl.toString());
                return;
            }
        } catch (e) {
            console.warn("Could not read language preference from storage", e);
        }
    }

    // Attach click listeners to language toggle buttons
    langButtons.forEach((btn) => {
        btn.addEventListener("click", (e) => {
            const targetLang = btn.getAttribute("data-lang");
            if (targetLang) {
                try {
                    localStorage.setItem("openclaw_lang", targetLang);
                    document.cookie = `openclaw_lang=${targetLang};path=/;max-age=2592000;SameSite=Lax`;
                } catch (err) {
                    console.warn("Could not save language to storage", err);
                }
            }
        });
    });
}

/**
 * Enhanced smooth scrolling for internal section anchors.
 */
function initSmoothScrolling() {
    const navLinks = document.querySelectorAll('a.nav-link[href^="#"]');
    navLinks.forEach((link) => {
        link.addEventListener("click", (e) => {
            const targetId = link.getAttribute("href");
            if (!targetId || targetId === "#") return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: "smooth",
                    block: "start",
                });
                history.pushState(null, "", targetId);
            }
        });
    });
}
