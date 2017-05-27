import pandas as pd
sales = pd.read_csv('../data/sales.csv',index_col = 0)

# Assign months to sales.index

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales.index=months

# Print the modified sales DataFrame
print(sales)

