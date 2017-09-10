import pandas as pd
sales3 = pd.read_csv('../data/sales3.csv',index_col = 0)
print(sales3)
sales3 = sales3.set_index(['state', 'month'])
print(sales3)
print(sales3.unstack('state'))
print(sales3.unstack('month'))
print(sales3.unstack('month').stack(level='month'))

