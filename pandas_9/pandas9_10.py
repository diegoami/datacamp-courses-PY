import pandas as pd
# Set the new index: users_idx
users = pd.read_csv('week2.csv',index_col=0)

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = pd.pivot_table(users,index='weekday',columns='city')

# Print by_city_day
print(by_city_day)
