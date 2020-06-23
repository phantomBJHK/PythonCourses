# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FruitPriceItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    product = scrapy.Field()
    market = scrapy.Field()
    price_low = scrapy.Field()
    price_high = scrapy.Field()
    price_mean = scrapy.Field()
    