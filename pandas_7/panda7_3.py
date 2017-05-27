import pandas as pd
election = pd.read_csv('../data/elections.csv',index_col = 'county')
# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())
