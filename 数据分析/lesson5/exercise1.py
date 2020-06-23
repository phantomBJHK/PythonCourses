import pandas as pd
df = pd.read_csv('data.csv',encoding='utf-8')
bools = df['关注']>100
df1 = df[bools]
# print(df1.shape)
print(df1)