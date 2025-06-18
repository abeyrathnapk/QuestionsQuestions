from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

# URL and output file can be passed as arguments
url = sys.argv[1] if len(sys.argv) > 1 else "https://pdsaiitm.github.io/"
output_file = sys.argv[2] if len(sys.argv) > 2 else "main_page_rendered.html"

def fetch_rendered_html(url, output_file):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Wait for JS to load images
    # Scroll to bottom to trigger lazy loading
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(3)  # Wait for any additional images to load
    html = driver.page_source
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    driver.quit()
    print(f"Rendered HTML saved to {output_file}")

if __name__ == "__main__":
    fetch_rendered_html(url, output_file)
