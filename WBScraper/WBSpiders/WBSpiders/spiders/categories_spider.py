import re
from typing import Any
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from ..ProductsJson.get_description import *
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from ..ImportCategoriesUrls.get_categories_url import get_categories_url
from aiohttp.client_exceptions import ClientResponseError
main_url = "https://www.wildberries.by"

# Название товара
# ◦ Цена
# ◦ Ссылка на товар
# ◦ Изображение товара
# ◦ Описание товара
# ◦ Рейтинг товара (если доступен)
# ◦ Количество отзывов (если доступно)

# urls = [
#             "https://www.wildberries.by/catalog?category=8126",
#             "https://www.wildberries.by/catalog?category=8140",
#             "https://www.wildberries.by/catalog?category=63010",
#             # "https://www.wildberries.by/catalog?category=8130",
#             # "https://www.wildberries.by/catalog?category=8137",
#             # "https://www.wildberries.by/catalog?category=8141",
#         ]


class CatalogSpider(scrapy.Spider):

    name = "CatalogSpider"

    def start_requests(self, urls=get_categories_url()):
        uri = "mongodb://localhost:27017"
        client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        self.db = client.wb_database
        for key, url in urls.items():
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs = {'name': key}, dont_filter=True)

    async def parse(self, response: Response, **kwargs: Any) -> Any:
        category_name = response.cb_kwargs
        for a in response.xpath('//*[@id="route-content"]/div/div[2]/div[2]/div[2]/div[2]/div/div/a'):
            product_brand = a.xpath('div[2]/div[3]/span[1]/text()').get()
            product_name = a.xpath('div[2]/div[3]/span[2]/text()').get()
            product_price = a.xpath('div[2]/div[1]/span/span[1]/span[2]/text()').get()
            re_product_price = re.search(r"\S+", product_price)[0]
            ###не пишет валюту
            ####################################################################################################
            product_href = a.xpath('./@href').get()
            product_img = a.xpath('div[1]/div[1]/div/div[1]/div[1]/picture/img/@src').get()
            product_rating = a.xpath('div[2]/div[4]/span[1]/span/text()').get()
            product_reviews = a.xpath('div[2]/div[4]/span[2]/text()').get()
            re_product_reviews = ''.join(re.findall(r"\w+", product_reviews))
            #пишет не цифры
            ####################################################################################################

            pattern = r"(\S+)(images\S+)"
            match = re.search(pattern, product_img)
            href_pages = f'{match[1]}info/ru/card.json'
            try:
                product_description = await get_product_description(href_pages)
            except ClientResponseError:
                continue
            items = {
                'name': f'{product_brand} {product_name}',
                'price': re_product_price,
                'url': response.urljoin(product_href),
                'img': product_img,
                'description': product_description,
                'rating': product_rating,
                'reviews': re_product_reviews,
            }
            await self.db[category_name.get('name')].insert_one(items)
            yield items

# process = CrawlerProcess()
# process.crawl(CatalogSpider)
# process.start()
