import os
import re
import time
from bs4 import BeautifulSoup
import google.generativeai as genai
import httpx
import io
from PIL import Image

# List of files that need to be retried (from previous output)
FILES_TO_RETRY = [
    "actor-network-visualization.md",
    "archive.md",
    "base64-encoding.md",
    "bash.md",
    "bbc-weather-api-with-python.md",
    "cleaning-data-with-openrefine.md",
    "colab.md",
    "correlation-with-excel.md",
    "crawling-cli.md",
    "data-analysis-with-duckdb.md",
    "data-analysis-with-python.md",
    "data-analysis-with-sql.md",
    "data-cleansing-in-excel.md",
    "data-preparation-in-duckdb.md",
    "data-preparation-in-the-shell.md",
    "data-sourcing.md",
    "data-transformation-in-excel.md",
    "data-visualization-with-seaborn.md",
    "docker.md",
    "extracting-audio-and-transcripts.md",
    "forecasting-with-excel.md",
    "geospatial-analysis-with-python.md",
    "geospatial-analysis-with-qgis.md",
    "git.md",
    "github-actions.md",
    "github-pages.md",
    "google-auth.md",
    "image-compression.md",
    "json.md",
    "live-session-2025-01-15.md",
    "live-session-2025-01-29.md",
    "live-session-2025-02-01.md",
    "live-session-2025-02-04.md",
    "live-session-2025-02-07.md",
    "llm-evals.md",
    "llm-sentiment-analysis.md",
    "llm-speech.md",
    "llm-text-extraction.md",
    "llm.md",
    "markdown.md",
    "narratives-with-excel.md",
    "network-analysis-in-python.md",
    "nominatim-api-with-python.md",
    "npx.md",
    "ollama.md",
    "parsing-json.md",
    "project-tds-virtual-ta.md",
    "README.md",
    "rest-apis.md",
    "scheduled-scraping-with-github-actions.md",
    "scraping-emarketer.md",
    "scraping-imdb-with-javascript.md",
    "scraping-live-sessions.md",
    "scraping-pdfs-with-tabula.md",
    "scraping-with-excel.md",
    "scraping-with-google-sheets.md",
    "splitting-text-in-excel.md",
    "spreadsheets.md",
    "sqlite.md",
    "topic-modeling.md",
    "vector-databases.md",
    "vision-models.md",
    "visualizing-animated-data-with-powerpoint.md",
    "visualizing-machine-learning.md",
    "visualizing-network-data-with-kumu.md"
]

IN_DIR = "course-content"
OUT_DIR = "image-free-course-content"

# Gemini logic from scrape_tds_discourse.py
def get_image_description_from_url(img_url):
    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            print("[ERROR] GOOGLE_API_KEY environment variable not set.")
            return "[Image description unavailable: No API key]"
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = httpx.get(img_url)
        if response.status_code != 200:
            print(f"[ERROR] Could not fetch image from {img_url}")
            return "[Image description unavailable: Could not fetch image]"
        image = Image.open(io.BytesIO(response.content))
        result = model.generate_content([
            "Describe this image in detail as if writing an alt text for visually impaired users. Include the main subject, context, colors, and any text in the image.",
            image
        ])
        return result.text.strip()
    except Exception as e:
        print(f"[ERROR] Could not get image description: {e}")
        return "[Image description unavailable]"

def process_markdown_images(md_text):
    # Replace markdown images ![alt](url)
    def md_img_repl(match):
        url = match.group(1)
        desc = get_image_description_from_url(url)
        time.sleep(70)  # 1 minute 10 seconds delay
        return f"[Image description: {desc}]"
    md_text = re.sub(r'!\[.*?\]\((.*?)\)', md_img_repl, md_text)
    # Replace HTML <img> tags
    soup = BeautifulSoup(md_text, "html.parser")
    for img in soup.find_all("img"):
        img_url = img.get("src")
        desc = get_image_description_from_url(img_url) if img_url else "[Image]"
        time.sleep(70)
        img.replace_with(f"[Image description: {desc}]")
    return str(soup)

def main():
    for filename in FILES_TO_RETRY:
        in_path = os.path.join(IN_DIR, filename)
        out_path = os.path.join(OUT_DIR, filename)
        if not os.path.exists(in_path):
            print(f"File not found: {in_path}")
            continue
        with open(in_path, "r", encoding="utf-8") as f:
            md_text = f.read()
        new_md = process_markdown_images(md_text)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(new_md)
        print(f"Processed {in_path} -> {out_path}")

if __name__ == "__main__":
    main()
