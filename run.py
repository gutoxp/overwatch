import argparse
import asyncio
import importlib

from downloader import Downloader


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("crawler", choices=["maps", "heroes"])
    parsed = parser.parse_args()

    crawler = importlib.import_module(f"overwatch.{parsed.crawler}")
    c = crawler.Crawler(Downloader())
    await c.init()


if __name__ == "__main__":
    asyncio.run(main())
