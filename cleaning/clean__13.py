import pandas as pd

ebola_melt = pd.read_csv('../data/ebola_melt.csv',index_col=0)
status_country = pd.read_csv('../data/status_country.csv',index_col=0)

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country],axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the he  ad of ebola_tidy
print(ebola_tidy.head())
