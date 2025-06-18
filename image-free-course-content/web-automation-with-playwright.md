## Web Scraping with Playwright in Python

Scrape JavaScript‑heavy sites effortlessly with Playwright.

[[Image description: Here's alt text describing the image:

"An illustration depicting web scraping with Playwright. A figure resembling a scarecrow, wearing a wide-brimmed hat and an Anonymous Guy Fawkes mask, uses a rake to gather glowing blue strands of data from a field of tall, thin stalks. The background is a stylized landscape with a warm, sunlit sky.  Overlaid on the image are two squares: one displays the Python programming language logo, and the other shows a red and green theatrical mask, suggesting both the technical and potentially deceptive aspects of web scraping.  Large text in the foreground proclaims 'WEB SCRAPING WITH PLAYWRIGHT' in a bright lime green font on a black box."]](https://youtu.be/biFzRHk4xpY) ([youtube.com](https://www.youtube.com/watch?v=biFzRHk4xpY&amp;utm_source=chatgpt.com))

Playwright offers:

- **JavaScript rendering**: Executes page scripts so you scrape only after content appears. ([playwright.dev](https://playwright.dev/python/docs/intro))
- **Headless &amp; headed modes**: Run without UI or in a real browser for debugging. ([playwright.dev](https://playwright.dev/python/docs/intro))
- **Auto‑waiting &amp; retry**: Built‑in locators reduce flakiness. ([playwright.dev](https://playwright.dev/python/docs/locators))
- **Multi‑browser support**: Chromium, Firefox, WebKit—all from one API. ([playwright.dev](https://playwright.dev/python/docs/intro))

### Example: Scraping a JS‑Rendered Site

We’ll scrape [Quotes to Scrape (JS)](https://quotes.toscrape.com/js/)—a site that loads quotes via JavaScript, so a simple `requests` call gets only an empty shell ([quotes.toscrape.com](https://quotes.toscrape.com/js/)). Playwright runs the scripts and gives us the real content:

```python
# /// script
# dependencies = ["playwright"]
# ///

from playwright.sync_api import sync_playwright

def scrape_quotes():
    with sync_playwright() as p:
        # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/js/")
        quotes = page.query_selector_all(".quote")
        for q in quotes:
            text = q.query_selector(".text").inner_text()
            author = q.query_selector(".author").inner_text()
            print(f"{text} — {author}")
        browser.close()

if __name__ == "__main__":
    scrape_quotes()
```

Save as `scraper.py` and run:

```bash
uv run scraper.py
```

You’ll see each quote plus author printed—fetched only after the JS executes.
