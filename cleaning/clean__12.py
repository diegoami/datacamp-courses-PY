import pandas as pd

uber1 = pd.read_csv('../data/uber1.csv',index_col=0)
uber2 = pd.read_csv('../data/uber2.csv',index_col=0)
uber3 = pd.read_csv('../data/uber3.csv',index_col=0)

# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1 , uber2 , uber3] )

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())
