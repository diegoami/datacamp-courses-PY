
import pandas as pd

medal_types = ['bronze', 'silver', 'gold']
medals = []
for medal in medal_types:
    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal

    # Create list of column names: columns
    columns = ['Country', medal]

    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv("../data/"+file_name, header=0, index_col='Country', names=columns)
    print(medal_df)
    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis='columns')

# Print medals
print(medals)