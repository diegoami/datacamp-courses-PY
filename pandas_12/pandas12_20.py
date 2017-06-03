
import pandas as pd

gold = pd.read_csv('../data/gold2.csv',index_col=0)
silver = pd.read_csv('../data/silver2.csv',index_col=0)
bronze = pd.read_csv('../data/bronze2.csv',index_col=0)
# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, axis=1, join='inner',keys=['bronze', 'silver', 'gold'])

# Print medals
print(medals)

