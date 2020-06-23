# -*- coding: utf-8 -*-
import scrapy, bs4
from ..items import DuozhiItem


class DuozhibotSpider(scrapy.Spider):
    name = 'duozhibot'
    allowed_domains = ['duozhi.com']
    start_urls = ['http://duozhi.com/']

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        post_list = bs.find_all('div', class_ = 'post-item')
        for post in post_list:
            item = DuozhiItem()
            item['title'] = post.find('a', class_ = 'post-title').text
            item['description'] = post.find('p', class_ = 'post-desc').text
            print(item['title'])
            yield item
        # print(post_list)
        # pass
