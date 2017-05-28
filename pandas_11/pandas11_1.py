import pandas as pd
medals = pd.read_csv('../data/medals.csv',index_col = 0)
USA_edition_grouped = medals.loc[medals.NOC == 'USA'].groupby('Edition')
print(USA_edition_grouped['Medal'].count())