import pandas as pd

df_dict = {
    'name': ['ZhangSan', 'LiSi', 'WangWu', 'ZhaoLiu'], 'age': ['18', '20', '19', '22'], 'weight': ['50', '55', '60', '80']
}
df = pd.DataFrame(data = df_dict, index = ['001', '002', '003', '004'])

# for index, row_data in  df.iterrows():
#     print(index, row_data)
print(df.iteritems())
# for col, col_data in  df.iteritems():
#     print(col, col_data)