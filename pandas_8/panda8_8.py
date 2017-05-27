import pandas as pd
sales = pd.read_csv('../data/sales3.csv',index_col = 0)

# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY',:])

