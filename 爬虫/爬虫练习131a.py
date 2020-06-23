import gevent, requests, bs4, openpyxl
from bs4 import BeautifulSoup
from gevent.queue import Queue
# from gevent import monkey

# monkey.patch_all()

url = 'https://food.hiyd.com/list-' + '1' + '-html?page=' + '1'

res = requests.get(url)
html = BeautifulSoup(res.text, 'html.parser')
total_pages = html.find(string = '...').find_next('a').text
# foods = html.find_all('li')
# food = foods[0]
# link = 'https:' + food.find('a')['href']
# print(link)

print(total_pages)
