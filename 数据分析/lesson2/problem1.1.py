from pandas import Series
emp = ['001', '002', '003', '004', '005', '006']
name = ['亚瑟', '后羿', '小乔', '哪吒', '虞姬', '王昭君']
series = Series(data=name, index=emp)

print(series.values)
# print(series.index.tolist())
# print(list(series.items()))

# print(series['001'])
# print('索引下标\n', series[['002':'004']])
# print('索引切片\n', series['001':'004'])

# print(series[0])
# print('位置下标\n', series[[1,3]])
# print('位置切片\n', series[0:3])

# sel = Series(data = ['1','2','3','4'], index = list('abcd'))
# print(sel[0],[3])
# print(sel[['a','c']])
# print(sel['a':'c'])
# print(sel[[0,3]])

# for value in sel:
#     print(value)
# for value in sel.keys():
#     print(value)
# for value in sel.items():
#     print(value)
