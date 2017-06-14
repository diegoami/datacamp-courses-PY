import pandas as pd

df1= pd.read_csv('a1.csv')
df2 = pd.read_csv('a2.csv')
print(df1)
print(df2)

df1, df2 = df1.align(df2)
print(df1.fillna(0) - df2.fillna(0))

