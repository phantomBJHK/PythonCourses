import requests
from kkb_tools import open_file

res = requests.get('https://www.baidu.com/img/bd_logo1.png')
photo = res.content
with open('爬虫作业1.2.png', 'wb') as file:
    file.write(photo)
    open_file('爬虫作业1.2.png')
