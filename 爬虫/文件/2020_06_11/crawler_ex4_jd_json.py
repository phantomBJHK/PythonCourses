# -*- conding: utf-8 -*-
# __project_name__ = untitled1 - 当前的项目名
# __Author__ = Zenger
# __date__ = '2020/5/17 8:14 下午'


# 爬取京东每日特价的9.9封顶商品、价格及购买链接    页面位置： www.jd.com  > 秒杀 > 每日特价 >  9.9封顶
# url='https://miaosha.jd.com/specialpricelist.html'


import json
import requests
s_url = 'https://api.m.jd.com/api'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'shshshfpa=cfad0fa0-a751-bda4-e08e-5d45a5b0e93b-1583591495; shshshfpb=kDwkcC0KsWbLvfU6sNy6A3w%3D%3D; __jdu=1583591492195254765739; __jdv=122270672|direct|-|none|-|1590758079925; areaId=5; ipLoc-djd=5-274-286-0; shshshfp=5f1634c6b95ef9ad52ab28fae5820a45; __jda=122270672.1583591492195254765739.1583591492.1591675864.1591679919.22; __jdc=122270672; shshshsID=49376c77383a238ae2d92a3674f1818d_6_1591682740890; 3AB9D23F7A4B3C9B=NNKBTKUEG5LJ6GYL37D7U5EJQGECP5D2H44MNDNDQG5OR7EZ7PFKD6TNBWYQTEZ2OOV5QFBE5JPKJ6GEH3YGRK7ODY; __jdb=122270672.22.1583591492195254765739|22.1591679919',
    'origin': 'https://miaosha.jd.com',
    'referer': 'https://miaosha.jd.com/specialprice.html',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
param = {
    'appid': 'o2_channels',
    'client': 'pc',
    'functionId': 'pcParitySeckillGoods',
    'body': '{"categoryId":2,"tabId":0}',
}

r = requests.get(url=s_url, params=param, headers=headers)
print(r.status_code)
print(r.url)
# print(r.text)

if r.status_code == 200:
    # json_r = r.json()
    json_r = json.loads(r)
    # print(json_r)
    for i in json_r:
        list_cp = json_r['floorList']['goodsInfo']
        # print(list_cp)
        for j in list_cp:
            print(i, j['wname'], j['jdPrice'], 'https://item.jd.com/'+j['wareId'])
else:
    print('爬取失败')

