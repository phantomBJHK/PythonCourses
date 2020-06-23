import csv
import random
for j in range(5):
    list = []
    for i in range(5):
        a = random.randint(1,100)
        list.append(a)
    with open(r'mytest.csv', 'a+') as r:
        csv_write = csv.writer(r)
        csv_write.writerow(list)
        
with open(r'mytest.csv', 'r') as r:
    content = r.read()
    print(content)