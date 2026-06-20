import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('analise/titanic.csv')

"""
#print(df.head())
print('--------- informações ---------------')
print(df.info())

print('--------- descrição ---------------')
print(df.describe())

print('---------- tipos de dados --------------')
print(df.dtypes)

print('---------- filtro --------------')
print(df[df['Age'] >= 10].head())

print('---------- linhas duplicadas --------------')
duplicateRows = df[df.duplicated()]
print(len(duplicateRows))

print('---------- linhas duplicadas --------------')
print(len(df))

df.drop_duplicates(keep='last', inplace=True)
print(len(df))

print('+++++++++++++++++++++++++++++++++++++++++++++++++=')
print(len(df))
df.dropna(subset=['Cabin'], inplace=True)
df.replace(np.nan, '0', inplace=True)
print(df)
print(len(df))


print(df)
print(df)
"""
df = df.rename(columns={'Name': 'Nome'})

sorted_df = df.sort_values(by='Nome', ascending=True)
print(sorted_df)

print('------------------------------------')
sorted_df = df.sort_values(by='Nome', ascending=False)
print(sorted_df)