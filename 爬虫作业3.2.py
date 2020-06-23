import requests
from bs4 import BeautifulSoup
#http://www.shicimingju.com/book/saguoyani.html
response = requests.get('http://www.shicimingju.com/book/sanguoyanyi.html')
datas = BeautifulSoup(response.text, 'html.parser')
contents = datas.find('div', class_='book-mulu')
content = contents.find_all('a')
content = content[:-1]
for chapter in content:
    print(chapter.text)
