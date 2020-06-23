import pandas as pd
dict1={
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3']
}
df1 = pd.DataFrame(dict1)
# print(df1)

dict2 = {
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}
df2 = pd.DataFrame(dict2)
# print(df2)
# df_new = pd.concat([df1, df2], axis = 0, join = 'inner')
# print(df_new)

df_new1 = pd.merge(df1, df2, how = 'inner', on = None)

print(df1,'\n', df2, '\n', df_new1)