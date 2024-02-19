# import time
#
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# time.sleep(3)
# driver.get('https://www.wildberries.by/catalog?category=8126')
# time.sleep(3)
# from requests_html import AsyncHTMLSession, HTML
#
# page = HTML(html="https://www.wildberries.by/catalog?category=8126")
# print(page)
# product_page = page.render(reload=False)
#
# print(product_page)
#
# for a in page.xpath('//*[@id="route-content"]/div/div[2]/div[2]/div[2]/div[2]/div/div/a'):
#     product_href = a.xpath('./@href').get()
#     href = f'{product_href}'
#     print(href)
import re
from urllib.request import urlopen
import asyncio
import aiohttp
import requests
import json

# headers = {
#     'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
#     'Referer': 'https://www.wildberries.by/',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# # u = 'https://basket-12.wbbasket.ru/vol1668/part166814/166814232/info/ru/card.json'
# u = 'https://basket-12.wbbasket.ru/vol1668/part166814/166814232/images/c516x688/1.webp'
#
# pattern = r"(\S+)(images\S+)"
# match = re.search(pattern, u)
# href_pages = f'{match[1]}info/ru/card.json'
#
#
# async def test(a):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(a) as response_aio:
#             response_product_json = await response_aio.json()
#             product_descr = response_product_json.get('description').strip()
#             return product_descr
#
#
# print(asyncio.run(test(f'{match[1]}info/ru/card.json')))
# response_product = requests.get(href_pages)
# response_product_json = response_product.json()
# product_descr = response_product_json.get('description').strip()

# response = requests.get(u)
# # data_json = json.loads(response.read())
# print(response.json())


import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

#
# async def ping_server():
#     # Replace the placeholder with your Atlas connection string
#     uri = "mongodb://localhost:27017"
#     # Set the Stable API version when creating a new client
#     client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
#     # Send a ping to confirm a successful connection
#     try:
#         await client.admin.command('ping')
#         print("Pinged your deployment. You successfully connected to MongoDB!")
#     except Exception as e:
#         print(e)
#
#
# asyncio.run(ping_server())

# uri = "mongodb://localhost:27017"
# # Set the Stable API version when creating a new client
# client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
# db = client.test_database
#
#
# async def do_insert():
#     document = {"key": "value"}
#     result = await db.блузки.insert_one(document)
#     print("result %s" % repr(result.inserted_id))
#
#
# import asyncio
# loop = client.get_io_loop()
# loop.run_until_complete(do_insert())
