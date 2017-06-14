import pandas as pd

df1= pd.read_csv('customer.csv',index_col=['Customer ID', 'Invoice ID'])
print(df1)
#mdf1 = pd.melt(df1,id_vars=['Customer ID','Invoice ID'],value_vars=['Invoice Total','Customer Total'])
#print(mdf1)
#mdf3 = mdf1.T
#mdf2 = pd.pivot_table(mdf1,  index=['Customer ID'],columns=['Invoice ID'],'variable', 'value'])
#print(mdf2)
#df2 =df1.unstack('Invoice ID').reset_index()
#
#mdf2 = pd.pivot_table(mdf2,  index=['Customer ID'],columns=['Invoice ID'],'variable', 'value'])
#print(df2.to_json())
df4 = df1.stack()
print(df4)
print(df4.T)
