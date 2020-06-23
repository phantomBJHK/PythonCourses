import random
list = []
for i in range(1,10):
    list.append(random.randint(1,1000))
print('10个整数：',list)
list.sort()
print('从小到大排序：',list)