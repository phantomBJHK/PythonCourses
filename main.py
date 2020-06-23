import csv

with open('mytest.csv', encoding = 'utf-8-sig') as r:
    print('内容如下：\n')
    
    reader = csv.reader(r)
    for content in reader:
        print(content)

    data = r.read()
    print(data)
print('读取完毕！') 

