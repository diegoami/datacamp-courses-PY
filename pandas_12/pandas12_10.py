# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('../data/sales-jan-2015.csv',parse_dates=True,index_col='Date')

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('../data/sales-feb-2015.csv',parse_dates=True,index_col='Date')

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('../data/sales-mar-2015.csv',parse_dates=True,index_col='Date')

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

print(units)
# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')
print(quarter1)

print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
