# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanmovieItem

class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com/chart']
    start_urls = ['http://movie.douban.com/chart/']

    def parse(self, response):
        pass
