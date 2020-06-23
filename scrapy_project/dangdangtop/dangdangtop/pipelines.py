# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class DangdangtopPipeline(object):

    def __init__(self):
        self.wb = openpyxl.Workbook()
        sefl.ws = self.wb.active
        self.ws.append(['书名','作者','价格'])

    def process_item(self, item, spider):
        line = [item['book_name'], item['author'], item['price']]
        self.ws.append(line)
        return item
