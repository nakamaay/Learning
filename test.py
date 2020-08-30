import pandas as pd

df_none_usecols = pd.read_csv('test.csv', encoding = 'utf-8', header=None, usecols=[2])
print(df_none_usecols)