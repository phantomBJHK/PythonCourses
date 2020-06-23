# -*- coding: utf-8 -*-
import scrapy, bs4
from ..items import FruitPriceItem


class FruitSpider(scrapy.Spider):
    name = 'fruit'
    allowed_domains = ['www.agronet.com.cn']
    start_urls = ['http://www.agronet.com.cn/Price/List?page=1&siteID=7']
    for page in range(1, 101):
        url = 'http://www.agronet.com.cn/Price/List?page='+str(page)+'&siteID=7'
        start_urls.append(url)
        # print('page'+' '+page)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        table = bs.find('ul', class_='price_table')
        info_list = table.find_all('li')
        del info_list[0]
        for info in info_list:
            item = FruitPriceItem()
            item['date'] = info.find('span', class_='tab_date').text
            item['product'] = info.find('span', class_='tab_breed').text
            item['market'] = info.find('span', class_='tab_terminal_market').text.replace('\r', '').replace('\n', '').replace(' ', '')
            # print('*****', item['market'])
            price = info.find_all('span', class_="tab_price")
            item['price_low'] = price[0].text.replace('\r', '').replace('\n', '').replace(' ', '')
            item['price_high'] = price[1].text.replace('\r', '').replace('\n', '').replace(' ', '')
            item['price_mean'] = price[2].text.replace('\r', '').replace('\n', '').replace(' ', '')
            yield item
