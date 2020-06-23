import csv
#from kkb_tools import open_file
b = 41
listrow = []
for i in range(3):
    listline = []
    a = b
    for j in range(3):
        listline.append(a)
        a += 1
    listrow.append(listline)
    b += 10
print(listrow)
    
with open("mytest.csv",'a')  as r:
    for i in listrow():
        print(listrow(i)
        writerx = csv.writer(r)
        writerx.writerow(listrow(i))
    print("写入完毕！")
#open_file("mytest.csv")