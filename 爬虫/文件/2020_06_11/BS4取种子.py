
import requests
from bs4 import BeautifulSoup

Url = 'http://www.a-seed.cn/index.php?m=content&c=search&catid=29&dosubmit=1&page=1'

req = requests.get(Url)

if req.status_code != 200:
    print('请求错误:请检查地址是否正确!返回代码[{}]'.format(req.status_code))
else:
    soup = BeautifulSoup(req.text, 'html.parser')  # 把网页解析为BeautifulSoup对象
    datas = soup.select_one('table[class="table_form"]').select('tr')
    for data in datas:
        # print(data)
        items = data.select('td')
        if len(items) > 1:
            Origin = items[0].text
            name = items[1].text
            link = items[1].select_one('a').get('href')
            print(Origin, name, link)