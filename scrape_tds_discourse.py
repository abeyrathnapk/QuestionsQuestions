import requests
import json
import time
import os
import html2text
from bs4 import BeautifulSoup
import google.generativeai as genai
from PIL import Image
import io
import httpx
from urllib.parse import urljoin
from datetime import datetime

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_PATH = "/c/courses/tds-kb/34"
OUTPUT_FILE = "tds_course_content.json"  # Use the same file as the course content

# Paste your _t cookie value here
SESSION_COOKIE = "op0dfzlDLILy46rRFEtzzH5wi%2FZHP9g%2Bp6EOK8jxzyiT22Z2zQkAWdBc7jWyWENAW7EWTxfE0TYddCcm2ZYRok2aD1MhsLjgQ3O6tRF55MBOahxPQXqI5kPEEL6ctNlx6g44H8tvZ6Pn%2FUTrs%2F1IEjKKZo%2FOr%2F7EI0b72yFeegWUrWULIOS%2FaoFRu16%2FAGn%2BgarAAKiZOSLGWifiilTjjX0vD6nO78V6%2FjHvWzKydQDi5RZFmMjL%2Fo3G77zab%2FpJjbatycPsydLTLsucySlBA%2BxrplEGDCSGXq2xgwgkuqZWFi%2FUPLlV6xRE5O6Qlpi4--uN11JuFn%2FIygUiUj--gxrgNEdvUoMgERDq%2FuN4hQ%3D%3D"

HEADERS = {
    'User-Agent': 'Mozilla/5.0',
}
COOKIES = {
    '_t': SESSION_COOKIE
}


def get_topics():
    topics = []
    page = 0
    while True:
        url = f"{BASE_URL}{CATEGORY_PATH}.json?page={page}"
        print(f"Fetching topics from: {url}")
        resp = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if resp.status_code != 200:
            break
        data = resp.json()
        topic_list = data.get('topic_list', {}).get('topics', [])
        if not topic_list:
            break
        topics.extend(topic_list)
        page += 1
        time.sleep(1)
    return topics


def get_posts_for_topic(topic_id, start_date=None, end_date=None):
    url = f"{BASE_URL}/t/{topic_id}.json"
    print(f"Fetching posts for topic: {url}")
    resp = requests.get(url, headers=HEADERS, cookies=COOKIES)
    if resp.status_code != 200:
        return []
    data = resp.json()
    posts = data.get('post_stream', {}).get('posts', [])
    topic_title = data.get('title', '')
    topic_slug = data.get('slug', '')
    topic_url = f"{BASE_URL}/t/{topic_slug}/{topic_id}"
    result = []
    for post in posts:
        created_at = post.get('created_at')
        if start_date and end_date:
            # Parse the date string
            post_date = datetime.strptime(created_at[:10], "%Y-%m-%d")
            if not (start_date <= post_date <= end_date):
                continue
        result.append({
            'source': 'discourse',
            'topic_id': topic_id,
            'topic_title': topic_title,
            'topic_url': topic_url,
            'post_number': post.get('post_number'),
            'author': post.get('username'),
            'created_at': created_at,
            'content': post.get('cooked')  # HTML content
        })
    return result


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


def html_with_gemini_img_to_md(html, base_url=None):
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.find_all("img"):
        img_url = img.get("src")
        if base_url and img_url and not img_url.startswith("http"):
            img_url = urljoin(base_url, img_url)
        alt_text = get_image_description_from_url(img_url) if img_url else "[Image]"
        md_img = f"![{alt_text}]({img_url})"
        img.replace_with(md_img)
    return html2text.html2text(str(soup))


def save_topic_as_markdown(topic_title, topic_url, posts, out_dir):
    # Sanitize filename
    import re
    filename = re.sub(r'[^\w\- ]', '', topic_title)[:80].replace(' ', '_')
    filepath = os.path.join(out_dir, f"{filename}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {topic_title}\n\n")
        f.write(f"[View on Discourse]({topic_url})\n\n")
        for post in posts:
            author = post.get('author', 'unknown')
            created = post.get('created_at', '')
            md = html_with_gemini_img_to_md(post.get('content', ''), base_url=topic_url)
            f.write(f"---\n**{author}** on {created}:\n\n{md}\n\n")


