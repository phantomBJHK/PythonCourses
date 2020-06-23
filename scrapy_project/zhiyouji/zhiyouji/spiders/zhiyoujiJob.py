import scrapy
import bs4
from ..items import ZhiyoujiItem


class Spider_GetJobInfo(scrapy.Spider):
    name = 'GetJobsInfo'
    allowed_domain = ['www.jobui.com']
    start_urls = ['http://www.jobui.com/rank/company']

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        ul_list = bs.find_all('ul', class_ = 'textList flsty cfix')
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                company_id = a['href']
                url = 'https://www.jobui.com{id}jobs'.format(id = company_id)
                yield scrapy.Request(url, callback = self.parse_GetJobInfo)

    def parse_GetJobInfo(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        company = bs.find(class_ = 'company-banner-name').text
        datas = bs.find_all('div', class_ = 'job-simpay-content')
        for data in datas:
            item = ZhiyoujiItem()
            item['company'] = company
            item['position'] = data.find_all('div', class_="job-segmetation")[0].find('h3').text
            item['address'] = data.find_all('div', class_="job-segmetation")[1].find_all('span')[0].text
            item['detail'] = data.find_all('div', class_="job-segmetation")[1].find_all('span')[1].text
            yield item

