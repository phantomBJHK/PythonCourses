import requests
import bs4

target_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=158%205450579819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId%20=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'

response = requests.get(target_url)
json_url = response.json()
job_list = json_url['Data']['Posts']
for item in job_list:
    print(item['RecruitPostName'])
