import os
import re
import glob
import shutil
from bs4 import BeautifulSoup
import google.generativeai as genai
import httpx
import io
from PIL import Image

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
        return f"[Image description: {desc}]"
    md_text = re.sub(r'!\[.*?\]\((.*?)\)', md_img_repl, md_text)
    # Replace HTML <img> tags
    soup = BeautifulSoup(md_text, "html.parser")
    for img in soup.find_all("img"):
        img_url = img.get("src")
        desc = get_image_description_from_url(img_url) if img_url else "[Image]"
        img.replace_with(f"[Image description: {desc}]")
    return str(soup)

def main():
    in_dir = "course-content"
    out_dir = "image-free-course-content"
    os.makedirs(out_dir, exist_ok=True)
    for md_path in glob.glob(os.path.join(in_dir, "*.md")):
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()
        new_md = process_markdown_images(md_text)
        out_path = os.path.join(out_dir, os.path.basename(md_path))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(new_md)
        print(f"Processed {md_path} -> {out_path}")

if __name__ == "__main__":
    main()
