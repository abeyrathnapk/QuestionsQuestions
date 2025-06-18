import requests

# List of image URLs from the topic (example, can be expanded)
image_urls = [
    "https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/24f2006531/48/111700_2.png",
    "https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png"
]

for url in image_urls:
    try:
        resp = requests.get(url)
        print(f"URL: {url}")
        print(f"Status: {resp.status_code}")
        print(f"Content-Type: {resp.headers.get('Content-Type')}")
        # Save the first 100 bytes for inspection
        with open(url.split('/')[-1], 'wb') as f:
            f.write(resp.content)
        print(f"Saved as {url.split('/')[-1]}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
