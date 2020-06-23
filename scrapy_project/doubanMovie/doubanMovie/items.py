# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名
    name = scrapy.Field()
    url = scrapy.Field()
    info = scrapy.Field()
    rating = scrapy.Field()
    # pass
