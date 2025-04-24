import aiohttp
import asyncio

async def fetch_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print("Title:", data['title'])
                print("Body:", data['body'])
            else:
                print("Failed to retrieve data. Status code:", response.status)

# Run the async function
asyncio.run(fetch_post())

