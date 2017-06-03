
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

# Print medals
print(medals)