import aiohttp
import asyncio

async def fetch_status(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"URL: {url} -> Status Code: {response.status}")

async def main():
    url = "https://example.com"  # Replace with your desired URL
    await fetch_status(url)

if __name__ == "__main__":
    asyncio.run(main())

