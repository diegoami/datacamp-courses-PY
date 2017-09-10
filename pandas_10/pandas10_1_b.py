import pandas as pd
sales = pd.read_csv('../data/sales3.csv',index_col = 0)

print(sales)

print(sales.groupby(['state'])['eggs','salt','spam'].sum())