def main():
    out_dir = "discourse_markdown"
    os.makedirs(out_dir, exist_ok=True)
    # Load existing course content if present
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
    else:
        all_data = []

    topics = get_topics()
    print(f"Found {len(topics)} topics.")
    for topic in topics:
        # Only process topics from the exact tds-kb category (category_id == 34)
        if topic.get('category_id') != 34:
            continue
        topic_id = topic['id']
        posts = get_posts_for_topic(topic_id)
        all_data.extend(posts)
        # Save progress after each topic
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        # Save each topic as a separate markdown file
        if posts:
            save_topic_as_markdown(posts[0]['topic_title'], posts[0]['topic_url'], posts, out_dir)
        time.sleep(1)
    print(f"Saved combined data to {OUTPUT_FILE}")
    print(f"Saved markdown files to {out_dir}")


def main_with_date_filter(start_date, end_date):
    out_dir = "discourse_markdown"
    os.makedirs(out_dir, exist_ok=True)
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
    else:
        all_data = []
    topics = get_topics()
    print(f"Found {len(topics)} topics.")
    filtered_topics = []
    for topic in topics:
        if topic.get('category_id') != 34:
            continue
        # Use topic metadata to filter by date range
        created_at = topic.get('created_at')
        last_posted_at = topic.get('last_posted_at')
        # Parse dates
        topic_created = datetime.strptime(created_at[:10], "%Y-%m-%d") if created_at else None
        topic_last_posted = datetime.strptime(last_posted_at[:10], "%Y-%m-%d") if last_posted_at else None
        # If topic's activity overlaps with date range, include it
        if topic_created and topic_last_posted and not (topic_last_posted < start_date or topic_created > end_date):
            filtered_topics.append(topic)
    print(f"Filtered to {len(filtered_topics)} topics in date range.")
    for topic in filtered_topics:
        topic_id = topic['id']
        posts = get_posts_for_topic(topic_id, start_date, end_date)
        if not posts:
            continue
        all_data.extend(posts)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        save_topic_as_markdown(posts[0]['topic_title'], posts[0]['topic_url'], posts, out_dir)
        print(f"Saved topic {topic_id} to markdown (filtered by date range).")
        time.sleep(1)
    print(f"Saved combined data to {OUTPUT_FILE}")
    print(f"Saved markdown files to {out_dir}")


if __name__ == "__main__":
    import sys
    from datetime import datetime
    if len(sys.argv) == 3:
        # Run for all topics in date range
        start_date = datetime.strptime(sys.argv[1], "%Y-%m-%d")
        end_date = datetime.strptime(sys.argv[2], "%Y-%m-%d")
        main_with_date_filter(start_date, end_date)
    elif len(sys.argv) > 3:
        # Run for a single topic ID with date range
        topic_id = sys.argv[1]
        start_date = datetime.strptime(sys.argv[2], "%Y-%m-%d")
        end_date = datetime.strptime(sys.argv[3], "%Y-%m-%d")
        out_dir = "discourse_markdown"
        os.makedirs(out_dir, exist_ok=True)
        posts = get_posts_for_topic(topic_id, start_date, end_date)
        if posts:
            save_topic_as_markdown(posts[0]['topic_title'], posts[0]['topic_url'], posts, out_dir)
            print(f"Saved topic {topic_id} to markdown (filtered by date range).")
        else:
            print(f"No posts found for topic {topic_id} in date range.")
    elif len(sys.argv) > 1:
        # Run for a single topic ID (no date filter)
        topic_id = sys.argv[1]
        out_dir = "discourse_markdown"
        os.makedirs(out_dir, exist_ok=True)
        posts = get_posts_for_topic(topic_id)
        if posts:
            save_topic_as_markdown(posts[0]['topic_title'], posts[0]['topic_url'], posts, out_dir)
            print(f"Saved topic {topic_id} to markdown.")
        else:
            print(f"No posts found for topic {topic_id}.")
    else:
        main()
