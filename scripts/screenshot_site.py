"""Take screenshots of the GitHub Pages site for layout review"""
from playwright.sync_api import sync_playwright
from pathlib import Path

SITE_URL = "https://digital-ai-finance.github.io/neural-networks-introduction/"
OUTPUT_DIR = Path(__file__).parent.parent / "screenshots"
OUTPUT_DIR.mkdir(exist_ok=True)

VIEWPORTS = {
    "desktop": {"width": 1920, "height": 1080},
    "laptop": {"width": 1366, "height": 768},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 812},
}

PAGES = [
    ("home", ""),
    ("lecture2", "Lecture-2-Perceptron-Fundamentals"),
    ("glossary", "Glossary"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for viewport_name, viewport_size in VIEWPORTS.items():
        context = browser.new_context(viewport=viewport_size)
        page = context.new_page()

        for page_name, page_path in PAGES:
            url = f"{SITE_URL}{page_path}"
            print(f"Capturing {page_name} at {viewport_name}...")

            page.goto(url)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1000)  # Extra wait for images

            # Full page screenshot
            filename = f"{page_name}_{viewport_name}.png"
            page.screenshot(path=str(OUTPUT_DIR / filename), full_page=True)
            print(f"  Saved: {filename}")

        context.close()

    browser.close()

print(f"\nScreenshots saved to: {OUTPUT_DIR}")
