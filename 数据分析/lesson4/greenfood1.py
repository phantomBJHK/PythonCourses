import requests
from openpyxl import Workbook
import time

url = 'http://wgh.agri.gov.cn/orderLogoProduc/middleCertificateInfo/prodListMiddleCertificateInfo'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

book = Workbook()
sheet = book.active
sheet.append(['序号', '单位', '产品', '年产'])

for page in range(1, 4731):

    data = {
        'pageSize': '15',
        'pageNo': page
    }

    response = requests.post(url, headers=headers, data=data)

    json_res = response.json()

    page_list = json_res['rows']

    for i in page_list:
        rownum = str(i['rownum'])
        applicant = str(i['applicantFullname'])
        annualoutput = i['annualOutput']
        product = str(i['productName'])
        applicant_list = [rownum, applicant, product, annualoutput]
        sheet.append(applicant_list)

    time.sleep(2)

book.save('test.xlsx')



# print(type)
# print(json_res)
# print(response)
