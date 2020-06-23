from pandas import Series, DataFrame


index_list = ['001','002','003','004','005','006','007','008','009','010']
name_list = ['李白','王昭君','诸葛亮','狄仁杰','孙尚香','妲己','周瑜','张飞','王昭君','大乔']
age_list = [25,28,27,25,30,29,25,32,28,26]
salary_list = ['10k','12.5k','20k','14k','12k','17k','18k','21k','22k','21.5k']
marital_list = ['NO','NO','YES','YES','NO','NO','NO','YES','NO','YES']

dic = {
    '姓名': Series(data = name_list, index = index_list),
    '年龄': Series(data = age_list, index = index_list),
    '薪水': Series(data = salary_list, index = index_list),
    '婚姻状况': Series(data = marital_list, index = index_list)
}

df = DataFrame(dic)

wage_list = []
for value in df['薪水']:
    wage = float(value.strip('k'))
    wage_list.append(wage)

print(max(wage_list))

# for index, row_data in df.iterrows():
#     print(row_data['薪水'])

# for col, col_data in df.iteritems():
#     if col == '薪水':
#         print(col_data)
        
# list1 = [float(value[:len(value)-1]) for value in col_data]
#1. 获取工号为003~007的所有员工信息
# print(df.loc['003': '007'])

#2. 获取所有员工的年龄和工资信息
# print(df.loc[:, ['姓名', '年龄', '薪水']])

#3. 查看一个你感兴趣员工的婚姻状况
# name = input('请输入姓名：')
# staff = df[df['姓名'] == name]
# print(staff[['姓名', '婚姻状况']])