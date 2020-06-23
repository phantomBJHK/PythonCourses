import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'list1'

url = 'https://www.shobserver.com/news/list?section=42'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')
news_list = soup.find_all('div', class_ = 'chengshi')

i = 0
for news in news_list:
    title = news.find('a')['title'].replace(' ', '')
    content = news.find('div', class_ = 'chengshi_wz_m').text.replace(' ', '')
    reporter = news.find('div', class_ = "chengshi_wz_f").text.replace(' ', '')
    i += 1
    if i > 12:
        break
    sheet.append([title, content, reporter])

wb.save('新闻摘要.xlsx')
wb.close()