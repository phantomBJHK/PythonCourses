from gevent import monkey
monkey.patch_all()
import gevent, requests, bs4
from gevent.queue import Queue
from openpyxl import Workbook

book = Workbook()
sheet = book.active
sheet.append(['食物名称', '食物热量', '详情链接'])

work = Queue()

url1 = 'http://www.boohee.com/food/group/{group}?page={page}'
for x in range(1,4):
    for y in range(1,4):
        real_url = url1.format(group = x, page = y)
        work.put_nowait(real_url)

def get_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    while not work.empty():
        res = requests.get(work.get_nowait(), headers=headers)
        html = bs4.BeautifulSoup(res.text, 'html.parser')
        foods = html.find_all('li', class_='item clearfix')
        for food in foods:
            food_link = 'http://www.boohee.com' + food.find_all('a')[1]['href']
            food_name = food.find_all('a')[1]['title']
            food_energy = food.find('p').text
            sheet.append([food_name, food_energy, food_link])

task_list = []

for x in range(5):
    task = gevent.spawn(get_page)
    task_list.append(task)

gevent.joinall(task_list)

book.save('食物热量表.xlsx')