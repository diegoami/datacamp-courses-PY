import pandas as pd
medals = pd.read_csv('../data/medals.csv',index_col = 0)

# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC',values='Athlete',columns='Medal',aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values('totals', ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))
