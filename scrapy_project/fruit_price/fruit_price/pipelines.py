# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl

class FruitPricePipeline(object):

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['日期', '产品', '市场名称', '最低价', '最高价', '均价'])
    
    def process_item(self, item, spider):
        line = [item['date'], item['product'], item['market'], item['price_low'], item['price_high'], item['price_mean']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('fruit_price.xlsx')
        self.wb.close()
