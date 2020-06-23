import scrapy
import bs4
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):

    name = 'book_douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('tr', class_='item')
        for data in datas:
            book_url = data.find_all('a')[1]['href']
            comment_url = book_url+'comments/'
            yield scrapy.Request(comment_url, callback=self.parse_comment)

    def parse_comment(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        name = bs.find('div', id='cotent').text.split()[0]
        datas = bs.find_all('div', class_='comment')
        for data in datas:
            item = DoubanItem()
            item['name'] = data.find_all('a')[1]['title']
            item['publish'] = data.find('p', class_='pl').text
            item['score'] = data.find('span', class_='rating_nums').text
            print(item['title'])
