import pandas as pd
sales = pd.read_csv('../data/sales.csv',index_col = 0)

# Create the list of new indexes: new_idx
new_idx = [idx.upper() for idx in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)
