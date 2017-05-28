import pandas as pd
medals = pd.read_csv('../data/medals.csv',index_col = 0)
# Select the 'NOC' column of medals: country_names
country_names = medals['NOC']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))

medal_unique = country_names.unique()
print(medal_unique)
