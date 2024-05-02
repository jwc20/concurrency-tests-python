# Example using Trio
import re
import time
import httpx
import trio

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


async def fetch_url(url):
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        headers = {"User-Agent": user_agent}
        response = await client.get(url, headers=headers)
        match = title_pattern.search(response.text)
        title = match.group(1) if match else "Unknown"
        print(f"URL: {url}\nTitle: {title}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for {url}: {elapsed_time:.4f} seconds\n")


async def main():
    global_start_time = time.time()
    async with trio.open_nursery() as nursery:
        for url in urls:
            nursery.start_soon(fetch_url, url)
    global_end_time = time.time()
    global_elapsed_time = global_end_time - global_start_time
    print(f"Total time taken for all URLs: {global_elapsed_time:.4f} seconds")


if __name__ == "__main__":
    trio.run(main)
