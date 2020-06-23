import json
a = {'title': '今天是学习爬虫的第一天！', 'date': '2019.10.1', "content": "今天是学习爬虫的第1天！我学习了爬虫基础啦！"}
b = json.dumps(a)
c = json.load(b)
print(c)
print(type(c))
