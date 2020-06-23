import gevent, requests, bs4, openpyxl
from bs4 import BeautifulSoup
from gevent.queue import Queue
from gevent import monkey
from openpyxl import Workbook
import sys
# sys.setrecursionlimit(100000)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

book = Workbook()
sheet = book.active
sheet.append(['食物名称', '食物热量', '详情链接'])

def get_page(list_num, page_num):
    url = 'https://food.hiyd.com/list-' + str(list_num) + '-html?page=' + str(page_num)
    res = requests.get(url, headers=headers)
    bs_html = BeautifulSoup(res.text, 'html.parser')
    return bs_html

def get_total_pages(list_num, page_num = None):
    bs = get_page(list_num, page_num)
    total_pages = bs.find(string = '...').find_next('a').text
    return 3 #total_pages

monkey.patch_all()

queue = Queue()
for list_num in [1,2,3]:
    for page_num in range(1, 4):
        queue.put_nowait([str(list_num), str(page_num)])

# url = 'https://food.hiyd.com/list-' + list_num + '-html?page=' + page_num

# res = requests.get(url, headers = headers)
# html = BeautifulSoup(res.text, 'html.parser')
def get_food(list_num, page_num):
    while not queue.empty():
        list_num, page_num = queue.get_nowait()
        html = get_page(list_num, page_num)
        foods = html.find_all('li')
        for food in foods:
            food_link = 'https:' + food.find('a')['href']
            food_name = food.find('h3')
            food_energy = food.find('p')
            sheet.append([food_name, food_energy, food_link])

task_list = []

for x in range(2):
    task = gevent.spawn(get_food(queue))
    task_list.append(task)

gevent.joinall(task_list)

book.save('食物热量表.xlsx')