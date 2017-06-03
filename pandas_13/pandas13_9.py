import pandas as pd
auto = pd.read_csv('../data/auto.csv',index_col=0,parse_dates=['yr'])
oil  = pd.read_csv('../data/oil.csv',index_col=0,parse_dates=['Date'])

auto.info()
oil.info()


# Merge auto and oil: merged
merged = pd.merge_asof(auto,oil,left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

# print yearly.corr()
print(yearly.corr())