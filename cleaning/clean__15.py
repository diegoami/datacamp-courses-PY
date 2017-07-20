import pandas as pd


site = pd.read_csv('site.csv')
visited = pd.read_csv('visited.csv')

# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)
