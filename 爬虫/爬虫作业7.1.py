import requests
from bs4 import BeautifulSoup
import openpyxl

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '果壳1-10'

for i in range(1,11):
    url = 'https://www.guokr.com/ask/highlight/?page=' + str(i)
    response = requests.get(url, headers=headers)
    datas = BeautifulSoup(response.text,'html.parser')
    quest = datas.find('ul', class_ = "ask-list-cp")
    questions = quest.find_all('li')

    for question in questions:
        qa = question.find('a', target = "_blank").text
        link = question.find('a')['href']
        sheet.append([qa, link])

print('提取完成')
wb.save('果壳问答.xlsx')
wb.close()