import pandas as pd
df = pd.read_csv('week4_australian_salary.csv', encoding = 'CP1252', index_col = 0)
df.info()

# import sys
# sys.path.append('data/2018/2018-04-23/week4_australian_salary.csv')

# from dvfe_01_03 import *
# display_australian_salary()