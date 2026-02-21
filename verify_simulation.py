from playwright.sync_api import sync_playwright
import os
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Construct file URL
        cwd = os.getcwd()
        file_path = os.path.join(cwd, "aquaswarm_3d_v2 (1).html")
        url = f"file://{file_path}"

        print(f"Navigating to {url}")
        page.goto(url)

        # Wait for button
        page.wait_for_selector("#btnL")

        # Click Launch
        print("Clicking Launch Swarm")
        page.click("#btnL")

        # Wait a bit for robots to spawn and move
        # We want to see them
        time.sleep(3)

        # Take screenshot
        output_path = "verification_simulation.png"
        page.screenshot(path=output_path)
        print(f"Screenshot saved to {output_path}")

        browser.close()

if __name__ == "__main__":
    run()
