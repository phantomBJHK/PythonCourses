""" import requests
import re
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
res = requests.get(url).text
text = re.findall('.*?<!--.*-->.*<!--(.*)-->',res,re.S)
# list转为str便于遍历字符
str = ''.join(text)
 
lst = []
key=[]
#遍历字符
for i in str:
    #将字符存到list中
    lst.append(i)
    #如果字符是唯一的，则添加进key
    if i not in key:
        key.append(i)
# 将list列表中的字符出现字数统计出来
for items in key:
    print(items,lst.count(items))
 """

from collections import Counter
text = open('ocr.html').read().replace('\n','')
freq = Counter(text)
avg_freq = sum(freq.values()) // len(freq)
print ''.join([c for c in text if freq[c] < avg_freq ])