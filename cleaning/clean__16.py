import pandas as pd


site = pd.read_csv('site.csv')
visited = pd.read_csv('visited_2.csv')

# Merge the DataFrames: m2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print m2o
print(m2o)
