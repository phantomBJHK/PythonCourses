# -*- coding: utf-8 -*-

import openpyxl
import requests
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '品种审定'
sheet['A1']='地域'
sheet['B1']='品种名称'
sheet['C1']='作物种类'
sheet['D1']='审订编号'
sheet['E1']='审订年份'
sheet['F1']='选育单位'
sheet['G1']='链接'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
for i in range(1,3):
    url='http://www.a-seed.cn/index.php?m=content&c=search&catid=29&dosubmit=1&page='+str(i)
    print(url)
    req = requests.get(url=url,headers=headers)
    if req.status_code != 200:
        print('请求错误:请检查地址是否正确!返回代码[{}],{}'.format(req.status_code, req.text))
    else:
        print(req.status_code)
        soup = BeautifulSoup(req.text, 'html.parser')
        print(soup)
        paragraph = soup.select_one('.table_form').select('tbody>tr')
        print(paragraph)
        for data in paragraph:
            lines = data.select('td')
            #link=data.select_one('a').get('href')
            data_list = []
            for line in lines:
                data_list.append(line.text)
                #data_list.append(str(link))
                #print(data_list)
            sheet.append(data_list)
wb.save('审定品种数据.xlsx')
# 保存修改的Excel
wb.close()



