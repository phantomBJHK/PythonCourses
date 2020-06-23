#decoding:gbk
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from bs4 import BeautifulSoup
import requests
import json
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# # sheet.title = '日期编号'
# # sheet['A1']='日期ID'
# # sheet['B1']='日期'
import datetime
begin=datetime.date(2020,5,4)
end=datetime.date(2020,5,5)
d=begin
delta=datetime.timedelta(days=1)
while d<=end:
    canshu=d.strftime('%Y-%m-%d')
    d += delta
    for i in range(1,2):
        url= 'http://www.wbncp.com/PriceDay.aspx?'
        params = {'PageNo': str(i),
                  'Type': '2',
                  'PostDate': str(canshu)}
        res = requests.get(url=url,params=params)
        print(res)
        soup=BeautifulSoup(res.text,'html.parser')
        #print(soup)
        datas=soup.find_all('tr',class_='Center')
        #print(datas)
        #data_list = []
        for lines in datas:
            data=lines.find_all('td',class_='Left')
            print(data,type(data))
            for data1 in data:
                data2=data1('td')
                print(data2)
            # for data_1 in data:
            #      data_2=data_1.text
            #      print(data_2,type(data_2))
                 #print(data_1,type(data_1))
                 #info=data_1.text#.replace(' ','').replace('\n','')
                 #print(info,type(info))
                 #data_list.append(info)
                 #print(data_list)
                 # sheet.append(info)
# wb.save('河南万邦批发市场4.xlsx')
# wb.close

# for data in paragraph:
#     lines = data.select('td')
#     data_list = []
#     if len(lines) < 8:
#         continue
#     else:
#         for line in lines:
#             data_list.append(line.text)
#     sheet.append(data_list)