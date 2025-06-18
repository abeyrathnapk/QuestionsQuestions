import os
import re
import httpx
import html2text
from bs4 import BeautifulSoup
from PIL import Image
import io
from urllib.parse import urljoin
import google.generativeai as genai

def get_image_description_from_url(img_url):
    """Get a description of the image from a URL using Google Gemini (Generative AI)."""
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

def convert_html_to_md_from_url(url, output_dir="./markdowns"):
    response = httpx.get(url)
    if response.status_code != 200:
        print(f"[ERROR] Could not fetch HTML from {url}")
        return
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    os.makedirs(output_dir, exist_ok=True)

    # Use html2text for main conversion
    md_content = html2text.html2text(str(soup))

    # Find all images in the HTML
    images = soup.find_all("img")
    print(f"[DEBUG] Found {len(images)} <img> tags:")
    img_desc_map = {}
    for img in images:
        img_src = img.get("src")
        alt = img.get("alt", "")
        if not img_src:
            continue
        # Build absolute URL if needed
        if not img_src.startswith("http"):
            img_url = urljoin(url, img_src)
        else:
            img_url = img_src
        print(f"  [DEBUG] src: {img_url}")
        description = get_image_description_from_url(img_url)
        img_desc_map[img_src] = description

    # Post-process markdown to add descriptions after each image
    def add_description(match):
        alt_text = match.group(1)
        img_path = match.group(2)
        for src, desc in img_desc_map.items():
            if img_path.endswith(os.path.basename(src)):
                return f"*{desc}*"
        return match.group(0)  # fallback

    # Replace all image markdowns with just the description
    md_content = re.sub(r'!\[(.*?)\]\((.*?)\)', add_description, md_content)

    # Append any image descriptions not already in markdown
    for src, desc in img_desc_map.items():
        if desc and desc not in md_content:
            md_content += f"\n\n*{desc}*\n"

    # Save markdown file
    md_filename = url.split("/")[-1].split("?")[0] or "index"
    if not md_filename.endswith(".md"):
        md_filename += ".md"
    md_path = os.path.join(output_dir, md_filename)
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)
    print(f"Markdown saved to {md_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 html_to_md.py <url> [output_dir]")
        sys.exit(1)
    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./markdowns"
    convert_html_to_md_from_url(url, output_dir)