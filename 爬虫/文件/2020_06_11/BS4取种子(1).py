import requests
from bs4 import BeautifulSoup

Url = 'http://www.a-seed.cn/index.php?m=content&c=search&catid=29&dosubmit=1&page=1'

req = requests.get(Url)

if req.status_code != 200:
    print('请求错误:请检查地址是否正确!返回代码[{}]'.format(req.status_code))
else:
    soup = BeautifulSoup(req.text, 'html.parser')  # 把网页解析为BeautifulSoup对象
    datas = soup.select('table[class="table_form"] tr')
    for data in datas:
        # print(data)
        items = data.select('td')
        if len(items) == 7:
            item_list = []
            for index in range(len(items) - 1):
                if index == 1:
                    item_list.append(items[index].select_one('a').get('href'))
                else:
                    item_list.append(items[index].text)
            print(item_list)
