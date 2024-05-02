# Example using gevent
import re
import time
import gevent
from gevent import monkey
from urllib.request import Request, urlopen

monkey.patch_all()

urls = [
    "https://www.bitecode.dev/p/relieving-your-python-packaging-pain",
    "https://www.bitecode.dev/p/hype-cycles",
    "https://www.bitecode.dev/p/why-not-tell-people-to-simply-use",
    "https://www.bitecode.dev/p/nobody-ever-paid-me-for-code",
    "https://www.bitecode.dev/p/python-cocktail-mix-a-context-manager",
    "https://www.bitecode.dev/p/the-costly-mistake-so-many-makes",
    "https://www.bitecode.dev/p/the-weirdest-python-keyword",
]

title_pattern = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE)
user_agent = (
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
)


def fetch_url(url):
    start_time = time.time()
    headers = {"User-Agent": user_agent}
    with urlopen(Request(url, headers=headers)) as response:
        html_content = response.read().decode("utf-8")
        match = title_pattern.search(html_content)
        title = match.group(1) if match else "Unknown"
        print(match, title)
        print(f"URL: {url}\nTitle: {title}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.4f} seconds\n")


def main():
    global_start_time = time.time()
    greenlets = [gevent.spawn(fetch_url, url) for url in urls]
    gevent.joinall(greenlets)
    global_end_time = time.time()
    global_elapsed_time = global_end_time - global_start_time
    print(f"Total time taken: {global_elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()
