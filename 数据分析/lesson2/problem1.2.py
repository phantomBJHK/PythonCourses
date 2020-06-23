import pandas as pd

df_dict = {
    'name': ['ZhangSan', 'LiSi', 'WangWu', 'ZhaoLiu'], 'age': ['18', '20', '19', '22'], 'weight': ['50', '55', '60', '80']
}
df = pd.DataFrame(data = df_dict, index = ['001', '002', '003', '004'])
# print(df)
# print(df.head(2))
# print(df.tail(2))
# print(df.shape)
# print(df.index.tolist())
# print(df.columns.tolist())
# print(df.ndim)
# print(df[0:1])
# print(df[1:3])
# print(df[1:3][['name', 'age']])
# print(df['name'])
print(df[['name', 'age']])
# print(df.loc['001'])
# print(df.loc['001', 'name'])
# print(df.loc['001', ['name', 'weight']])
# print(df.loc[['001', '003'], ['name', 'weight']])
# print(df.loc['001': '003', 'name': 'weight'])
# print(df.iloc[1:3, 0: 2])
# print(df.iloc[1]) #取一行
# print(df.iloc[0:2]) #取多行
# print(df.iloc[[0,2], :]) #间断多行
# print(df.iloc[:, 1]) #取一列
# print(df.iloc[2, 2]) #取某一个值