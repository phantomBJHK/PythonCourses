import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
inquery = input('请输入搜索内容：')
url = 'https://www.so.com/s?ie=utf-8&fr=none&src=home_none&q=' + inquery
try:
    response = requests.get(url, headers=headers)
    datas = BeautifulSoup(response.text,'html.parser')
    amount = datas.find('span', class_ = 'nums').text
    print(amount)
except:
    print('爬取失败')
