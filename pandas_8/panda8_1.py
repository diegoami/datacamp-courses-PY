import pandas as pd
sales = pd.read_csv('../data/sales.csv',index_col = 0)
sales.index = range(len(sales))


