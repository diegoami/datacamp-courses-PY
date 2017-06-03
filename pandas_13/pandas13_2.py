import pandas as pd
revenue = pd.read_csv('../data/revenue.csv')
managers = pd.read_csv('../data/managers_2.csv')

combined = pd.merge(revenue, managers, left_on='city', right_on='branch')
print(combined)