import pandas as pd
# Set the new index: users_idx
sales3 = pd.read_csv('../data/sales3.csv',index_col=0)

# Create the DataFrame with the appropriate pivot table: by_city_day
print(pd.pivot_table(sales3,index='state',columns='month'))
