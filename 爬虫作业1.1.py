import requests
res = requests.get(
    'https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc')
content = res.text
with open('data.txt', 'w') as file:
    file.write(content)
