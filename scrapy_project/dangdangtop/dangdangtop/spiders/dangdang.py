# -*- coding: utf-8 -*-
import scrapy, bs4
from ..items import DangdangtopItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = []
    for x in range(1,4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-'+str(x)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('li')
        for data in datas:
            item = DangdangtopItem()
            item['name'] = data.find('div', class_='name').find('a').text
            item['author'] = data.find('div', class_='publisher_info').find('a').text
            item['price'] = data.find('div', class_='price').find('span', class_='price_n')
            yield item
