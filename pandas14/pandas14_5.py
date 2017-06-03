# Import pandas
import pandas as pd

# Load DataFrame from file_path: editions
medals = pd.read_csv('../data/medals_2.csv')

# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition',values='Athlete',columns='NOC',aggfunc='count')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())
