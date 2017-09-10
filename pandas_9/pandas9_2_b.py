import pandas as pd
sales3 = pd.read_csv('../data/sales3.csv',index_col = 0)
print(sales3)

print(sales3.pivot(index='state',columns='month'))