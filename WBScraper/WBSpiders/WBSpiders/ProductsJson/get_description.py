import asyncio
import aiohttp


async def get_product_description(href_pages):
    async with aiohttp.ClientSession() as session:
        async with session.get(href_pages) as response_aio:
            response_aio.raise_for_status()
            response_product_json = await response_aio.json()
            product_descr = response_product_json.get('description').strip().replace('\n', '')
            return product_descr
