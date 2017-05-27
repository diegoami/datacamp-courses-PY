import pandas as pd
election = pd.read_csv('../data/elections.csv',index_col = 0)
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue', 'Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election['winner'].map(lambda x: red_vs_blue[x])

# Print the output of election.head()
print(election.head())




