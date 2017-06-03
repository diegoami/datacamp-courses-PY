
import pandas as pd

medal_types = ['bronze', 'silver', 'gold']
medals = []
for medal in medal_types:
    # Create the file name: file_name
    file_name = "%s_top5_2.csv" % medal



    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv("../data/"+file_name,index_col='Country')
    print(medal_df)
    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])

# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'], :])
