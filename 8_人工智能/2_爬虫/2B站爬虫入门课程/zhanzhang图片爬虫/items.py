# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    content = scrapy.Field()
    pass


class ImgsproItem(scrapy.Item):
    # define the fields for your item here like:
    img_url = scrapy.Field()
