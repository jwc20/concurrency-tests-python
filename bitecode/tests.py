# Synchronous example with stdlib
import re
import time
from urllib.request import urlopen, Request

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

global_start_time = time.time()
for url in urls:
    start_time = time.time()
    with urlopen(Request(url, headers={"User-Agent": user_agent})) as response:
        html_content = response.read().decode("utf-8")
        match = title_pattern.search(html_content)
        title = match.group(1) if match else "Unknown"
        print(f"URL: {url}\nTitle: {title}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.4f} seconds\n")
global_end_time = time.time()
global_elapsed_time = global_end_time - global_start_time
print(f"Total time taken: {global_elapsed_time:.4f} seconds")

# Asynchronous example with asyncio and httpx
import asyncio
import re
import time
import httpx

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
        response = await client.get(url, headers={"User-Agent": user_agent})
        match = title_pattern.search(response.text)
        title = match.group(1) if match else "Unknown"
        print(f"URL: {url}\nTitle: {title}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for {url}: {elapsed_time:.4f} seconds\n")


async def main():
    global_start_time = time.time()
    await asyncio.gather(*map(fetch_url, urls))
    global_end_time = time.time()
    global_elapsed_time = global_end_time - global_start_time
    print(f"Total time taken for all URLs: {global_elapsed_time:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

# Example using Twisted
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

agent = Agent(reactor)
d = agent.request(
    b"GET",
    b"https://www.bitecode.dev/p/relieving-your-python-packaging-pain",
    Headers({"User-Agent": ["Twisted Web Client Example"]}),
    None,
)


def cbResponse(ignored):
    print("Response received")


d.addCallback(cbResponse)


def cbShutdown(ignored):
    reactor.stop()


d.addBoth(cbShutdown)

reactor.run()

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
