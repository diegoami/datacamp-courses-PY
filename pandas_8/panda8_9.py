import pandas as pd
sales = pd.read_csv('../data/sales3.csv',index_col = 0)
# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY',1),:]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA','TX'],2),:]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[pd.IndexSlice[:,2] ,:]

print(NY_month1)
print(CA_TX_month2)
print(all_month2)
