import time


print('日期：',time.strftime('%Y-%m-%d', time.localtime()))
expression = input('请输入算式：')
start_time = time.time()
time.sleep(1)
print(expression, '=', eval(expression))
end_time = time.time()
time_used = round(end_time - start_time,2)
print('程序花费时间为：%s秒' %time_used)
