import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#构建url
for x in range(1,5):
    url="http://www.xinfadi.com.cn/marketanalysis/2/list/"+str(x)+".shtml"
    x=x+1
    data=requests.get(url,headers=headers)
    data_1=BeautifulSoup(data.text,'html.parser')
    data_2=data_1.find_all('tr',class_='tr_color')
    print(data_2)
    for data in data_2:
        name = data.find('td').text
        print(name)

