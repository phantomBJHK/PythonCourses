import requests
from bs4 import BeautifulSoup
#https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc
response = requests.get(
    'https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc')
content = BeautifulSoup(response.text, 'html.parser')
texts = content.find_all('span', class_='bjh-p')
for tex in texts:
    print(tex.text)
